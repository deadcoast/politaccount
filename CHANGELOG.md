# Changelog

## 1.2.0 — 2026-09-18

**Two scales.** New page `scales.html`, computed from the record by `build/scales.py` with two code files per leader.
- *Operational Accountability* — counted, not graded. For the 41 cases where a body found against him, his government or a minister, or they admitted the fault: what consequence landed on the person responsible (0 · ½ on a minister or official · 1 on him), whether he owned it before a ruling or fought it, whether anything changed — each dated, in office only. Words score nothing; nothing after March 14, 2025 counts; money the treasury pays is not a consequence. Result: **18.7 / 100, Unaccountable** — 0 of 41 consequences landed on him.
- *Provable Observable Corruption* — an elements test in plain words for seven types, graded by evidence (adjudicated, admitted, documented; never-examined lists and scores nothing), weighted by who did it and how big the matter was. Legality is not the bar; an act cleared under a statute narrower than the word scores on the admitted facts, flagged. Result: **90.7 points, Systemic** — 26 proven acts across 21 cases; the band's five tests all met on adjudicated or admitted evidence.
- `SCALES.md` carries the method and the ledger; `scales_trudeau.json` the full result.

**Charcoal.** The ground is now charcoal on both pages by default, with light as an explicit choice from the toggle. No green cast anywhere in the palette.

**Record.** A `Scales` link in the masthead. Cash-for-access carries the Open and Accountable Government source (the standard it breached). Version 1.2.0 in the footer and the JSON.

**README.** A "Two scales" section with both results, the build tree and the flowchart updated.


## 1.1.0 — 2026-09-18

**Titles.** "The score" is now "Tally". "The big ones" is now "Large cases". Section ids changed to `#tally` and `#large`; the README nav matches.

**Wording.** All "balance" framing removed from the page, the README and the method text. The cleared cases stay in the data as cases, labelled by what the deciding body found, and nothing more is said about them.

**Stephen Harper removed.** No case text, plain-language line or finding refers to the previous government. Aga Khan (grant timing), Phoenix (procurement history) and McKinsey (baseline spend) were reworded to state the facts without him.

**Four cases added, all sourced.**
- `boil-water-advisories-promise` — Promise broken. Auditor General Report 3 (Feb 2021): "did not meet its commitment"; 58 advisories in place when the five-year deadline passed. With a said-vs-record block.
- `pandemic-preparedness-audit` — Audit: unprepared. Auditor General Report 8 (Mar 2021): early-warning system silent, risk rated low until March 12, 2020, two-thirds of quarantines unverified.
- `khadr-settlement` — Cost on record. $10.5 million paid July 5, 2017; official Statement of Apology (Public Safety Canada) is the primary source.
- `firearms-buyback-program` — Cost on record. $67.2 million spent to September 2024, no firearms collected.

**Data.** New `cost_cad` field: the public bill as a plain number on 21 cases, for sorting and summing. New `large_cases` list (the order of the Large cases section). New stats: `cases_with_cost_cad`, `sources`, `official_sources`. Dataset carries `version`.

**Build.** `build.py` writes `index.html` alongside `politaccount-trudeau.html`. `make_readme.py` reads version, date and the large-case order from the JSON. Lede counts (audits, large cases) are generated, not typed.

**Totals.** 63 cases · 198 sources · 64 official documents · 29 said-vs-record blocks · 14 large cases · 6 audits.

## 1.0.0 — 2026-09-17

First release. 59 cases, plain-language layer, said-vs-record, README.
