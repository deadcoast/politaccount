# -*- coding: utf-8 -*-
"""
Corruption codes for Record 001 (Justin Trudeau) — the Provable Observable Corruption scale in scales.py.

One entry per case in trudeau.json. A case scores only where every element of a type is on the record;
the elements text says which fact carries each element. Evidence E1 = listed, scores nothing.

  harm            direct harm to identifiable people or a democratic process, on the record (weight)
  money_in_play   public money at stake where cost_cad is absent (documented programme value) (weight)
  against         a finding against them by a body not already implied by the result type (weight)
  repeat_after_finding   the same type recurred after an adverse finding on this case (band test)
  poc             corrupt-act types whose elements are all on the record; first = primary, others half weight
"""

def T(type, evidence, who, elements, note="", cleared_under_law=False):
    return dict(type=type, evidence=evidence, who=who, elements=elements, note=note, cleared_under_law=cleared_under_law)

CODES = {
"boil-water-advisories-promise": dict(harm=True,
    poc=[],
    poc_note="A missed commitment. No private benefit, no false statement, no rule broken: not corruption."),

"fiscal-record-2015-promise": dict(
    poc=[],
    poc_note="A fiscal outcome. Not corruption unless the promise was made knowing it would not be kept; the record does not show that."),

"electoral-reform": dict(
    poc=[],
    poc_note="A broken promise, not a false statement of fact. Not corruption."),

"phoenix-pay-system": dict(harm=True,
    poc=[],
    poc_note="Mismanagement on a vast scale. No insider benefit, no rule-breaking for gain: not corruption. Scored in OA."),

"elbowgate": dict(
    poc=[],
    poc_note="Personal conduct. Not corruption."),

"cash-for-access-fundraisers": dict(
    poc=[
        T("T7", "E3", "him",
           "His own Open and Accountable Government (2015), Annex B: 'no preferential access to government, or appearance of preferential access ... because they have made financial contributions'. Face time sold at $1,525 in private homes is the appearance the standard names. Admitted by ending the format.",
           note="Cleared under the Conflict of Interest Act; scored under his own written standard, which is broader.", cleared_under_law=True),
    ],
    poc_note="Element (b) of self-dealing — that the guests had business before the government — is not on this record for each guest, so the case scores as a breach of his own standard, not as self-dealing."),

"tootoo-resignation": dict(
    poc=[],
    poc_note="Personal conduct. Not corruption."),

"trudeau-foundation-donation": dict(
    poc=[
        T("T1", "E1", "him",
           "If proven: a benefit to a family foundation, directed by a foreign state. His own role is not on the record."),
    ],
    poc_note="Listed. Never examined. Scores nothing."),

"butts-telford-moving-expenses": dict(
    poc=[
        T("T4", "E3", "office",
           "Public money ($207,052) went to his two most senior aides; the excess was admitted by the repayment of $65,000 as 'unreasonable'.",
           note="Within the policy; scored on the admitted excess only."),
    ],
    poc_note=""),

"aga-khan-vacation": dict(repeat_after_finding=True,
    poc=[
        T("T1", "E4", "him",
           "A gift (the island stay, the helicopter) from a party whose foundation was registered to lobby his office with a $15-million grant pending; not refused. Found by the commissioner."),
        T("T5", "E4", "him",
           "'The Aga Khan has been a long-time family friend' — the commissioner found no private interaction between the two men until Trudeau became Liberal leader, and that the relationship 'cannot be described as one of friends for the purposes of the Act'."),
    ],
    poc_note=""),

"mark-norman-prosecution": dict(harm=True,
    poc=[
        T("T2", "E2", "him",
           "Publicly pre-judged (twice, on the record) a decision reserved to police and prosecutors. The statements are his; their effect was never examined by any body.",
           note="Counsel's claims that records were withheld and code names used were argued in court, not ruled on: not scored."),
    ],
    poc_note=""),

"sajjan-operation-medusa": dict(
    poc=[
        T("T5", "E3", "minister",
           "A public statement of fact ('the architect' of Operation Medusa), retracted by the minister himself, about his own service."),
    ],
    poc_note=""),

"khadr-settlement": dict(
    poc=[],
    poc_note="A settlement, not corruption."),

"julie-payette": dict(harm=True,
    poc=[],
    poc_note="A skipped process and a bad appointment. Not corruption."),

"kang-harassment": dict(harm=True,
    poc=[],
    poc_note="Personal conduct. Not corruption."),

"morneau-french-villa": dict(
    poc=[
        T("T7", "E4", "minister",
           "The disclosure rule of the Conflict of Interest Act, broken; found by the commissioner. No private benefit shown."),
    ],
    poc_note=""),

"hehr-resignation": dict(
    poc=[],
    poc_note="Personal conduct. The withheld report was sought by no investigator or committee: not obstruction under the elements."),

"india-trip-atwal": dict(against=True,
    poc=[],
    poc_note="A screening failure and a deflection. No element of any type met."),

"leblanc-surf-clam": dict(
    poc=[
        T("T1", "E4", "minister",
           "A lucrative licence to a company run by a relative of the minister's wife; the company had business before the department; no recusal. Found by the commissioner."),
    ],
    poc_note=""),

"vance-allegations-2018": dict(harm=True,
    poc=[],
    poc_note="A refusal to look at evidence. No element of obstruction (no investigator sought records), no benefit, no false statement adjudicated: not corruption. Scored in OA."),

"trans-mountain": dict(
    poc=[],
    poc_note="A policy decision with a public bill. Not corruption."),

"kokanee-summit-allegation": dict(
    poc=[],
    poc_note="Personal conduct, pre-office, never examined. Not corruption under any type; listed in the record as never investigated."),

"grewal-charges": dict(
    poc=[],
    poc_note="Acquitted. Not corruption."),

"snc-lavalin-affair": dict(repeat_after_finding=True,
    poc=[
        T("T2", "E4", "him",
           "The prime minister, his staff, the finance minister's office and the clerk pressed the attorney general over months to overrule the prosecution service on SNC-Lavalin — a decision reserved to her alone. Found by the commissioner."),
        T("T5", "E4", "him",
           "'The allegations in the Globe story this morning are false.' The commissioner found the pressure the story described had happened."),
        T("T6", "E4", "office",
           "The commissioner reported he was denied access to cabinet confidences for nine witnesses; the RCMP said cabinet secrecy blocked much of its investigation. The limits of the waiver were a cabinet decision."),
    ],
    poc_note=""),

"liberalist-judicial-vetting": dict(
    poc=[
        T("T4", "E1", "office",
           "If proven: appointments steered to party-connected candidates. The vetting is admitted; that appointments were skewed by it is not on this record."),
    ],
    poc_note="Listed. The practice is admitted; the outcome element is not on the record, so it scores nothing."),

"ng-pomp-circumstance": dict(
    poc=[
        T("T1", "E4", "minister",
           "Contracts ($22,790) to a friend's firm; the firm had business with the office; no recusal. Found by the commissioner."),
    ],
    poc_note=""),

"winnipeg-lab-documents": dict(against=True,
    poc=[
        T("T6", "E3", "office",
           "Parliament twice ordered the records; the government withheld them and filed a Federal Court application against the Speaker. The agency president was formally admonished by the House. All of it on the record, by the government's own acts."),
    ],
    poc_note="The security lapse itself is scored in OA; the obstruction is the corrupt act."),

"blackface-images": dict(
    poc=[],
    poc_note="Personal conduct. Not corruption."),

"pandemic-preparedness-audit": dict(
    poc=[],
    poc_note="Unpreparedness. Not corruption."),

"baylis-ventilators": dict(
    poc=[
        T("T4", "E1", "government",
           "If proven: a $237-million contract steered to a party-connected firm. The chain of contracts is documented; favouritism was never examined."),
    ],
    poc_note="Listed. Scores nothing."),

"covid-benefit-overpayments": dict(
    poc=[],
    poc_note="A design choice and its cost. Not corruption."),

"we-charity": dict(money_in_play=912_000_000,
    poc=[
        T("T1", "E3", "him",
           "A benefit to his family (about $282,000 in fees from WE); WE had a $912-million programme before cabinet; he did not recuse — all admitted. Cleared because the Act's 'private interest' excludes relatives' fees.",
           note="Cleared under the Act, May 2021. The Supreme Court struck down the clause shielding that clearance in July 2026; the Federal Court of Appeal now reviews it.", cleared_under_law=True),
        T("T6", "E3", "him",
           "Four committee studies were under way; prorogation on August 18, 2020 ended them. A motion for a special committee was made a confidence vote and defeated. Both his decisions, on the record."),
    ],
    poc_note=""),

"lucki-nova-scotia-call": dict(
    poc=[],
    poc_note="Examined and no interference found. Not corruption."),

"arrivecan": dict(
    poc=[
        T("T4", "E4", "government",
           "Some $60 million of public money went to contractors without the controls the rules require; in 76% of contracts people paid for did no work (procurement ombud). Found by the Auditor General."),
    ],
    poc_note=""),

"firearms-buyback-program": dict(
    poc=[],
    poc_note="A programme that did not deliver. Not corruption."),

"morneau-we-charity": dict(money_in_play=912_000_000,
    poc=[
        T("T1", "E4", "minister",
           "Free travel from WE; WE had a $912-million programme before the minister; no recusal. Found by the commissioner: preferential treatment, a decision in conflict, failure to recuse."),
    ],
    poc_note=""),

"nuctech-standing-offer": dict(
    poc=[],
    poc_note="A procurement lapse, reversed. Not corruption."),

"access-to-information-decline": dict(against=True,
    poc=[],
    poc_note="Systemic non-transparency, scored in OA. No specific order or investigator refused in this case: not obstruction under the elements."),

"michael-chong-zhao-wei": dict(harm=True, against=True,
    poc=[],
    poc_note="Negligence, not corruption."),

"blair-csis-warrant-delay": dict(against=True,
    poc=[],
    poc_note="Delay, not corruption."),

"afghanistan-evacuation-2021": dict(harm=True, against=True,
    poc=[],
    poc_note="Operational failure. Not corruption."),

"snap-election-2021": dict(
    poc=[],
    poc_note="Calling an election is politics, whatever it costs. Not corruption."),

"sajjan-afghan-sikhs": dict(
    poc=[
        T("T4", "E1", "minister",
           "If proven: military resources directed for a domestic political constituency. Reported; denied; never examined."),
    ],
    poc_note="Listed. Scores nothing."),

"tofino-truth-reconciliation-day": dict(
    poc=[
        T("T5", "E3", "office",
           "The itinerary his office issued stated a location that was false; corrected after a reporter asked. The office knew where he was."),
    ],
    poc_note=""),

"emergencies-act-2022": dict(harm=True,
    poc=[
        T("T3", "E4", "him",
           "Bank accounts frozen (about 257) and protest powers used under a declaration the courts found had no lawful basis and breached the Charter. The declaration was cabinet's, announced by him."),
    ],
    poc_note=""),

"mendicino-police-request-claim": dict(
    poc=[
        T("T5", "E3", "minister",
           "'Police asked for it' — contradicted by the police chiefs' testimony and walked back by his own deputy. The minister was in a position to know."),
    ],
    poc_note=""),

"boissonnault-global-health-imports": dict(
    poc=[],
    poc_note="Examined; no element met at grade E2 or better."),

"london-hotel-queen-funeral": dict(
    poc=[],
    poc_note="Extravagance and a refusal to answer a reporter. Not corruption under the elements."),

"foreign-interference-response": dict(against=True,
    poc=[],
    poc_note="Slowness and poor communication. Not corruption."),

"mckinsey-outsourcing": dict(
    poc=[
        T("T4", "E4", "government",
           "$209 million in contracts awarded with frequent disregard for the procurement rules. Found by the Auditor General."),
    ],
    poc_note="The Auditor General found no evidence of political direction in the awards; scored as money without the rules, at the department's proximity."),

"hussen-constituency-contracts": dict(
    poc=[
        T("T4", "E1", "minister",
           "If proven: $93,050 to a firm run by a staffer's sister. The payments are documented; impropriety was never examined."),
    ],
    poc_note="Listed. Scores nothing."),

"han-dong": dict(
    poc=[],
    poc_note="Undetermined by the inquiry. Not scored."),

"mendicino-bernardo-transfer": dict(
    poc=[
        T("T5", "E2", "minister",
           "'Found out from the news' — Corrections' records show his office was briefed months before. Whether the minister himself was told was never examined."),
    ],
    poc_note=""),

"david-johnston-rapporteur": dict(against=True,
    poc=[
        T("T4", "E2", "him",
           "A $4.5-million appointment went to a long-time family friend; the House voted 174–150 that he step aside. The friendship is on the record; the vote is Parliament's, not an adjudication."),
    ],
    poc_note=""),

"hunka-recognition": dict(
    poc=[],
    poc_note="Not corruption."),

"sdtc-green-fund": dict(
    poc=[
        T("T4", "E4", "government",
           "$76 million in 90 funding decisions where conflict-of-interest rules were not followed; $59 million to ineligible projects; the chair found in breach. Found by the Auditor General and the commissioner."),
        T("T6", "E3", "office",
           "The House ordered the documents; the government did not fully comply; the House sat on the privilege question for four months. On the record."),
    ],
    poc_note=""),

"carbon-charge-heating-oil": dict(
    poc=[],
    poc_note="Regional relief and a partisan remark. Relief to a region is not money to insiders: not scored."),

"jamaica-vacation": dict(
    poc=[
        T("T5", "E3", "office",
           "'The family was covering the cost' — then 'at no cost at a location owned by family friends' — then 'with family friends'. The office's own three statements, on the record."),
    ],
    poc_note="The stay itself was cleared in advance and the host had no dealings with the government: not self-dealing under the elements."),

"nsicop-2024-parliamentarians": dict(
    poc=[],
    poc_note="Not corruption."),

"immigration-could-have-acted-quicker": dict(
    poc=[],
    poc_note="An admitted policy error. Not corruption."),

"freeland-resignation": dict(
    poc=[],
    poc_note="A resignation and a missed target. Not corruption."),

"prorogation-2025": dict(
    poc=[],
    poc_note="Examined by a court and upheld. The green-fund order it ended is scored in that case."),

"trudeau-resignation": dict(
    poc=[],
    poc_note="Not corruption."),

}
