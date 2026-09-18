# -*- coding: utf-8 -*-
"""
Accountability codes for Record 001 (Justin Trudeau) — the Operational Accountability scale in scales.py.

Accountability is counted, not graded. For every case where it was owed — a body found against him, his
government or a minister, or they admitted the fault — three things are checked, each with a date:

  consequence   what landed on the person responsible, in office
                  1    on the leader personally: resigned over it, fined, sanctioned, repaid, or his own
                       decision reversed under pressure
                  0.5  on the responsible minister or official: resigned or removed over it, sanctioned;
                       or the specific decision reversed
                  0    nothing. Words are nothing: an apology, "accepting" a report, a review ordered, a
                       recommendation accepted. Money paid by the treasury is nothing. Anything after leaving
                       office is nothing.
  posture       what he did with it before a body ruled
                  owned    admitted it or acted on it before any finding, and did not obstruct
                  nothing  said nothing of substance, or accepted the finding only once it was made
                  fought   denied, minimized, blamed others, appealed, litigated, withheld records, invoked
                           cabinet confidence, prorogued, or refused an order
  change        whether anything actually changed, in office
                  1    a law, a rule, a process or a decision changed, and the conduct did not recur
                  0    nothing changed; a change promised, accepted or "under implementation"; the same
                       conduct recurred; or the change came after leaving office

Each item is (value, date, what). scales.py enforces the time rules: nothing after the last day in office
counts; "owned" only counts before the finding date. The engine, not this file, decides whether a case is
owed, from the result type; `owed` here only overrides that with a stated reason.
"""

OA = {

# ── 2015 ──
"boil-water-advisories-promise": dict(
    consequence=(0, None, "Nobody. The minister restated the commitment and set no date."),
    posture=("fought", "2021-03-10", "'Remains firm' — the deadline missed that month; no new date. Minimized."),
    change=(0, None, "More money pledged; the funding formula the Auditor General flagged was left as it was.")),

"fiscal-record-2015-promise": dict(
    repeat_of=["freeland-resignation"],
    consequence=(0, None, "Nobody."),
    posture=("fought", None, "The balanced-budget target was replaced with a 'debt-to-GDP anchor' rather than acknowledged as missed."),
    change=(0, None, "A second written ceiling ($40.1 billion, 2023–24) was missed by $21.8 billion.")),

"electoral-reform": dict(
    repeat_of=["fiscal-record-2015-promise", "boil-water-advisories-promise"],
    consequence=(0, None, "Nobody."),
    posture=("fought", "2017-02-01", "Cancelled by his own mandate letter and blamed on the absence of consensus."),
    change=(0, None, "Two more written commitments missed after this one: the balanced budget, the water advisories.")),

# ── 2016 ──
"phoenix-pay-system": dict(
    consequence=(0, None, "No minister or deputy minister was removed."),
    posture=("nothing", None, "The reports were accepted once made."),
    change=(0, None, "Phoenix still running at the end of the tenure with a backlog above 233,000; the replacement not delivered.")),

"elbowgate": dict(
    consequence=(0, "2016-05-19", "Two apologies. Words."),
    posture=("owned", "2016-05-18", "Apologized in the House the same evening, before the committee referral."),
    change=(0, None, "Nothing to change; nothing recurred.")),

"cash-for-access-fundraisers": dict(
    owed=(True, "His own written standard, Open and Accountable Government, was breached (see the corruption ledger); accountability was owed under his own rules."),
    consequence=(0.5, "2017-01-27", "The private-home format ended: his own decision reversed under pressure."),
    posture=("owned", "2017-01-27", "Ended the format before the commissioner's letter of February 14, 2017."),
    change=(1, "2018-06", "Bill C-50: advance notice and reporting of leaders' fundraisers, in law. No repeat in the record.")),

"tootoo-resignation": dict(
    owed=(True, "He resigned over a relationship with a staffer he acknowledged; the fault is his own admission."),
    consequence=(0.5, "2016-05-31", "The minister left cabinet and caucus the same day."),
    posture=("owned", "2016-05-31", "Resigned at once; no investigation was needed to make him."),
    change=(0, None, "Individual conduct.")),

"trudeau-foundation-donation": dict(owed=(False, "Never examined by any body; nothing established to answer for.")),

"butts-telford-moving-expenses": dict(
    consequence=(0.5, "2016-09-22", "$64,992 repaid by the two aides; $142,060 stood."),
    posture=("owned", "2016-09-22", "Repaid part and called it unreasonable the day the figures were reported; no finding forced it."),
    change=(0, None, "A new relocation policy was ordered; its outcome is not on this record.")),

"aga-khan-vacation": dict(
    repeat_of=["snc-lavalin-affair", "jamaica-vacation"],
    consequence=(0, None, "Nothing. No penalty exists; none imposed; nothing repaid."),
    posture=("fought", "2017-01-10", "'A long-time family friend' — rejected by the commissioner. Accepted the report only once it ruled."),
    change=(0, None, "Broke the same Act again within two years (SNC-Lavalin).")),

# ── 2017 ──
"mark-norman-prosecution": dict(
    owed=(True, "The Crown stayed the charge for no reasonable prospect of conviction and the House apologized unanimously: the failure is on the record."),
    consequence=(0, None, "Nothing on anyone in government. Norman's legal fees were paid by the treasury: a cost to you, not a consequence to them."),
    posture=("fought", "2019-05-08", "'Entirely independent of my office.' Left the chamber before the apology vote."),
    change=(0, None, "Nothing changed.")),

"sajjan-operation-medusa": dict(
    consequence=(0, "2017-05-02", "Retraction and apology. Words. Kept the portfolio."),
    posture=("owned", "2017-05-02", "Retracted within days; no body was involved."),
    change=(0, None, "Individual conduct.")),

"khadr-settlement": dict(owed=(False, "A settlement of Charter breaches found against earlier governments; no fault of this one on the record.")),

"julie-payette": dict(
    owed=(True, "The independent review found the workplace toxic and abusive; the skipped vetting was admitted by the promise to strengthen it."),
    consequence=(0.5, "2021-01-21", "The governor general and her secretary resigned. Nothing on the office that skipped the vetting."),
    posture=("fought", "2020-09-02", "'We have an excellent governor general right now' — two months after the abuse reports, four and a half months before she resigned."),
    change=(1, "2021-07", "An advisory group was used for the next appointment (Mary Simon, July 2021). No repeat.")),

"kang-harassment": dict(
    owed=(True, "A House of Commons investigation found harassment, upheld on appeal."),
    consequence=(0.5, "2018-08-31", "Out of caucus for good; the House finding upheld on appeal."),
    posture=("owned", "2017-08-31", "Left the caucus the day the allegations surfaced, seven months before the finding."),
    change=(0, None, "Individual conduct.")),

"morneau-french-villa": dict(
    repeat_of=["morneau-we-charity"],
    consequence=(0.5, "2017-10-26", "A $200 penalty on the minister; the only fine on any member of the ministry in the tenure. Kept the job."),
    posture=("nothing", None, "Disclosed after CBC inquiries; 'early administrative confusion'."),
    change=(0, None, "The same minister broke the same Act three ways in 2020.")),

# ── 2018 ──
"hehr-resignation": dict(
    owed=(True, "The PMO's own investigation concluded and he was not returned to cabinet; the report itself was withheld."),
    consequence=(0.5, "2018-01-25", "Out of cabinet for good; kept in caucus."),
    posture=("fought", "2018-06-06", "The PMO commissioned the report and withheld it."),
    change=(0, None, "Individual conduct.")),

"india-trip-atwal": dict(
    consequence=(0, None, "Nobody in the PMO was disciplined for the screening failures the committee identified."),
    posture=("fought", "2018-02", "The national security adviser briefed reporters that factions in India had orchestrated it."),
    change=(0, None, "The committee recommended background checks for guest lists; no change on this record.")),

"leblanc-surf-clam": dict(
    repeat_of=["ng-pomp-circumstance", "morneau-we-charity"],
    consequence=(0.5, "2018-07", "The licence award was withdrawn and the process restarted. The minister was kept through 2025."),
    posture=("nothing", None, "Accepted the finding 'without reservation' once it was made."),
    change=(0, None, "Two more ministers failed to recuse and were found in breach: Ng (2022), Morneau (2021).")),

"vance-allegations-2018": dict(
    owed=(True, "The general pleaded guilty to obstruction; the ombudsman's sworn account of the minister refusing the evidence stands unrebutted; Arbour's review found the system failed."),
    consequence=(0, None, "The minister was moved, not sanctioned. No PMO or PCO official disciplined."),
    posture=("fought", "2021-03", "'Confidence in Sajjan' after the ombudsman's testimony; the minister: allegations were 'very quickly put forward to the proper authorities'."),
    change=(0, None, "48 recommendations 'accepted', 'under implementation'. Accepted is not changed.")),

"trans-mountain": dict(owed=(False, "A purchase on the record; no finding of fault.")),
"kokanee-summit-allegation": dict(owed=(False, "Never examined by any body.")),
"grewal-charges": dict(owed=(False, "Acquitted.")),

# ── 2019 ──
"snc-lavalin-affair": dict(
    repeat_of=["we-charity"],
    consequence=(0.5, "2019-02-18", "His principal secretary resigned; the clerk retired. Nothing on him. The two ministers who resisted were expelled."),
    posture=("fought", "2019-02-07", "'The allegations are false.' Cabinet confidence waived only in part; the commissioner and the RCMP both said it blocked them. 'I won't apologize.'"),
    change=(0, None, "Within a year he sat in on a $912-million decision involving an organization that had paid his family.")),

"liberalist-judicial-vetting": dict(owed=(False, "Never examined by any body.")),

"ng-pomp-circumstance": dict(
    consequence=(0, None, "Apology. No repayment, no penalty, kept in cabinet."),
    posture=("nothing", None, "Apologized once the finding was made."),
    change=(0, None, "Nothing changed.")),

"winnipeg-lab-documents": dict(
    repeat_of=["sdtc-green-fund"],
    consequence=(0.5, "2021-06-21", "The agency's president was admonished at the bar of the House. Nothing on the ministers who withheld the records."),
    posture=("fought", "2021-06", "Refused two orders of the House and sued the Speaker in Federal Court, the first such application ever."),
    change=(0, None, "In 2024 another House order for documents (the green fund) was not fully met.")),

"blackface-images": dict(
    consequence=(0, "2019-09-19", "Two apologies. Words."),
    posture=("owned", "2019-09-18", "Admitted it the night it was published."),
    change=(0, None, "Personal conduct; nothing to change in office.")),

# ── 2020 ──
"pandemic-preparedness-audit": dict(
    consequence=(0, None, "Nothing on any minister."),
    posture=("nothing", None, "Recommendations accepted once the report was made."),
    change=(0, None, "No change on this record.")),

"baylis-ventilators": dict(owed=(False, "Never examined by any body.")),

"covid-benefit-overpayments": dict(
    consequence=(0, None, "Nothing on any minister."),
    posture=("fought", "2022-12-06", "The tax agency disputed the Auditor General's figure and told MPs a full review would not be worth it."),
    change=(0, None, "Recovery letters went out; the position that full verification is not worthwhile stood.")),

"we-charity": dict(
    owed=(True, "He admitted he should have recused; his finance minister was found in breach over the same decision."),
    consequence=(0.5, "2020-08-17", "The finance minister resigned; the programme was withdrawn from WE. Nothing on him."),
    posture=("fought", "2020-08-18", "Apologized on July 13, then prorogued Parliament, ending four committee studies, and made a motion for a special committee a confidence vote."),
    change=(0, None, "No rule changed. The next free stay was cleared in advance; that is a phone call, not a rule.")),

"lucki-nova-scotia-call": dict(owed=(False, "The inquiry found no attempted political interference.")),

"arrivecan": dict(
    consequence=(0.5, "2024", "Two agency executives suspended without pay; the contractor barred and admonished by the House. No minister sanctioned."),
    posture=("nothing", None, "'Unacceptable', once the audit was out."),
    change=(0, None, "No procurement rule changed on this record.")),

"firearms-buyback-program": dict(owed=(False, "A cost on the record; no finding of fault.")),

"morneau-we-charity": dict(
    consequence=(0.5, "2020-08-17", "The minister resigned as minister and MP."),
    posture=("owned", "2020-07-22", "Repaid $41,366 for the trips ten months before the finding."),
    change=(0, None, "He left office.")),

"nuctech-standing-offer": dict(
    consequence=(0.5, "2020-11-17", "The standing offer was set aside; no equipment bought."),
    posture=("owned", "2020-11-17", "Reversed once reported; the Deloitte review confirmed the gap."),
    change=(1, "2020-11-17", "The department designed a new procurement route with a national-security exemption. No repeat.")),

# ── 2021 ──
"access-to-information-decline": dict(
    repeat_of=["sdtc-green-fund"],
    consequence=(0, None, "Nobody."),
    posture=("nothing", None, "The report was left unanswered; the law unchanged."),
    change=(0, None, "A House order for documents was not fully met the following year.")),

"michael-chong-zhao-wei": dict(
    consequence=(0, None, "No minister, adviser or official disciplined. The diplomat was expelled; that is a consequence for China, not for them."),
    posture=("nothing", None, "Said he learned of it from the newspaper; the inquiry recorded the same."),
    change=(1, "2024-06-20", "The Countering Foreign Interference Act, in law, in office. No repeat.")),

"blair-csis-warrant-delay": dict(
    consequence=(0, None, "No sanction; the minister stayed to the end."),
    posture=("fought", "2024-10", "Said he did not learn of the warrant until days before signing; the inquiry placed 54 days in his office."),
    change=(0, None, "A tracking process was recommended; none on this record.")),

"afghanistan-evacuation-2021": dict(
    consequence=(0, None, "No minister resigned; two were moved to other portfolios."),
    posture=("nothing", None, "The committee reported; the government did not dispute it."),
    change=(1, "2023-06", "Bill C-41 exempted humanitarian aid from the terrorism-financing provisions the committee flagged. No repeat.")),

"snap-election-2021": dict(owed=(False, "Lawful; a cost on the record; no finding of fault.")),
"sajjan-afghan-sikhs": dict(owed=(False, "Never examined by any body.")),

"tofino-truth-reconciliation-day": dict(
    consequence=(0, "2021-10-06", "Apology and a visit. Words."),
    posture=("owned", "2021-10-06", "'A mistake, and I regret it' — six days later; no body was involved."),
    change=(0, None, "Nothing recurred; nothing changed.")),

# ── 2022 ──
"emergencies-act-2022": dict(
    consequence=(0, None, "No minister resigned. No sanction after either ruling."),
    posture=("fought", "2024-01-23", "Appealed the first ruling; 'that continues to be my belief today'. Sought leave to appeal the second."),
    change=(0, None, "The Act was not amended; the inquiry's recommendations accepted in principle.")),

"mendicino-police-request-claim": dict(
    consequence=(0, None, "Nothing. The minister stayed a year, and was dropped over a different matter."),
    posture=("nothing", None, "Walked back by his deputy minister, not by him."),
    change=(0, None, "Individual conduct.")),

"boissonnault-global-health-imports": dict(owed=(False, "Closed by the commissioner with no evidence of a breach.")),
"london-hotel-queen-funeral": dict(owed=(False, "A cost on the record; no finding of fault.")),

"foreign-interference-response": dict(
    consequence=(0, None, "No minister resigned."),
    posture=("fought", "2023-03-15", "Refused a public inquiry and appointed a rapporteur instead; agreed to the inquiry six months later under a House vote."),
    change=(1, "2024-06-20", "The Countering Foreign Interference Act, in law, in office.")),

# ── 2023 ──
"mckinsey-outsourcing": dict(
    consequence=(0, None, "Nobody sanctioned."),
    posture=("nothing", None, "Ministers were asked to review the contracts."),
    change=(0, None, "No rule changed on this record.")),

"hussen-constituency-contracts": dict(owed=(False, "Never examined by any body.")),
"han-dong": dict(owed=(False, "The inquiry left the irregularities undetermined.")),
"mendicino-bernardo-transfer": dict(owed=(False, "Never formally examined; the minister's own statement is scored on the corruption scale.")),

"david-johnston-rapporteur": dict(
    consequence=(0.5, "2023-06-09", "The rapporteur resigned; the inquiry he had recommended against was called in September. His decision, reversed."),
    posture=("fought", "2023-05-31", "Defended the appointment against a 174–150 vote of the House."),
    change=(0, None, "Nothing changed in how such appointments are made.")),

"hunka-recognition": dict(owed=(False, "The Speaker's invitation; the Speaker resigned. No fault of the government on the record.")),

"sdtc-green-fund": dict(
    consequence=(0.5, "2023-11", "The chair resigned and was found in breach; the foundation was dissolved. Nothing on the minister."),
    posture=("fought", "2024-09-26", "The House order for the documents was not fully met; the privilege debate ran to prorogation."),
    change=(1, "2024-06-04", "The foundation was wound down into the National Research Council; the conduct did not recur.")),

"carbon-charge-heating-oil": dict(owed=(False, "A policy reversal on the record; no fault found or admitted.")),
"jamaica-vacation": dict(owed=(False, "Cleared in advance; the office's three statements are scored on the corruption scale.")),

# ── 2024 ──
"nsicop-2024-parliamentarians": dict(owed=(False, "The inquiry found the committee's claim overshot the intelligence.")),

"immigration-could-have-acted-quicker": dict(
    consequence=(0, "2024-11-17", "An admission on video. Words."),
    posture=("owned", "2024-11-17", "'We could have acted quicker and turned off the taps faster.'"),
    change=(1, "2024-10-24", "Permanent-resident targets cut by about a fifth; a target set for temporary residents. In office.")),

"freeland-resignation": dict(
    owed=(True, "Her own ceiling, missed by $21.8 billion, on the government's own statement."),
    consequence=(0.5, "2024-12-16", "The finance minister left. Nothing on him."),
    posture=("nothing", None, "No dispute of the figure; no acknowledgment of it either."),
    change=(0, None, "End of tenure.")),

# ── 2025 ──
"prorogation-2025": dict(owed=(False, "Upheld by the court.")),
"trudeau-resignation": dict(owed=(False, "A resignation under caucus pressure after nine years; the record ties it to no single case.")),
}
