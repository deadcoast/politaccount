# -*- coding: utf-8 -*-
"""
Politaccount scales — two rating scales for leaders of first-world democracies.

  OA   Operational Accountability   for every case where accountability was owed: what consequence landed on
                                    the person responsible, in office; whether they owned it before a body
                                    ruled or fought it; whether anything actually changed. Counted, dated,
                                    never graded on words.
  POC  Provable Observable Corruption
                                    corrupt acts on the public record, scored by the common meaning of
                                    the word and by the strength of the evidence — not by whether the
                                    act was illegal where and when it happened.

Both scales are computed from the same case data every leader gets (trudeau.json) plus two code files per
leader (codes_<leader>.py for corruption, oa_<leader>.py for accountability). Every rule, weight and threshold lives here, fixed before any second leader is
scored. Nothing in this file refers to a party or a policy.
"""
import json, os, sys, datetime

# ────────────────────────────────────────────────────────────────────────────────────────────────────
# SHARED — case weight (severity), computed from the record, not chosen
# ────────────────────────────────────────────────────────────────────────────────────────────────────
# S = 1 + [harm or money] + [a body found against them], capped at 3.
#   harm   direct harm to identifiable people or to a democratic process, on the record (coded, with the fact)
#   money  ≥ $10 million of public money spent, or in play (cost_cad or a documented programme value)
#   against a finding against the leader, the government or a minister by a court, an officer of Parliament,
#          an auditor, a public inquiry, a committee report, or the record itself (a written commitment not met)
MONEY_THRESHOLD = 10_000_000
AGAINST_BY_RESULT = {"VIOLATION_FOUND", "COURT_AGAINST_GOVERNMENT", "AUDIT_ADVERSE", "BROKEN_COMMITMENT"}

# ────────────────────────────────────────────────────────────────────────────────────────────────────
# OA — counted, dated, over the cases where accountability was owed
# ────────────────────────────────────────────────────────────────────────────────────────────────────
# A case is OWED when a body found against the leader, the government or a minister, or they admitted the
# fault. Cleared, upheld, never-examined and cost-only cases are neither for nor against: they are out.
OWED_BY_RESULT = {"VIOLATION_FOUND", "COURT_AGAINST_GOVERNMENT", "AUDIT_ADVERSE", "BROKEN_COMMITMENT", "ADMISSION"}
OWED_IF_AGAINST = {"INQUIRY_FINDING", "CHARGES", "CHARGES_STAYED", "RESIGNATION", "CLEARED", "RECORD"}

OA_ITEMS = {
 "consequence": ("Consequence", "What landed on the person responsible, in office.", {
    "1":   "On the leader personally: resigned over it, fined, sanctioned, repaid, or his own decision reversed under pressure.",
    "0.5": "On the responsible minister or official: resigned or removed over it, sanctioned; or the specific decision reversed.",
    "0":   "Nothing. Words are nothing: an apology, 'accepting' a report, a review ordered, a recommendation accepted. Money paid by the treasury is nothing. Anything after leaving office is nothing."}),
 "posture": ("Posture", "What he did with it before a body ruled.", {
    "owned":   "Admitted it or acted on it before any finding, and did not obstruct.",
    "nothing": "Said nothing of substance, or accepted the finding only once it was made.",
    "fought":  "Denied, minimized, blamed others, appealed, litigated, withheld records, invoked cabinet confidence, prorogued, or refused an order."}),
 "change": ("Change", "Whether anything actually changed, in office.", {
    "1": "A law, a rule, a process or a decision changed, and the conduct did not recur.",
    "0": "Nothing changed; a change promised, accepted or 'under implementation'; the same conduct recurred; or the change came after leaving office."}),
}
POSTURE_VALUE = {"owned": 1.0, "nothing": 0.0, "fought": 0.0}
OA_BANDS = [  # lower bound, name, one line — the score is the mean share of the three things that happened
 (80, "Fully accountable", "Owned it, paid for it, changed it, in office."),
 (60, "Accountable",       "Most findings owned before they were forced; consequences borne at the top; rules changed in office."),
 (40, "Partly accountable","Some consequences borne at the top; some findings owned before they were forced; some rules changed."),
 (20, "Others paid",       "Consequences fell on ministers and officials, not on him. More findings fought than owned. Little changed."),
 (0,  "Unaccountable",     "Fought or ignored the findings. Nothing landed on him. The same conduct again."),
]

# ────────────────────────────────────────────────────────────────────────────────────────────────────
# POC — corrupt-act types, defined by observable elements (an elements test, in plain words)
# ────────────────────────────────────────────────────────────────────────────────────────────────────
# A case scores only if EVERY element of the type is on the record at evidence grade E2 or better.
# The case's grade is the LOWEST grade among its elements. Legality is not an element.
POC_TYPES = {
 "T1": ("Self-dealing and conflicts", 3.0, [
        "a benefit — a gift, money, travel, a contract, a licence, a programme — to the office-holder, their family, their party, or a close associate",
        "the giver or recipient had, or sought, business with the government",
        "the office-holder did not refuse it, or did not recuse from the decision"]),
 "T2": ("Interference with an independent process", 4.0, [
        "the office-holder or their office intervened in, pressured, or publicly pre-judged",
        "a decision reserved to an independent actor: a prosecutor, a judge, the police, an officer of Parliament, an arm's-length appointment",
        "without lawful authority to direct that decision"]),
 "T3": ("Abuse of state power against people", 4.0, [
        "state power was used against people: detention, property, bank accounts, prosecution, surveillance",
        "a court found the legal conditions for using it were not met, or that it breached their rights"]),
 "T4": ("Public money to insiders, or without the rules", 3.0, [
        "public funds, contracts, grants or appointments went",
        "to insiders, friends, party-connected people, ineligible recipients, or without the controls the rules require",
        "as found by an auditor, an officer of Parliament, a court, a recorded vote of Parliament, or admitted — beyond ordinary error"]),
 "T5": ("False statements to the public", 2.0, [
        "a public statement of fact by the office-holder, their office, or a minister",
        "contradicted by a document, a finding, or their own later statement on the record",
        "about a matter they were in a position to know"]),
 "T6": ("Obstruction of scrutiny", 3.0, [
        "an investigator, a committee, a court, an inquiry, or Parliament sought records or answers",
        "the office-holder or government withheld them, redacted beyond the order, ended the process (prorogation, a confidence vote, dissolution), or went to court against disclosure",
        "as shown by an order, a ruling, a formal admonishment, or the record"]),
 "T7": ("Breach of their own written standard", 1.5, [
        "a written standard the office-holder set, signed, or swore to",
        "was broken, per a finding or an admission",
        "with none of the types above present"]),
}
EVIDENCE = {  # grade: (name, multiplier, meaning)
 "E4": ("Adjudicated", 1.0, "A court, an officer of Parliament, an auditor, or a public inquiry found it."),
 "E3": ("Admitted / own record", 1.0, "They admitted it, or it is their own act or document on the record: a settlement paid, a lawsuit filed, an itinerary issued, a statement made."),
 "E2": ("Documented, no ruling", 0.6, "On the public record — sworn testimony, released documents, a recorded vote of the House — but no body with authority ruled on it."),
 "E1": ("Reported, never examined", 0.0, "Reported by major outlets, denied or unanswered, examined by nobody. Listed. Scores nothing."),
}
PROXIMITY = {  # who did it: (name, multiplier)
 "him":        ("The leader personally: his own act or statement, or a decision he announced and defended as his own", 1.0),
 "office":     ("His staff, or a cabinet decision carried by a minister", 0.8),
 "minister":   ("A minister or MP, personally", 0.5),
 "government": ("A department, agency or body under the government", 0.4),
}
SECONDARY_WEIGHT = 0.5     # a second or third type on the same case, with its own distinct elements met
MAX_SECONDARY = 2
LEADER_MAJOR_ACT = 12.0    # the unit the bands are expressed in: B4 × E1.0 × him × S3

# POC bands are structural — each is a checkable fact about the ledger, not a threshold alone.
POC_BANDS = [
 ("None",     "No proven corrupt act on the record."),
 ("Isolated", "Proven acts, none by the leader personally."),
 ("Repeated", "More than one proven act by the leader personally, or one by the leader and three or more across the government."),
 ("Pattern",  "Proven acts by the leader personally in three or more types, or the same type again after an adverse finding."),
 ("Systemic", "A pattern, plus obstruction of scrutiny and false statements to the public both proven, plus a repeat after an adverse finding."),
]

# ────────────────────────────────────────────────────────────────────────────────────────────────────
# engine
# ────────────────────────────────────────────────────────────────────────────────────────────────────
def severity(e, code):
    harm = bool(code.get("harm"))
    money = (e.get("cost_cad") or 0) >= MONEY_THRESHOLD or (code.get("money_in_play") or 0) >= MONEY_THRESHOLD
    against = e["finding"]["result"] in AGAINST_BY_RESULT or bool(code.get("against"))
    s = 1 + (1 if (harm or money) else 0) + (1 if against else 0)
    return min(3, s), {"harm": harm, "money": money, "against": against}

def poc_points(code, S):
    """Returns (points, rows) — one row per scored type on the case."""
    rows = []
    types = code.get("poc") or []
    for i, t in enumerate(types):
        base = POC_TYPES[t["type"]][1]
        emul = EVIDENCE[t["evidence"]][1]
        pmul = PROXIMITY[t["who"]][1]
        w = 1.0 if i == 0 else SECONDARY_WEIGHT
        pts = base * emul * pmul * S * w if t["evidence"] != "E1" else 0.0
        rows.append({"type": t["type"], "type_name": POC_TYPES[t["type"]][0], "evidence": t["evidence"], "who": t["who"],
                     "role": "primary" if i == 0 else "secondary", "base": base, "e_mult": emul, "p_mult": pmul, "weight": w,
                     "points": round(pts, 2), "elements": t.get("elements", ""), "cleared_under_law": bool(t.get("cleared_under_law")), "note": t.get("note", "")})
    assert len(types) <= 1 + MAX_SECONDARY
    return round(sum(r["points"] for r in rows), 2), rows

def _d(s):
    """'YYYY', 'YYYY-MM' or 'YYYY-MM-DD' → date (first day of the period); None → None."""
    if not s: return None
    p = [int(x) for x in str(s).split("-")]
    return datetime.date(p[0], p[1] if len(p) > 1 else 1, p[2] if len(p) > 2 else 1)

def oa_case(e, oc, term_end):
    """Returns None if accountability was not owed, else a dict with the three dated items, time rules applied."""
    result = e["finding"]["result"]
    against = result in AGAINST_BY_RESULT or bool(oc.get("against"))
    owed = result in OWED_BY_RESULT or (result in OWED_IF_AGAINST and against)
    reason = ""
    if "owed" in oc: owed, reason = oc["owed"]
    if not owed: return {"owed": False, "reason": reason}
    fdate = _d(e["finding"].get("date"))
    items = {}; flags = []
    # consequence
    v, dt, what = oc["consequence"]; d = _d(dt)
    if d and d > term_end: flags.append("consequence after leaving office: not counted"); v = 0
    items["consequence"] = {"value": float(v), "date": dt, "what": what}
    # posture
    kind, dt, what = oc["posture"]; d = _d(dt)
    if kind == "owned" and result != "ADMISSION" and fdate and d and d > fdate:
        flags.append("owned only after the finding: counts as nothing"); kind = "nothing"
    if kind == "owned" and d and d > term_end: flags.append("after leaving office: counts as nothing"); kind = "nothing"
    items["posture"] = {"kind": kind, "value": POSTURE_VALUE[kind], "date": dt, "what": what}
    # change
    v, dt, what = oc["change"]; d = _d(dt)
    if v and d and d > term_end: flags.append("change after leaving office: not counted"); v = 0
    if v and oc.get("repeat_of"): flags.append("the conduct recurred: change not counted"); v = 0
    items["change"] = {"value": float(v), "date": dt, "what": what}
    score = (items["consequence"]["value"] + items["posture"]["value"] + items["change"]["value"]) / 3.0
    return {"owed": True, "reason": reason, "items": items, "score": round(score, 4), "flags": flags}

def band_oa(score):
    for lo, name, line in OA_BANDS:
        if score >= lo: return name, line
    return OA_BANDS[-1][1], OA_BANDS[-1][2]

def band_poc(ledger):
    """Structural band. Only adjudicated or admitted acts (E4, E3) count toward the band tests;
    documented-but-unruled acts (E2) score points but never move the band."""
    scored = [r for r in ledger if r["points"] > 0 and r["evidence"] in ("E4", "E3")]
    if not scored: return "None", POC_BANDS[0][1], {}
    leader_types = {r["type"] for r in scored if r["who"] == "him"}
    leader_cases = {r["case"] for r in scored if r["who"] == "him"}
    all_cases = {r["case"] for r in scored}
    obstruction = any(r["type"] == "T6" for r in scored)
    deception = any(r["type"] == "T5" for r in scored)
    repeat = any(r.get("repeat_after_finding") for r in scored)
    facts = {"leader_cases": len(leader_cases), "leader_types": sorted(leader_types), "cases": len(all_cases),
             "obstruction_proven": obstruction, "false_statements_proven": deception, "repeat_after_adverse_finding": repeat}
    if len(leader_cases) == 0: return "Isolated", POC_BANDS[1][1], facts
    pattern = len(leader_types) >= 3 or repeat
    if pattern and obstruction and deception and repeat: return "Systemic", POC_BANDS[4][1], facts
    if pattern: return "Pattern", POC_BANDS[3][1], facts
    if len(leader_cases) >= 2 or len(all_cases) >= 4: return "Repeated", POC_BANDS[2][1], facts
    return "Isolated", POC_BANDS[1][1], facts

def compute(dataset, codes, oa_codes):
    entries = dataset["entries"]; by_id = {e["id"]: e for e in entries}
    for cs in (codes, oa_codes):
        missing = [e["id"] for e in entries if e["id"] not in cs]; extra = [k for k in cs if k not in by_id]
        assert not missing and not extra, (missing, extra)
    term = dataset["subject"]; term_end = datetime.date.fromisoformat(term["term_end"])
    years = (term_end - datetime.date.fromisoformat(term["term_start"])).days / 365.25

    cases = []; ledger = []; listed = []
    for e in entries:
        c = codes[e["id"]]; oc = oa_codes[e["id"]]
        S, sfacts = severity(e, {**c, "against": c.get("against") or oc.get("against"), "harm": c.get("harm") or oc.get("harm")})
        oa = oa_case(e, {**oc, "against": c.get("against") or oc.get("against")}, term_end)
        pts, rows = poc_points(c, S)
        for r in rows:
            r.update({"case": e["id"], "headline": e["plain"]["headline"], "years": e["years"], "who_case": e["who"], "S": S,
                      "repeat_after_finding": bool(c.get("repeat_after_finding")) if r["role"] == "primary" else False})
            (ledger if r["evidence"] != "E1" else listed).append(r)
        cases.append({"id": e["id"], "no": e["no"], "headline": e["plain"]["headline"], "who": e["who"], "subject_key": e["subject_key"], "years": e["years"],
                      "label": e["plain"]["label"], "result": e["finding"]["result"], "result_class": e["result_class"], "S": S, "S_facts": sfacts,
                      "oa": oa, "repeat_of": oc.get("repeat_of"), "poc_points": pts, "poc_rows": rows, "poc_note": c.get("poc_note", "")})

    # OA aggregate — over owed cases only, weighted by S
    owed = [x for x in cases if x["oa"]["owed"]]
    def agg(sel):
        den = sum(x["S"] for x in sel)
        return round(100 * sum(x["S"] * x["oa"]["score"] for x in sel) / den, 1) if den else None
    def item_agg(sel, k):
        den = sum(x["S"] for x in sel)
        return round(100 * sum(x["S"] * x["oa"]["items"][k]["value"] for x in sel) / den, 1) if den else None
    oa_score = agg(owed) if owed else 0.0
    name, line = band_oa(oa_score)
    cons = [x["oa"]["items"]["consequence"]["value"] for x in owed]; post = [x["oa"]["items"]["posture"]["kind"] for x in owed]
    oa = {"score": oa_score, "band": name, "band_line": line, "owed": len(owed), "not_owed": len(cases) - len(owed),
          "items": {k: {"name": OA_ITEMS[k][0], "line": OA_ITEMS[k][1], "score": item_agg(owed, k)} for k in OA_ITEMS},
          "by_who": {w: agg([x for x in owed if x["subject_key"] == w]) for w in ("pm", "gov", "min")},
          "owed_by_who": {w: sum(1 for x in owed if x["subject_key"] == w) for w in ("pm", "gov", "min")},
          "consequence_on_him": sum(1 for v in cons if v == 1), "consequence_on_others": sum(1 for v in cons if v == 0.5), "consequence_none": sum(1 for v in cons if v == 0),
          "owned": post.count("owned"), "fought": post.count("fought"), "silent": post.count("nothing"),
          "changed": sum(1 for x in owed if x["oa"]["items"]["change"]["value"] == 1), "repeats": sorted(x["id"] for x in owed if x.get("repeat_of")),
          "fought_cases": sorted(x["id"] for x in owed if x["oa"]["items"]["posture"]["kind"] == "fought"),
          "owned_cases": sorted(x["id"] for x in owed if x["oa"]["items"]["posture"]["kind"] == "owned"),
          "changed_cases": sorted(x["id"] for x in owed if x["oa"]["items"]["change"]["value"] == 1),
          "time_flags": {x["id"]: x["oa"]["flags"] for x in owed if x["oa"]["flags"]},
          "term_end": term["term_end"]}

    # POC aggregate
    total = round(sum(r["points"] for r in ledger), 1)
    band, band_line, facts = band_poc(ledger)
    by_type = {t: round(sum(r["points"] for r in ledger if r["type"] == t), 1) for t in POC_TYPES}
    by_who = {w: round(sum(r["points"] for r in ledger if r["who"] == w), 1) for w in PROXIMITY}
    by_ev = {g: sum(1 for r in ledger if r["evidence"] == g) for g in ("E4", "E3", "E2")}
    poc = {"points": total, "per_year": round(total / years, 1), "leader_major_acts": round(total / LEADER_MAJOR_ACT, 1),
           "band": band, "band_line": band_line, "band_facts": facts,
           "scored_acts": len(ledger), "scored_cases": len({r["case"] for r in ledger}), "listed_unexamined": len(listed),
           "cleared_under_law": sorted({r["case"] for r in ledger if r["cleared_under_law"]}),
           "by_type": by_type, "by_who": by_who, "by_evidence": by_ev,
           "ledger": sorted(ledger, key=lambda r: -r["points"]), "listed": listed}

    return {"scales_version": "1.1.0", "computed": datetime.date.today().isoformat(), "subject": term, "years_in_office": round(years, 2),
            "oa": oa, "poc": poc, "cases": cases,
            "definitions": {"oa_items": {k: {"name": v[0], "line": v[1], "rubric": v[2]} for k, v in OA_ITEMS.items()},
                            "oa_owed": "A body found against the leader, the government or a minister, or they admitted the fault. Cleared, upheld, never-examined and cost-only cases are out: neither for nor against.",
                            "oa_time": "Nothing after the last day in office counts. Owning it counts only before the finding. Cooperating with a process the law requires is not owning it.",
                            "oa_bands": [{"min": lo, "name": n, "line": l} for lo, n, l in OA_BANDS],
                            "poc_types": {k: {"name": v[0], "base": v[1], "elements": v[2]} for k, v in POC_TYPES.items()},
                            "evidence": {k: {"name": v[0], "multiplier": v[1], "meaning": v[2]} for k, v in EVIDENCE.items()},
                            "proximity": {k: {"name": v[0], "multiplier": v[1]} for k, v in PROXIMITY.items()},
                            "severity": {"rule": "S = 1 + [harm or ≥$10M public money] + [a body found against them], capped at 3", "money_threshold": MONEY_THRESHOLD},
                            "secondary_weight": SECONDARY_WEIGHT, "leader_major_act_points": LEADER_MAJOR_ACT,
                            "poc_bands": [{"name": n, "test": t} for n, t in POC_BANDS]}}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
    from codes_trudeau import CODES
    from oa_trudeau import OA as OA_CODES
    d = json.load(open(os.path.join(here, "..", "out", "trudeau.json"), encoding="utf-8"))
    r = compute(d, CODES, OA_CODES)
    out = os.path.join(here, "..", "out", "scales_trudeau.json")
    json.dump(r, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    oa, poc = r["oa"], r["poc"]
    print(f"OA  {oa['score']}  {oa['band']}   owed={oa['owed']} (pm {oa['owed_by_who']['pm']} gov {oa['owed_by_who']['gov']} min {oa['owed_by_who']['min']})  "
          f"consequence={oa['items']['consequence']['score']} posture={oa['items']['posture']['score']} change={oa['items']['change']['score']}  "
          f"by who: pm={oa['by_who']['pm']} gov={oa['by_who']['gov']} min={oa['by_who']['min']}")
    print(f"    on him {oa['consequence_on_him']} · on others {oa['consequence_on_others']} · none {oa['consequence_none']} | owned {oa['owned']} · fought {oa['fought']} · silent {oa['silent']} | changed {oa['changed']} · repeats {len(oa['repeats'])}")
    if oa["time_flags"]: print("    time flags:", oa["time_flags"])
    print(f"POC {poc['points']} pts  {poc['band']}   acts={poc['scored_acts']} cases={poc['scored_cases']} listed={poc['listed_unexamined']} "
          f"per_year={poc['per_year']} LMA={poc['leader_major_acts']}  by_type={poc['by_type']}  by_who={poc['by_who']}  ev={poc['by_evidence']}")
    print("facts:", poc["band_facts"])
    for row in poc["ledger"]:
        print(f"  {row['points']:>5}  {row['type']} {row['evidence']} {row['who']:<10} S{row['S']} {row['role'][:3]}  {row['case']}")
