# Changelog

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
