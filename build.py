# -*- coding: utf-8 -*-
"""Build index.html and trudeau.json from data_trudeau.py + plain_trudeau.py."""
import json, html, re, datetime, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from data_trudeau import ENTRIES, SUBJECT, CABINET_DEPARTURES, PM, GOV, MIN
from plain_trudeau import PLAIN, CLASS_PLAIN, GROUPS
from said_trudeau import SAID

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "out")
os.makedirs(OUT_DIR, exist_ok=True)
GENERATED = "September 17, 2026"

RESULT_META = {
    "VIOLATION_FOUND":          ("critical",   "Broke the ethics law"),
    "COURT_AGAINST_GOVERNMENT": ("critical",   "Court: illegal"),
    "AUDIT_ADVERSE":            ("warning",    "Audit"),
    "INQUIRY_FINDING":          ("warning",    "Inquiry"),
    "BROKEN_COMMITMENT":        ("warning",    "Promise broken"),
    "CHARGES":                  ("proceeding", "Charged"),
    "CHARGES_STAYED":           ("proceeding", "Case collapsed"),
    "RESIGNATION":              ("proceeding", "Quit / pushed out"),
    "CLEARED":                  ("good",       "Cleared"),
    "COURT_FOR_GOVERNMENT":     ("good",       "Upheld by court"),
    "ADMISSION":                ("neutral",    "Admitted / reversed"),
    "UNADJUDICATED":            ("neutral",    "Never investigated"),
    "RECORD":                   ("neutral",    "On the record"),
}
CLASS_ORDER = ["critical", "warning", "proceeding", "neutral", "good"]
SUBJECT_KEY = {PM: "pm", GOV: "gov", MIN: "min"}
WHO = {PM: "Trudeau himself", GOV: "His government", MIN: "His ministers & MPs"}
BIG_ORDER = ["aga-khan-vacation", "snc-lavalin-affair", "emergencies-act-2022", "we-charity", "arrivecan",
             "sdtc-green-fund", "foreign-interference-response", "vance-allegations-2018", "mark-norman-prosecution",
             "covid-benefit-overpayments", "phoenix-pay-system", "blackface-images"]

MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
MON = [m[:3] for m in MONTHS]

def esc(s): return html.escape(s, quote=True) if s else ""
def parse_date(d):
    if not d: return None, None
    p = d.split("-")
    if len(p) == 1: return datetime.date(int(p[0]), 1, 1), "y"
    if len(p) == 2: return datetime.date(int(p[0]), int(p[1]), 1), "m"
    return datetime.date(int(p[0]), int(p[1]), int(p[2])), "d"
def fmt_long(d):
    dt, prec = parse_date(d)
    if not dt: return ""
    if prec == "y": return str(dt.year)
    if prec == "m": return f"{MONTHS[dt.month-1]} {dt.year}"
    return f"{MONTHS[dt.month-1]} {dt.day}, {dt.year}"
def years(a, b):
    ya = parse_date(a)[0].year
    yb = parse_date(b)[0].year if b else None
    if not yb: return f"{ya} –"
    return str(ya) if ya == yb else f"{ya}–{yb}"
def to_ordinal(dt): return (dt - datetime.date(2015, 1, 1)).days
def is_none(s): return s.strip().lower().startswith(("nothing", "none"))

# ── normalize ──
entries = []
missing = [e["id"] for e in ENTRIES if e["id"] not in PLAIN]
assert not missing, f"plain layer missing: {missing}"
for e in ENTRIES:
    e = dict(e)
    cls, generic = RESULT_META[e["finding"]["result"]]
    p = PLAIN[e["id"]]
    e["result_class"] = cls
    e["result_generic"] = generic
    e["subject_key"] = SUBJECT_KEY[e["subject"]]
    e["who"] = WHO[e["subject"]]
    e["years"] = years(e["date_start"], e.get("date_end"))
    e["plain"] = {"headline": p["headline"], "telling": p["plain"], "found": p["found"], "him": p["him"],
                  "others": p["others"], "cost": p["cost"], "label": p["label"]}
    e["big"] = e["id"] in BIG_ORDER
    e["said"] = SAID.get(e["id"])
    e.setdefault("secondary", [])
    for gi, (gkey, gtitle, gblurb, pred) in enumerate(GROUPS):
        if pred(e): e["group"] = gkey; e["group_index"] = gi; break
    else: raise SystemExit(f"no group for {e['id']}")
    entries.append(e)
entries.sort(key=lambda e: (parse_date(e["date_start"])[0], e["title"]))
for i, e in enumerate(entries, 1): e["no"] = i
by_id = {e["id"]: e for e in entries}

# ── stats ──
def count(pred): return sum(1 for e in entries if pred(e))
term_start = datetime.date.fromisoformat(SUBJECT["term_start"]); term_end = datetime.date.fromisoformat(SUBJECT["term_end"])
days_in_office = (term_end - term_start).days
stats = {
    "cases": len(entries),
    "by_subject": {k: count(lambda e, k=k: e["subject"] == k) for k in (PM, GOV, MIN)},
    "pm_broke_ethics_law": count(lambda e: e["subject"] == PM and e["finding"]["result"] == "VIOLATION_FOUND"),
    "ministers_broke_ethics_law": count(lambda e: e["subject"] == MIN and e["finding"]["result"] == "VIOLATION_FOUND"),
    "ruled_illegal": count(lambda e: e["finding"]["result"] == "COURT_AGAINST_GOVERNMENT"),
    "audits": count(lambda e: e["finding"]["result"] == "AUDIT_ADVERSE"),
    "inquiries": count(lambda e: e["finding"]["result"] == "INQUIRY_FINDING"),
    "cleared_or_upheld": count(lambda e: e["finding"]["result"] in ("CLEARED", "COURT_FOR_GOVERNMENT")),
    "never_investigated": count(lambda e: e["finding"]["result"] == "UNADJUDICATED"),
    "ministers_out": len(CABINET_DEPARTURES),
    "penalties_on_pm": 0,
    "total_fines_dollars": 200,
    "days_in_office": days_in_office,
    "by_class": {c: count(lambda e, c=c: e["result_class"] == c) for c in CLASS_ORDER},
    "cases_with_said_vs_record": count(lambda e: bool(e.get("said"))),
}

dataset = {
    "platform": "politaccount", "subject": SUBJECT, "generated": "2026-09-17", "current_as_of": "2026-09-17",
    "labels": {k: {"class": v[0], "plain": v[1]} for k, v in RESULT_META.items()},
    "class_plain": CLASS_PLAIN,
    "groups": [{"key": g[0], "title": g[1], "blurb": g[2]} for g in GROUPS],
    "stats": stats, "cabinet_departures": CABINET_DEPARTURES, "entries": entries,
}
with open(os.path.join(OUT_DIR, "trudeau.json"), "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

# ── HTML pieces ──
def tag(e):
    return f'<span class="tag tag-{e["result_class"]}"><i class="dot" aria-hidden="true"></i>{esc(e["plain"]["label"])}</span>'

def him_html(e):
    him = e["plain"]["him"]
    if is_none(him):
        first = re.match(r"(.+?[.!])(\s|$)", him); head = first.group(1) if first else him
        rest = him[len(head):].strip()
        return f'<p>{esc(head)}{("<small>"+esc(rest)+"</small>") if rest else ""}</p>', "none"
    return f"<p>{esc(him)}</p>", ""

def answers(e):
    p = e["plain"]; hh, cls = him_html(e)
    cost = p["cost"] or "No public bill on the record."
    return f'''<div class="answers">
  <div><span class="lbl">What they found</span><p>{esc(p["found"])}</p></div>
  <div><span class="lbl">What it cost you</span><p>{esc(cost)}</p></div>
  <div class="him {cls}"><span class="lbl">What happened to him</span>{hh}</div>
</div>'''

def said_html(e):
    sr = e.get("said")
    if not sr: return ""
    items = []
    for q in sr["said"]:
        body = f"“{esc(q['quote'])}”" if q.get("quote") else esc(q.get("said", ""))
        items.append(f'<li><span class="sd-meta">{esc(fmt_long(q["date"]))} · {esc(q["who"])}</span><span class="sd-q">{body}</span>'
                     f'<a class="sd-src" href="{esc(q["src_url"])}" target="_blank" rel="noopener">{esc(q["src_title"])}</a></li>')
    return f'''<div class="saidrec">
  <div class="sd-said"><span class="lbl">Said</span><ol>{"".join(items)}</ol></div>
  <div class="sd-rec rec-{e["result_class"]}"><span class="lbl">The record</span><p>{esc(sr["record"])}</p></div>
</div>'''

def evidence(e, eid):
    f = e["finding"]; p = e["plain"]
    src = esc(f["body"]) + (f" · {esc(fmt_long(f['date']))}" if f.get("date") else "")
    secondary = "".join(f'<span class="chip">{esc(s)}</span>' for s in e["secondary"])
    srcs = []
    for s in e["sources"]:
        meta = esc(s["publisher"]) + (f" · {esc(fmt_long(s['date']))}" if s.get("date") else "")
        prim = '<span class="prim">Official</span>' if s.get("primary") else ""
        srcs.append(f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s["title"])}</a><span class="src-meta">{meta}{prim}</span></li>')
    dates = esc(fmt_long(e["date_start"])) + (f' to {esc(fmt_long(e["date_end"]))}' if e.get("date_end") else ", still open")
    return f'''<div class="evidence" id="{eid}" hidden>
  <div>
    <span class="lbl">In the deciding body’s own words</span>
    <blockquote class="quote quote-{e["result_class"]}">{esc(f["quote"])}</blockquote>
    <p class="qsrc">{src}</p>
    {("<div class='chips'>"+secondary+"</div>") if secondary else ""}
  </div>
  <div class="ev-side">
    <span class="lbl">What happened to everyone else</span><p>{esc(p["others"])}</p>
    <span class="lbl">Where it stands, September 2026</span><p>{esc(e["status"])}</p>
    <span class="lbl">Dates</span><p>{dates}</p>
    <span class="lbl">Sources</span><ol class="sources">{"".join(srcs)}</ol>
  </div>
</div>'''

def big_card(e):
    p = e["plain"]; eid = f"ev-big-{e['id']}"
    return f'''<article class="big cls-{e["result_class"]}" id="big-{e["id"]}">
  <div class="meta">{tag(e)}<span class="who">{esc(e["who"])} · {esc(e["years"])}</span></div>
  <h3>{esc(p["headline"])}</h3>
  <p class="plain">{esc(p["telling"])}</p>
  {answers(e)}
  {said_html(e)}
  <button class="ev-btn" type="button" aria-expanded="false" aria-controls="{eid}">Show the evidence</button>
  {evidence(e, eid)}
</article>'''

def row(e):
    p = e["plain"]; eid = f"ev-row-{e['id']}"
    him_short = re.match(r"(.+?[.!])(\s|$)", p["him"]); him_short = him_short.group(1) if him_short else p["him"]
    return f'''<article class="case" id="c-{e["id"]}" data-id="{e["id"]}" data-subject="{e["subject_key"]}" data-group="{e["group"]}" data-date="{to_ordinal(parse_date(e["date_start"])[0])}">
  <button class="case-head" type="button" aria-expanded="false" aria-controls="cb-{e["id"]}">
    <span class="tagcol">{tag(e)}<span class="who">{esc(e["who"])} · {esc(e["years"])}</span></span>
    <span class="hl">{esc(p["headline"])}</span>
    <span class="himcol"><b>Him</b>{esc(him_short)}</span>
    <span class="chev" aria-hidden="true"></span>
  </button>
  <div class="case-body" id="cb-{e["id"]}" hidden>
    <p class="plain">{esc(p["telling"])}</p>
    {answers(e)}
    {said_html(e)}
    <button class="ev-btn" type="button" aria-expanded="false" aria-controls="{eid}">Show the evidence</button>
    {evidence(e, eid)}
  </div>
</article>'''

def group_head(gkey, gtitle, gblurb, n):
    return f'<div class="ghead" data-group="{gkey}"><h3>{esc(gtitle)}<span class="n">{n}</span></h3><p>{esc(gblurb)}</p></div>'

def table_row(e):
    p = e["plain"]
    him = p["him"]; first = re.match(r"(.+?[.!])(\s|$)", him); head = first.group(1) if first else him; rest = him[len(head):].strip()
    him_html_ = (f"<b>{esc(head)}</b> {esc(rest)}" if is_none(him) else esc(him))
    return (f'<tr><td><a href="#c-{e["id"]}" class="tlink" data-id="{e["id"]}">{esc(e["title"])}</a><div class="src-meta">{esc(e["who"])} · {esc(e["years"])}</div></td>'
            f'<td>{tag(e)}<div style="margin-top:6px">{esc(p["found"])}</div></td>'
            f'<td>{him_html_}</td><td>{esc(p["others"])}</td></tr>')

# ── timeline ──
T0 = datetime.date(2015, 7, 1); T1 = datetime.date(2025, 7, 1); W, H = 1000, 236; LX, RX = 160, 992
LANES = [(PM, 52), (GOV, 122), (MIN, 192)]
def xpos(dt): return LX + (RX - LX) * (dt - T0).days / (T1 - T0).days
def mark(e, cx, cy):
    cls = e["result_class"]; c = f"var(--c-{cls})"
    title = f'<title>{esc(e["plain"]["headline"])} — {esc(e["plain"]["label"])}</title>'
    common = f'class="mk mk-{cls}" data-id="{e["id"]}" tabindex="0" role="button" aria-label="{esc(e["plain"]["headline"])}"'
    if cls == "critical": return f'<rect {common} x="{cx-5.5:.1f}" y="{cy-5.5:.1f}" width="11" height="11" fill="{c}" stroke="var(--surface)" stroke-width="2">{title}</rect>'
    if cls == "warning": return f'<rect {common} x="{cx-5:.1f}" y="{cy-5:.1f}" width="10" height="10" transform="rotate(45 {cx:.1f} {cy:.1f})" fill="{c}" stroke="var(--surface)" stroke-width="2">{title}</rect>'
    if cls == "good": return f'<polygon {common} points="{cx:.1f},{cy-6.5:.1f} {cx+6:.1f},{cy+4.5:.1f} {cx-6:.1f},{cy+4.5:.1f}" fill="{c}" stroke="var(--surface)" stroke-width="2">{title}</polygon>'
    if cls == "neutral": return f'<circle {common} cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="var(--surface)" stroke="{c}" stroke-width="2">{title}</circle>'
    return f'<circle {common} cx="{cx:.1f}" cy="{cy:.1f}" r="5.5" fill="{c}" stroke="var(--surface)" stroke-width="2">{title}</circle>'
def timeline_svg():
    parts = [f'<svg class="tl" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Timeline of all cases, 2015 to 2025, in three rows: Trudeau himself, his government, his ministers and MPs">']
    for y in range(2016, 2026):
        x = xpos(datetime.date(y, 1, 1))
        parts.append(f'<line x1="{x:.1f}" y1="22" x2="{x:.1f}" y2="{H-24}" class="grid"/><text x="{x:.1f}" y="{H-8}" class="tick" text-anchor="middle">{y}</text>')
    for d, lab, anchor in ((term_start, "Sworn in", "start"), (term_end, "Left office", "end")):
        x = xpos(d)
        parts.append(f'<line x1="{x:.1f}" y1="14" x2="{x:.1f}" y2="{H-24}" class="bound"/><text x="{x + (4 if anchor=="start" else -4):.1f}" y="12" class="tick" text-anchor="{anchor}">{lab} · {MON[d.month-1]} {d.year}</text>')
    for name, cy in LANES:
        parts.append(f'<line x1="{LX}" y1="{cy}" x2="{RX}" y2="{cy}" class="lane"/><text x="{LX-10}" y="{cy+4}" class="lane-label" text-anchor="end">{esc(WHO[name])}</text>')
    lane_y = {n: y for n, y in LANES}; placed = {n: [] for n, _ in LANES}
    for e in entries:
        dt, _ = parse_date(e["date_start"]); cx = xpos(dt); cy = lane_y[e["subject"]]; offset = 0
        for (px, po) in placed[e["subject"]]:
            if abs(px - cx) < 12 and po == offset: offset += 1
        dy = [0, -14, 14, -28, 28][min(offset, 4)]
        placed[e["subject"]].append((cx, offset)); parts.append(mark(e, cx, cy + dy))
    parts.append('</svg>'); return "".join(parts)

# ── assemble ──
bigs = "".join(big_card(by_id[i]) for i in BIG_ORDER)
list_html = []
for gkey, gtitle, gblurb, pred in GROUPS:
    rows = sorted([e for e in entries if e["group"] == gkey], key=lambda e: parse_date(e["date_start"])[0])
    list_html.append(group_head(gkey, gtitle, gblurb, len(rows)))
    list_html.extend(row(e) for e in rows)
table = "".join(table_row(e) for e in sorted(entries, key=lambda e: (e["group_index"], parse_date(e["date_start"])[0])))
departures = "".join(f'<li><span class="mono">{esc(fmt_long(d["date"]))}</span> {esc(d["name"])} — {esc(d["how"])}</li>' for d in CABINET_DEPARTURES)

page = open(os.path.join(os.path.dirname(__file__), "template.html"), encoding="utf-8").read()
repl = {
    "{{GENERATED}}": GENERATED, "{{N}}": str(stats["cases"]), "{{DAYS}}": f"{days_in_office:,}",
    "{{PM_CONTRAVENTIONS}}": str(stats["pm_broke_ethics_law"]), "{{MIN_CONTRAVENTIONS}}": str(stats["ministers_broke_ethics_law"]),
    "{{COURT_AGAINST}}": str(stats["ruled_illegal"]), "{{AUDITS}}": str(stats["audits"]), "{{INQUIRIES}}": str(stats["inquiries"]),
    "{{CLEARED}}": str(stats["cleared_or_upheld"]), "{{DEPARTURES}}": str(stats["ministers_out"]), "{{UNADJ}}": str(stats["never_investigated"]),
    "{{N_BIG}}": str(len(BIG_ORDER)), "{{BIG}}": bigs, "{{TIMELINE}}": timeline_svg(), "{{LIST}}": "".join(list_html), "{{TABLE}}": table,
    "{{DEPARTURE_LIST}}": departures, "{{N_SAID}}": str(stats["cases_with_said_vs_record"]),
    "{{N_CRIT}}": str(stats["by_class"]["critical"]), "{{N_WARN}}": str(stats["by_class"]["warning"]), "{{N_PROC}}": str(stats["by_class"]["proceeding"]),
    "{{N_GOOD}}": str(stats["by_class"]["good"]), "{{N_NEUT}}": str(stats["by_class"]["neutral"]),
}
for k, v in repl.items(): page = page.replace(k, v)
leftover = re.findall(r"\{\{[A-Z_]+\}\}", page); assert not leftover, leftover
with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f: f.write(page)
print(f"cases={stats['cases']} big={len(BIG_ORDER)} classes={json.dumps(stats['by_class'])} html={len(page)/1024:.0f}KB")
