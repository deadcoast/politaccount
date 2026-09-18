# -*- coding: utf-8 -*-
"""Render out/scales.html from out/scales_trudeau.json (+ trudeau.json for links)."""
import json, os, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "out")
R = json.load(open(os.path.join(OUT, "scales_trudeau.json"), encoding="utf-8"))
D = json.load(open(os.path.join(OUT, "trudeau.json"), encoding="utf-8"))
RECORD_URL = "https://deadcoast.github.io/politaccount/"
def esc(s): return html.escape(str(s), quote=True) if s is not None else ""
def n1(x): return f"{x:.1f}"

OA, POC, DEF = R["oa"], R["poc"], R["definitions"]
cases = R["cases"]; by_id = {c["id"]: c for c in cases}
OA_BAND_CLASS = {"Fully accountable": "good", "Accountable": "proceeding", "Partly accountable": "warning", "Others paid": "critical", "Unaccountable": "critical"}
POC_BAND_CLASS = {"None": "good", "Isolated": "proceeding", "Repeated": "warning", "Pattern": "critical", "Systemic": "critical"}
PIP_CLASS = {0: "critical", 1: "critical", 2: "warning", 3: "proceeding", 4: "good"}
WHO_NAME = {"pm": "Trudeau himself", "gov": "His government", "min": "His ministers & MPs"}
PROX_SHORT = {"him": "Him", "office": "His office / cabinet", "minister": "A minister", "government": "A department"}
EV_SHORT = {"E4": "Adjudicated", "E3": "Admitted / own record", "E2": "Documented", "E1": "Never examined"}

n_e = POC["by_evidence"]
owed_cases = [c for c in cases if c["oa"]["owed"]]; not_owed = [c for c in cases if not c["oa"]["owed"]]
term_end_long = datetime.date.fromisoformat(OA["term_end"]).strftime("%B %-d, %Y")
CONS_MARK = {1.0: ("1", "good", "on him"), 0.5: ("½", "warning", "on others"), 0.0: ("0", "critical", "nobody")}
POST_MARK = {"owned": ("owned", "good"), "nothing": ("nothing", "neutral"), "fought": ("fought", "critical")}
CHG_MARK = {1.0: ("1", "good", "changed"), 0.0: ("0", "critical", "nothing")}

# ── pieces ──
def bar(label, value, maxv, sub="", cls="", n=None):
    pct = 0 if not maxv else max(0, min(100, 100 * value / maxv))
    val = n1(value) if isinstance(value, float) else str(value)
    return f'''<div class="bar {cls}"><div class="bar-l"><span class="bar-name">{esc(label)}</span>{f'<span class="bar-sub">{esc(sub)}</span>' if sub else ''}</div>
<div class="bar-t"><i style="width:{pct:.1f}%"></i></div><span class="bar-v mono">{val}{f'<small>{esc(n)}</small>' if n else ''}</span></div>'''

def pips(v):
    if v is None: return '<span class="pips na" title="Not applicable">—</span>'
    cls = PIP_CLASS[v]
    return f'<span class="pips p-{cls}" title="{v} of 4">' + "".join(f'<i class="{"on" if i < v else ""}"></i>' for i in range(4)) + f'<b class="mono">{v}</b></span>'

def oa_scale_strip(score):
    segs = []
    bands = sorted(DEF["oa_bands"], key=lambda b: b["min"])
    for i, b in enumerate(bands):
        lo = b["min"]; hi = bands[i + 1]["min"] if i + 1 < len(bands) else 100
        segs.append(f'<div class="seg seg-{OA_BAND_CLASS[b["name"]]}" style="width:{hi-lo}%"><span>{esc(b["name"])}</span><small class="mono">{lo}–{hi}</small></div>')
    return f'<div class="strip"><div class="strip-segs">{"".join(segs)}</div><div class="strip-mark" style="left:{score}%"><b class="mono">{n1(score)}</b></div></div>'

# ── results ──
oa_items = "".join(bar(OA["items"][k]["name"], OA["items"][k]["score"], 100, sub=OA["items"][k]["line"], n="/100") for k in ("consequence", "posture", "change"))
oa_facts = f'''<div class="ofacts">
<div class="ofrow"><span class="lbl">Consequence</span>
  <div class="hero"><b class="mono s-critical">{OA["consequence_on_him"]}<small> of {OA["owed"]}</small></b><span>landed on him</span></div>
  <div><b class="mono">{OA["consequence_on_others"]}</b><span>on a minister or official</span></div>
  <div><b class="mono">{OA["consequence_none"]}</b><span>on no one</span></div></div>
<div class="ofrow"><span class="lbl">Posture</span>
  <div><b class="mono s-critical">{OA["fought"]}</b><span>fought</span></div>
  <div><b class="mono">{OA["silent"]}</b><span>said nothing</span></div>
  <div><b class="mono">{OA["owned"]}</b><span>owned before a ruling</span></div></div>
<div class="ofrow"><span class="lbl">Change</span>
  <div><b class="mono">{OA["changed"]}</b><span>changed, in office</span></div>
  <div><b class="mono s-critical">{len(OA["repeats"])}</b><span>same conduct again</span></div></div>
</div>'''
oa_who = "".join(f'<div><span class="lbl">{esc(WHO_NAME[w])}</span><b class="mono">{n1(OA["by_who"][w])}</b></div>' for w in ("pm", "gov", "min"))
poc_types = "".join(bar(DEF["poc_types"][t]["name"], POC["by_type"][t], max(POC["by_type"].values()), sub=f"{t} · base {DEF['poc_types'][t]['base']:g}", n=" pts") for t in sorted(POC["by_type"], key=lambda t: -POC["by_type"][t]))
poc_who = "".join(f'<div><span class="lbl">{esc(DEF["proximity"][w]["name"].split(":")[0].split(",")[0])}</span><b class="mono">{n1(POC["by_who"][w])}</b></div>' for w in ("him", "office", "minister", "government"))

# ── band ladder for POC ──
f = POC["band_facts"]
poc_tests = [
 ("None", "No proven corrupt act on the record.", f["cases"] == 0),
 ("Isolated", "Proven acts, none by the leader personally.", f["cases"] > 0 and f["leader_cases"] == 0),
 ("Repeated", "More than one proven act by the leader personally, or one by the leader and three or more across the government.", f["leader_cases"] >= 2 or (f["leader_cases"] >= 1 and f["cases"] >= 4)),
 ("Pattern", "Proven acts by the leader personally in three or more types, or the same type again after an adverse finding.", len(f["leader_types"]) >= 3 or f["repeat_after_adverse_finding"]),
 ("Systemic", "A pattern, plus obstruction of scrutiny and false statements to the public both proven, plus a repeat after an adverse finding.",
  (len(f["leader_types"]) >= 3 or f["repeat_after_adverse_finding"]) and f["obstruction_proven"] and f["false_statements_proven"] and f["repeat_after_adverse_finding"]),
]
ladder = "".join(f'''<div class="rung {"met" if met else ""} {"is" if name == POC["band"] else ""} rung-{POC_BAND_CLASS[name]}">
  <span class="rung-mark mono">{"met" if met else "—"}</span><span class="rung-name">{esc(name)}</span><span class="rung-test">{esc(test)}</span></div>''' for name, test, met in poc_tests)
type_names = ", ".join(f'{t} {DEF["poc_types"][t]["name"].lower()}' for t in f["leader_types"])
facts_html = f'''<div class="facts">
<div><span class="lbl">Proven acts by him, adjudicated or admitted</span><b class="mono">{f["leader_cases"]} cases</b><small>{esc(type_names)}</small></div>
<div><span class="lbl">Proven cases across the government</span><b class="mono">{f["cases"]}</b></div>
<div><span class="lbl">Obstruction of scrutiny proven</span><b class="mono">{"yes" if f["obstruction_proven"] else "no"}</b><small>SNC-Lavalin, WE Charity, the Winnipeg lab, the green fund</small></div>
<div><span class="lbl">False statements to the public proven</span><b class="mono">{"yes" if f["false_statements_proven"] else "no"}</b><small>Aga Khan, SNC-Lavalin, Tofino, Jamaica, three ministers</small></div>
<div><span class="lbl">Repeat after an adverse finding</span><b class="mono">{"yes" if f["repeat_after_adverse_finding"] else "no"}</b><small>The ethics law broken a second time after the first ruling</small></div>
</div>'''

# ── corruption ledger ──
def poc_row(r, i):
    c = by_id[r["case"]]
    chips = ""
    if r["cleared_under_law"]: chips += '<span class="chip chip-warn">Cleared under the Act · scored on the admitted facts</span>'
    if r["role"] == "secondary": chips += '<span class="chip">Second act on the same case · half weight</span>'
    calc = f'{r["base"]:g} × {r["e_mult"]:g} × {r["p_mult"]:g} × S{r["S"]}' + (f' × {r["weight"]:g}' if r["weight"] != 1 else "")
    return f'''<div class="lrow cls-{POC_BAND_CLASS["Pattern"] if r["points"] >= 6 else "neutral"}">
  <button class="lhead" type="button" aria-expanded="false" aria-controls="pl-{i}">
    <span class="lpts mono">{n1(r["points"])}</span>
    <span class="ltype"><b>{esc(r["type_name"])}</b><span class="lmeta mono">{r["type"]} · {esc(EV_SHORT[r["evidence"]])} · {esc(PROX_SHORT[r["who"]])} · S{r["S"]}</span></span>
    <span class="lcase"><a href="{RECORD_URL}#c-{esc(r["case"])}" target="_blank" rel="noopener" onclick="event.stopPropagation()">{esc(r["headline"])}</a><span class="lmeta">{esc(c["who"])} · {esc(r["years"])}</span></span>
    <span class="chev" aria-hidden="true"></span>
  </button>
  <div class="lbody" id="pl-{i}" hidden>
    <span class="lbl">The elements, on the record</span><p>{esc(r["elements"])}</p>
    {f'<p class="note">{esc(r["note"])}</p>' if r["note"] else ""}
    <div class="chips">{chips}<span class="chip mono">{calc} = {n1(r["points"])}</span></div>
  </div>
</div>'''
ledger_html = "".join(poc_row(r, i) for i, r in enumerate(POC["ledger"]))
listed_html = "".join(f'''<div class="listed"><span class="lbl">{esc(r["type_name"])} · never examined</span><a href="{RECORD_URL}#c-{esc(r["case"])}" target="_blank" rel="noopener">{esc(r["headline"])}</a><p>{esc(r["elements"])}</p></div>''' for r in POC["listed"])

# ── accountability ledger ──
def oa_row(c, i):
    o = c["oa"]; it = o["items"]; sc = o["score"] * 100
    scls = "critical" if sc < 20 else "warning" if sc < 40 else "neutral" if sc < 60 else "proceeding" if sc < 80 else "good"
    facts = c["S_facts"]; why = " · ".join(x for x, ok in (("harm on the record", facts["harm"]), ("≥ $10M public money", facts["money"]), ("a body found against them", facts["against"])) if ok) or "no aggravating fact"
    cm, cc, cl = CONS_MARK[it["consequence"]["value"]]; pm_, pc = POST_MARK[it["posture"]["kind"]]; gm, gc, gl = CHG_MARK[it["change"]["value"]]
    def cell(k, mark, cls, label):
        d = it[k].get("date"); dd = f' <span class="mono">{esc(d)}</span>' if d else ""
        return f'<div><span class="lbl">{esc(OA["items"][k]["name"])} · <b class="s-{cls}">{esc(label)}</b>{dd}</span><p>{esc(it[k]["what"])}</p></div>'
    rep = ""
    if c.get("repeat_of"):
        rep = '<p class="note">Recurred in: ' + ", ".join(f'<a href="{RECORD_URL}#c-{esc(x)}" target="_blank" rel="noopener">{esc(by_id[x]["headline"][:70])}…</a>' for x in c["repeat_of"]) + "</p>"
    flags = "".join(f'<p class="note">Time rule: {esc(f)}.</p>' for f in o["flags"])
    reason = f'<p class="note">Owed because: {esc(o["reason"])}</p>' if o["reason"] else ""
    return f'''<div class="arow" data-who="{c["subject_key"]}" data-score="{sc:.1f}" data-no="{c["no"]}">
  <button class="ahead" type="button" aria-expanded="false" aria-controls="al-{i}">
    <span class="ascore mono s-{scls}">{n1(sc)}</span>
    <span class="acase"><span class="ahl">{esc(c["headline"])}</span><span class="lmeta">{esc(c["who"])} · {esc(c["years"])} · <span class="mono">S{c["S"]}</span></span></span>
    <span class="amarks"><span class="mk mk-{cc}" title="Consequence: {cl}">{cm}</span><span class="mk mk-{pc}" title="Posture">{pm_}</span><span class="mk mk-{gc}" title="Change: {gl}">{gm}</span></span>
    <span class="chev" aria-hidden="true"></span>
  </button>
  <div class="abody" id="al-{i}" hidden>
    <div class="anotes">{cell("consequence", cm, cc, cl)}{cell("posture", pm_, pc, pm_)}{cell("change", gm, gc, gl)}</div>
    {reason}<p class="note">Weight S{c["S"]}: {esc(why)}.</p>{rep}{flags}
    <p class="note"><a href="{RECORD_URL}#c-{esc(c["id"])}" target="_blank" rel="noopener">Open the case on the record →</a></p>
  </div>
</div>'''
arows = "".join(oa_row(c, i) for i, c in enumerate(sorted(owed_cases, key=lambda c: (c["oa"]["score"], c["no"]))))
not_owed_html = "".join(f'''<div class="listed"><span class="lbl">{esc(c["label"])} · {esc(c["who"])} · {esc(c["years"])}</span><a href="{RECORD_URL}#c-{esc(c["id"])}" target="_blank" rel="noopener">{esc(c["headline"])}</a><p>{esc(c["oa"]["reason"] or "Not owed under the rule.")}</p></div>''' for c in not_owed)

# ── rules ──
def rubric(k):
    v = DEF["oa_items"][k]
    return f'<div class="rub"><h4>{esc(v["name"])}<span>{esc(v["line"])}</span></h4><ol>' + "".join(f'<li><b class="mono">{esc(s)}</b>{esc(txt)}</li>' for s, txt in v["rubric"].items()) + "</ol></div>"
rubrics = "".join(rubric(k) for k in ("consequence", "posture", "change"))
types_html = "".join(f'<div class="typ"><h4><span class="mono">{t}</span>{esc(v["name"])}<b class="mono">base {v["base"]:g}</b></h4><ol>' + "".join(f"<li>{esc(el)}</li>" for el in v["elements"]) + "</ol></div>" for t, v in DEF["poc_types"].items())
ev_html = "".join(f'<div class="kv"><span class="mono">{g} × {v["multiplier"]:g}</span><b>{esc(v["name"])}</b><p>{esc(v["meaning"])}</p></div>' for g, v in DEF["evidence"].items())
prox_html = "".join(f'<div class="kv"><span class="mono">× {v["multiplier"]:g}</span><b>{esc(v["name"])}</b></div>' for w, v in DEF["proximity"].items())
oa_bands_html = "".join(f'<div class="kv"><span class="mono">{b["min"]}–{100 if i == 0 else DEF["oa_bands"][i-1]["min"]}</span><b>{esc(b["name"])}</b><p>{esc(b["line"])}</p></div>' for i, b in enumerate(DEF["oa_bands"]))

computed = datetime.date.fromisoformat(R["computed"]).strftime("%B %-d, %Y")
term = R["subject"]

page = f'''<title>Politaccount · Scales</title>
<meta name="description" content="Two rating scales for Record 001, Justin Trudeau: Operational Accountability and Provable Observable Corruption, scored from {len(cases)} cases on the record, every point traced to a case and a source.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Serif:ital,wght@0,400;0,500;1,400&display=swap">
<style>
/* charcoal by default; light is an explicit choice from the toggle */
:root{{
  color-scheme:dark;
  --ground:#1F2123;--surface:#26282B;--surface-2:#2E3134;--rule:#3A3D41;--rule-strong:#585C62;
  --ink:#ECEAE4;--ink-2:#BDBBB4;--ink-3:#8C8B86;--accent:#E0596A;
  --c-critical:#E0596A;--c-warning:#C9A227;--c-proceeding:#6E8FE8;--c-good:#3FB06A;--c-neutral:#8E9196;
  --on-color:#1F2123;
  --sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--serif:"IBM Plex Serif",Georgia,"Times New Roman",serif;--mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}}
:root[data-theme="light"]{{
  color-scheme:light;
  --ground:#F2F1EE;--surface:#FAF9F7;--surface-2:#E9E7E2;--rule:#D3D0CA;--rule-strong:#A19D96;
  --ink:#1B1C1E;--ink-2:#48494C;--ink-3:#6C6D70;--accent:#A11C15;
  --c-critical:#A11C15;--c-warning:#8F6600;--c-proceeding:#3B5BA9;--c-good:#2E7D4F;--c-neutral:#6B7280;
  --on-color:#FFFFFF;
}}

*{{box-sizing:border-box}} [hidden]{{display:none!important}} html{{scroll-behavior:smooth}}
body{{margin:0;padding-inline:clamp(16px,4vw,44px);padding-block:0;background:var(--ground);color:var(--ink);font:16px/1.5 var(--sans);-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration-color:var(--rule-strong);text-underline-offset:2px}} a:hover{{text-decoration-color:var(--ink)}}
:focus-visible{{outline:2px solid var(--c-proceeding);outline-offset:2px}} button{{font:inherit;color:inherit}}
h1,h2,h3,h4{{margin:0;font-family:var(--sans);letter-spacing:-.01em;text-wrap:balance}}
.wrap{{max-width:1120px;margin-inline:auto}} section{{padding-block:44px;border-top:1px solid var(--rule);scroll-margin-top:64px}}
.sec-head{{display:flex;align-items:baseline;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:8px}} .sec-head h2{{font-size:30px;font-weight:700}}
.sec-sub{{font-size:16px;color:var(--ink-2);margin:0 0 22px;max-width:72ch}}
.lbl{{font:600 11px/1.2 var(--sans);letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3)}} .mono{{font-family:var(--mono);font-variant-numeric:tabular-nums}}
small{{font-size:.8em}} p{{margin:0}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}*{{transition:none!important}}}}

.masthead{{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:color-mix(in srgb,var(--ground) 90%,transparent);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--rule)}}
.masthead .wrap{{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:54px;flex-wrap:wrap;padding-block:8px}}
.brand{{display:flex;align-items:baseline;gap:14px;text-decoration:none}} .wordmark{{font:700 15px/1 var(--mono);letter-spacing:.22em;text-transform:uppercase}} .tagline{{font:italic 400 13.5px/1 var(--serif);color:var(--ink-2)}}
.nav{{display:flex;align-items:center;gap:2px;flex-wrap:wrap}} .nav a{{font:600 12.5px/1 var(--sans);text-decoration:none;padding:8px 10px;border-radius:3px;color:var(--ink-2)}} .nav a:hover{{background:var(--surface-2);color:var(--ink)}}
.theme-btn{{border:1px solid var(--rule);background:var(--surface);border-radius:3px;padding:7px 10px;font:600 12px/1 var(--sans);cursor:pointer;color:var(--ink-2)}}
@media (max-width:720px){{.tagline{{display:none}}.masthead{{position:static;backdrop-filter:none}}}}

#top{{border-top:0;padding-block:40px 32px}}
.eyebrow{{font:600 12px/1.3 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);margin-bottom:12px}} .eyebrow b{{color:var(--accent)}}
#top h1{{font-size:clamp(46px,7.5vw,84px);line-height:.98;letter-spacing:-.03em;font-weight:700}}
.sub{{font-size:18px;color:var(--ink-2);margin:12px 0 22px}}
.lede{{font-size:clamp(19px,2.3vw,24px);line-height:1.4;font-weight:500;max-width:34em;margin:0 0 10px}} .lede b{{color:var(--accent);font-weight:600}}
.lede-note{{font-size:14.5px;color:var(--ink-2);margin:0;max-width:66ch}}

/* results */
.results{{display:grid;grid-template-columns:1fr 1fr;gap:22px}} @media (max-width:860px){{.results{{grid-template-columns:1fr}}}}
.panel{{background:var(--surface);border:1px solid var(--rule);border-top:3px solid var(--ink);padding:22px 22px 18px;display:flex;flex-direction:column;gap:18px}}
.panel-critical{{border-top-color:var(--c-critical)}} .panel-warning{{border-top-color:var(--c-warning)}} .panel-proceeding{{border-top-color:var(--c-proceeding)}} .panel-good{{border-top-color:var(--c-good)}}
.panel-h{{display:flex;flex-direction:column;gap:6px}} .panel-h h3{{font-size:22px;font-weight:700}} .panel-h p{{color:var(--ink-2);font-size:14.5px;max-width:52ch}}
.score{{display:flex;align-items:flex-end;gap:16px;flex-wrap:wrap}}
.score .num{{font:700 clamp(58px,8vw,88px)/.9 var(--sans);letter-spacing:-.04em}} .score .num small{{font:500 16px/1 var(--mono);letter-spacing:0;color:var(--ink-3);margin-left:6px}}
.band{{display:inline-flex;flex-direction:column;gap:4px;padding:8px 12px;border:1.5px solid;border-radius:3px;max-width:34ch}}
.band b{{font:700 15px/1.1 var(--sans);letter-spacing:.02em;text-transform:uppercase}} .band span{{font-size:13px;line-height:1.35;color:var(--ink-2)}}
.band-critical{{border-color:var(--c-critical)}} .band-critical b{{color:var(--c-critical)}} .band-warning{{border-color:var(--c-warning)}} .band-warning b{{color:var(--c-warning)}}
.band-proceeding{{border-color:var(--c-proceeding)}} .band-proceeding b{{color:var(--c-proceeding)}} .band-good{{border-color:var(--c-good)}} .band-good b{{color:var(--c-good)}}
.bars{{display:flex;flex-direction:column;gap:10px}}
.bar{{display:grid;grid-template-columns:minmax(0,1fr) 44%;grid-template-rows:auto auto;gap:2px 12px;align-items:center}}
.bar-l{{grid-row:1/3;display:flex;flex-direction:column}} .bar-name{{font-weight:600;font-size:14.5px}} .bar-sub{{font-size:12.5px;color:var(--ink-3);line-height:1.35}}
.bar-t{{height:9px;background:var(--surface-2);border-radius:2px;overflow:hidden;align-self:end}} .bar-t i{{display:block;height:100%;background:var(--ink)}}
.bar-v{{font-size:13px;font-weight:600;align-self:start}} .bar-v small{{color:var(--ink-3);font-weight:400;margin-left:2px}}
.who{{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;padding-top:14px;border-top:1px solid var(--rule)}}
.who div{{display:flex;flex-direction:column;gap:3px}} .who b{{font-size:22px;font-weight:600}}
.facts-line{{font-size:13.5px;color:var(--ink-2);line-height:1.5}} .facts-line b{{color:var(--ink);font-weight:600}}

/* bands */
.bands{{display:grid;grid-template-columns:1fr 1fr;gap:28px}} @media (max-width:860px){{.bands{{grid-template-columns:1fr}}}}
.bands h3{{font-size:18px;margin-bottom:12px}}
.strip{{position:relative;padding-top:30px;padding-bottom:6px}} .strip-segs{{display:flex;height:34px;border-radius:3px;overflow:hidden}}
.seg{{display:flex;flex-direction:column;justify-content:center;padding-inline:8px;color:var(--on-color);font:600 11px/1.1 var(--sans);letter-spacing:.04em;text-transform:uppercase;overflow:hidden;white-space:nowrap}} .seg small{{opacity:.8;font-weight:500;letter-spacing:0;text-transform:none}}
.seg-good{{background:var(--c-good)}} .seg-proceeding{{background:var(--c-proceeding)}} .seg-warning{{background:var(--c-warning)}} .seg-critical{{background:var(--c-critical)}} .seg-critical+.seg-critical{{filter:brightness(.8)}}
.strip-mark{{position:absolute;top:0;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center}} .strip-mark b{{font-size:15px;font-weight:600;background:var(--ink);color:var(--ground);padding:3px 7px;border-radius:3px}}
.strip-mark::after{{content:"";width:2px;height:40px;background:var(--ink)}}
@media (max-width:520px){{.seg span{{display:none}}}}
.rung{{display:grid;grid-template-columns:42px 110px minmax(0,1fr);gap:10px;padding:10px 0;border-bottom:1px solid var(--rule);color:var(--ink-3);align-items:baseline}}
.rung.met{{color:var(--ink)}} .rung-mark{{font-size:12px;font-weight:600}} .rung.met .rung-mark{{color:var(--c-good)}} .rung-name{{font-weight:700}} .rung-test{{font-size:14px;line-height:1.45}}
.rung.is{{background:var(--surface);margin-inline:-10px;padding-inline:10px}} .rung.is .rung-name{{color:var(--c-critical)}}
@media (max-width:520px){{.rung{{grid-template-columns:42px minmax(0,1fr)}}.rung-test{{grid-column:2}}}}
.facts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin-top:16px}}
.facts div{{display:flex;flex-direction:column;gap:3px;padding:12px;background:var(--surface);border:1px solid var(--rule)}} .facts b{{font-size:20px;font-weight:600}} .facts small{{color:var(--ink-2);font-size:12.5px;line-height:1.4}}

/* ledgers */
.ledger{{border-top:2px solid var(--ink)}}
.lrow,.arow{{border-bottom:1px solid var(--rule)}}
.lhead,.ahead{{display:grid;width:100%;text-align:left;background:none;border:0;padding:12px 0;gap:6px 16px;align-items:center;cursor:pointer}}
.lhead{{grid-template-columns:64px 230px minmax(0,1fr) 20px}} .ahead{{grid-template-columns:56px minmax(0,1fr) 210px 20px}}
.lhead:hover,.ahead:hover{{background:var(--surface)}}
.lpts{{font-size:22px;font-weight:600}} .ltype b{{display:block;font-size:14.5px}} .lmeta{{display:block;font-size:12px;color:var(--ink-3);margin-top:2px}}
.lcase a{{font-weight:600;font-size:14.5px;line-height:1.35}} .lbody,.abody{{padding:4px 0 18px 80px;display:flex;flex-direction:column;gap:8px;max-width:84ch}} .lbody p,.abody p{{font-size:14.5px;line-height:1.5}}
.note{{color:var(--ink-2);font-size:13.5px}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}} .chip{{font:500 11.5px/1.2 var(--sans);padding:4px 8px;border:1px solid var(--rule);border-radius:3px;background:var(--surface);color:var(--ink-2)}} .chip-warn{{border-color:var(--c-warning);color:var(--ink)}}
.chev{{width:9px;height:9px;border-right:2px solid var(--ink-3);border-bottom:2px solid var(--ink-3);transform:rotate(45deg);justify-self:center;transition:transform .15s}} [aria-expanded="true"] .chev{{transform:rotate(-135deg)}}
.listed{{padding:12px 0;border-bottom:1px solid var(--rule);display:flex;flex-direction:column;gap:4px;max-width:84ch}} .listed a{{font-weight:600;font-size:14.5px}} .listed p{{font-size:13.5px;color:var(--ink-2)}}
.ascore{{font-size:20px;font-weight:600}} .s-critical{{color:var(--c-critical)}} .s-warning{{color:var(--c-warning)}} .s-neutral{{color:var(--ink)}} .s-proceeding{{color:var(--c-proceeding)}} .s-good{{color:var(--c-good)}} .s-na{{color:var(--ink-3)}}
.ahl{{display:block;font-weight:600;font-size:14.5px;line-height:1.35}}
.apips{{display:flex;gap:14px;justify-content:flex-end}} .pips{{display:inline-flex;align-items:center;gap:2px}} .pips i{{width:9px;height:9px;border:1.5px solid var(--rule-strong);border-radius:1px}} .pips b{{font-size:11px;margin-left:4px;color:var(--ink-3);font-weight:600}}
.p-critical i.on{{background:var(--c-critical);border-color:var(--c-critical)}} .p-warning i.on{{background:var(--c-warning);border-color:var(--c-warning)}} .p-proceeding i.on{{background:var(--c-proceeding);border-color:var(--c-proceeding)}} .p-good i.on{{background:var(--c-good);border-color:var(--c-good)}}
.pips.na{{color:var(--ink-3);font-size:12px;width:50px;justify-content:center}}
.amarks{{display:flex;gap:6px;justify-content:flex-end}} .mk{{min-width:52px;text-align:center;font:600 11.5px/1 var(--mono);padding:6px 6px;border:1.5px solid;border-radius:3px}}
.mk-critical{{color:var(--c-critical);border-color:var(--c-critical)}} .mk-warning{{color:var(--c-warning);border-color:var(--c-warning)}} .mk-good{{color:var(--c-good);border-color:var(--c-good)}} .mk-neutral{{color:var(--ink-3);border-color:var(--rule-strong)}}
.ofacts{{display:flex;flex-direction:column;border-top:1px solid var(--rule)}}
.ofrow{{display:grid;grid-template-columns:96px repeat(3,minmax(0,1fr));gap:8px 12px;align-items:end;padding:12px 0;border-bottom:1px solid var(--rule)}} .ofrow:last-child{{border-bottom:0}}
.ofrow>.lbl{{align-self:center}} .ofrow>div{{display:flex;flex-direction:column;gap:2px}} .ofrow b{{font-size:24px;font-weight:600;line-height:1}} .ofrow span{{font-size:12.5px;color:var(--ink-2);line-height:1.3}} .ofrow b small{{font-size:12px;color:var(--ink-3);font-weight:500}}
.ofrow .hero b{{font-size:34px}}
@media (max-width:520px){{.ofrow{{grid-template-columns:repeat(3,minmax(0,1fr))}}.ofrow>.lbl{{grid-column:1 / -1}}}}
.rub li b{{font-size:11.5px;text-transform:none}} .rub li{{grid-template-columns:64px minmax(0,1fr)}}
.anotes{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}} .anotes div{{display:flex;flex-direction:column;gap:4px}} .anotes p{{font-size:13.5px}} .anotes .lbl b{{font-size:11px}}
.controls{{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:14px}} .controls .lbl{{margin-right:4px}}
.ctl{{border:1px solid var(--rule);background:var(--surface);border-radius:3px;padding:7px 10px;font:600 12.5px/1 var(--sans);cursor:pointer;color:var(--ink-2)}} .ctl[aria-pressed="true"]{{background:var(--ink);color:var(--ground);border-color:var(--ink)}}
.pips-key{{display:flex;gap:16px;flex-wrap:wrap;font-size:12.5px;color:var(--ink-3);margin-bottom:10px}}
@media (max-width:860px){{.lhead{{grid-template-columns:56px minmax(0,1fr) 20px}}.ltype{{grid-column:2}}.lcase{{grid-column:2}}.lbody,.abody{{padding-left:0}}.ahead{{grid-template-columns:56px minmax(0,1fr) 20px}}.apips{{grid-column:2;justify-content:flex-start}}.anotes{{grid-template-columns:1fr}}}}

/* rules */
.rules{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}} @media (max-width:860px){{.rules{{grid-template-columns:1fr}}}}
.rub h4,.typ h4{{font-size:15.5px;display:flex;flex-wrap:wrap;gap:8px 10px;align-items:baseline;margin-bottom:8px}} .rub h4 span{{font-weight:400;color:var(--ink-2);font-size:13.5px}} .typ h4 b{{margin-left:auto;font-weight:500;color:var(--ink-3);font-size:12px}}
.rub ol{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}} .rub li{{display:grid;grid-template-columns:22px minmax(0,1fr);gap:8px;font-size:13.5px;line-height:1.45;color:var(--ink-2)}} .rub li b{{color:var(--ink)}}
.types{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px 26px;margin-top:8px}} .typ ol{{margin:0;padding-left:18px;font-size:13.5px;line-height:1.45;color:var(--ink-2)}} .typ li{{margin-bottom:3px}}
.kvs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px 22px;margin-top:8px}} .kv{{display:grid;grid-template-columns:78px minmax(0,1fr);gap:2px 10px;font-size:13.5px}} .kv span{{color:var(--ink-3);font-weight:600}} .kv b{{font-weight:600}} .kv p{{grid-column:2;color:var(--ink-2);line-height:1.45}}
.h3{{font-size:18px;margin:30px 0 4px}} .h3:first-child{{margin-top:0}}
.method{{max-width:72ch;display:flex;flex-direction:column;gap:12px;font-size:15px;line-height:1.55}} .method b{{font-weight:600}}
footer{{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding-block:22px 40px;border-top:1px solid var(--rule);font:12.5px/1.4 var(--mono);color:var(--ink-3)}}
</style>

<header class="masthead"><div class="wrap">
  <a class="brand" href="#top"><span class="wordmark">politaccount</span><span class="tagline">Accountability through History.</span></a>
  <nav class="nav" aria-label="Sections">
    <a href="#results">Results</a><a href="#bands">Bands</a><a href="#corruption">Corruption</a><a href="#accountability">Accountability</a><a href="#rules">Rules</a><a href="{RECORD_URL}" target="_blank" rel="noopener">The record ↗</a>
    <button class="theme-btn" id="themeBtn" type="button" aria-label="Switch theme">Theme: charcoal</button>
  </nav>
</div></header>

<main id="top" class="wrap">
<section id="hdr" style="border-top:0;padding-block:40px 30px">
  <div class="eyebrow"><b>Record 001</b> · Justin Trudeau · Two scales</div>
  <h1>Two scales</h1>
  <p class="sub">Operational Accountability. Provable Observable Corruption. One rulebook, written before any leader was scored, for the leaders of first-world democracies.</p>
  <p class="lede">Scored from the <b>{len(cases)} cases</b> on the record. Conduct, never policy. Every point traces to a case, a date and a source. Accountability is <b>counted, not graded</b>: what landed on him, whether he fought it, what changed, while he held office. The law is not the bar for corruption: the <b>common meaning of the word</b> is, tested element by element.</p>
  <p class="lede-note">Words count for nothing. Nothing after {term_end_long} counts. Allegations nobody examined score nothing and are listed. An act cleared under a statute narrower than the word still scores on the facts admitted, and is flagged.</p>
</section>

<section id="results">
  <div class="sec-head"><h2>Results</h2><span class="lbl">Record 001 · {esc(term["term_start"])} to {esc(term["term_end"])} · {R["years_in_office"]} years</span></div>
  <div class="results">
    <div class="panel panel-{OA_BAND_CLASS[OA["band"]]}">
      <div class="panel-h"><span class="lbl">Scale 1</span><h3>Operational Accountability</h3><p>In the <b>{OA["owed"]} cases</b> where a body found against him, his government or a minister, or they admitted the fault: what consequence landed on the person responsible, whether he owned it before a ruling or fought it, and whether anything changed. Each counted and dated, in office only, weighted by how big the matter was.</p></div>
      <div class="score"><div class="num">{n1(OA["score"])}<small>/ 100</small></div><div class="band band-{OA_BAND_CLASS[OA["band"]]}"><b>{esc(OA["band"])}</b><span>{esc(OA["band_line"])}</span></div></div>
      {oa_facts}
      <div class="bars">{oa_items}</div>
      <div class="who">{oa_who}</div>
      <p class="facts-line">The {OA["not_owed"]} other cases are out: cleared, upheld, never examined, or a cost with no finding. They count neither for nor against.</p>
    </div>
    <div class="panel panel-{POC_BAND_CLASS[POC["band"]]}">
      <div class="panel-h"><span class="lbl">Scale 2</span><h3>Provable Observable Corruption</h3><p>Corrupt acts on the public record, by the common meaning of the word. Each act must meet every element of its type at documented grade or better. Points = type × evidence × who did it × how big the matter was.</p></div>
      <div class="score"><div class="num">{n1(POC["points"])}<small>points</small></div><div class="band band-{POC_BAND_CLASS[POC["band"]]}"><b>{esc(POC["band"])}</b><span>{esc(POC["band_line"])}</span></div></div>
      <div class="bars">{poc_types}</div>
      <div class="who">{poc_who}</div>
      <p class="facts-line"><b>{POC["scored_acts"]}</b> proven acts across <b>{POC["scored_cases"]}</b> cases: {n_e["E4"]} adjudicated, {n_e["E3"]} admitted or on their own record, {n_e["E2"]} documented without a ruling. <b>{POC["per_year"]}</b> points a year in office; the equivalent of <b>{POC["leader_major_acts"]}</b> leader-level major acts. <b>{POC["listed_unexamined"]}</b> allegations never examined: listed, scored nothing. <b>{len(POC["cleared_under_law"])}</b> acts cleared under the Act, scored on the admitted facts.</p>
    </div>
  </div>
</section>

<section id="bands">
  <div class="sec-head"><h2>How the bands are decided</h2><span class="lbl">Fixed before scoring · the same for anyone</span></div>
  <div class="bands">
    <div>
      <h3>Operational Accountability is the share of what happened, banded</h3>
      <p class="sec-sub" style="margin-bottom:10px">For each owed case: consequence (0, ½ or 1), posture (owned = 1, else 0), change (0 or 1), averaged, then weighted by the size of the matter across the {OA["owed"]} cases. A leader who never bore anything, fought everything and changed nothing scores 0.</p>
      {oa_scale_strip(OA["score"])}
      <div class="kvs" style="margin-top:14px">{oa_bands_html}</div>
    </div>
    <div>
      <h3>Provable Observable Corruption is banded by what the ledger contains</h3>
      <p class="sec-sub" style="margin-bottom:10px">Points measure how much. The band is a set of yes-or-no tests on the ledger, and only adjudicated or admitted acts count toward them. The highest test met is the band.</p>
      <div class="ladder">{ladder}</div>
      {facts_html}
    </div>
  </div>
</section>

<section id="corruption">
  <div class="sec-head"><h2>Corruption ledger</h2><span class="lbl">{POC["scored_acts"]} acts · {n1(POC["points"])} points · largest first</span></div>
  <p class="sec-sub">One line per proven act. Open a line for the elements as they sit on the record and the arithmetic. The case link opens the full record: the deciding body's words, the dates, the sources.</p>
  <div class="ledger">{ledger_html}</div>
  <h3 class="h3">Listed, not scored</h3>
  <p class="sec-sub" style="margin-bottom:6px">Reported by major outlets, denied or unanswered, examined by no one. They stay on the record with that label and add nothing to the score.</p>
  <div class="ledger">{listed_html}</div>
</section>

<section id="accountability">
  <div class="sec-head"><h2>Accountability ledger</h2><span class="lbl">{OA["owed"]} owed cases · lowest first</span></div>
  <p class="sec-sub">One line per case where accountability was owed. Three marks: what landed on the person responsible (0, ½ on a minister or official, 1 on him), what he did with it before a ruling (owned, nothing, fought), and whether anything changed in office (0 or 1). Open a line for the facts and dates. Weight S is 1 to 3: 1, plus one if people were harmed or $10 million or more was at stake, plus one if a body found against them.</p>
  <div class="controls"><span class="lbl">Show</span>
    <button class="ctl" data-who="all" aria-pressed="true" type="button">All</button><button class="ctl" data-who="pm" aria-pressed="false" type="button">Trudeau himself</button><button class="ctl" data-who="gov" aria-pressed="false" type="button">His government</button><button class="ctl" data-who="min" aria-pressed="false" type="button">His ministers &amp; MPs</button>
    <span class="lbl" style="margin-left:12px">Order</span><button class="ctl" data-sort="score" aria-pressed="true" type="button">Lowest score first</button><button class="ctl" data-sort="date" aria-pressed="false" type="button">By date</button>
  </div>
  <div class="pips-key"><span>Marks, left to right: Consequence · Posture · Change</span></div>
  <div class="ledger" id="aledger">{arows}</div>
  <h3 class="h3">Out of the score</h3>
  <p class="sec-sub" style="margin-bottom:6px">Cleared, upheld, never examined, or a cost with no finding of fault: nothing was established to answer for. They count neither for nor against.</p>
  <div class="ledger">{not_owed_html}</div>
</section>

<section id="rules">
  <div class="sec-head"><h2>The rules</h2><span class="lbl">Scales v{R["scales_version"]} · scales.py</span></div>
  <div class="method">
    <p><b>What the scales are for.</b> A leader of a first-world democracy is measured against the standard that office claims for itself: the rule of law, independent officers and courts, a free press, an oath. Not against a dictator or a warlord. The scales are neutral in one specific way: they score conduct, never policy, and every rule below was fixed before any leader was scored.</p>
    <p><b>What counts as evidence.</b> Only the record: a court, an officer of Parliament, an auditor, a public inquiry, a recorded vote, sworn testimony, released documents, or their own words and acts. An allegation nobody examined is listed and scores nothing. Legality is not a test. When a statute's definition is narrower than the word, the admitted facts still score, and the line says the act was cleared under the Act.</p>
    <p><b>How the two scales differ.</b> Accountability counts what happened where it was owed: consequences, posture, change, each dated, in office. Cleared and upheld cases are out of it, neither for nor against. Corruption asks only what corrupt acts are proven, by whom, and how strongly. A leader can score badly on one and not the other.</p>
    <p><b>Time.</b> {esc(DEF["oa_time"])}</p>
  </div>

  <h3 class="h3">Operational Accountability — three things counted per owed case</h3>
  <p class="sec-sub" style="margin-bottom:4px">{esc(DEF["oa_owed"])}</p>
  <div class="rules">{rubrics}</div>

  <h3 class="h3">Provable Observable Corruption — the seven types and their elements</h3>
  <p class="sec-sub" style="margin-bottom:4px">An act scores only if every element is on the record at documented grade or better; its grade is the lowest grade among its elements. A case may carry up to two further acts of a different type, each at half weight.</p>
  <div class="types">{types_html}</div>

  <h3 class="h3">Evidence grades</h3><div class="kvs">{ev_html}</div>
  <h3 class="h3">Who did it</h3><div class="kvs">{prox_html}</div>
  <h3 class="h3">Weight of the matter</h3>
  <div class="method"><p>S = 1 + [people harmed, or $10 million or more of public money] + [a body found against them], capped at 3. It multiplies both scales. Points on the corruption scale are base × evidence × who × S; the bands are expressed in units of a leader-level major act, {DEF["leader_major_act_points"]:g} points: the gravest type, adjudicated, the leader personally, on a matter of weight 3.</p></div>
</section>
</main>

<footer class="wrap"><span>politaccount · Accountability through History.</span><span>Record 001 · Scales v{R["scales_version"]} · computed {computed} · data: scales_trudeau.json</span></footer>

<script>
(function(){{
  var root=document.documentElement, themeBtn=document.getElementById('themeBtn'), mode='charcoal';
  try{{ if(localStorage.getItem('pa-theme')==='light') mode='light'; }}catch(e){{}}
  function applyTheme(){{ if(mode==='light') root.setAttribute('data-theme','light'); else root.removeAttribute('data-theme'); themeBtn.textContent='Theme: '+mode; }}
  applyTheme(); themeBtn.addEventListener('click',function(){{ mode = mode==='light' ? 'charcoal' : 'light'; try{{localStorage.setItem('pa-theme',mode);}}catch(e){{}} applyTheme(); }});
  document.querySelectorAll('.lhead,.ahead').forEach(function(b){{ var body=document.getElementById(b.getAttribute('aria-controls'));
    b.addEventListener('click',function(){{ var open=b.getAttribute('aria-expanded')==='true'; b.setAttribute('aria-expanded',String(!open)); body.hidden=open; }}); }});
  var ledger=document.getElementById('aledger'), rows=Array.prototype.slice.call(ledger.children), who='all', sort='score';
  function render(){{ rows.sort(function(a,b){{ return sort==='date' ? (+a.dataset.no)-(+b.dataset.no) : (+a.dataset.score)-(+b.dataset.score); }});
    rows.forEach(function(r){{ r.hidden = !(who==='all' || r.dataset.who===who); ledger.appendChild(r); }}); }}
  document.querySelectorAll('.ctl[data-who]').forEach(function(b){{ b.addEventListener('click',function(){{ who=b.dataset.who; document.querySelectorAll('.ctl[data-who]').forEach(function(x){{x.setAttribute('aria-pressed',String(x===b));}}); render(); }}); }});
  document.querySelectorAll('.ctl[data-sort]').forEach(function(b){{ b.addEventListener('click',function(){{ sort=b.dataset.sort; document.querySelectorAll('.ctl[data-sort]').forEach(function(x){{x.setAttribute('aria-pressed',String(x===b));}}); render(); }}); }});
}})();
</script>
'''
open(os.path.join(OUT, "scales.html"), "w", encoding="utf-8").write(page)
print(f"scales.html {len(page)/1024:.0f}KB  OA={OA['score']} {OA['band']}  POC={POC['points']} {POC['band']}")


# ── SCALES.md — the method, for the repo ──
def md_types():
    out = []
    for k, v in DEF["poc_types"].items():
        out.append(f"**{k} · {v['name']}** — base {v['base']:g}\n" + "\n".join(f"{i}. {el}" for i, el in enumerate(v["elements"], 1)))
    return "\n\n".join(out)
def md_rubric(k):
    v = DEF["oa_items"][k]
    return f"**{v['name']}** — {v['line']}\n\n| Value | Meaning |\n|:--|:--|\n" + "\n".join(f"| {s} | {txt} |" for s, txt in v["rubric"].items())
ledger_md = "\n".join(f"| {r['points']:.1f} | {r['type']} {r['type_name']} | {EV_SHORT[r['evidence']]} | {PROX_SHORT[r['who']]} | S{r['S']} | {r['headline']} |" for r in POC["ledger"])
md = f"""# The two scales

Politaccount scores every leader on the same two scales, from the same kind of case record, with rules fixed here before anyone is scored. They measure conduct, never policy. Every point traces to a case and a source.

**Operational Accountability (OA)** — in every case where a body found against them or they admitted the fault: what consequence landed on the person responsible, whether they owned it before a ruling or fought it, and whether anything changed — counted, dated, in office only. The share of what happened, 0–100, banded. Words count for nothing.

**Provable Observable Corruption (POC)** — corrupt acts on the public record, by the common meaning of the word, tested element by element and graded by the strength of the evidence. Points, plus a structural band.

Legality is not the bar. When a statute's definition is narrower than the word, the admitted facts still score, and the line is flagged *cleared under the Act*. Allegations nobody examined score nothing and are listed.

## Record 001 — Justin Trudeau, computed {R['computed']}

| Scale | Result | Band |
|:--|--:|:--|
| Operational Accountability | **{OA['score']} / 100** | **{OA['band']}** — {OA['band_line']} |
| Provable Observable Corruption | **{POC['points']} points** | **{POC['band']}** — {POC['band_line']} |

OA over {OA['owed']} owed cases: consequences landed on him in **{OA['consequence_on_him']}**, on a minister or official in {OA['consequence_on_others']}, on no one in {OA['consequence_none']}; he owned {OA['owned']} before a ruling, fought {OA['fought']}, said nothing in {OA['silent']}; {OA['changed']} changed in office; the same conduct recurred after {len(OA['repeats'])}. Shares: consequence {OA['items']['consequence']['score']} · posture {OA['items']['posture']['score']} · change {OA['items']['change']['score']}. By who: him {OA['by_who']['pm']} · his government {OA['by_who']['gov']} · his ministers {OA['by_who']['min']}.

POC: {POC['scored_acts']} proven acts across {POC['scored_cases']} cases ({n_e['E4']} adjudicated, {n_e['E3']} admitted or own record, {n_e['E2']} documented without a ruling); {POC['per_year']} points a year; {POC['leader_major_acts']} leader-level major acts; {POC['listed_unexamined']} allegations listed and unscored; {len(POC['cleared_under_law'])} acts cleared under the Act and scored on the admitted facts.

## Weight of the matter (both scales)

`S = 1 + [people harmed, or ≥ $10M of public money] + [a body found against them]`, capped at 3. *Harm* is direct harm to identifiable people or a democratic process, on the record. *Against* is a court, an officer of Parliament, an auditor, a public inquiry, a committee report, or the record itself (a written commitment not met).

## Operational Accountability

**Owed.** {DEF['oa_owed']}

**Time.** {DEF['oa_time']}

Case score = (consequence + posture + change) ÷ 3. OA = 100 × Σ(S × case score) ÷ Σ S over owed cases.

{md_rubric('consequence')}

{md_rubric('posture')}

{md_rubric('change')}

Bands: """ + " · ".join(f"**{b['name']}** {b['min']}–{100 if i == 0 else DEF['oa_bands'][i-1]['min']} ({b['line']})" for i, b in enumerate(DEF["oa_bands"])) + f"""

## Provable Observable Corruption

An act scores only if **every element** of its type is on the record at grade E2 or better; its grade is the lowest grade among its elements. Points = base × evidence × who × S. A case may carry up to two further acts of a different type, each at half weight.

{md_types()}

**Evidence** — """ + " · ".join(f"**{g}** {v['name']} ×{v['multiplier']:g}: {v['meaning']}" for g, v in DEF["evidence"].items()) + """

**Who did it** — """ + " · ".join(f"**{v['name']}** ×{v['multiplier']:g}" for v in DEF["proximity"].values()) + f"""

**Bands** are structural tests on the ledger; only adjudicated or admitted acts (E4, E3) count toward them; the highest test met is the band.

""" + "\n".join(f"- **{b['name']}** — {b['test']}" for b in DEF["poc_bands"]) + f"""

The unit the bands are expressed in is a leader-level major act: {DEF['leader_major_act_points']:g} points (the gravest type, adjudicated, the leader personally, S = 3).

## The corruption ledger, Record 001

| Points | Type | Evidence | Who | S | Case |
|--:|:--|:--|:--|:--|:--|
{ledger_md}

## Files

- `build/scales.py` — every rule, weight and band above; computes both scales from `trudeau.json` + a code file.
- `build/codes_trudeau.py` — the corruption codes: for each case, which types' elements are on the record, at what evidence grade, by whom.
- `build/oa_trudeau.py` — the accountability codes: for each owed case, the consequence, the posture and the change, each with its date and the fact that carries it.
- `out/scales_trudeau.json` — the computed result: scores, bands, the ledgers, and the definitions.
- `scales.html` — the page.

To score a second leader: build their case record the same way, write `codes_<leader>.py` and `oa_<leader>.py` against the same rules, run `scales.py`. Do not touch the weights.
"""
open(os.path.join(HERE, "..", "out", "SCALES.md"), "w", encoding="utf-8").write(md)
print(f"SCALES.md {len(md)/1024:.0f}KB")
