# -*- coding: utf-8 -*-
"""Generate README.md for github.com/deadcoast/politaccount from trudeau.json."""
import json, os, datetime

HERE = os.path.dirname(__file__)
d = json.load(open(os.path.join(HERE, "..", "out", "trudeau.json"), encoding="utf-8"))
E = d["entries"]; S = d["stats"]
by_id = {e["id"]: e for e in E}
SITE = "https://deadcoast.github.io/politaccount/"
REPO = "https://github.com/deadcoast/politaccount"

SC = json.load(open(os.path.join(HERE, "..", "out", "scales_trudeau.json"), encoding="utf-8"))
SOA, SPOC = SC["oa"], SC["poc"]
n_sources = sum(len(e["sources"]) for e in E)
n_primary = sum(1 for e in E for s in e["sources"] if s["primary"])
VERSION = d["version"]; CURRENT = d["current_as_of"]
CURRENT_LONG = datetime.date.fromisoformat(CURRENT).strftime("%B %-d, %Y"); CURRENT_MONTH = datetime.date.fromisoformat(CURRENT).strftime("%B_%Y")
WORDS = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen"}
def first_sentence(s):
    import re
    m = re.match(r"(.+?[.!])(\s|$)", s); return m.group(1) if m else s
def money(n):
    if n >= 1e9: return f"${n/1e9:,.1f} billion".replace(".0 billion", " billion")
    if n >= 1e6: return f"${n/1e6:,.1f} million".replace(".0 million", " million")
    return f"${n:,.0f}"
large = [by_id[i] for i in d["large_cases"]]
large_md = "\n".join(f"| <kbd>{e['plain']['label']}</kbd> | {e['plain']['headline']} | {money(e['cost_cad']) if e.get('cost_cad') else '—'} | {first_sentence(e['plain']['him'])} |" for e in large)
CLASS_NAMES = [("critical", "Broke the law · ruled illegal"), ("warning", "Audit · inquiry · promise broken"),
               ("proceeding", "Quit · forced out · charged"), ("neutral", "Admitted · on the record · never investigated"),
               ("good", "Cleared · upheld")]
mx = max(S["by_class"].values())

def bar(n, width=24):
    filled = round(n / mx * width)
    return "█" * filled + "░" * (width - filled)

bars = "\n".join(f"{name:<46}{bar(S['by_class'][k])}  {S['by_class'][k]:>2}" for k, name in CLASS_NAMES)

# ── groups → details list, headlines from the data ──
group_blocks = []
for g in d["groups"]:
    rows = [e for e in E if e["group"] == g["key"]]
    rows.sort(key=lambda e: e["date_start"])
    lines = "\n".join(f"| <kbd>{e['plain']['label']}</kbd> | {e['plain']['headline']} | {e['years']} |" for e in rows)
    group_blocks.append(f"""<details>
<summary><b>{g['title']}</b> — {len(rows)} · <i>{g['blurb']}</i></summary>
<br>

| Label | Case | Years |
|:--|:--|:--|
{lines}

</details>""")
groups_md = "\n\n".join(group_blocks)

# ── example case (Aga Khan) ──
ak = by_id["aga-khan-vacation"]; p = ak["plain"]
said = ak["said"]
import textwrap
def diff_wrap(sign, text, width=104):
    return "\n".join(f"{sign} {line}" for line in textwrap.wrap(text, width))
diff_lines = []
for q in said["said"]:
    txt = f"“{q['quote']}”" if q.get("quote") else q["said"]
    diff_lines.append(diff_wrap("-", f"{q['date']} · {q['who']}: {txt}"))
diff_lines.append(diff_wrap("+", f"The record: {said['record']}"))
diff_block = "\n".join(diff_lines)
src_fn = "\n".join(f"[^{i}]: {s['title']} — {s['publisher']}{' · official document' if s['primary'] else ''}. {s['url']}" for i, s in enumerate(ak["sources"], 1))
src_refs = "".join(f"[^{i}]" for i in range(1, len(ak["sources"]) + 1))

# ── vocabulary table ──
vocab = "\n".join(f"| `{k}` | {v['class']} | <kbd>{v['plain']}</kbd> |" for k, v in d["labels"].items())

# ── trimmed JSON sample ──
sample = {
    "id": ak["id"], "subject": ak["subject"], "category": ak["category"],
    "date_start": ak["date_start"], "date_end": ak["date_end"], "cost_cad": ak["cost_cad"],
    "plain": {"headline": p["headline"], "found": p["found"], "cost": p["cost"], "him": p["him"], "label": p["label"]},
    "finding": {"body": ak["finding"]["body"], "date": ak["finding"]["date"], "result": ak["finding"]["result"],
                "quote": ak["finding"]["quote"][:120] + " […]"},
    "said": [{"date": said["said"][0]["date"], "who": said["said"][0]["who"], "quote": said["said"][0]["quote"][:60] + " […]"}],
    "sources": [{"title": ak["sources"][0]["title"], "publisher": ak["sources"][0]["publisher"], "primary": True, "url": ak["sources"][0]["url"]}],
}
sample_json = json.dumps(sample, ensure_ascii=False, indent=2)

readme = f"""<div align="center">

<h1>P O L I T A C C O U N T</h1>

<p><em>Accountability through History.</em></p>

<p>
<a href="{SITE}"><img alt="Live page" src="https://img.shields.io/badge/live-deadcoast.github.io%2Fpolitaccount-2E7D4F?style=for-the-badge&logo=github&logoColor=white"></a>
</p>

<p>
<img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img alt="CSS" src="https://img.shields.io/badge/CSS-663399?style=for-the-badge&logo=css&logoColor=white">
<img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img alt="JSON" src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white">
<img alt="Python" src="https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white">
</p>

<p>
<img alt="Cases" src="https://img.shields.io/badge/cases-{S['cases']}-A11C15?style=flat-square">
<img alt="Sources" src="https://img.shields.io/badge/sources-{n_sources}-151A17?style=flat-square">
<img alt="Official documents" src="https://img.shields.io/badge/official_documents-{n_primary}-151A17?style=flat-square">
<img alt="Said vs record" src="https://img.shields.io/badge/said_vs_record-{S['cases_with_said_vs_record']}_cases-151A17?style=flat-square">
<img alt="Version" src="https://img.shields.io/badge/dataset-v{VERSION}-151A17?style=flat-square">
<img alt="Current as of" src="https://img.shields.io/badge/record_current-{CURRENT_MONTH}-6B7280?style=flat-square">
<a href="{REPO}/commits"><img alt="Last commit" src="https://img.shields.io/github/last-commit/deadcoast/politaccount?style=flat-square&color=6B7280"></a>
</p>

<p>
<a href="#tally">Tally</a> &nbsp;·&nbsp;
<a href="#two-scales">Two scales</a> &nbsp;·&nbsp;
<a href="#large-cases">Large cases</a> &nbsp;·&nbsp;
<a href="#what-a-case-looks-like">What a case looks like</a> &nbsp;·&nbsp;
<a href="#nine-years">Nine years</a> &nbsp;·&nbsp;
<a href="#all-{S['cases']}-cases">All {S['cases']} cases</a> &nbsp;·&nbsp;
<a href="#how-its-built">How it’s built</a> &nbsp;·&nbsp;
<a href="#the-data">The data</a> &nbsp;·&nbsp;
<a href="#the-rules">The rules</a>
</p>

</div>

<br>

Politaccount is a record of what Canadian leaders did in office, written so that anyone can read it. Each case answers three questions in plain words: **what they found**, **what it cost you**, **what happened to him**. Under every case sits the evidence: the deciding body’s own words, the dates, and the sources, official documents first.

**Record 001 is Justin Trudeau**, Prime Minister from November 4, 2015 to March 14, 2025. {S['days_in_office']:,} days, three elections, {S['cases']} cases.

> [!IMPORTANT]
> The ethics commissioner ruled **twice** that he broke the law. **Two courts** ruled his use of the Emergencies Act was illegal. **{WORDS[S['audits']]}** audits found money wasted, rules ignored, or the country unprepared. Fines, sanctions or charges he ever faced: **0**.

---

## Tally

<table align="center">
<tr>
<td align="center" width="34%"><h1>0</h1><b>Fines, sanctions or charges he faced</b><br><sub>The ethics law has no penalty for what he did. Nobody imposed one.</sub></td>
<td align="center" width="22%"><h1>{S['pm_broke_ethics_law']}</h1><b>Times he broke the ethics law</b><br><sub>Aga Khan 2017 · SNC-Lavalin 2019</sub></td>
<td align="center" width="22%"><h1>{S['ruled_illegal']}</h1><b>Action ruled illegal by the courts</b><br><sub>Emergencies Act · 2024, upheld 2026</sub></td>
<td align="center" width="22%"><h1>{S['audits']}</h1><b>Audits: money wasted or rules ignored</b><br><sub>Phoenix · COVID benefits · ArriveCAN · McKinsey · green fund · pandemic readiness</sub></td>
</tr>
<tr>
<td align="center"><h1>{S['ministers_broke_ethics_law']}</h1><b>Ethics-law breaches by his ministers</b><br><sub>Morneau ×2 · LeBlanc · Ng · total fines: $200</sub></td>
<td align="center"><h1>{S['ministers_out']}</h1><b>Ministers who quit or were pushed out</b></td>
<td align="center"><h1>{S['inquiries']}</h1><b>Official inquiries into his government</b></td>
<td align="center"><h1>{S['never_investigated']}</h1><b>Allegations nobody investigated</b><br><sub>Kept, and labelled that way</sub></td>
</tr>
</table>

Counted from the {S['cases']} cases, by what was found:

```text
{bars}
```

```mermaid
%%{{init: {{'theme':'base','themeVariables':{{'pie1':'#A11C15','pie2':'#C48A00','pie3':'#3B5BA9','pie4':'#6B7280','pie5':'#2E7D4F'}}}}}}%%
pie showData
    title What was found, {S['cases']} cases
    "Broke the law, or ruled illegal" : {S['by_class']['critical']}
    "Audit, inquiry, or promise broken" : {S['by_class']['warning']}
    "Quit, forced out, or charged" : {S['by_class']['proceeding']}
    "Admitted, on the record, or never investigated" : {S['by_class']['neutral']}
    "Cleared or upheld" : {S['by_class']['good']}
```

---

## Two scales

Every leader is scored on the same two scales, with rules fixed before anyone was scored. Conduct, never policy. Every point traces to a case, a date and a source. The method is in [`SCALES.md`](SCALES.md); the page is [`scales.html`]({SITE}scales.html).

<table align="center">
<tr>
<td align="center" width="50%"><sub>OPERATIONAL ACCOUNTABILITY</sub><h1>{SOA['score']}<sub> / 100</sub></h1><b>{SOA['band']}</b><br><sub>{SOA['band_line']}</sub></td>
<td align="center" width="50%"><sub>PROVABLE OBSERVABLE CORRUPTION</sub><h1>{SPOC['points']}<sub> points</sub></h1><b>{SPOC['band']}</b><br><sub>{SPOC['band_line']}</sub></td>
</tr>
</table>

**Accountability** is counted, not graded. In the {SOA['owed']} cases where a body found against him, his government or a minister, or they admitted the fault: a consequence landed on him personally in **{SOA['consequence_on_him']}**, on a minister or official in {SOA['consequence_on_others']}, on no one in {SOA['consequence_none']}. He fought {SOA['fought']}, said nothing in {SOA['silent']}, owned {SOA['owned']} before a ruling. {SOA['changed']} changed in office; the same conduct recurred after {len(SOA['repeats'])}. Words count for nothing; nothing after the last day in office counts.

**Corruption** is an elements test in plain words, graded by evidence. {SPOC['scored_acts']} proven acts across {SPOC['scored_cases']} cases, {SPOC['by_evidence']['E4']} of them adjudicated; {SPOC['per_year']} points a year in office. The band is five yes-or-no tests on the ledger, every one of them met.

---

## Large cases

The {WORDS[len(large)].lower()} that matter most, in the order the page gives them. Costs are the public bill on the record; blank means none was ever put on the record.

| Label | Case | What it cost you | What happened to him |
|:--|:--|--:|:--|
{large_md}

---

## What a case looks like

Every case on the page has the same shape. Here is one, exactly as the data renders it.

<kbd>{p['label']}</kbd> &nbsp; <sub>{ak['who']} · {ak['years']}</sub>

### {p['headline']}

{p['telling']}

| What they found | What it cost you | What happened to him |
|:--|:--|:--|
| {p['found']} | {p['cost']} | **Nothing.** {p['him'].split('. ', 1)[1] if '. ' in p['him'] else ''} |

**Said, against the record**

```diff
{diff_block}
```

<sub>Sources for this case</sub> {src_refs}

<details>
<summary>What sits under “Show the evidence”</summary>
<br>

> {ak['finding']['quote']}
>
> — {ak['finding']['body']}, {ak['finding']['date']}

**What happened to everyone else.** {p['others']}

**Where it stands, September 2026.** {ak['status']}

</details>

---

## Nine years

```mermaid
timeline
    title {S['cases']} cases, November 2015 to March 2025
    2015 : Sworn in, November 4
         : Platform promises a last election under first past the post, and a balanced budget by 2019
    2016 : Phoenix pay system switched on
         : Cash-for-access dinners
         : Aga Khan island, December
    2017 : Vice-Admiral Norman suspended
         : $10.5 million paid to Omar Khadr, July
         : Ethics ruling on the Aga Khan trip, four sections broken
         : Payette appointed without vetting
    2018 : Defence minister refuses to see the Vance evidence
         : India trip, Atwal at the reception
         : LeBlanc clam licence, ethics law broken
    2019 : SNC-Lavalin, ethics law broken
         : Blackface photos, mid-campaign
         : Judges vetted through Liberalist
    2020 : Assault-style firearms banned by order, May
         : WE Charity, then prorogation
         : ArriveCAN launched at an $80,000 estimate
         : Nova Scotia shooting briefing
    2021 : Auditor General: water-advisory promise missed, pandemic warning system left to decay
         : Kabul falls, election called the same day
         : Tofino on the first Truth and Reconciliation Day
         : Winnipeg lab documents fought in court
    2022 : Emergencies Act invoked, accounts frozen
         : Foreign-interference leaks begin
    2023 : Johnston appointed, then out
         : Green fund suspended
         : Jamaica
    2024 : Federal Court rules the Emergencies Act use unlawful
         : ArriveCAN and green-fund audits
         : Freeland resigns
    2025 : Resigns, January 6
         : Leaves office, March 14
         : Hogue final report
    2026 : Appeal court affirms the Emergencies Act ruling
         : Supreme Court reopens the WE clearance
```

---

## All {S['cases']} cases

Grouped by what was found, most damning first. Every headline below is the one on the page.

{groups_md}

---

## How it’s built

One data file holds the facts. Two more hold the plain-language layer and the statements. One script turns them into the page and the dataset, and the page is what GitHub Pages serves.

```mermaid
flowchart LR
    D["data_trudeau.py<br/>{S['cases']} cases · findings · consequences · {n_sources} sources"] --> B["build.py"]
    P["plain_trudeau.py<br/>headline · telling · the three answers"] --> B
    Q["said_trudeau.py<br/>said vs the record · {S['cases_with_said_vs_record']} cases"] --> B
    T["template.html"] --> B
    B --> J[("trudeau.json")]
    B --> H["index.html"]
    J --> S["scales.py<br/>+ codes_trudeau.py + oa_trudeau.py"]
    S --> K[("scales_trudeau.json")]
    K --> L["scales.html"]
    H --> G(["deadcoast.github.io/politaccount"])
    L --> G
    style D fill:#EDEFE8,stroke:#98A094,color:#151A17
    style P fill:#EDEFE8,stroke:#98A094,color:#151A17
    style Q fill:#EDEFE8,stroke:#98A094,color:#151A17
    style T fill:#EDEFE8,stroke:#98A094,color:#151A17
    style B fill:#151A17,stroke:#151A17,color:#EDEFE8
    style J fill:#F7F8F3,stroke:#A11C15,color:#151A17
    style H fill:#F7F8F3,stroke:#A11C15,color:#151A17
    style S fill:#151A17,stroke:#151A17,color:#EDEFE8
    style K fill:#F7F8F3,stroke:#A11C15,color:#151A17
    style L fill:#F7F8F3,stroke:#A11C15,color:#151A17
    style G fill:#2E7D4F,stroke:#2E7D4F,color:#ffffff
```

```text
politaccount/
├── index.html              the record, self-contained: no build step to view it
├── scales.html             the two scales, computed from the record
├── trudeau.json            the dataset the page is generated from
├── scales_trudeau.json     both scales: scores, bands, ledgers, definitions
├── SCALES.md               the method: rules, weights, bands, the ledger
├── build/
│   ├── data_trudeau.py     {S['cases']} cases: what happened, the finding, the consequence, the sources
│   ├── plain_trudeau.py    the reader-facing layer: headline, telling, three answers, label
│   ├── said_trudeau.py     dated statements against the record, {S['cases_with_said_vs_record']} cases
│   ├── template.html       layout, styles, filters, timeline, light and dark themes
│   ├── build.py            data → trudeau.json + index.html
│   ├── scales.py           every rule, weight and band of the two scales
│   ├── codes_trudeau.py    corruption codes: which elements are on the record, at what grade
│   ├── oa_trudeau.py       accountability codes: consequence, posture, change, each dated
│   ├── make_scales_page.py scales_trudeau.json → scales.html + SCALES.md
│   └── make_readme.py      trudeau.json → README.md
└── README.md
```

One command rebuilds everything:

```sh
python3 build/build.py && python3 build/scales.py && python3 build/make_scales_page.py && python3 build/make_readme.py
```

Three layers, in the order a reader meets them:

| Layer | What it holds | Written for |
|:--|:--|:--|
| **Plain** | headline · telling · what they found · what it cost you · what happened to him | anyone, in the time it takes to scroll past |
| **Said / the record** | the person’s own statements, dated and linked, beside what the evidence later showed | anyone who says it was taken out of context |
| **Evidence** | the deciding body’s own words · dates · status · sources, official document first | anyone who wants to dispute a line |

The page runs with no framework and no dependencies: one HTML file, fonts from Google Fonts with system fallbacks, and about 300 lines of vanilla JavaScript for the filters, the timeline and the theme switch. It reads at phone width and in dark mode.

---

## The data

`trudeau.json` is the whole record, ready to ingest. One entry, trimmed:

```json
{sample_json}
```

Where a public bill exists, `cost_cad` carries it as a plain number ({S['cases_with_cost_cad']} cases), so the record can be sorted and summed without parsing prose.

Every `finding.result` is one of thirteen values. The class drives the colour and the shape on the timeline; the plain label is what a reader sees.

<details>
<summary><b>The thirteen result values</b></summary>
<br>

| `finding.result` | class | reader sees |
|:--|:--|:--|
{vocab}

</details>

---

## The rules

**What counts as a case.** Something an official body ruled on, a court decided, an auditor reported, someone resigned over, or the government admitted in its own words, plus a promise made in writing and not kept. Allegations that major outlets reported and nobody ever investigated are kept and labelled <kbd>Never investigated</kbd>, with the person’s answer and nothing more.

**“Nothing” means nothing.** No fine, no sanction, no resignation, no reversal. Where the law provides no penalty, the case says so, because that is part of the record.

**The evidence carries the legal language.** The reader-facing layer never does. “Contravened section 9 of the Conflict of Interest Act” lives one click down; the headline says he broke the ethics law.

> [!WARNING]
> **Two matters are still moving.** The government has sought leave to appeal the Emergencies Act rulings to the Supreme Court of Canada (filed March 17, 2026; no decision on leave yet). On July 30, 2026 the Supreme Court struck down the clause that shielded the WE Charity clearance from judicial review and sent it back to the Federal Court of Appeal.

> [!NOTE]
> Every line traces to a source. If one is wrong, open an issue with the document that contradicts it. The first source listed for a case is the deciding body’s own document wherever one exists.

---

<div align="center">
<sub>Record 001 · Justin Trudeau · {S['cases']} cases · {n_sources} sources · dataset v{VERSION} · current as of {CURRENT_LONG}</sub>
<br>
<sub><a href="{SITE}">deadcoast.github.io/politaccount</a></sub>
</div>

{src_fn}
"""

out = os.path.join(HERE, "..", "deliver", "README.md")
open(out, "w", encoding="utf-8").write(readme)
print(f"README.md: {len(readme)/1024:.0f} KB, {readme.count(chr(10))} lines")
