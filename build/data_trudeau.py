# -*- coding: utf-8 -*-
"""Politaccount — Justin Trudeau ledger. Source of truth for trudeau.json and the page.

Every entry: what happened, what the deciding body found (verbatim where possible),
what happened to the Prime Minister, what happened to everyone else, what it cost,
where it stands as of September 2026, and where to check.

result (primary tag) vocabulary:
  VIOLATION_FOUND            Ethics Commissioner found a contravention of the Conflict of Interest Act
  COURT_AGAINST_GOVERNMENT   a court ruled the government's action unlawful
  AUDIT_ADVERSE              Auditor General adverse report
  INQUIRY_FINDING            commission / parliamentary committee / officer of Parliament finding
  BROKEN_COMMITMENT          documented promise, documented non-delivery
  CHARGES                    criminal proceeding (outcome in result_label)
  CHARGES_STAYED             Crown stayed the charge
  RESIGNATION                resignation or removal
  CLEARED                    body examined the matter and found no contravention
  COURT_FOR_GOVERNMENT       a court ruled for the government
  ADMISSION                  on-record admission, apology or policy reversal; no adjudication
  UNADJUDICATED              allegation or reported fact never examined by any body
  RECORD                     spending or cost on the public record; no finding
"""

def S(title, publisher, url, date=None, primary=False):
    return {"title": title, "publisher": publisher, "url": url, "date": date, "primary": primary}

PM, GOV, MIN = "Prime Minister", "Government", "Ministers & caucus"

SUBJECT = {
    "name": "Justin Trudeau",
    "office": "23rd Prime Minister of Canada",
    "party": "Liberal Party of Canada",
    "term_start": "2015-11-04",
    "term_end": "2025-03-14",
    "successor": "Mark Carney",
    "elections": [
        {"year": 2015, "result": "Majority", "seats": 184},
        {"year": 2019, "result": "Minority", "seats": 157},
        {"year": 2021, "result": "Minority", "seats": 160},
    ],
    "resignation_announced": "2025-01-06",
}

# Cabinet departures tied to a ledger entry (for the scorecard). Dates verified in entries.
CABINET_DEPARTURES = [
    {"name": "Hunter Tootoo", "date": "2016-05-31", "entry": "tootoo-resignation", "how": "Resigned (cabinet and caucus)"},
    {"name": "Kent Hehr", "date": "2018-01-25", "entry": "hehr-resignation", "how": "Resigned (cabinet)"},
    {"name": "Jody Wilson-Raybould", "date": "2019-02-12", "entry": "snc-lavalin-affair", "how": "Resigned (cabinet); expelled from caucus Apr 2, 2019"},
    {"name": "Jane Philpott", "date": "2019-03-04", "entry": "snc-lavalin-affair", "how": "Resigned (cabinet); expelled from caucus Apr 2, 2019"},
    {"name": "Bill Morneau", "date": "2020-08-17", "entry": "morneau-we-charity", "how": "Resigned (cabinet and seat)"},
    {"name": "Marco Mendicino", "date": "2023-07-26", "entry": "mendicino-bernardo-transfer", "how": "Dropped in shuffle"},
    {"name": "Randy Boissonnault", "date": "2024-11-20", "entry": "boissonnault-global-health-imports", "how": "Stepped away from cabinet"},
    {"name": "Chrystia Freeland", "date": "2024-12-16", "entry": "freeland-resignation", "how": "Resigned (cabinet)"},
]

ENTRIES = [

# ───────────────────────────── 2015 ─────────────────────────────
dict(
id="electoral-reform",
subject=PM, category="commitments",
title="Electoral reform: “the last election under first past the post”",
date_start="2015-10-19", date_end="2017-02-01",
actors=["Justin Trudeau", "Karina Gould", "Maryam Monsef"],
summary=(
"The 2015 Liberal platform stated that 2015 “will be the last federal election conducted under the "
"first-past-the-post voting system” and promised electoral-reform legislation within 18 months of forming "
"government. On December 1, 2016 the all-party Special Committee on Electoral Reform recommended a proportional "
"system and a referendum on it. On February 1, 2017 the Prime Minister’s mandate letter to the new Minister of "
"Democratic Institutions removed the item. The 2019, 2021 and 2025 elections were held under first past the post."
),
finding=dict(body="Prime Minister’s mandate letter to the Minister of Democratic Institutions", date="2017-02-01",
    result="BROKEN_COMMITMENT", label="Commitment withdrawn",
    quote="A clear preference for a new electoral system, let alone a consensus, has not emerged. Furthermore, without a clear preference or a clear question, a referendum would not be in Canada’s interest. […] Changing the electoral system will not be in your mandate."),
consequence_pm="None. The commitment was withdrawn by his own mandate letter. Announcing his resignation on January 6, 2025, Trudeau said: “I do wish that we’d been able to change the way we elect our governments in this country so that people could simply choose a second choice or a third choice on the same ballot.”",
consequence_others="None.",
public_cost=None,
status="Unfulfilled. Federal elections remain first past the post.",
sources=[
S("Real Change: A New Plan for a Strong Middle Class (2015 platform), p. 27", "Liberal Party of Canada", "https://liberal.ca/wp-content/uploads/sites/292/2020/09/New-plan-for-a-strong-middle-class.pdf", "2015-10-05", True),
S("Minister of Democratic Institutions Mandate Letter (archived)", "Prime Minister of Canada", "https://www.pm.gc.ca/en/mandate-letters/2017/02/01/archived-minister-democratic-institutions-mandate-letter", "2017-02-01", True),
S("Strengthening Democracy in Canada — committee news release", "House of Commons, Special Committee on Electoral Reform", "https://www.ourcommons.ca/DocumentViewer/en/42-1/ERRE/news-release/8647636", "2016-12-01", True),
S("Opposition accuses Trudeau of ‘betrayal’ as Liberals abandon promise of electoral reform", "CBC News", "https://www.cbc.ca/news/politics/trudeau-electoral-reform-mandate-1.3961736", "2017-02-01"),
S("Trudeau says abandoning electoral reform is his biggest regret", "CBC News", "https://amp.cbc.ca/lite/story/1.7426407", "2025-01-07"),
]),

dict(
id="fiscal-record-2015-promise",
subject=PM, category="commitments",
title="Deficits and debt against the 2015 balanced-budget promise",
date_start="2015-10-19", date_end="2025-03-14",
actors=["Justin Trudeau", "Bill Morneau", "Chrystia Freeland"],
summary=(
"The 2015 platform promised deficits “of less than $10 billion in each of the next two fiscal years” and a "
"return to balance in 2019. Deficits were $19.0 billion in 2016–17, $19.0 billion in 2017–18 and $14.0 billion in "
"2018–19, then $39.4 billion in 2019–20 before the pandemic. No budget was balanced in the tenure. Federal debt "
"stood at $628.9 billion on March 31, 2015 (restated basis) and $1,266.5 billion on March 31, 2025; public debt "
"charges reached $53.4 billion in 2024–25. In February 2014 Trudeau had said “the budget will balance itself.”"
),
finding=dict(body="Department of Finance Canada — Fiscal Reference Tables and Annual Financial Reports", date="2025-12-01",
    result="BROKEN_COMMITMENT", label="Commitment broken",
    quote="Platform: deficits “of less than $10 billion in each of the next two fiscal years” and a “balanced budget in 2019.” Record: no balanced budget in any year, 2015–16 to 2024–25."),
consequence_pm="None. The balanced-budget target was replaced by a declining debt-to-GDP “fiscal anchor”; federal debt-to-GDP rose from 31.5% (2014–15) to 42.1% (2023–24).",
consequence_others="None.",
public_cost="Federal debt rose from $628.9 billion (March 31, 2015, restated) to $1,266.5 billion (March 31, 2025). Public debt charges: $53.4 billion in 2024–25.",
status="Record closed with the 2024–25 fiscal year, the last to overlap the tenure.",
sources=[
S("Fiscal Reference Tables 2022, Part 1 (Table 1)", "Department of Finance Canada", "https://www.canada.ca/en/department-finance/services/publications/fiscal-reference-tables/2022/part-1.html", "2022-11-01", True),
S("Annual Financial Report of the Government of Canada, 2023–2024", "Department of Finance Canada", "https://www.canada.ca/en/department-finance/services/publications/annual-financial-report/2024.html", "2024-12-17", True),
S("Annual Financial Report of the Government of Canada, 2024–2025", "Department of Finance Canada", "https://www.canada.ca/en/department-finance/services/publications/annual-financial-report/2025.html", "2025-12-01", True),
S("Real Change: A New Plan for a Strong Middle Class (2015 platform)", "Liberal Party of Canada", "https://liberal.ca/wp-content/uploads/sites/292/2020/09/New-plan-for-a-strong-middle-class.pdf", "2015-10-05", True),
]),

# ───────────────────────────── 2016 ─────────────────────────────
dict(
id="phoenix-pay-system",
subject=GOV, category="spending",
title="Phoenix pay system",
date_start="2016-02-24", date_end=None,
actors=["Public Services and Procurement Canada", "IBM Canada", "Michael Ferguson (Auditor General)", "Karen Hogan (Auditor General)"],
summary=(
"Phoenix was procured from 2009 and switched on by the Trudeau government "
"in February 2016. The Auditor General reported in November 2017 that the department had failed to resolve pay "
"problems, and in May 2018 called the project “an incomprehensible failure of project management and oversight.” "
"By 2025 the cost of fixing Phoenix had reached $5.1 billion. The Auditor General’s 2026 report counted more than "
"233,000 unresolved pay transactions as of September 30, 2025 and put the Dayforce replacement at $4.2 billion "
"before transition costs."
),
finding=dict(body="Auditor General of Canada — Spring 2018 Report 1, Building and Implementing the Phoenix Pay System", date="2018-05-29",
    result="AUDIT_ADVERSE", label="Adverse audit",
    quote="An incomprehensible failure of project management and oversight."),
consequence_pm="None.",
consequence_others="No minister or deputy minister was removed.",
public_cost="$5.1 billion spent fixing Phoenix to 2025 (official testimony to a Commons committee); replacement estimated at $4.2 billion before transition costs (Auditor General, 2026).",
status="Still in use as of September 2026 with a backlog above 233,000 transactions; the Dayforce transition is under way on a shortened timeline.",
sources=[
S("Report 1—Building and Implementing the Phoenix Pay System (2018 Spring Reports)", "Office of the Auditor General of Canada", "https://www.oag-bvg.gc.ca/internet/english/parl_oag_201805_01_e_43033.html", "2018-05-29", True),
S("Report 1, Building and implementing the Phoenix pay system — publication record", "Government of Canada Publications", "https://publications.gc.ca/site/eng/9.864945/publication.html", "2018-05-29", True),
S("Fixing problems with Phoenix payroll system cost taxpayers $5.1 billion: official", "The Canadian Press", "https://www.thecanadianpressnews.ca/politics/fixing-problems-with-phoenix-payroll-system-cost-taxpayers-5-1-billion-official/article_6d5c2997-e509-5bac-8b20-06fbd06051db.html", "2025-06-01"),
S("Replacing Phoenix pay system will cost at least $4.2-billion, Auditor-General report says", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-phoenix-pay-system-auditor-general-report-42-billion/", "2026-03-01"),
S("From Phoenix to Dayforce: Auditor general warns of risks", "Canadian HR Reporter", "https://www.hrreporter.com/focus-areas/hr-technology/from-phoenix-to-dayforce-auditor-general-warns-of-risks/394204", "2026-03-23"),
]),

dict(
id="elbowgate",
subject=PM, category="conduct",
title="Physical contact in the House (“Elbowgate”)",
date_start="2016-05-18", date_end="2016-05-31",
actors=["Justin Trudeau", "Gord Brown", "Ruth Ellen Brosseau"],
summary=(
"On May 18, 2016, during a delay before a vote, Trudeau crossed the floor, took Conservative whip Gord Brown by "
"the arm to move him through a group of NDP MPs and elbowed NDP MP Ruth Ellen Brosseau, who left the chamber and "
"missed the vote. He apologized in the House that day and again on May 19. The Speaker found a prima facie question "
"of privilege and the House referred the matter to the Procedure and House Affairs committee, which on May 31 agreed "
"unanimously to take no further action after Brosseau accepted the apology."
),
finding=dict(body="Standing Committee on Procedure and House Affairs (referral on a prima facie question of privilege)", date="2016-05-31",
    result="ADMISSION", label="Apologized; no further action",
    quote="The committee agreed unanimously to take no further action after Ms. Brosseau stated she accepted the Prime Minister’s apology."),
consequence_pm="Two apologies in the House (May 18 and 19, 2016). No sanction.",
consequence_others="None.",
public_cost=None,
status="Closed.",
sources=[
S("All-party committee agrees to accept Trudeau’s apology and move on", "The Canadian Press via National Observer", "https://www.nationalobserver.com/2016/05/31/news/all-party-committee-agrees-accept-trudeaus-apology-and-move", "2016-05-31"),
S("Committee drops matter of Trudeau’s tussle after NDP MP’s request", "The Globe and Mail", "https://www.theglobeandmail.com/news/politics/move-on-former-mp-advises-committee-studying-elbowgate/article30216595/", "2016-05-31"),
S("Justin Trudeau apologizes for ‘failing to live up to a higher standard’", "CBC News", "https://www.cbc.ca/lite/story/1.3589007", "2016-05-19"),
]),

dict(
id="cash-for-access-fundraisers",
subject=PM, category="ethics",
title="Cash-for-access fundraisers",
date_start="2016-05-19", date_end="2017-02-14",
actors=["Justin Trudeau", "Zhang Bin", "Benson Wong", "Miaofei Pan", "Mary Dawson (Ethics Commissioner)"],
summary=(
"Through 2016 Trudeau attended Liberal Party fundraisers at private homes with tickets of up to $1,525: on May 19, "
"2016 at the Toronto home of Chinese Business Chamber of Commerce chair Benson Wong, attended by businessman Zhang "
"Bin, and on November 7, 2016 at the West Vancouver home of developer Miaofei Pan, with about 80 guests. Weeks after "
"the May event, Zhang Bin and Niu Gensheng announced a $1-million gift that included $200,000 to the Pierre Elliott "
"Trudeau Foundation and $50,000 for a statue of Pierre Trudeau. Commissioner Dawson called the practice “not very "
"savoury” in December 2016 and, by letter of February 14, 2017, found no reason to believe Trudeau had contravened "
"the Act."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Mary Dawson — letter to the Prime Minister (no formal examination)", date="2017-02-14",
    result="CLEARED", label="Cleared",
    quote="After carefully reviewing the information and documents provided by Mr. Trudeau in response to my request… I have found no reason to believe that Mr. Trudeau contravened sections 7 or 16 of the act in relation to the fundraisers."),
consequence_pm="None. Trudeau announced in January 2017 that the private-home format would end; Bill C-50 later required advance notice and reporting of leaders’ fundraisers.",
consequence_others="None.",
public_cost=None,
status="Closed. The $200,000 Foundation donation resurfaced in 2023 (see the Trudeau Foundation entry).",
sources=[
S("Open and Accountable Government — Annex B, Fundraising and Dealing with Lobbyists: “no preferential access to government, or appearance of preferential access, accorded to individuals or organizations because they have made financial contributions to politicians and political parties”", "Office of the Prime Minister", "https://www.pm.gc.ca/en/news/backgrounders/2015/11/27/open-and-accountable-government", "2015-11-27", primary=True),
S("Trudeau attended cash-for-access fundraiser with Chinese billionaires", "The Globe and Mail", "https://www.theglobeandmail.com/news/politics/trudeau-attended-cash-for-access-fundraiser-with-chinese-billionaires/article32971362/", "2016-11-22"),
S("Ethics Commissioner to question Trudeau on cash-for-access fundraisers", "The Globe and Mail", "https://www.theglobeandmail.com/news/politics/ethics-commissioner-to-question-trudeau-on-cash-for-access-fundraisers/article33329767/", "2016-12-15"),
S("Ethics commissioner cleared Trudeau’s fundraising in February", "CBC News", "https://amp.cbc.ca/lite/story/1.4089202", "2017-04-27"),
S("Trudeau to end controversial cash-for-access fundraisers", "The Globe and Mail", "https://www.theglobeandmail.com/news/politics/trudeau-cash-for-access-fundraisers-changes/article33788333/", "2017-01-27"),
]),

dict(
id="tootoo-resignation",
subject=MIN, category="conduct",
title="Hunter Tootoo leaves cabinet and caucus",
date_start="2016-05-31", date_end="2016-08-04",
actors=["Hunter Tootoo", "Justin Trudeau"],
summary=(
"On May 31, 2016 Fisheries Minister Hunter Tootoo resigned from cabinet and the Liberal caucus and entered "
"treatment for alcohol addiction. In August 2016 he disclosed “a consensual but inappropriate relationship” in the "
"workplace; the Prime Minister’s Office confirmed Tootoo had told Trudeau of the relationship and agreed to withdraw "
"from cabinet and caucus. He sat as an Independent for the rest of the Parliament."
),
finding=dict(body="None (resignation; no formal investigation reported)", date="2016-05-31",
    result="RESIGNATION", label="Resigned",
    quote="“I am ashamed, and I apologize to all involved, especially the people of Nunavut. I am deeply sorry.” — Tootoo, August 2016."),
consequence_pm="None.",
consequence_others="Tootoo left cabinet and caucus on May 31, 2016 and did not return.",
public_cost=None,
status="Closed.",
sources=[
S("Hunter Tootoo apologizes for ‘consensual but inappropriate relationship’", "CBC News", "https://www.cbc.ca/news/canada/north/hunter-tootoo-apologizes-for-relationship-1.3706394", "2016-08-04"),
S("Hunter Tootoo quit caucus, cabinet over ‘inappropriate relationship’", "The Globe and Mail", "https://www.theglobeandmail.com/news/politics/mp-hunter-tootoo-quit-caucus-cabinet-over-consensual-relationship/article31264673/", "2016-08-04"),
]),

dict(
id="butts-telford-moving-expenses",
subject=GOV, category="spending",
title="PMO relocation expenses for Butts and Telford",
date_start="2016-09-22", date_end="2016-09-22",
actors=["Gerald Butts", "Katie Telford", "Justin Trudeau"],
summary=(
"In September 2016 the Globe and Mail reported that the government had paid $207,052 in relocation expenses for "
"principal secretary Gerald Butts ($126,670) and chief of staff Katie Telford ($80,383) to move from Toronto to "
"Ottawa under a Treasury Board policy dating to the 1970s; relocation for 47 political staff totalled about $1.1 "
"million. On September 22, 2016 Butts and Telford announced they would repay $64,992 between them, and Trudeau asked "
"the Treasury Board to write a new relocation policy."
),
finding=dict(body="None (repayment; no audit or examination)", date="2016-09-22",
    result="ADMISSION", label="Repaid in part",
    quote="“While the rules were clear and we followed them, we both know that’s not always enough. […] We take full responsibility for this having happened and because of that we are sorry.” — Butts and Telford, September 22, 2016."),
consequence_pm="None. Ordered a review of the relocation policy.",
consequence_others="Butts repaid $41,619 and Telford $23,374; the remaining $142,060 stood.",
public_cost="$207,052 approved for two staff, reduced by $64,992 in repayments; about $1.1 million for 47 political staff overall.",
status="Closed.",
sources=[
S("Top Trudeau aides Butts, Telford expensed over $200,000 for moving homes", "The Globe and Mail", "https://www.theglobeandmail.com/news/politics/top-trudeau-aides-butts-telford-expensed-over-200000-for-moving-homes/article31995512/", "2016-09-21"),
S("Senior PMO staffers Gerald Butts and Katie Telford to return $65K in ‘unreasonable’ moving expenses", "CBC News", "https://amp.cbc.ca/lite/story/1.3774979", "2016-09-22"),
]),

dict(
id="aga-khan-vacation",
subject=PM, category="ethics",
title="Aga Khan vacation (Bells Cay, Bahamas)",
date_start="2016-12-26", date_end="2017-12-20",
actors=["Justin Trudeau", "The Aga Khan", "Mary Dawson (Ethics Commissioner)", "RCMP"],
summary=(
"Trudeau, his family and friends stayed on the Aga Khan’s private island in the Bahamas from December 26, 2016 to "
"January 4, 2017; family members had stayed there in March 2016. The Aga Khan Foundation Canada was registered to "
"lobby the Prime Minister’s Office at the time. On December 20, 2017 Commissioner Mary Dawson found that Trudeau "
"contravened sections 5, 11, 12 and 21 of the Conflict of Interest Act — the first prime minister found in "
"contravention since the Act took effect in 2007. Security and travel for the December trip cost $215,398. RCMP "
"records released in April 2022 showed the force had weighed a charge under s. 121(1)(c) of the Criminal Code "
"(frauds on the government) and closed its file in 2019."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Mary Dawson — The Trudeau Report", date="2017-12-20",
    result="VIOLATION_FOUND", label="Contravened ss. 5, 11, 12, 21",
    quote="I found that Mr. Trudeau contravened sections 5, 11, 12 and 21 of the Act. […] The vacations accepted by Mr. Trudeau or his family might reasonably be seen to have been given to influence Mr. Trudeau. […] There were no private interactions between Mr. Trudeau and the Aga Khan until Mr. Trudeau became Leader of the Liberal Party of Canada. This led me to conclude that their relationship cannot be described as one of friends for the purposes of the Act."),
consequence_pm="No penalty. The Act’s administrative penalties (s. 52, maximum $500) apply only to reporting failures; s. 47 leaves any further measure to others, and none was taken. Trudeau said he accepted the report and would clear future family vacations with the Commissioner.",
consequence_others="RCMP: no charge. Commissioner Brenda Lucki wrote to MP Peter Kent in August 2019 that the force “cannot productively pursue a criminal investigation.” The released analysis said it was “unclear whether Mr. Trudeau can be prosecuted under Section 121(1)(c)” because that section permits benefits accepted with the written consent of the head of the official’s branch of government, and it “cannot be definitely determined whether or not Mr. Trudeau can simply provide consent to himself.”",
public_cost="$215,398 for the December 2016 trip: RCMP $153,504; Global Affairs $15,172; Privy Council Office $13,000; DND Challenger flying time about $32,000 plus $1,720 in food and beverages. Parliament had first been told $127,187.",
status="Closed. The finding stands; RCMP file closed 2019; no reopening reported.",
sources=[
S("The Trudeau Report (PDF)", "Office of the Conflict of Interest and Ethics Commissioner, via publications.gc.ca", "https://publications.gc.ca/collections/collection_2017/ccie-ciec/ET4-22-2017-eng.pdf", "2017-12-20", True),
S("Conflict of Interest Act, ss. 47 and 52", "Justice Laws Website", "https://laws-lois.justice.gc.ca/eng/acts/C-36.65/page-4.html", None, True),
S("Trudeau’s Bahamas vacation cost over $215K — far more than initially disclosed", "CBC News", "https://www.cbc.ca/lite/story/1.4286033", "2017-09-13"),
S("Newly released documents show RCMP considered whether to charge Justin Trudeau over Aga Khan trip", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-newly-released-documents-show-rcmp-considered-whether-to-charge-justin/", "2022-04-27"),
S("Conservatives call on RCMP to reopen Trudeau Aga Khan vacation investigation", "Global News", "https://globalnews.ca/news/8790122/justin-trudeau-aga-khan-vacation-rcmp-investigation", "2022-04-27"),
]),

# ───────────────────────────── 2017 ─────────────────────────────
dict(
id="mark-norman-prosecution",
subject=GOV, category="governance",
title="Prosecution of Vice-Admiral Mark Norman",
date_start="2017-01-16", date_end="2019-06-26",
actors=["Mark Norman", "Justin Trudeau", "Harjit Sajjan", "Marie Henein", "Public Prosecution Service of Canada"],
summary=(
"Vice-Chief of the Defence Staff Mark Norman was relieved of duty in January 2017 over the alleged leak of cabinet "
"deliberations about the Davie Shipbuilding supply-ship contract. In April 2017 Trudeau said the case would end up "
"in court, and on February 2, 2018 said it would “inevitably” lead to “court processes”; the RCMP laid one count of "
"breach of trust the following month. Norman’s counsel argued that officials withheld records and used code names to "
"discuss the case. On May 8, 2019 the Crown stayed the charge: “There is no reasonable prospect of conviction.” The "
"House of Commons unanimously apologized to Norman and his family; Trudeau left the chamber before the vote. Norman "
"retired in June 2019 under a confidential settlement."
),
finding=dict(body="Public Prosecution Service of Canada — stay of proceedings", date="2019-05-08",
    result="CHARGES_STAYED", label="Charge stayed",
    quote="“There is no reasonable prospect of conviction.” — Crown prosecutor Barbara Mercier, May 8, 2019. House of Commons motion, adopted unanimously: to “express regret for the personal and professional hardships he endured as a result of his failed prosecution and apologize to him and his family.”"),
consequence_pm="None. Trudeau said the prosecution was “entirely independent of my office.” No inquiry examined his two pre-charge statements or the alleged withholding of records.",
consequence_others="Norman: charge stayed, never returned to his post, retired under a confidential settlement, legal fees paid by the government (reported above $500,000). Sajjan: no consequence.",
public_cost="Norman’s legal fees, reported to exceed $500,000; settlement terms confidential.",
status="Closed.",
sources=[
S("Mark Norman charges dropped", "Global News", "https://globalnews.ca/news/5253178/mark-norman-charges-dropped", "2019-05-08"),
S("Trudeau says case against suspended vice-admiral will ‘inevitably’ go to court", "CBC News", "https://www.cbc.ca/lite/story/1.4516573", "2018-02-02"),
S("Trudeau leaves House before motion for Mark Norman apology unanimously passes", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-trudeau-leaves-house-before-mps-unanimously-pass-motion-apologizing-to/", "2019-05-14"),
S("Vice-Admiral Mark Norman reaches settlement with government, announces retirement", "CBC News", "https://www.cbc.ca/news/politics/mark-norman-retiring-1.5191111", "2019-06-26"),
]),

dict(
id="sajjan-operation-medusa",
subject=MIN, category="conduct",
title="Harjit Sajjan’s “architect of Operation Medusa” claim",
date_start="2017-04-18", date_end="2017-05-02",
actors=["Harjit Sajjan", "Justin Trudeau"],
summary=(
"In a speech in New Delhi on April 18, 2017, Defence Minister Harjit Sajjan said: “I became the architect of an "
"operation called Operation Medusa, where we removed about 1,500 fighters, Taliban fighters, off the battlefield.” "
"Operation Medusa, the September 2006 offensive in Kandahar’s Panjwaii district, was commanded by Brig.-Gen. David "
"Fraser; Sajjan served as a reservist intelligence liaison. After criticism from veterans and the opposition he "
"retracted the description and apologized. Trudeau rejected calls for his resignation."
),
finding=dict(body="None (retraction)", date="2017-04-29",
    result="ADMISSION", label="Retracted",
    quote="“I made a mistake in describing my role. I wish to retract that description and apologize for it. I am truly sorry.” — Sajjan."),
consequence_pm="None. Rebuffed calls for the minister’s resignation.",
consequence_others="Sajjan retained the Defence portfolio.",
public_cost=None,
status="Closed.",
sources=[
S("Defence Minister Sajjan apologizes for claiming he was architect of Operation Medusa", "The Globe and Mail", "https://www.theglobeandmail.com/news/national/defence-minister-sajjan-apologizes-for-claiming-he-was-architect-of-operation-medusa/article34858041/", "2017-04-29"),
S("Defence Minister Harjit Sajjan takes political hit over ‘architect’ claim in Afghan war", "CBC Radio, The Current", "https://www.cbc.ca/radio/thecurrent/the-current-for-may-2-2017-1.4093792/defence-minister-harjit-sajjan-takes-political-hit-over-architect-claim-in-afghan-war-1.4093834", "2017-05-02"),
]),

dict(
id="julie-payette",
subject=GOV, category="governance",
title="Julie Payette: appointment and resignation as Governor General",
date_start="2017-07-13", date_end="2021-01-21",
actors=["Justin Trudeau", "Julie Payette", "Assunta Di Lorenzo", "Privy Council Office"],
summary=(
"Trudeau announced Payette’s appointment on July 13, 2017 without using the vice-regal appointments advisory "
"committee created in 2012. Reports that month disclosed a 2011 second-degree assault charge in Maryland, dropped and "
"expunged, and a 2011 collision in which she struck and killed a pedestrian, closed without a finding of fault; "
"neither had surfaced in vetting. After CBC reported verbal abuse at Rideau Hall in July 2020, the Privy Council "
"Office retained Quintet Consulting, whose review found she “belittled, berated and publicly humiliated” staff in a "
"“toxic, verbally abusive workplace.” Payette resigned January 21, 2021."
),
finding=dict(body="Quintet Consulting — independent workplace review commissioned by the Privy Council Office", date="2021-01-21",
    result="RESIGNATION", label="Resigned",
    quote="The review found a “toxic, verbally abusive workplace” marked by “yelling, screaming, aggressive conduct, demeaning comments and public humiliations.”"),
consequence_pm="None. Trudeau said the vetting process would be strengthened; an advisory group was used for the 2021 appointment of Mary Simon.",
consequence_others="Payette and her secretary Assunta Di Lorenzo resigned. Payette retains a lifetime pension of about $150,000 a year and eligibility for up to $206,000 a year in expenses under the former governors general program.",
public_cost="Lifetime pension of about $150,000 a year plus an expense program of up to $206,000 a year (Governor General’s Act; 1979 cabinet program).",
status="Closed. Pension and expense eligibility continue by statute.",
sources=[
S("Payette resignation shines light on generous pension, expense account for former GGs", "The Canadian Press via Global News", "https://globalnews.ca/news/7610439/julie-payette-pension-expense-account", "2021-01-31"),
S("Trudeau on Payette resignation", "CBC News", "https://www.cbc.ca/news/politics/trudeau-payette-1.5883471", "2021-01-22"),
]),

dict(
id="kang-harassment",
subject=MIN, category="conduct",
title="Darshan Kang: harassment complaint substantiated",
date_start="2017-08-31", date_end="2018-08-31",
actors=["Darshan Kang", "Justin Trudeau", "Pierre Parent (House of Commons Chief Human Resources Officer)"],
summary=(
"In August 2017 a staff member in Liberal MP Darshan Kang’s Calgary constituency office alleged unwanted physical "
"contact, an attempt to enter her hotel room and an offer of money to stay silent; a second woman alleged non-"
"consensual touching from his time in the Alberta legislature. Kang left the Liberal caucus on August 31, 2017. A "
"House of Commons investigation reported in March 2018 found the complaint “partially substantiated” and that some "
"of his proven conduct “represented harassment”; an appeal panel upheld the report in August 2018. Trudeau said "
"Kang would not be readmitted to caucus."
),
finding=dict(body="House of Commons Chief Human Resources Officer — harassment investigation; appeal panel", date="2018-03-02",
    result="RESIGNATION", label="Left caucus; harassment found",
    quote="Complaint “partially substantiated”: “some of Mr. Kang’s proven behaviour and conduct toward Ms. Bassi […] represented harassment.”"),
consequence_pm="None.",
consequence_others="Kang sat as an Independent until the 2019 dissolution and was not readmitted to caucus.",
public_cost=None,
status="Closed.",
sources=[
S("Investigation finds Calgary MP Darshan Kang violated harassment rules", "CBC News", "https://www.cbc.ca/news/canada/calgary/darshan-kang-harassment-mp-investigation-1.4558619", "2018-03-02"),
S("Liberal MP Darshan Kang resigns from caucus amid sexual-harassment allegations", "The Globe and Mail", "https://www.theglobeandmail.com/news/politics/liberal-mp-darshan-kang-resigns-from-caucus-amid-sexual-harassment-allegations/article36140289/", "2017-08-31"),
]),

dict(
id="morneau-french-villa",
subject=MIN, category="ethics",
title="Bill Morneau: undisclosed corporation holding a French villa",
date_start="2017-09-22", date_end="2018-06-25",
actors=["Bill Morneau", "Mary Dawson (Ethics Commissioner)", "Mario Dion (Ethics Commissioner)"],
summary=(
"Finance Minister Bill Morneau held a villa in Provence through a French private corporation incorporated in 2007 "
"and did not disclose the corporation to the Ethics Commissioner until September 22, 2017, after CBC inquiries; his "
"office cited “early administrative confusion.” On October 26, 2017 he agreed to pay a $200 administrative penalty, "
"announced the sale of about one million Morneau Shepell shares and placed his remaining assets in a blind trust. "
"A separate examination of whether he was in conflict in sponsoring pension Bill C-27 ended in June 2018 with no "
"contravention, because the bill was of general application."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner — administrative monetary penalty (s. 52)", date="2017-10-26",
    result="VIOLATION_FOUND", label="Penalty: $200",
    quote="$200 administrative monetary penalty for failing to disclose the private corporation. On Bill C-27 (Dion, June 2018): “Because Bill C-27 is of general application, Mr. Morneau’s interests, those of his relatives, and those of Morneau Shepell Inc. in this matter are excluded from the application of the act.”"),
consequence_pm="None.",
consequence_others="Morneau paid $200 — the only monetary penalty imposed on any member of the ministry in the tenure — and remained Finance Minister.",
public_cost=None,
status="Closed.",
sources=[
S("Finance Minister Bill Morneau waited 2 years to disclose company that owns his French villa to ethics watchdog", "CBC News", "https://amp.cbc.ca/news/politics/morneau-company-france-ethics-1.4351933", "2017-10-13"),
S("Bill Morneau promises share profits to charity, as watchdog considers new investigation", "CBC News", "https://amp.cbc.ca/news/politics/morneau-charity-shares-1.4373653", "2017-10-26"),
S("Ethics watchdog clears Bill Morneau in pension bill fallout", "CBC News", "https://amp.cbc.ca/news/politics/morneau-pension-bill-cleared-1.4710721", "2018-06-25"),
]),

# ───────────────────────────── 2018 ─────────────────────────────
dict(
id="hehr-resignation",
subject=MIN, category="conduct",
title="Kent Hehr resigns from cabinet",
date_start="2018-01-25", date_end="2018-06-06",
actors=["Kent Hehr", "Justin Trudeau"],
summary=(
"On January 25, 2018 Sport and Persons with Disabilities Minister Kent Hehr resigned from cabinet after Kristin "
"Raworth alleged that, as an Alberta MLA, he made sexually suggestive comments to women at the legislature; a "
"second woman alleged inappropriate touching at an event, which Hehr said was unintentional. The Prime Minister’s "
"Office commissioned an independent investigation. On June 6, 2018 the PMO announced Hehr would not return to "
"cabinet and would remain in caucus; the report was not released."
),
finding=dict(body="Independent investigation commissioned by the Prime Minister’s Office; decision by the Prime Minister", date="2018-06-06",
    result="RESIGNATION", label="Resigned; report withheld",
    quote="Outcome announced: Hehr would not be invited back to cabinet and would remain in the Liberal caucus. The investigation report was not made public."),
consequence_pm="None.",
consequence_others="Hehr stayed in caucus as MP for Calgary Centre until the 2019 election.",
public_cost=None,
status="Closed.",
sources=[
S("Liberals’ Kent Hehr resigns from cabinet over sexual-harassment allegations", "The Globe and Mail", "https://www.theglobeandmail.com/news/politics/liberals-kent-hehr-resigns-over-sexual-harassment-allegations/article37733581/", "2018-01-25"),
S("Hehr won’t return to cabinet, but remains in Liberal caucus after harassment investigation", "CBC News", "https://www.cbc.ca/news/politics/hehr-harassment-report-liberal-1.4694165", "2018-06-06"),
]),

dict(
id="india-trip-atwal",
subject=PM, category="governance",
title="India trip and the Jaspal Atwal invitation",
date_start="2018-02-17", date_end="2018-12-03",
actors=["Justin Trudeau", "Jaspal Atwal", "Randeep Sarai", "Daniel Jean (National Security and Intelligence Advisor)", "NSICOP"],
summary=(
"During Trudeau’s February 17–24, 2018 visit to India, Jaspal Atwal — convicted of the 1986 attempted murder of a "
"Punjab minister — attended a Prime Minister’s reception in Mumbai as a guest invited through the PMO and was "
"photographed with Sophie Grégoire Trudeau; his invitation to a Delhi reception was rescinded. MP Randeep Sarai "
"took responsibility. National Security Advisor Daniel Jean briefed journalists on background suggesting factions "
"in India had orchestrated the affair. The National Security and Intelligence Committee of Parliamentarians "
"reviewed the matter and reported on December 3, 2018. The trip cost about $1.66 million, including $17,044 to fly "
"chef Vikram Vij to India."
),
finding=dict(body="National Security and Intelligence Committee of Parliamentarians — Special Report on the India visit", date="2018-12-03",
    result="INQUIRY_FINDING", label="PMO screening failures",
    quote="“Some of the issues raised by Mr. Atwal’s appearance at the events in India should have been more properly addressed by the Prime Minister’s Office, including failures to screen invitees.” […] “The RCMP recognizes that it erred in not providing that information to the Prime Minister’s Protective Detail.” […] “There is no evidence to suggest that the NSIA briefed journalists at the explicit direction of the Prime Minister’s Office.”"),
consequence_pm="None. No one in the PMO was disciplined for the screening failures NSICOP identified.",
consequence_others="Sarai took responsibility for the invitation. The RCMP acknowledged its error. NSICOP recommended background checks for guest lists at foreign events with the Prime Minister.",
public_cost="About $1.66 million for the nine-day trip (Order Paper response, September 2018), including $485,070 in aircraft rental and $17,044 for the chef’s flight.",
status="Closed.",
sources=[
S("Special report into the allegations associated with Prime Minister Trudeau’s official visit to India in February 2018 (PDF)", "National Security and Intelligence Committee of Parliamentarians", "https://www.nsicop-cpsnr.ca/reports/rp-2018-12-03/SpecialReport-en.pdf", "2018-12-03", True),
S("Trudeau’s India trip cost more than the government first disclosed", "CBC News", "https://amp.cbc.ca/news/politics/trudeau-india-spending-scheer-1.4829121", "2018-09-25"),
]),

dict(
id="leblanc-surf-clam",
subject=MIN, category="ethics",
title="Dominic LeBlanc: Arctic surf clam licence",
date_start="2018-02-21", date_end="2018-09-12",
actors=["Dominic LeBlanc", "Mario Dion (Ethics Commissioner)", "Gilles Thériault", "Five Nations Clam Company"],
summary=(
"In February 2018 Fisheries Minister Dominic LeBlanc awarded a new Arctic surf clam licence, a quarter of the total "
"allowable catch, to the Five Nations Clam Company, whose intended general manager, Gilles Thériault, was a first "
"cousin of LeBlanc’s wife and had raised the licensing issue with him before the decision. The department cancelled "
"the process in July 2018. On September 12, 2018 Commissioner Mario Dion found LeBlanc contravened subsection 6(1) "
"of the Conflict of Interest Act. LeBlanc accepted the finding “without reservation.”"
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Mario Dion — The LeBlanc Report", date="2018-09-12",
    result="VIOLATION_FOUND", label="Contravened s. 6(1)",
    quote="“When they are aware of an opportunity to further the private interests of a relative through the exercise of an official power, duty or function, they must be vigilant.”"),
consequence_pm="None. LeBlanc stayed in cabinet through the end of the tenure.",
consequence_others="LeBlanc: no penalty (the Act provides none for s. 6). The licence award was withdrawn and the process restarted.",
public_cost=None,
status="Closed.",
sources=[
S("LeBlanc report, made under the Conflict of Interest Act — publication record", "Government of Canada Publications", "https://publications.gc.ca/site/eng/9.861934/publication.html", "2018-09-12", True),
S("Dominic LeBlanc found in conflict of interest over lucrative fishing licence", "CBC News", "https://amp.cbc.ca/news/politics/leblanc-conflict-of-interest-fishing-licence-1.4820213", "2018-09-12"),
S("Cabinet minister Dominic LeBlanc broke rules in awarding clam licence, ethics commissioner finds", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-dominic-leblanc-found-in-conflict-of-interest-for-awarding-clam/", "2018-09-12"),
]),

dict(
id="vance-allegations-2018",
subject=GOV, category="governance",
title="Gen. Jonathan Vance: the 2018 warning",
date_start="2018-03-01", date_end="2022-05-30",
actors=["Harjit Sajjan", "Jonathan Vance", "Gary Walbourne", "Katie Telford", "Elder Marques", "Justin Trudeau"],
summary=(
"On March 1, 2018 Canadian Forces Ombudsman Gary Walbourne told Defence Minister Harjit Sajjan of an allegation "
"of inappropriate behaviour against Chief of the Defence Staff Gen. Jonathan Vance. Walbourne testified in 2021 that "
"when he reached to show the evidence, Sajjan “pushed back from the table and said, No.” Chief of staff Katie "
"Telford testified the PMO learned of a complaint the next day but not its nature and did not tell the Prime "
"Minister. Vance remained Chief of the Defence Staff until January 2021. Military police charged him with "
"obstruction of justice in 2021; he pleaded guilty on March 30, 2022 to repeatedly contacting a complainant to "
"persuade her to make false statements. Justice Louise Arbour’s review followed in May 2022."
),
finding=dict(body="Ontario Court of Justice — guilty plea (Vance); Independent External Comprehensive Review (Arbour)", date="2022-03-30",
    result="CHARGES", label="Guilty plea (Vance)",
    quote="Walbourne, March 3, 2021: “I reached into my pocket to show him the evidence I was holding. He pushed back from the table and said, No. The minister didn’t want to see the evidence.” Telford, May 7, 2021: “We didn’t know the nature of the allegation.”"),
consequence_pm="None. Trudeau kept confidence in Sajjan after the ombudsman’s testimony.",
consequence_others="Sajjan: no sanction; moved to International Development in October 2021. Vance: conditional discharge, 12 months’ probation, 80 hours of community service, no criminal conviction recorded. No PMO or PCO official was disciplined. Arbour made 48 recommendations, all accepted.",
public_cost=None,
status="Closed. Arbour recommendations under implementation.",
sources=[
S("Government releases final Independent External Comprehensive Review", "Department of National Defence", "https://www.canada.ca/en/department-national-defence/news/2022/05/government-releases-final-independent-external-comprehensive-review-of-the-department-of-national-defence-and-the-canadian-armed-forces-and-outline.html", "2022-05-30", True),
S("Vance investigation: Walbourne testifies", "Global News", "https://globalnews.ca/news/7673801/vance-investigation-walbourne-testify", "2021-03-03"),
S("Telford says PMO didn’t know nature of allegations against Gen. Vance", "Global News", "https://globalnews.ca/news/7842824/canadian-forces-sexual-misconduct-justin-trudeau-katie-telford", "2021-05-07"),
S("Former top military commander pleads guilty to obstruction of justice", "CBC News", "https://www.cbc.ca/lite/story/1.6402233", "2022-03-30"),
S("Trudeau says he still has confidence in Sajjan after ombudsman’s testimony", "CBC News", "https://www.cbc.ca/news/politics/sajjan-vance-walbourne-trudeau-canadian-forces-1.5938534", "2021-03-04"),
]),

dict(
id="trans-mountain",
subject=GOV, category="spending",
title="Trans Mountain purchase and expansion",
date_start="2018-05-29", date_end=None,
actors=["Justin Trudeau", "Bill Morneau", "Trans Mountain Corporation", "Parliamentary Budget Officer"],
summary=(
"On May 29, 2018 the government announced it would buy the Trans Mountain pipeline and expansion project from "
"Kinder Morgan for $4.5 billion; the purchase closed August 31, 2018. The expansion’s cost rose from a $21.4-billion "
"estimate in 2022 to $34.2 billion, and the line entered service in May 2024. The Parliamentary Budget Officer’s "
"November 2024 report valued the system at $29.6 billion to $33.4 billion against $35.2 billion in assets on the "
"corporation’s books, so a sale at those values would record a loss. The pipeline remains federally owned."
),
finding=dict(body="Office of the Parliamentary Budget Officer — Trans Mountain Pipeline, 2024 Report", date="2024-11-08",
    result="RECORD", label="PBO: likely loss on sale",
    quote="“Whether the Government records a profit or a loss on the eventual sale of the Trans Mountain Pipeline system will depend on what someone is willing to pay for it.”"),
consequence_pm="None.",
consequence_others="None. The federal government remains owner and financier through the Canada Development Investment Corporation.",
public_cost="$4.5 billion purchase (2018) plus a $34.2 billion expansion (PBO, 2024); PBO valuation of $29.6–33.4 billion implies a loss against book value.",
status="Federally owned as of September 2026; no sale announced.",
sources=[
S("Trans Mountain Pipeline – 2024 Report", "Office of the Parliamentary Budget Officer", "https://www.pbo-dpb.ca/en/publications/RP-2425-021-S--trans-mountain-pipeline-2024-report--reseau-pipelines-trans-mountain-rapport-2024", "2024-11-08", True),
S("Federal government faces potential loss if Trans Mountain pipeline sold: budget watchdog", "CBC News", "https://www.cbc.ca/news/politics/government-potential-loss-trans-mountain-sale-1.7378043", "2024-11-08"),
]),

dict(
id="kokanee-summit-allegation",
subject=PM, category="conduct",
title="Kokanee Summit allegation (2000 editorial)",
date_start="2018-06-06", date_end="2018-07-06",
actors=["Justin Trudeau", "Rose Knight", "Creston Valley Advance"],
summary=(
"In August 2000 the Creston Valley Advance published an unsigned editorial stating that Trudeau, then 28, had "
"groped a female reporter at the Kokanee Summit festival and apologized the next day, saying he would not have "
"“been so forward” had he known she was reporting for a national newspaper. The editorial recirculated in June 2018. "
"Trudeau said on July 1, 2018 that he did not “remember any negative interactions that day at all,” and on July 5 "
"that he was “confident I did not act inappropriately” and that a woman, “particularly in a professional context, can "
"experience it differently.” On July 6 the reporter, Rose Knight, stated: “The incident referred to in the editorial "
"did occur, as reported… I did not pursue the incident at the time and will not be pursuing the incident further.”"
),
finding=dict(body="None — no complaint filed, no body examined the matter", date=None,
    result="UNADJUDICATED", label="No adjudication",
    quote="The complainant confirmed the editorial’s account and declined further participation; the Prime Minister stated he did not act inappropriately."),
consequence_pm="None. No investigation, no finding.",
consequence_others="None.",
public_cost=None,
status="No proceeding of any kind.",
sources=[
S("Woman Who Says Justin Trudeau Groped Her Identifies Herself", "Time", "https://time.com/5328843/canadian-prime-minister-justin-trudeu-denies-groping-reporter/", "2018-07-03"),
S("The Woman Who Accused Trudeau of Groping Speaks Out", "Vice", "https://www.vice.com/en/article/the-woman-who-accused-trudeau-of-groping-speaks-out/", "2018-07-06"),
]),

dict(
id="grewal-charges",
subject=MIN, category="conduct",
title="Raj Grewal: charged with breach of trust, acquitted",
date_start="2018-11-22", date_end="2023-03-10",
actors=["Raj Grewal", "RCMP", "Justice Sylvia Corthorn"],
summary=(
"Liberal MP Raj Grewal left caucus in November 2018 after disclosing a gambling problem and large personal debts, "
"and did not run in 2019. In September 2020 the RCMP charged him with four counts of breach of trust and one of "
"fraud, alleging he traded access to events with the Prime Minister and help with immigration files for loans. The "
"Crown withdrew three counts before trial; the two remaining counts concerned $200,000 loans from each of two "
"Brampton-area businessmen, neither of whom testified that they expected anything in return. On March 10, 2023 "
"Justice Sylvia Corthorn entered a directed verdict of not guilty."
),
finding=dict(body="Ontario Superior Court of Justice — directed verdict", date="2023-03-10",
    result="CHARGES", label="Charged; acquitted",
    quote="“I find Mr. Grewal not guilty.” A reasonable jury “would not have been able to render a guilty verdict.”"),
consequence_pm="None.",
consequence_others="Grewal left caucus (November 2018) and did not seek re-election; acquitted March 10, 2023.",
public_cost=None,
status="Closed.",
sources=[
S("Breach of trust charges against former Liberal MP Raj Grewal dismissed", "The Canadian Press via Global News", "https://globalnews.ca/news/9543036/breach-of-trust-charges-raj-grewal-dismissed/", "2023-03-10"),
S("Former Liberal MP found not guilty on breach of trust charges", "CBC News", "https://www.cbc.ca/news/politics/raj-grewal-breach-of-trust-1.6774707", "2023-03-10"),
]),

# ───────────────────────────── 2019 ─────────────────────────────
dict(
id="snc-lavalin-affair",
subject=PM, category="ethics",
title="SNC-Lavalin affair",
date_start="2019-02-07", date_end="2019-08-14",
actors=["Justin Trudeau", "Jody Wilson-Raybould", "Gerald Butts", "Michael Wernick", "Jane Philpott", "Mario Dion (Ethics Commissioner)", "SNC-Lavalin"],
summary=(
"In September 2018 the Director of Public Prosecutions declined to invite SNC-Lavalin to negotiate a remediation "
"agreement in its fraud and corruption case. Over the following months the Prime Minister, his staff, the Finance "
"Minister’s office and the Clerk of the Privy Council pressed Attorney General Jody Wilson-Raybould to intervene. "
"The Globe and Mail reported the pressure on February 7, 2019. Wilson-Raybould resigned from cabinet February 12; "
"principal secretary Gerald Butts resigned February 18; Wilson-Raybould testified February 27; Jane Philpott "
"resigned March 4; Clerk Michael Wernick announced his retirement March 18; Trudeau expelled both former ministers "
"from caucus April 2. On August 14, 2019 Commissioner Mario Dion found Trudeau contravened section 9 of the Act."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Mario Dion — Trudeau II Report", date="2019-08-14",
    result="VIOLATION_FOUND", label="Contravened s. 9",
    quote="“The evidence showed there were many ways in which Mr. Trudeau, either directly or through the actions of those under his direction, sought to influence the Attorney General. […] The actions that sought to further these interests were improper since they were contrary to the Shawcross doctrine and the principles of prosecutorial independence and the rule of law. […] Therefore, I find that Mr. Trudeau contravened section 9 of the Act.”"),
consequence_pm="No penalty: section 9 carries none under the Act, and no parliamentary measure followed. Trudeau said he took responsibility for what happened and could not apologize “for standing up for Canadian jobs.”",
consequence_others="Wilson-Raybould and Philpott lost their cabinet posts and their caucus seats; Butts resigned; Wernick retired. RCMP: file concluded by January 2023 with “insufficient evidence to substantiate a criminal offence”; Commissioner Michael Duheme told MPs in February 2024 that cabinet privilege limited the investigation and that Trudeau was not interviewed. SNC-Lavalin Construction Inc. pleaded guilty to fraud on December 18, 2019 and was fined $280 million.",
public_cost=None,
status="Closed. The finding stands; no charges.",
sources=[
S("Trudeau II Report (PDF)", "Office of the Conflict of Interest and Ethics Commissioner, via publications.gc.ca", "https://publications.gc.ca/collections/collection_2019/ccie-ciec/ET4-28-2019-eng.pdf", "2019-08-14", True),
S("Evidence, Standing Committee on Access to Information, Privacy and Ethics, Meeting 105 (RCMP Commissioner Duheme)", "House of Commons of Canada", "https://www.ourcommons.ca/documentviewer/en/44-1/ETHI/meeting-105/evidence", "2024-02-27", True),
S("SNC-Lavalin Construction Inc. Pleads Guilty to Fraud", "Public Prosecution Service of Canada", "https://www.ppsc-sppc.gc.ca/eng/nws-nvs/2019/18_12_19.html", "2019-12-18", True),
S("RCMP says there was ‘insufficient evidence’ to lay charges in SNC-Lavalin affair", "CBC News", "https://amp.cbc.ca/lite/story/1.6881779", "2023-06-21"),
S("Canada’s PM Trudeau found guilty by ethics commissioner", "Al Jazeera", "https://www.aljazeera.com/news/2019/8/15/canadas-pm-trudeau-found-guilty-by-ethics-commissioner", "2019-08-15"),
]),

dict(
id="liberalist-judicial-vetting",
subject=GOV, category="governance",
title="Vetting judicial candidates with the Liberalist database",
date_start="2019-03-07", date_end="2021-06-01",
actors=["Prime Minister’s Office", "David Lametti", "Justin Trudeau"],
summary=(
"On March 7, 2019 the Globe and Mail reported, from confidential PMO documents, that the Prime Minister’s Office ran "
"judicial candidates recommended by the independent advisory committees through the Liberal Party’s Liberalist voter "
"database. The PMO said all appointments followed a “merit-based process” and that political activity had “no impact "
"on a person’s candidacy.” The Canadian Bar Association said in November 2020 that political vetting threatened "
"public faith in the judiciary. In June 2021 CBC reported that the government had stopped using Liberalist for the "
"purpose while continuing to review candidates’ partisan histories from other sources."
),
finding=dict(body="None — no examination by the Ethics Commissioner or the Canadian Judicial Council", date=None,
    result="UNADJUDICATED", label="No adjudication",
    quote="The PMO confirmed the practice and defended it as merit-based; it was reported discontinued in June 2021."),
consequence_pm="None.",
consequence_others="None.",
public_cost=None,
status="No adjudication.",
sources=[
S("PMO vets potential judges with private Liberal database", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-pmo-vets-potential-judges-with-liberal-database/", "2019-03-07"),
S("Federal government stops using Liberal Party database to vet would-be judges", "CBC News", "https://www.cbc.ca/news/politics/liberalist-judicial-appointments-trudeau-lametti-1.6059297", "2021-06-01"),
S("‘Political vetting’ of appointments threatens public faith in judiciary, says bar association", "CBC News", "https://www.cbc.ca/news/politics/judges-appointment-liberalist-canadian-bar-association-1.5795327", "2020-11-17"),
]),

dict(
id="ng-pomp-circumstance",
subject=MIN, category="ethics",
title="Mary Ng: contracts to a friend’s firm",
date_start="2019-03-26", date_end="2022-12-13",
actors=["Mary Ng", "Amanda Alvaro", "Mario Dion (Ethics Commissioner)"],
summary=(
"Mary Ng, as Minister of Small Business and later International Trade, awarded two media-training contracts to "
"Pomp & Circumstance, a public-relations firm co-founded by Amanda Alvaro, a friend of about twenty years: $5,840 "
"on March 26, 2019 and $16,950 on April 8, 2020. On December 13, 2022 Commissioner Dion found that the relationship "
"met the Act’s definition of friendship and that Ng contravened the Act by failing to recuse herself. Ng: “I should "
"have recused myself and apologize to all for not having done so.”"
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Mario Dion — The Ng Report", date="2022-12-13",
    result="VIOLATION_FOUND", label="Contravened the Act (failure to recuse)",
    quote="Dion found Ng contravened the Act by awarding contracts to a friend’s firm without recusing herself, and noted that “the Conflict of Interest Act does not provide for any sanctions for contraventions.”"),
consequence_pm="None. Trudeau did not remove her; she remained in cabinet until March 2025.",
consequence_others="Ng apologized. No penalty; the contract amounts were not repaid.",
public_cost="$22,790 in the two contracts, paid from departmental funds.",
status="Closed.",
sources=[
S("Trade minister apologizes for breaking conflict of interest rules", "CBC News", "https://www.cbc.ca/news/politics/trade-minister-conflict-of-interest-1.6684025", "2022-12-13"),
S("Trade Minister Mary Ng broke ethics rules over contract to friend, commissioner finds", "Global News", "https://globalnews.ca/news/9345150/trade-minister-mary-ng-ethics-violations/", "2022-12-13"),
]),

dict(
id="winnipeg-lab-documents",
subject=GOV, category="governance",
title="Winnipeg lab scientists and the fight over documents",
date_start="2019-07-05", date_end="2024-02-28",
actors=["Xiangguo Qiu", "Keding Cheng", "Public Health Agency of Canada", "Iain Stewart", "Mark Holland", "Justin Trudeau", "CSIS"],
summary=(
"Scientists Xiangguo Qiu and Keding Cheng were escorted from the National Microbiology Laboratory on July 5, 2019 "
"and dismissed in January 2021. In June 2021 the House of Commons twice ordered the Public Health Agency to produce "
"the unredacted records; on June 21, 2021 PHAC president Iain Stewart was admonished at the bar of the House for "
"refusing, and the government filed a Federal Court application against the Speaker to block the orders — the first "
"of its kind — which it dropped after the August 2021 dissolution. The documents were released on February 28, "
"2024 after review by a panel of former judges. CSIS had assessed that Qiu had an “extensive relationship” with "
"PRC-linked institutions, held a collaboration agreement with the Wuhan Institute of Virology, and “not only failed "
"to inform her employer of these activities but made efforts to conceal her projects.”"
),
finding=dict(body="CSIS security assessments (2020), released via an ad hoc committee of parliamentarians; statement by Health Minister Mark Holland", date="2024-02-28",
    result="ADMISSION", label="Documents withheld, then released",
    quote="Holland, February 28, 2024: the situation was “unacceptable,” reflecting “a lax adherence to the security protocols” and “an inadequate understanding of the threat of foreign interference.”"),
consequence_pm="None. The government’s court application against the Speaker was discontinued and the documents were released two and a half years after the House ordered them.",
consequence_others="Both scientists were dismissed; no charges reported. PHAC’s president was formally admonished by the House.",
public_cost=None,
status="Documents released; studied by the Canada–China committee in 2024.",
sources=[
S("Winnipeg lab documents: what the released records show", "Global News", "https://globalnews.ca/news/10323939/winnipeg-lab-scientists-documents-released/", "2024-02-28"),
S("Winnipeg lab document summary", "Global News", "https://globalnews.ca/news/10327139/winnipeg-lab-document-summary/", "2024-02-28"),
]),

dict(
id="blackface-images",
subject=PM, category="conduct",
title="Blackface and brownface images",
date_start="2019-09-18", date_end="2019-09-19",
actors=["Justin Trudeau"],
summary=(
"On September 18, 2019, during the election campaign, Time published a 2001 yearbook photograph of Trudeau, then a "
"teacher at West Point Grey Academy, in dark makeup and an Aladdin costume at an “Arabian Nights” gala. That evening "
"he apologized and disclosed a second instance from a high-school talent show. On September 19 Global News broadcast "
"a video from the early 1990s showing him in blackface. Asked how many times it had happened, he said he could not "
"say definitively. Three instances are documented."
),
finding=dict(body="None (public apology)", date="2019-09-19",
    result="ADMISSION", label="Admitted; apologized",
    quote="“I shouldn’t have done that. I should have known better… I’m really sorry.” […] “It was something that I didn’t think was racist at the time, but now I recognize it was something racist.”"),
consequence_pm="Public apologies on September 18 and 19, 2019. No investigation. The Liberal Party formed a minority government on October 21, 2019.",
consequence_others="None.",
public_cost=None,
status="Closed.",
sources=[
S("Trudeau says he is ‘deeply sorry’ he appeared in brownface at school gala in 2001", "CBC News", "https://amp.cbc.ca/lite/story/1.5289165", "2019-09-18"),
S("Trudeau apologizes after new video shows he wore blackface", "PBS NewsHour / Associated Press", "https://www.pbs.org/newshour/amp/world/canadian-prime-minister-justin-trudeau-apologizes-for-2001-brownface-photo", "2019-09-19"),
S("Video shows Trudeau in blackface in 3rd instance of racist makeup", "Global News", "https://globalnews.ca/news/5922861/justin-trudeau-brownface-video/amp", "2019-09-19"),
]),

# ───────────────────────────── 2020 ─────────────────────────────
dict(
id="covid-benefit-overpayments",
subject=GOV, category="spending",
title="COVID-19 benefit overpayments and verification",
date_start="2020-04-06", date_end=None,
actors=["Canada Revenue Agency", "Bob Hamilton", "Employment and Social Development Canada", "Karen Hogan (Auditor General)"],
summary=(
"The pandemic benefit programs covered by the Auditor General’s audit paid out $210.7 billion. Her December 6, 2022 "
"report found $4.6 billion in overpayments to ineligible individuals and estimated that at least $27.4 billion in "
"payments to individuals and employers should be investigated further; the agencies “did not develop rigorous and "
"comprehensive plans to verify the eligibility of recipients.” The CRA disputed the $27.4-billion estimate, and its "
"commissioner, Bob Hamilton, told MPs that a full review of flagged wage-subsidy payments would not be worth the "
"effort. By December 2025 the CRA reported $10.35 billion in outstanding COVID benefit debts."
),
finding=dict(body="Auditor General of Canada — 2022 Report 10, Specific COVID-19 Benefits", date="2022-12-06",
    result="AUDIT_ADVERSE", label="Adverse audit",
    quote="“$4.6 billion of overpayments made to ineligible recipients of benefits for individuals”; “at least $27.4 billion of payments to individuals and employers should be investigated further.” Hogan: “I am concerned about the lack of rigour on post-payment verifications and collection activities.”"),
consequence_pm="None.",
consequence_others="None to ministers. The CRA began sending recovery letters in 2023 and terminated some of its own employees who had improperly claimed benefits.",
public_cost="$4.6 billion in confirmed overpayments and at least $27.4 billion flagged for investigation (AG, 2022); $10.35 billion outstanding and about $3.3 billion repaid as of late 2025 (CRA).",
status="Collection ongoing as of September 2026.",
sources=[
S("Report 10—Specific COVID-19 Benefits, 2022 Reports of the Auditor General of Canada", "Office of the Auditor General of Canada", "https://www.canada.ca/en/auditor-general/our-work/audit-reports/parl-oag-202212-10-e.html", "2022-12-06", True),
S("Canada’s auditor general says $27.4B in COVID benefits need more scrutiny", "Global News", "https://globalnews.ca/news/9328690/covid-benefits-cerb-ceba-overpayment-eligibility-ag-report/", "2022-12-06"),
S("Review of billions of COVID-19 wage benefits not worth the effort, CRA head says", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-covid-wage-benefits-cra/", "2023-01-26"),
S("CRA says it’s owed more than $10B in COVID benefit payments", "Global News", "https://globalnews.ca/news/11595446/cra-owed-covid-benefit-payments/", "2025-12-31"),
]),

dict(
id="baylis-ventilators",
subject=GOV, category="procurement",
title="Baylis Medical ventilator subcontract",
date_start="2020-04", date_end="2020-12-04",
actors=["FTI Professional Grade", "Baylis Medical", "Frank Baylis", "Public Services and Procurement Canada"],
summary=(
"In spring 2020 the government contracted FTI Professional Grade, a firm formed by the Ventilators for Canadians "
"consortium, to supply 10,000 ventilators for about $237 million, with Baylis Medical — co-owned by Frank Baylis, "
"Liberal MP for Pierrefonds–Dollard until 2019 — as manufacturing subcontractor. On November 27, 2020 the Ethics "
"Commissioner determined that Baylis, as a former MP, was no longer subject to the Members’ Code and that the "
"contract was not concluded with him. Baylis told the ethics committee on December 4, 2020 that he had not "
"approached the Prime Minister, ministers or party officials to obtain it."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner — jurisdictional determination; ETHI committee hearings", date="2020-11-27",
    result="UNADJUDICATED", label="No finding",
    quote="The Commissioner determined that Frank Baylis, as a former MP, was no longer subject to the Members’ Code and that the contract was not concluded with him. No body made a finding of wrongdoing."),
consequence_pm="None.",
consequence_others="None.",
public_cost="About $237 million for 10,000 ventilators (widely reported; not verified against a contract disclosure here).",
status="Closed. Canada later held a large surplus of unused pandemic ventilators.",
sources=[
S("Evidence – ETHI (43-2) – Meeting 14", "House of Commons of Canada", "https://www.ourcommons.ca/DocumentViewer/en/43-2/ETHI/meeting-14/evidence", "2020-12-04", True),
S("Canadian companies warn Conservative motion could deter domestic production of PPE", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-canadian-companies-warn-conservative-motion-could-deter-domestic/", "2020-10-20"),
]),

dict(
id="we-charity",
subject=PM, category="ethics",
title="WE Charity and the Canada Student Service Grant",
date_start="2020-04-22", date_end="2021-05-13",
actors=["Justin Trudeau", "Bill Morneau", "Margaret Trudeau", "Alexandre Trudeau", "Sophie Grégoire Trudeau", "Craig Kielburger", "Marc Kielburger", "Mario Dion (Ethics Commissioner)"],
summary=(
"On April 22, 2020 Trudeau announced the Canada Student Service Grant, budgeted at up to $912 million. Cabinet "
"approved WE Charity as administrator on May 22; Trudeau and Finance Minister Morneau did not recuse themselves. "
"WE withdrew on July 3, the day the Ethics Commissioner opened an examination, and on July 9 disclosed that it had "
"paid Margaret Trudeau about $250,000 in honoraria for 28 events since 2016 and Alexandre Trudeau about $32,000 for "
"eight. Trudeau apologized on July 13 for not recusing and testified to the Finance committee on July 30. Morneau "
"resigned August 17; Parliament was prorogued August 18, ending four committee studies. On May 13, 2021 the "
"Commissioner found Trudeau had not contravened the Act, and found Morneau had."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Mario Dion — Trudeau III Report", date="2021-05-13",
    result="CLEARED", label="Cleared — now under judicial review",
    quote="“There was no opportunity to further Mr. Trudeau’s own interests or those of his relatives from WE’s role as administrator of the CSSG.” […] “Without an actual conflict of interest or a clear legislative prohibition against apparent conflicts of interest, I could not conclude that a contravention occurred.”"),
secondary=["Morneau: contravened ss. 6(1), 7, 21", "Parliament prorogued Aug 18, 2020", "Clearance under judicial review since July 2026"],
consequence_pm="No contravention found. Trudeau apologized for not recusing himself. On October 21, 2020 the government made a Conservative motion for a special committee on the matter a confidence vote; it was defeated 180–146 with NDP support.",
consequence_others="Morneau: contravened three sections of the Act (see his entry); resigned as minister and MP August 17, 2020. WE Charity closed its Canadian operations on September 9, 2020. Democracy Watch’s challenge to the clearance was blocked by s. 66 of the Act until the Supreme Court struck that section down.",
public_cost="Program budgeted at up to $912 million; WE’s administration fee reported at $19.5 million initially and up to $43.5 million under the agreement. The program was not delivered.",
status="Open. On July 30, 2026 the Supreme Court of Canada held 9–0 (Wagner C.J.) that s. 66 of the Conflict of Interest Act “violates the constitutional guarantee that courts can review whether public authorities have acted lawfully,” and returned Democracy Watch’s challenge to the Federal Court of Appeal “to consider whether the Commissioner’s decision was lawful.” That review is pending.",
sources=[
S("Trudeau III Report", "Office of the Conflict of Interest and Ethics Commissioner", "https://ciec-ccie.parl.gc.ca/en/investigations-enquetes/Pages/trudeau3Report.aspx", "2021-05-13", True),
S("Democracy Watch v. Canada (Attorney General) — case in brief", "Supreme Court of Canada", "https://www.scc-csc.ca/judgments-jugements/cb/2026/41576/", "2026-07-30", True),
S("Questions of Conflict of Interest and Lobbying in Relation to Pandemic Spending — ETHI Report 2, p. 48", "House of Commons of Canada", "https://www.ourcommons.ca/DocumentViewer/en/43-2/ETHI/report-2/page-48", "2021-06-10", True),
S("Trudeau did not break federal ethics rules in WE Charity scandal — but Morneau did: report", "Global News", "https://globalnews.ca/news/7858498/justin-trudeau-we-charity-scandal-ethics-report/", "2021-05-13"),
S("PM’s mother Margaret and brother Alexandre were both paid to speak at WE Charity events", "CBC News", "https://www.cbc.ca/news/politics/margaret-justin-trudeau-we-charity-1.5643586", "2020-07-09"),
S("Judicial review of ethics ruling in Trudeau We Charity case to proceed", "Global News", "https://globalnews.ca/news/12002804/justin-trudeau-we-charity-supreme-court-of-canada/", "2026-07-30"),
S("Liberals survive confidence vote, avert imminent election with NDP help", "Global News", "https://globalnews.ca/news/7409890/trudeau-liberals-face-confidence-vote-fall-election/", "2020-10-21"),
]),

dict(
id="lucki-nova-scotia-call",
subject=GOV, category="governance",
title="RCMP Commissioner Lucki and the Nova Scotia shooting briefing",
date_start="2020-04-28", date_end="2023-03-30",
actors=["Brenda Lucki", "Bill Blair", "Justin Trudeau", "Darren Campbell", "Mass Casualty Commission"],
summary=(
"Notes by RCMP Supt. Darren Campbell, disclosed by the Mass Casualty Commission in June 2022, recorded that on an "
"April 28, 2020 call Commissioner Brenda Lucki said she had promised the Public Safety Minister’s office and the "
"Prime Minister’s Office that the RCMP would release details of the weapons used in the Nova Scotia mass shooting, "
"in connection with pending firearms legislation. Lucki and Minister Bill Blair denied political interference; "
"Trudeau said the government “had a lot of questions” but did not interfere. The Commission’s final report of "
"March 30, 2023 found no attempted political interference and criticized Lucki’s remarks."
),
finding=dict(body="Mass Casualty Commission — final report", date="2023-03-30",
    result="INQUIRY_FINDING", label="No interference found",
    quote="“Commissioner Lucki’s audio recorded remarks about the benefits to police of proposed firearms legislation were ill-timed and poorly expressed, but they were not partisan and they do not show that there had been attempted political interference.”"),
consequence_pm="None.",
consequence_others="No finding against Blair or the PMO. Lucki announced her retirement in February 2023 and left before the report’s release. The Commission recommended rules for communications between the RCMP and government on operational matters.",
public_cost=None,
status="Closed.",
sources=[
S("Contentious Lucki call not political interference, Nova Scotia mass shooting inquiry finds", "CTV News", "https://www.ctvnews.ca/politics/contentious-lucki-call-not-political-interference-nova-scotia-mass-shooting-inquiry-finds-1.6336132", "2023-03-30"),
S("Lucki’s gun call wasn’t political interference but new rules are needed: N.S. mass shooting report", "CBC News", "https://www.cbc.ca/news/politics/lucki-nova-scotia-gun-massacre-report-rcmp-1.6797250", "2023-03-30"),
S("Trudeau says Ottawa ‘had a lot of questions’ after N.S. mass shooting but didn’t interfere in investigation", "CBC News", "https://amp.cbc.ca/lite/story/1.6498884", "2022-06-22"),
]),

dict(
id="arrivecan",
subject=GOV, category="procurement",
title="ArriveCAN",
date_start="2020-04-29", date_end=None,
actors=["Canada Border Services Agency", "GC Strategies", "Kristian Firth", "Darren Anthony", "Karen Hogan (Auditor General)", "Office of the Procurement Ombud"],
summary=(
"The Canada Border Services Agency launched ArriveCAN in April 2020 to collect travellers’ health and customs "
"information. Auditor General Karen Hogan’s February 12, 2024 report estimated the app cost about $59.5 million "
"against an initial estimate of $80,000, and said the agency’s records were so poor the precise cost could not be "
"determined; GC Strategies, a two-person firm, received an estimated $19.1 million. The Procurement Ombud found that "
"in 76% of applicable contracts some or all of the resources the winning supplier proposed did no work. On April 17, "
"2024 Kristian Firth was admonished at the bar of the House of Commons and questioned by MPs. On June 6, 2025 the "
"government declared GC Strategies ineligible for federal contracts for seven years."
),
finding=dict(body="Auditor General of Canada — 2024 Report 1, ArriveCAN; Office of the Procurement Ombud — Procurement Practice Review", date="2024-02-12",
    result="AUDIT_ADVERSE", label="Adverse audit",
    quote="“Glaring disregard for basic management and contracting practices surrounds the government’s ArriveCAN application.” […] “The Canada Border Services Agency’s documentation, financial records, and controls were so poor that we were unable to determine the precise cost of the ArriveCAN application.” Procurement Ombud: “In 76% of the applicable contracts, some or all of the resources proposed by the successful supplier did not perform any work on the contract.”"),
consequence_pm="None. No minister was sanctioned.",
consequence_others="Firth: found in contempt of Parliament, admonished at the bar and questioned by MPs — the second person called to the bar since 1913 and the first questioned there. GC Strategies: contracts terminated, security status suspended, barred from federal contracts until June 2032; Dalian Enterprises and Coradix also barred. Two CBSA executives suspended without pay in January 2024. RCMP investigation: no charges reported as of September 2026.",
public_cost="About $59.5 million (Auditor General estimate; precise cost undeterminable) against an initial $80,000 estimate. GC Strategies received an estimated $19.1 million.",
status="No criminal charges located as of September 2026; the RCMP has not announced an outcome.",
sources=[
S("Report 1—ArriveCAN, 2024 Reports of the Auditor General of Canada", "Office of the Auditor General of Canada", "https://www.canada.ca/en/auditor-general/our-work/audit-reports/parl-oag-202402-01-e.html", "2024-02-12", True),
S("Glaring disregard for basic management and contracting practices surrounds the government’s ArriveCAN application (news release)", "Office of the Auditor General of Canada", "https://www.canada.ca/en/auditor-general/media-room/2024-reports-of-the-auditor-general-of-canada-to-the-parliament-of-canada-glaring-disregard-for-basic-management-and-contracting-practices-surrounds-the-governments-arrivecan-application.html", "2024-02-12", True),
S("Procurement Practice Review of ArriveCAN", "Office of the Procurement Ombud", "https://opo-boa.gc.ca/praapp-prorev/2024/epa-ppr-01-2024-eng.html", "2024-01-29", True),
S("GC Strategies Inc. determined to be ineligible under the Ineligibility and Suspension Policy", "Public Services and Procurement Canada", "https://www.canada.ca/en/public-services-procurement/news/2025/06/gc-strategies-inc-determined-to-be-ineligible-under-the-ineligibility-and-suspension-policy.html", "2025-06-06", True),
S("RCMP conduct search of GC Strategies’ office as partner appears before House of Commons", "CBC News", "https://www.cbc.ca/lite/story/1.7175408", "2024-04-17"),
]),

dict(
id="morneau-we-charity",
subject=MIN, category="ethics",
title="Bill Morneau: WE Charity (Morneau II Report)",
date_start="2020-06-25", date_end="2021-05-13",
actors=["Bill Morneau", "Mario Dion (Ethics Commissioner)", "WE Charity", "Craig Kielburger"],
summary=(
"As Finance Minister, Morneau took part in the 2020 decision to have WE Charity administer the Canada Student "
"Service Grant while his ministerial office assisted WE in seeking federal funding. On July 22, 2020 he repaid "
"$41,366 to WE for family travel to Kenya and Ecuador in 2017, saying he had believed the costs were already paid; "
"his family had also donated $100,000 to WE and one daughter worked there. He resigned as Finance Minister and MP on "
"August 17, 2020. On May 13, 2021 Commissioner Dion found Morneau contravened subsection 6(1), section 7 and section "
"21 of the Conflict of Interest Act."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Mario Dion — Morneau II Report", date="2021-05-13",
    result="VIOLATION_FOUND", label="Contravened ss. 6(1), 7, 21",
    quote="“Mr. Morneau gave WE preferential treatment by permitting his ministerial staff to disproportionately assist it when it sought federal funding.” Dion found Morneau and Craig Kielburger were friends within the meaning of the Act and that Morneau should have recused himself."),
secondary=["Resigned Aug 17, 2020"],
consequence_pm="None.",
consequence_others="Morneau had already resigned as minister and MP. No statutory penalty applies to the sections contravened.",
public_cost=None,
status="Closed.",
sources=[
S("Questions of Conflict of Interest and Lobbying in Relation to Pandemic Spending — ETHI Report 2, p. 51", "House of Commons of Canada", "https://www.ourcommons.ca/documentviewer/en/43-2/ETHI/report-2/page-51", "2021-06-10", True),
S("Morneau II Report", "Office of the Conflict of Interest and Ethics Commissioner", "https://ciec-ccie.parl.gc.ca/en/investigations-enquetes/Pages/Morneau2Report.aspx", "2021-05-13", True),
S("Trudeau in apparent conflict on WE but not a formal ethics breach, commissioner finds; Morneau’s actions declared a clear violation", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-trudeau-cleared-in-we-charity-controversy-but-ethics-commissioner/", "2021-05-13"),
]),

dict(
id="nuctech-standing-offer",
subject=GOV, category="procurement",
title="Nuctech security-equipment standing offer",
date_start="2020-07", date_end="2020-11-17",
actors=["Public Services and Procurement Canada", "Global Affairs Canada", "Nuctech", "Deloitte"],
summary=(
"In July 2020 Public Services and Procurement Canada awarded standing offers worth a projected $6.8 million to "
"Nuctech, a Chinese state-linked firm, for X-ray machines and metal detectors at Canadian embassies. After the award "
"was reported, Global Affairs commissioned a Deloitte review, completed in September 2020 at a cost slightly above "
"$250,000; it found no non-compliance but concluded security experts had not been integrated into the procurement. "
"Global Affairs said in November 2020 it would not use the standing offer, and no equipment was bought from Nuctech "
"under it. A Commons committee recommended barring Chinese state-owned enterprises from federal security contracts."
),
finding=dict(body="Global Affairs Canada / PSPC decision following the Deloitte review; Commons government operations committee report", date="2020-11-17",
    result="ADMISSION", label="Reversed",
    quote="PSPC: “No equipment has been purchased from Nuctech Company Limited under the standing offer.” Deloitte found that security experts were not integrated throughout the procurement process."),
consequence_pm="None.",
consequence_others="None. The department designed a new procurement route with a national-security exemption.",
public_cost="Slightly over $250,000 for the Deloitte review.",
status="Closed; the standing offers expired unused.",
sources=[
S("Question Period Note: Security screening equipment for Global Affairs Canada", "Public Services and Procurement Canada, via Open Government", "https://search.open.canada.ca/qpnotes/record/pwgsc-tpsgc%2CPSPC-2020-QP-00038", "2020-11-17", True),
S("Committee Report No. 4 – OGGO (43-2)", "House of Commons of Canada", "https://www.ourcommons.ca/DocumentViewer/en/43-2/OGGO/report-4/page-81", "2021-02-01", True),
S("Canada rejects deal with China’s Nuctech for embassy security equipment", "Global News", "https://globalnews.ca/news/7470250/china-canada-nuctech-deal-rejected", "2020-11-18"),
]),

# ───────────────────────────── 2021 ─────────────────────────────
dict(
id="access-to-information-decline",
subject=GOV, category="governance",
title="Access to information: “no longer serves its intended purpose”",
date_start="2021-01-31", date_end="2023-06-13",
actors=["Caroline Maynard (Information Commissioner)", "Treasury Board of Canada Secretariat", "Mona Fortier"],
summary=(
"Information Commissioner Caroline Maynard told the government’s review of the Access to Information Act in January "
"2021 that the regime “had already entered a critical phase before the pandemic and could soon be beyond repair.” "
"The review concluded in December 2022 without proposing legislative change. Her 2022–23 annual report, released "
"June 13, 2023, stated that over her tenure she had “observed the steady decline of the access-to-information system "
"to the point where it no longer serves its intended purpose,” and she said transparency was “not a priority for the "
"government.” A Commons committee recommended bringing ministers’ offices under the Act; Liberal members dissented."
),
finding=dict(body="Information Commissioner of Canada — review submission and annual reports", date="2023-06-13",
    result="INQUIRY_FINDING", label="Officer of Parliament: system in decline",
    quote="“Over the course of my time as commissioner, I have observed the steady decline of the access-to-information system to the point where it no longer serves its intended purpose.”"),
consequence_pm="None.",
consequence_others="No amendments followed the 2022 review; the Treasury Board President said the government would prioritize administering the existing law.",
public_cost=None,
status="The Act has not been amended since 2019.",
sources=[
S("Observations and Recommendations from the Information Commissioner on the Government of Canada’s Review of the Access to Information Regime", "Office of the Information Commissioner of Canada", "https://www.oic-ci.gc.ca/en/resources/reports-publications/observations-and-recommendations-information-commissioner-review", "2021-01-31", True),
S("2021–2022 Annual Report", "Office of the Information Commissioner of Canada", "https://www.oic-ci.gc.ca/en/resources/reports-publications/2021-2022-annual-report", "2022-06-14", True),
S("Transparency ‘not a priority’ for Trudeau government, information commissioner says", "Global News", "https://globalnews.ca/news/9766102/transparency-trudeau-government-access-to-information", "2023-06-13"),
]),

dict(
id="michael-chong-zhao-wei",
subject=GOV, category="foreign-interference",
title="Michael Chong: targeted by a PRC diplomat, not told for two years",
date_start="2021-02-22", date_end="2025-01-28",
actors=["Michael Chong", "Zhao Wei", "Bill Blair", "Justin Trudeau", "CSIS", "Marie-Josée Hogue"],
summary=(
"After Chong’s Uyghur-genocide motion passed the House in February 2021, CSIS assessed that Toronto consulate "
"official Zhao Wei was gathering information on Chong and his relatives in Hong Kong. CSIS sent an issues-management "
"note to Public Safety Minister Bill Blair in May 2021; it never reached him. Chong received a defensive briefing in "
"June 2021 that did not mention the diplomat. The Globe and Mail reported the assessment on May 1, 2023; the Hogue "
"Commission later recorded that the Prime Minister, senior PMO staff and Blair first learned of it from that article. "
"Zhao Wei was declared persona non grata on May 8, 2023."
),
finding=dict(body="Public Inquiry into Foreign Interference (Hogue) — Final Report, Vol. 4, ch. 14", date="2025-01-28",
    result="INQUIRY_FINDING", label="Information-flow failure",
    quote="“The evidence shows that the information about the PRC’s interest in several MPs after the Uyghur Motion did not flow as it should have in the spring of 2021.” […] “The May 2021 IMU was sent specifically to make the Minister of Public Safety aware of CSIS’s intelligence and its action plan, and the information never reached the Minister.” […] “I query how the threshold for a TRM could have been met in 2023 when it was not in 2021.”"),
consequence_pm="None. Hogue found the failure was in information flow, with no finding of intent.",
consequence_others="Zhao Wei expelled; China expelled a Canadian diplomat in return. No minister, adviser or official was disciplined; Blair stayed in cabinet until March 2025.",
public_cost=None,
status="Adjudicated by the Hogue Commission; outcome of an RCMP investigation opened in May 2023 not located.",
sources=[
S("Final Report, Volume 4 — Intelligence Flow within Government (PDF)", "Foreign Interference Commission", "https://foreigninterferencecommission.ca/fileadmin/PIFI_-_Final_Report_Vol._4__2025_.pdf", "2025-01-28", True),
S("First Report — Independent Special Rapporteur on Foreign Interference", "Government of Canada", "https://www.canada.ca/en/democratic-institutions/services/reports/first-report-david-johnston-independent-special-rapporteur-foreign-interference.html", "2023-05-23", True),
S("Canada declares Chinese diplomat Zhao Wei ‘persona non grata’ over foreign interference", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-ottawa-expels-chinese-diplomat-over-foreign-interference/", "2023-05-08"),
]),

dict(
id="blair-csis-warrant-delay",
subject=GOV, category="foreign-interference",
title="The 54-day CSIS warrant delay in Bill Blair’s office",
date_start="2021-03-01", date_end="2025-01-28",
actors=["Bill Blair", "Zita Astravas", "Rob Stewart", "David Vigneault", "Marie-Josée Hogue"],
summary=(
"In 2021 CSIS sent Public Safety a Federal Court warrant application with a recommendation for approval within six "
"days. The deputy minister signed off on day 4 and asked the minister’s office for same-day approval; chief of staff "
"Zita Astravas was briefed on day 13; the CSIS director discussed the file with her on day 48; Blair approved it on "
"day 54. Blair testified he did not learn the warrant was waiting until two or three days before his briefing. The "
"Commission withheld the target’s identity; the Globe and Mail reported it was Liberal organizer Michael Chan."
),
finding=dict(body="Public Inquiry into Foreign Interference (Hogue) — Final Report, Vol. 4, ch. 14", date="2025-01-28",
    result="INQUIRY_FINDING", label="Delay “unacceptable”; no wrongdoing found",
    quote="“Nothing in the evidence really explains the highly unusual delay… It seems to me that everyone involved dropped the ball. […] Although the delay itself was unacceptable, the evidence does not show any wrongdoing beyond lack of diligence.”"),
consequence_pm="None.",
consequence_others="No sanction. Blair remained in cabinet as Defence Minister until March 2025; Astravas had left government. The Commission recommended a tracking process for warrant applications.",
public_cost=None,
status="Adjudicated; no further proceeding found.",
sources=[
S("Final Report, Volume 4 — The CSIS warrant (PDF)", "Foreign Interference Commission", "https://foreigninterferencecommission.ca/fileadmin/PIFI_-_Final_Report_Vol._4__2025_.pdf", "2025-01-28", True),
S("Blair says he never knew CSIS warrant sat in his office for 54 days", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-blair-says-he-never-knew-csis-warrant-sat-in-his-office-for-54-days/", "2024-10-11"),
]),

dict(
id="afghanistan-evacuation-2021",
subject=GOV, category="governance",
title="Kabul evacuation and the election call",
date_start="2021-08-15", date_end="2022-06-08",
actors=["Justin Trudeau", "Harjit Sajjan", "Marco Mendicino", "Marc Garneau", "Special Committee on Afghanistan"],
summary=(
"Trudeau asked the Governor General to dissolve Parliament on August 15, 2021, the day the Taliban entered Kabul. "
"Canadian evacuation flights had begun August 4; Canadian personnel left Kabul on the morning of August 26, having "
"airlifted about 3,700 people on 17 flights. Global Affairs did not provide firm numbers of Canadians left behind. "
"The Commons Special Committee on Afghanistan reported in June 2022 on contingency-planning failures, the evacuation "
"and the Criminal Code barrier to humanitarian aid, with Conservative and NDP supplementary opinions attached."
),
finding=dict(body="House of Commons Special Committee on Afghanistan — Report 1", date="2022-06-08",
    result="INQUIRY_FINDING", label="Committee report",
    quote="Gen. Wayne Eyre, August 26, 2021, on ending the airlift: “the feeling of helplessness and guilt from having to leave people behind.”"),
consequence_pm="None.",
consequence_others="No minister resigned; Sajjan and Mendicino were moved to other portfolios in October 2021. Bill C-41 (2023) later exempted humanitarian aid from the terrorism-financing provisions.",
public_cost=None,
status="Closed as to the evacuation; resettlement continued into 2024.",
sources=[
S("Honouring Canada’s Legacy in Afghanistan — Report 1 of the Special Committee on Afghanistan", "House of Commons of Canada", "https://www.ourcommons.ca/documentviewer/en/44-1/AFGH/report-1/page-ToC", "2022-06-08", True),
S("Question Period Note: Afghanistan (DND-2022-QP-00027)", "Department of National Defence, via Open Government", "https://search.open.canada.ca/qpnotes/record/dnd-mdn%2CDND-2022-QP-00027", "2022-06-09", True),
S("Evacuation over: Kabul, Afghanistan, Canada, Taliban", "Global News", "https://globalnews.ca/news/8142337/evacuation-over-kabul-afghanistan-canada-taliban/", "2021-08-26"),
]),

dict(
id="snap-election-2021",
subject=PM, category="spending",
title="The 2021 snap election",
date_start="2021-08-15", date_end="2021-09-20",
actors=["Justin Trudeau", "Elections Canada"],
summary=(
"Two years into a minority Parliament, Trudeau called an election for September 20, 2021, held during the pandemic. "
"Elections Canada had estimated the cost at about $610 million, the most expensive in Canadian history; its "
"accounting as of January 2025 put the cost at $574.2 million, plus $150.3 million in readiness activities, "
"$81.8 million more than 2019. The Liberals won 160 seats, a minority, against 157 in 2019."
),
finding=dict(body="Elections Canada — Estimated Cost of the 44th General Election", date="2025-02-25",
    result="RECORD", label="Spending record",
    quote="Total $574.2 million (2025 dollars), about $20.87 per registered elector, $81.8 million more than the 43rd general election."),
consequence_pm="None. Parliament returned with a minority of similar size.",
consequence_others="None.",
public_cost="$574.2 million (Elections Canada, January 2025) plus $150.3 million in readiness activities.",
status="Closed.",
sources=[
S("Estimated Cost of the 44th General Election", "Elections Canada", "https://www.elections.ca/content.aspx?section=res&dir=rep%2Foff%2Fcou&document=index44&lang=e", "2025-02-25", True),
S("Many Canadians angry after election produces a $610M bill and not much change", "CBC News", "https://www.cbc.ca/news/canada/angry-canadian-voters-expensive-federal-election-1.6184285", "2021-09-22"),
]),

dict(
id="sajjan-afghan-sikhs",
subject=MIN, category="conduct",
title="Harjit Sajjan and the Afghan Sikh rescue tasking",
date_start="2021-08-26", date_end="2024-07-04",
actors=["Harjit Sajjan", "Canadian Special Operations Forces Command", "World Sikh Organization"],
summary=(
"In July 2024 the Globe and Mail reported, citing three military sources, that during the August 2021 evacuation "
"Defence Minister Harjit Sajjan instructed special forces to rescue about 225 Afghan Sikhs, relayed the group’s "
"location to the military and texted commanders during the attempt; the sources said the group had no link to Canada, "
"that the tasking diverted resources from Canadians and priority Afghans, and that none of the group was evacuated "
"by Canada. Sajjan said he never ordered the operation, that his instructions were not an order, and that the "
"department had already cleared the group for evacuation. His father had served on the board of the World Sikh "
"Organization, which had pressed for the rescue."
),
finding=dict(body="None — media investigation; no adjudicative finding", date=None,
    result="UNADJUDICATED", label="No adjudication",
    quote="Globe and Mail: Sajjan “instructed Canadian special forces to rescue about 225 Afghan Sikhs.” Sajjan: he “never ordered the military to conduct the operation.”"),
consequence_pm="None.",
consequence_others="None. Sajjan remained in cabinet until March 2025.",
public_cost=None,
status="No parliamentary report or independent finding located as of September 2026.",
sources=[
S("Sajjan instructed special forces to rescue Afghan Sikhs during fall of Kabul", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-sajjan-instructed-special-forces-to-rescue-afghan-sikhs-during-fall-of/", "2024-07-02"),
S("Sajjan says he relayed information on rescuing Sikhs in Afghanistan during chaotic fall of Kabul", "CBC News", "https://www.cbc.ca/news/politics/sajjan-relayed-information-sikhs-in-afghanistan-1.7248417", "2024-07-03"),
]),

dict(
id="tofino-truth-reconciliation-day",
subject=PM, category="conduct",
title="Tofino on the first National Day for Truth and Reconciliation",
date_start="2021-09-30", date_end="2021-10-18",
actors=["Justin Trudeau", "Tk’emlúps te Secwépemc", "Kukpi7 Rosanne Casimir"],
summary=(
"On September 30, 2021 the Prime Minister’s itinerary listed “private meetings” in Ottawa; he had flown to Tofino "
"with his family. The itinerary was amended after Global News asked. Tk’emlúps te Secwépemc, which had announced "
"about 215 suspected unmarked graves at the former Kamloops residential school in May, had twice invited him to its "
"ceremony that day. He telephoned Kukpi7 Rosanne Casimir the following weekend to apologize, said publicly on "
"October 6 that “travelling on September 30th was a mistake, and I regret it,” and visited Kamloops on October 18."
),
finding=dict(body="None (public apology)", date="2021-10-06",
    result="ADMISSION", label="Admitted; apologized",
    quote="“Travelling on September 30th was a mistake, and I regret it.”"),
consequence_pm="Apology by telephone and in public; visit to Tk’emlúps te Secwépemc on October 18, 2021. No penalty.",
consequence_others="None.",
public_cost=None,
status="Closed.",
sources=[
S("Trudeau says Tofino trip on Truth and Reconciliation Day was ‘a mistake’", "Global News", "https://globalnews.ca/news/8247262/trudeau-tofino-truth-reconciliation-apology-mistake", "2021-10-06"),
S("Trudeau flew to Tofino, B.C., with family on 1st National Day for Truth and Reconciliation", "CBC News", "https://www.cbc.ca/lite/story/1.6195591", "2021-10-01"),
]),

# ───────────────────────────── 2022 ─────────────────────────────
dict(
id="emergencies-act-2022",
subject=PM, category="governance",
title="Invocation of the Emergencies Act",
date_start="2022-02-14", date_end=None,
actors=["Justin Trudeau", "Chrystia Freeland", "Marco Mendicino", "David Lametti", "Paul Rouleau", "Richard Mosley", "Yves de Montigny"],
summary=(
"Cabinet declared a public order emergency on February 14, 2022 in response to the Freedom Convoy protests and "
"blockades and revoked it on February 23. Under the Emergency Economic Measures Order, banks froze more than 200 "
"accounts holding about $7.8 million; the Federal Court later recorded about 257. The Rouleau Commission concluded "
"on February 17, 2023 that the very high threshold for invocation had been met, a conclusion it reached with "
"reluctance. On January 23, 2024 Justice Richard Mosley of the Federal Court held the invocation unreasonable and "
"ultra vires and found the regulations and economic order infringed Charter sections 2(b) and 8. The government "
"appealed. On January 16, 2026 the Federal Court of Appeal unanimously dismissed the appeal. On March 17, 2026 the "
"Carney government sought leave to appeal to the Supreme Court of Canada."
),
finding=dict(body="Federal Court of Appeal, 2026 FCA 6 (de Montigny C.J.), affirming Federal Court, 2024 FC 42 (Mosley J.)", date="2026-01-16",
    result="COURT_AGAINST_GOVERNMENT", label="Ruled unlawful — affirmed on appeal",
    quote="Federal Court (2024 FC 42, para. 255): “There was no national emergency justifying the invocation of the Emergencies Act and the decision to do so was therefore unreasonable and ultra vires.” Federal Court of Appeal (2026 FCA 6): the government “did not demonstrate that it had reasonable grounds to believe that a threat to national security or a national emergency existed”; the freezing of accounts was “ad hoc and fraught with confusion” and “not reasonable within the meaning of section 8 of the Charter.” Rouleau Commission (February 17, 2023): the threshold for invocation was met, a conclusion reached “with reluctance,” and “reasonable people could come to a different conclusion.”"),
secondary=["Rouleau Commission: threshold met (Feb 2023)", "Leave to appeal sought at the Supreme Court (Mar 2026)"],
consequence_pm="None. No minister resigned and no sanction followed either ruling. Freeland, January 23, 2024: “We believed we were doing something necessary and something legal at the time. That continues to be my belief today.”",
consequence_others="None. The successor government continued the litigation.",
public_cost="More than 200 accounts holding about $7.8 million frozen (Finance Canada testimony, February 22, 2022); the Federal Court recorded about 257 accounts.",
status="Two courts have held the invocation unlawful. Leave to appeal was sought at the Supreme Court of Canada on March 17, 2026; no decision on leave found as of September 2026.",
sources=[
S("2026 FCA 6 — plain-language decision summary, Attorney General of Canada v. Canadian Civil Liberties Association", "Federal Court of Appeal", "https://www.fca-caf.ca/en/pages/decisions/plain-language-decision-summaries/2026-fca-6", "2026-01-16", True),
S("Canadian Frontline Nurses et al. v. Canada (Attorney General), 2024 FC 42 (PDF)", "Federal Court", "https://www.fct-cf.ca/Content/assets/pdf/base/2024.01.23-306-22-T-316-22-T-347-22-T-382-22.pdf", "2024-01-23", True),
S("Report of the Public Inquiry into the 2022 Public Order Emergency", "Public Order Emergency Commission", "https://publicorderemergencycommission.ca/final-report/", "2023-02-17", True),
S("Parliamentary Committee Notes: Federal Court Ruling on the Invocation of the Emergencies Act and Appeal", "Public Safety Canada", "https://www.publicsafety.gc.ca/cnt/trnsprnc/brfng-mtrls/prlmntry-bndrs/20240626/09-en.aspx", "2024-06-26", True),
S("Use of Emergencies Act to stop ‘Freedom Convoy’ unreasonable: appeal court", "Global News", "https://globalnews.ca/news/11616533/freedom-convoy-emergencies-act-appeal-court/", "2026-01-16"),
S("Federal government appeals Emergencies Act use during convoy protest to Supreme Court", "CBC News", "https://www.cbc.ca/news/politics/government-appealing-emergencies-act-use-supreme-court-9.7132438", "2026-03-17"),
S("Ottawa’s use of Emergencies Act against convoy protests was unreasonable, violated Charter, court rules", "CBC News", "https://www.cbc.ca/lite/story/1.7091891", "2024-01-23"),
S("The Emergencies Act’s ‘very high threshold’ was met, commissioner rules in major report", "Global News", "https://globalnews.ca/news/9493106/emergencies-act-inquiry-report-ramifications/", "2023-02-17"),
]),

dict(
id="mendicino-police-request-claim",
subject=MIN, category="conduct",
title="Marco Mendicino’s claim that police asked for the Emergencies Act",
date_start="2022-04-26", date_end="2022-06-07",
actors=["Marco Mendicino", "Rob Stewart", "Brenda Lucki", "Steve Bell"],
summary=(
"After the Emergencies Act was invoked, Public Safety Minister Marco Mendicino told a parliamentary committee in "
"April 2022 that “the advice we received was to invoke the Emergencies Act” and repeatedly said the government acted "
"on the advice of law enforcement. RCMP Commissioner Brenda Lucki and Ottawa interim police chief Steve Bell then "
"testified that they had not requested the Act. On June 7, 2022 Deputy Minister Rob Stewart told MPs the minister "
"had been “misunderstood” and meant that police had asked for the tools the Act contained."
),
finding=dict(body="Deputy Minister of Public Safety — committee testimony; Public Order Emergency Commission evidence", date="2022-06-07",
    result="ADMISSION", label="Statement walked back",
    quote="Stewart: “I believe that the intention that he was trying to express was that law enforcement asked for the tools that were contained in the Emergencies Act.” Lucki’s February 13, 2022 email to the minister’s office stated that police had not yet exhausted all available tools."),
consequence_pm="None.",
consequence_others="None at the time; Mendicino was dropped from cabinet in July 2023 (see the Bernardo entry).",
public_cost=None,
status="Closed.",
sources=[
S("Mendicino was ‘misunderstood’ in saying police asked for Emergencies Act: deputy minister", "CTV News", "https://www.ctvnews.ca/politics/mendicino-was-misunderstood-in-saying-police-asked-for-emergencies-act-deputy-minister-1.5937524", "2022-06-07"),
S("Marco Mendicino tries to clarify whether police asked for Emergencies Act", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-marco-mendicino-tries-to-clarify-whether-police-asked-for-emergencies/", "2022-06-08"),
]),

dict(
id="boissonnault-global-health-imports",
subject=MIN, category="ethics",
title="Randy Boissonnault: Global Health Imports and the identity claims",
date_start="2022-09-06", date_end="2025-03-22",
actors=["Randy Boissonnault", "Stephen Anderson", "Global Health Imports", "Konrad von Finckenstein (Ethics Commissioner)", "Justin Trudeau"],
summary=(
"Boissonnault co-founded Global Health Imports with Stephen Anderson in 2020 and remained a half-owner after "
"joining cabinet in October 2021, surrendering his shares in June 2024. In June 2024 Global News reported text "
"messages Anderson sent on September 6–8, 2022, during a deal negotiation, referring to “Randy”; Boissonnault "
"denied any involvement, and Anderson told the ethics committee that autocorrect produced the name and later "
"admitted lying to journalists about another Randy at the firm. The Ethics Commissioner closed his review by letter "
"on September 12, 2024. Boissonnault had described himself as “non-status adopted Cree” and was listed as Indigenous "
"in party communications; in November 2024 he said his adoptive mother and brother are Métis and apologized. He "
"left cabinet on November 20, 2024."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Konrad von Finckenstein — letter closing the review", date="2024-09-12",
    result="CLEARED", label="Cleared by letter; left cabinet",
    quote="“In the absence of any evidence giving me a reason to believe you may have been operating or managing GHI in contravention of [the Conflict of Interest Act], I consider this matter closed.”"),
secondary=["Left cabinet Nov 20, 2024"],
consequence_pm="None. The PMO said Boissonnault was stepping away “to focus on clearing the allegations made against him.”",
consequence_others="Boissonnault left cabinet and did not run in the 2025 election. Global Health Imports was declared ineligible for federal contracts until 2030 after describing itself as “wholly Indigenous-owned” in bids; Edmonton police opened an investigation into the company and Anderson.",
public_cost=None,
status="No contravention found. Outcomes of the civil suits against the company and the police investigation not located as of September 2026.",
sources=[
S("Ethics commissioner closes most recent probe into Randy Boissonnault’s business dealings", "CBC News", "https://www.cbc.ca/news/politics/randy-boissonnault-konrad-von-finckenstein-1.7327519", "2024-09-18"),
S("Randy Boissonnault leaves Liberal cabinet after shifting Indigenous identity claims", "The Canadian Press via CP24", "https://www.cp24.com/news/canada/2024/11/20/randy-boissonnault-leaves-liberal-cabinet-after-shifting-indigenous-identity-claims/", "2024-11-20"),
S("Randy Boissonnault’s former company ineligible for government contracts for 5 years", "The Globe and Mail", "https://www.theglobeandmail.com/canada/article-randy-boissonnaults-former-company-ineligible-for-government-contracts/", "2025-02-21"),
S("Texts from ‘Randy’ raise questions about minister’s role at company while in office", "Global News", "https://globalnews.ca/news/10541126/randy-boissonault-ppe-text-messages/", "2024-06-05"),
]),

dict(
id="london-hotel-queen-funeral",
subject=PM, category="spending",
title="Corinthia Hotel suite at the Queen’s funeral",
date_start="2022-09-15", date_end="2023-04-13",
actors=["Justin Trudeau", "Global Affairs Canada", "Prime Minister’s Office"],
summary=(
"Access-to-information records reported in February 2023 showed the Canadian delegation to Queen Elizabeth II’s "
"funeral spent $397,843 on London hotels, including one Corinthia suite at £4,800 ($6,089) a night for five nights. "
"The records did not identify the suite’s occupant; the Governor General’s office said it was not her, and neither "
"the PMO nor Global Affairs answered before publication. In April 2023 the PMO confirmed Trudeau and his wife had "
"stayed in the suite and said hotel prices had surged as about 500 delegations arrived."
),
finding=dict(body="None — disclosure through an Access to Information release", date=None,
    result="RECORD", label="Spending record",
    quote="Hotel accommodation for the delegation: $397,842.81, including a suite at $6,089.16 per night for five nights."),
consequence_pm="None. The occupant was confirmed only after further reporting.",
consequence_others="None.",
public_cost="$397,843 in hotel accommodation, of which about $30,446 for the suite.",
status="Closed.",
sources=[
S("Government spent nearly $400K on hotels for Queen’s funeral, including $6K/night suite", "CTV News", "https://www.ctvnews.ca/politics/government-spent-nearly-400k-on-hotels-for-queen-s-funeral-including-6k-night-suite-1.6286113", "2023-02-23"),
S("Trudeau stayed in $6,000 London hotel suite for Queen Elizabeth’s funeral", "CBC News", "https://amp.cbc.ca/lite/story/1.6789338", "2023-04-13"),
]),

dict(
id="foreign-interference-response",
subject=GOV, category="foreign-interference",
title="Foreign interference: the government’s response, 2022–2025",
date_start="2022-11-07", date_end="2025-01-28",
actors=["Justin Trudeau", "Dominic LeBlanc", "Marco Mendicino", "Bill Blair", "CSIS", "Marie-Josée Hogue", "NSICOP"],
summary=(
"On November 7, 2022 Global News reported that CSIS had briefed the Prime Minister and officials in early 2022 on a "
"PRC-directed network involving at least eleven 2019 candidates; Trudeau said he had not been briefed on any "
"candidate receiving money from China. On February 17, 2023 the Globe and Mail reported CSIS documents describing a "
"PRC strategy to favour a Liberal minority in 2021. Trudeau appointed a special rapporteur in March 2023 (see the "
"Johnston entry) and agreed to a public inquiry only in September 2023. The Hogue Commission reported in May 2024 "
"and January 2025: interference did not change which party formed government, may have affected a small number of "
"ridings, and eroded public confidence; the government was slow, poorly coordinated and “insufficiently transparent.”"
),
finding=dict(body="Public Inquiry into Foreign Interference (Hogue) — Initial Report (May 3, 2024) and Final Report (January 28, 2025); NSICOP Special Report (June 3, 2024)", date="2025-01-28",
    result="INQUIRY_FINDING", label="Government slow, “insufficiently transparent”",
    quote="Hogue: “The government has sometimes taken too long to act, and that coordination between the various players involved has not always been optimal.” […] “The government has proven to be a poor communicator and insufficiently transparent when it comes to foreign interference.” […] “Did foreign interference impact which party came into power in 2019 or 2021? No, it did not.” […] “Nor have I seen any evidence of ‘traitors’ in Parliament plotting with foreign states to act against Canada.” NSICOP: “The Committee expected the government to act. It was slow to do so.”"),
consequence_pm="None. Hogue made no finding of personal wrongdoing against Trudeau.",
consequence_others="No minister resigned. The government enacted the Countering Foreign Interference Act (2024) and received 51 recommendations from the Commission.",
public_cost=None,
status="Commission closed January 28, 2025; implementation of its recommendations rests with the successor government.",
sources=[
S("Final Report, Volume 1 — Overview and Recommendations (PDF)", "Foreign Interference Commission", "https://foreigninterferencecommission.ca/fileadmin/report_volume_1.pdf", "2025-01-28", True),
S("Initial Report, May 2024 (PDF)", "Foreign Interference Commission", "https://foreigninterferencecommission.ca/fileadmin/user_upload/Foreign_Interference_Commission_-_Initial_Report__May_2024__-_Digital.pdf", "2024-05-03", True),
S("Special Report on Foreign Interference in Canada’s Democratic Processes and Institutions (public version, PDF)", "National Security and Intelligence Committee of Parliamentarians", "https://www.nsicop-cpsnr.ca/reports/rp-2024-06-03/special-report-foreign-interference.pdf", "2024-06-03", True),
S("Release of latest Assessment of the Critical Election Incident Public Protocol", "Government of Canada", "https://www.canada.ca/en/democratic-institutions/news/2023/02/release-of-latest-assessment-of-the-critical-election-incident-public-protocol.html", "2023-02-28", True),
S("Trudeau says he has not been briefed on candidates receiving money from China", "Global News", "https://globalnews.ca/news/9293238/justin-trudeau-china-interference-allegations", "2022-11-20"),
S("No evidence of ‘traitors’: Takeaways from the foreign interference inquiry’s final report", "The Canadian Press via CP24", "https://www.cp24.com/politics/2025/01/28/no-evidence-of-traitors-takeaways-from-the-foreign-interference-inquirys-final-report/", "2025-01-28"),
]),

# ───────────────────────────── 2016 (Foundation, dated by pledge) ─────────────────────────────
dict(
id="trudeau-foundation-donation",
subject=PM, category="foreign-interference",
title="The Trudeau Foundation’s Beijing-linked donation",
date_start="2016-06", date_end="2023-04-24",
actors=["Pierre Elliott Trudeau Foundation", "Zhang Bin", "Niu Gensheng", "Pascale Fournier", "Justin Trudeau"],
summary=(
"In 2016 Zhang Bin and Niu Gensheng pledged $200,000 to the Pierre Elliott Trudeau Foundation as part of a "
"$1-million gift that also funded a statue of Pierre Trudeau; the Foundation received $140,000. In February 2023 "
"the Globe and Mail reported that CSIS had intercepted a 2014 conversation in which a Chinese diplomat instructed "
"Zhang to make the donation, with Beijing to reimburse him. The Foundation said it would return the money; on "
"April 11, 2023 its president and entire board resigned, citing “the politicization of the foundation.” The Auditor "
"General declined the Foundation’s request to investigate, saying the source and motives of private donations were "
"outside her authority. Trudeau said he had disassociated himself from the Foundation on becoming Prime Minister."
),
finding=dict(body="None — the Auditor General declined jurisdiction", date="2023-04-24",
    result="UNADJUDICATED", label="No adjudication",
    quote="Office of the Auditor General: “It would be outside the Auditor-General’s authority to examine the source of private donations, the identity of other donors or their motivations.”"),
consequence_pm="None. Trudeau held no role in the Foundation’s governance during his premiership; no finding was made against him.",
consequence_others="The Foundation’s CEO and board resigned; the $140,000 was to be returned.",
public_cost=None,
status="No adjudication.",
sources=[
S("Trudeau Foundation CEO, board resign after revelation of gift tied to China", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-trudeau-foundation-ceo-board-resigns/", "2023-04-11"),
S("Auditor-General’s office says it can’t probe Trudeau Foundation donation from Chinese benefactors", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-trudeau-foundation-donation-auditor-general/", "2023-04-24"),
S("Trudeau Foundation board pushed back on audit of alleged China-linked donation: ex-CEO", "Global News", "https://globalnews.ca/news/9658738/trudeau-foundation-china-donation-audit/", "2023-05-04"),
]),

# ───────────────────────────── 2023 ─────────────────────────────
dict(
id="mckinsey-outsourcing",
subject=GOV, category="procurement",
title="McKinsey contracts and outsourcing",
date_start="2023-01-04", date_end="2024-06-04",
actors=["McKinsey & Company", "Dominic Barton", "Public Services and Procurement Canada", "Karen Hogan (Auditor General)"],
summary=(
"Radio-Canada reported in January 2023 that McKinsey’s federal contracts had grown from $2.2 million over the nine "
"years before Trudeau took office to $66 million over his first seven; later tallies exceeded $100 million. "
"Dominic Barton, McKinsey’s global managing partner until 2018, chaired Trudeau’s Advisory Council on Economic Growth "
"and served as ambassador to China. The Auditor General’s June 4, 2024 report examined 97 McKinsey contracts worth "
"$209 million awarded between 2011 and 2023: 68 were non-competitive and 18 of 19 under the master standing offer "
"lacked the required justification. Federal spending on professional and special services reached a record $20.7 "
"billion in 2023–24."
),
finding=dict(body="Auditor General of Canada — 2024 Report 5, Professional Services Contracts", date="2024-06-04",
    result="AUDIT_ADVERSE", label="Adverse audit",
    quote="“Frequent disregard for procurement policies and guidance” across 97 contracts valued at $209 million; about 70% awarded non-competitively."),
consequence_pm="None. Trudeau asked ministers to review McKinsey contracts in January 2023.",
consequence_others="No individual sanctioned. The audited organizations accepted the recommendations.",
public_cost="$209 million in 97 McKinsey contracts, 2011–2023 (about $200 million spent); $20.7 billion in professional and special services spending in 2023–24.",
status="Closed as an audit matter.",
sources=[
S("Report 5—Professional Services Contracts, 2024 Reports of the Auditor General of Canada", "Office of the Auditor General of Canada", "https://www.canada.ca/en/auditor-general/our-work/audit-reports/parl-oag-202406-05-e.html", "2024-06-04", True),
S("The value of one consulting firm’s federal contracts has skyrocketed under the Trudeau government", "Radio-Canada", "https://ici.radio-canada.ca/rci/en/news/1946212/the-value-of-one-consulting-firms-federal-contracts-has-skyrocketed-under-the-trudeau-government", "2023-01-04"),
S("Feds spent a record $20.7-billion on outsourcing contracts last fiscal year", "The Hill Times", "https://www.hilltimes.com/story/2025/01/11/feds-spent-a-record-20-7-billion-on-outsourcing-contracts-last-fiscal-year/447046/", "2025-01-11"),
]),

dict(
id="hussen-constituency-contracts",
subject=MIN, category="spending",
title="Ahmed Hussen: constituency contracts to a staffer’s sister’s firm",
date_start="2023-01-20", date_end="2023-01-20",
actors=["Ahmed Hussen", "Munch More Media"],
summary=(
"On January 20, 2023 Global News reported that Ahmed Hussen’s constituency office had paid $93,050 since January "
"2021 to Munch More Media, a firm whose director is the sister of Hussen’s director of policy. Hussen’s office said "
"the arrangement had been disclosed to the Ethics Commissioner, that “the rules were followed,” and that the staffer "
"had no involvement in the firm’s work. No examination or finding followed."
),
finding=dict(body="None", date=None,
    result="UNADJUDICATED", label="No adjudication",
    quote="Hussen’s office: the arrangement was disclosed to the Ethics Commissioner and “the rules were followed in this case.”"),
consequence_pm="None.",
consequence_others="None. Hussen remained in cabinet.",
public_cost="$93,050 from the member’s constituency budget, January 2021 to January 2023.",
status="No adjudication.",
sources=[
S("Hussen’s office gave $93k in PR work to senior staffer’s sister’s foodie firm", "Global News", "https://globalnews.ca/news/9424015/hussens-office-93k-pr-work-foodie-firm/", "2023-01-20"),
]),

dict(
id="han-dong",
subject=GOV, category="foreign-interference",
title="Han Dong: the 2019 nomination and the Two Michaels allegation",
date_start="2023-02-24", date_end="2025-06-15",
actors=["Han Dong", "Justin Trudeau", "Jeremy Broadhurst", "Global News", "Marie-Josée Hogue"],
summary=(
"In February–March 2023 Global News reported that CSIS intelligence indicated PRC officials had arranged buses of "
"international students to support Dong’s 2019 Liberal nomination in Don Valley North, and that Dong had advised a "
"PRC consular official against releasing Michael Kovrig and Michael Spavor. Dong left caucus on March 22, 2023 and "
"sued. The Hogue Commission established that CSIS briefed cleared Liberal Party officials on September 28, 2019 and "
"that campaign director Jeremy Broadhurst briefed Trudeau two days later; Trudeau decided the information was not "
"sufficiently credible to remove Dong as candidate. Hogue found the classified record corroborated Dong’s denial on "
"the Two Michaels and declined to determine what happened at the nomination. Dong settled with Global News in June 2025."
),
finding=dict(body="Public Inquiry into Foreign Interference (Hogue) — Final Report, Vol. 2, ch. 7", date="2025-01-28",
    result="INQUIRY_FINDING", label="Michaels claim not supported; nomination undetermined",
    quote="“I can say the classified information available to me corroborates Mr. Dong’s denial of the allegation that he suggested the PRC should hold off releasing the Two Michaels.” […] “It is not the mandate of this Commission to determine what actually took place at the DVN nomination meeting in 2019… However, this incident makes clear that nomination contests may be gateways for foreign states who wish to interfere in our democratic processes.”"),
consequence_pm="None. Trudeau’s 2019 decision to keep Dong as candidate was recorded without an adverse finding.",
consequence_others="Dong lost his caucus seat, sat as an Independent and did not run in 2025; no body found wrongdoing by him.",
public_cost=None,
status="Closed. Lawsuit settled June 2025 on undisclosed terms.",
sources=[
S("Final Report, Volume 2 — The 2019 General Election (PDF)", "Foreign Interference Commission", "https://foreigninterferencecommission.ca/fileadmin/PIFI_-_Final_Report_Vol._2__2025_.pdf", "2025-01-28", True),
S("Global News and former MP Han Dong settle lawsuit", "Global News", "https://globalnews.ca/news/11242170/han-dong-global-news-settlement/", "2025-06-15"),
S("MP Han Dong sues Global News for defamation over foreign interference report", "Global News", "https://globalnews.ca/news/9640899/mp-han-dong-sues-global-news/", "2023-04-20"),
]),

dict(
id="mendicino-bernardo-transfer",
subject=MIN, category="conduct",
title="Marco Mendicino and the Bernardo transfer notification",
date_start="2023-03-02", date_end="2023-07-26",
actors=["Marco Mendicino", "Anne Kelly", "Justin Trudeau"],
summary=(
"Correctional Service Canada moved Paul Bernardo from maximum to medium security on May 29, 2023. The service said "
"Public Safety Minister Marco Mendicino’s office had been notified in early March and again in late May, and that the "
"Prime Minister’s Office was briefed on May 29. Mendicino said he learned of the transfer only after it happened, "
"called it “shocking and incomprehensible,” acknowledged a staff error and issued a directive requiring direct "
"ministerial notification. He was dropped from cabinet in the July 26, 2023 shuffle."
),
finding=dict(body="None — records released under the Access to Information Act; statements by Correctional Service Canada", date=None,
    result="UNADJUDICATED", label="Dropped from cabinet",
    quote="CSC records show the minister’s office was notified in advance; Mendicino stated his staff did not inform him."),
consequence_pm="None. The PMO had been briefed the day of the transfer.",
consequence_others="Mendicino was not reappointed in the July 26, 2023 shuffle and did not run in 2025.",
public_cost=None,
status="Closed.",
sources=[
S("Corrections head personally alerted Mendicino’s office before Bernardo transfer, documents reveal", "The Globe and Mail", "https://www.theglobeandmail.com/canada/article-corrections-head-questioned-how-mendicino-was-kept-in-dark-over/", "2023-06-14"),
S("Trudeau knew about Bernardo transfer before Mendicino, Poilievre calls for minister to resign", "CTV News", "https://beta.ctvnews.ca/national/politics/2023/6/14/1_6440480.amp.html", "2023-06-14"),
]),

dict(
id="david-johnston-rapporteur",
subject=GOV, category="foreign-interference",
title="David Johnston as special rapporteur",
date_start="2023-03-15", date_end="2023-06-09",
actors=["David Johnston", "Justin Trudeau", "Sheila Block", "Navigator"],
summary=(
"Trudeau named former governor general David Johnston Independent Special Rapporteur on Foreign Interference on "
"March 15, 2023. Opposition parties objected that Johnston was a member of the Pierre Elliott Trudeau Foundation "
"and a long-time family friend, and that his lead counsel had donated to the Liberal Party. His May 23, 2023 report "
"recommended against a public inquiry. On May 31 the House voted 174–150 for him to step aside. His office retained "
"the crisis-communications firm Navigator, then dropped it on learning the firm had advised Han Dong. Johnston "
"resigned on June 9, 2023, citing “the highly partisan atmosphere around my appointment.” A public inquiry followed."
),
finding=dict(body="House of Commons, Vote No. 339; Johnston’s resignation", date="2023-06-09",
    result="RESIGNATION", label="Resigned after House vote",
    quote="Vote No. 339 (May 31, 2023): motion calling on the rapporteur to step aside and for a public inquiry — agreed to, 174 to 150. Johnston, June 9: “the highly partisan atmosphere around my appointment” had “the opposite effect” of building trust."),
consequence_pm="None. His chosen alternative to a public inquiry lasted under three months; the inquiry he had recommended against was established in September 2023.",
consequence_others="Johnston resigned. No conflict-of-interest finding was made against him.",
public_cost="Privy Council Office records: a sole-source contract with Torys LLP valued at up to $4,496,888 (April–October 2023), with Navigator subcontracted at an undisclosed amount; Johnston paid $1,600 a day.",
status="Closed.",
sources=[
S("Vote No. 339 — 44th Parliament, 1st Session", "House of Commons of Canada", "https://www.ourcommons.ca/members/en/votes/44/1/339", "2023-05-31", True),
S("First Report — Independent Special Rapporteur on Foreign Interference", "Government of Canada", "https://www.canada.ca/en/democratic-institutions/services/reports/first-report-david-johnston-independent-special-rapporteur-foreign-interference.html", "2023-05-23", True),
S("David Johnston resigns as special rapporteur on foreign interference", "Global News", "https://globalnews.ca/news/9759131/david-johnston-resigns-special-rapporteur-foreign-interference", "2023-06-09"),
S("Special rapporteur David Johnston cuts ties with crisis management firm Navigator", "CTV News", "https://www.ctvnews.ca/politics/article/special-rapporteur-david-johnston-cuts-ties-with-crisis-management-firm-navigator/", "2023-06-08"),
]),

dict(
id="hunka-recognition",
subject=GOV, category="governance",
title="Recognition of Yaroslav Hunka in the House of Commons",
date_start="2023-09-22", date_end="2023-09-27",
actors=["Anthony Rota", "Justin Trudeau", "Yaroslav Hunka", "Volodymyr Zelenskyy"],
summary=(
"During President Zelenskyy’s address on September 22, 2023, Speaker Anthony Rota introduced Yaroslav Hunka, a "
"constituent who had served in the 14th Waffen-SS Division, as a “Canadian hero,” and the House gave him a standing "
"ovation. The Prime Minister’s Office said the Speaker’s guest list had not been shared with it. On September 26 the "
"House unanimously withdrew the recognition and Rota resigned as Speaker. On September 27 Trudeau apologized on "
"behalf of Parliament. Poland’s education minister said he had taken steps toward extradition."
),
finding=dict(body="House of Commons — Speaker’s resignation; unanimous motion withdrawing the recognition", date="2023-09-26",
    result="RESIGNATION", label="Speaker resigned",
    quote="Trudeau, September 27, 2023: “This was a mistake that has deeply embarrassed Parliament and Canada.”"),
consequence_pm="Apology on behalf of Parliament. No PMO or protocol official resigned.",
consequence_others="Rota resigned as Speaker and remained an MP.",
public_cost=None,
status="Closed. No formal extradition request was verified.",
sources=[
S("Anthony Rota resigns as Speaker after honouring Ukrainian veteran who fought with Nazi unit", "CBC News", "https://www.cbc.ca/lite/story/1.6978422", "2023-09-26"),
S("Trudeau apologizes after man who fought in Nazi unit was praised by parliamentarians at Zelenskyy event", "CBC News", "https://amp.cbc.ca/lite/story/1.6979628", "2023-09-27"),
]),

dict(
id="sdtc-green-fund",
subject=GOV, category="spending",
title="Sustainable Development Technology Canada",
date_start="2023-10-03", date_end=None,
actors=["François-Philippe Champagne", "Sustainable Development Technology Canada", "Annette Verschuren", "Karen Hogan (Auditor General)", "Konrad von Finckenstein (Ethics Commissioner)", "RCMP"],
summary=(
"Following a whistleblower complaint, Industry Minister François-Philippe Champagne suspended new funding to the "
"clean-technology foundation on October 3, 2023; its chair, Annette Verschuren, resigned in November. The Auditor "
"General’s June 4, 2024 report found that 10 of 58 examined projects, worth $59 million, did not meet eligibility "
"requirements, and that 90 approval decisions worth nearly $76 million were made where conflict-of-interest policies "
"were not followed. The foundation was wound down into the National Research Council. On July 24, 2024 the Ethics "
"Commissioner found Verschuren had contravened the Conflict of Interest Act. A House order for unredacted documents "
"to be sent to the RCMP was not fully met; the privilege debate that followed consumed the House from September 26, "
"2024 until prorogation on January 6, 2025."
),
finding=dict(body="Auditor General of Canada — 2024 Report 6, Sustainable Development Technology Canada; Ethics Commissioner — Verschuren Report", date="2024-06-04",
    result="AUDIT_ADVERSE", label="Adverse audit",
    quote="“We found that the foundation awarded funding to 10 ineligible projects of 58 we examined. These 10 projects were awarded $59 million even though they did not meet key requirements.” […] “We found 90 cases… representing nearly $76 million in funding awarded to projects, where the foundation’s conflict-of-interest policies were not followed.” […] “Innovation, Science and Economic Development Canada did not sufficiently monitor the compliance with the contribution agreements.”"),
secondary=["Chair found in contravention (July 2024)", "House paralyzed Sept 2024 – Jan 2025"],
consequence_pm="None.",
consequence_others="Verschuren resigned and was found in contravention (no penalty available). The foundation was dissolved. No consequence to Champagne. RCMP Commissioner Duheme wrote in July 2024 that the reports “do not identify any criminal offences or evidence of criminal wrongdoing at this time”; an investigation was confirmed in October 2024.",
public_cost="$59 million to ineligible projects and nearly $76 million in conflict-affected decisions (Auditor General).",
status="No charges located as of September 2026.",
sources=[
S("Report 6—Sustainable Development Technology Canada, 2024 Reports of the Auditor General of Canada", "Office of the Auditor General of Canada", "https://www.canada.ca/en/auditor-general/our-work/audit-reports/parl-oag-202406-06-e.html", "2024-06-04", True),
S("Former SDTC Chairperson failed to comply with Conflict of Interest Act: Verschuren Report (news release)", "Office of the Conflict of Interest and Ethics Commissioner", "https://ciec-ccie.parl.gc.ca/en/news-nouvelles/Pages/NR24072024-1.aspx", "2024-07-24", True),
S("RCMP says it has documents at the centre of a debate bogging down the Commons", "CBC News", "https://amp.cbc.ca/lite/story/1.7342942", "2024-10-04"),
S("No clear end in sight as House of Commons gridlock approaches 2-month mark", "CBC News", "https://www.cbc.ca/lite/story/1.7386424", "2024-11-19"),
S("Ottawa abolishes Sustainable Development Technology Canada", "CBC News", "https://www.cbc.ca/news/politics/ottawa-abolishes-sustainable-development-technology-canada-1.7223993", "2024-06-04"),
]),

dict(
id="carbon-charge-heating-oil",
subject=GOV, category="governance",
title="The heating-oil carve-out from the carbon charge",
date_start="2023-10-26", date_end="2023-11-01",
actors=["Justin Trudeau", "Gudie Hutchings", "Atlantic Liberal caucus"],
summary=(
"On October 26, 2023, after months of pressure from Atlantic Liberal MPs, Trudeau announced a three-year pause of "
"the federal fuel charge on home heating oil, a fuel used mainly in Atlantic Canada, together with a larger rural "
"rebate and heat-pump grants. Trudeau: “We are nothing if not a government that listens to people… and is willing to "
"adjust as necessary.” On CTV three days later, Rural Economic Development Minister Gudie Hutchings said Prairie "
"residents should “elect more Liberals” if they wanted the same consideration. On November 1 Trudeau said there would "
"“absolutely not” be further carve-outs. Saskatchewan responded by ceasing to remit the charge on natural gas."
),
finding=dict(body="Government of Canada — Prime Minister’s announcement", date="2023-10-26",
    result="ADMISSION", label="Policy reversal",
    quote="Hutchings, October 29, 2023: “Perhaps they need to elect more Liberals in the Prairies so that we can have that conversation as well.” Trudeau, November 1: “There will absolutely not be any other carve-outs or suspensions of the price on pollution.”"),
consequence_pm="None.",
consequence_others="Hutchings remained in cabinet. The consumer fuel charge was set to zero by the successor government on April 1, 2025.",
public_cost=None,
status="Overtaken by the elimination of the consumer fuel charge in 2025.",
sources=[
S("Trudeau pauses carbon price on home heating oil for 3 years, doubles rural rebate top-up", "Global News", "https://globalnews.ca/news/10051832/trudeau-affordability-heating-oil-carbon-price", "2023-10-26"),
S("Prairies should elect more Liberals if they want voices heard on carbon pricing: rural economic development minister", "CTV News", "https://www.ctvnews.ca/politics/prairies-should-elect-more-liberals-if-they-want-voices-heard-on-carbon-pricing-rural-economic-development-minister-1.6621490", "2023-10-29"),
S("‘Absolutely not’: No more carve-outs when it comes to carbon pricing, Trudeau says", "The Canadian Press via 620 CKRM", "https://www.620ckrm.com/2023/11/01/absolutely-not-no-more-carve-outs-when-it-comes-to-carbon-pricing-trudeau-says/", "2023-11-01"),
]),

dict(
id="jamaica-vacation",
subject=PM, category="ethics",
title="Jamaica vacation at Prospect Estate",
date_start="2023-12-26", date_end="2024-01-30",
actors=["Justin Trudeau", "Prime Minister’s Office", "Konrad von Finckenstein (Ethics Commissioner)"],
summary=(
"Trudeau and his family flew to Jamaica on December 26, 2023 and stayed at a property of the Green family, friends "
"of the Trudeaus for decades. The PMO first said the family was paying for the stay, then on January 3, 2024 that "
"they stayed “at no cost at a location owned by family friends,” then that they stayed “with family friends.” The PMO "
"said it had consulted the Ethics Commissioner’s office before the trip. On January 30, 2024 Commissioner von "
"Finckenstein told the ethics committee that his office had given advice in advance and had verified the host was a "
"friend with no dealings with the government. Security and travel cost $230,442."
),
finding=dict(body="Conflict of Interest and Ethics Commissioner Konrad von Finckenstein — pre-trip advice; testimony to the ethics committee", date="2024-01-30",
    result="CLEARED", label="Pre-cleared",
    quote="“They consulted us. We gave advice. They went to Jamaica.” […] “If it had not been an acceptable gift, it would have had to be reported on our website.” On the PMO’s shifting descriptions: “I’m not responsible for the spokesman of the prime minister and the way he characterizes our interaction.”"),
consequence_pm="None. Three successive PMO descriptions of the arrangement are on the record.",
consequence_others="None.",
public_cost="$230,442 for the trip: RCMP $162,051; Canadian Armed Forces flights $57,553, including $20,835 for a second aircraft; Privy Council Office $10,838. Trudeau reimburses the equivalent commercial airfare for personal travel on government aircraft.",
status="Closed. No examination opened.",
sources=[
S("Ethics commissioner tells MPs Trudeau’s Jamaica trip followed the rules", "Global News", "https://globalnews.ca/news/10259902/justin-trudeau-jamaica-trip-committee", "2024-01-30"),
S("PMO clarifies Trudeau and family stayed ‘at no cost’ during vacation in Jamaica", "The Canadian Press via Lethbridge News Now", "https://lethbridgenewsnow.com/2024/01/03/pmo-clarifies-trudeau-and-family-stayed-at-no-cost-during-vacation-in-jamaica/", "2024-01-03"),
S("Trudeau’s Jamaica vacation cost far more than same trip the year before", "CBC News", "https://www.cbc.ca/news/politics/trudeau-jamaica-vacation-cost-1.7149906", "2024-03-21"),
]),

# ───────────────────────────── 2024 ─────────────────────────────
dict(
id="nsicop-2024-parliamentarians",
subject=GOV, category="foreign-interference",
title="NSICOP’s “semi-witting or witting” parliamentarians",
date_start="2024-03-22", date_end="2025-01-28",
actors=["NSICOP", "Justin Trudeau", "Dominic LeBlanc", "Marie-Josée Hogue"],
summary=(
"The National Security and Intelligence Committee of Parliamentarians delivered a classified report to the Prime "
"Minister on March 22, 2024 and released a redacted version on June 3. It stated that some parliamentarians were, "
"in the intelligence services’ words, “semi-witting or witting” participants in foreign states’ efforts to interfere "
"in Canadian politics, and that “the Committee expected the government to act. It was slow to do so.” The government "
"declined to name anyone; Trudeau said he had concerns with how the committee drew its conclusions. The House "
"referred the report to the Hogue Commission, which reviewed the underlying intelligence."
),
finding=dict(body="Public Inquiry into Foreign Interference (Hogue) — Final Report, Vol. 4, ch. 18", date="2025-01-28",
    result="INQUIRY_FINDING", label="Hogue: claims overstated",
    quote="“Some of the findings in the NSICOP Report regarding the ‘witting’ participation of individual parliamentarians in foreign interference activities were more definitive than the underlying intelligence could support. […] There are legitimate concerns about parliamentarians potentially having problematic relationships with foreign officials, exercising poor judgment, behaving naively and perhaps displaying questionable ethics. But I did not see evidence of parliamentarians conspiring with foreign states against Canada.”"),
consequence_pm="None.",
consequence_others="No parliamentarian was named, charged or sanctioned. NSICOP’s finding that ministers “did not request policy advice in response to intelligence reporting” stands as a criticism of the government’s process.",
public_cost=None,
status="Closed as to adjudication; no names released.",
sources=[
S("Special Report on Foreign Interference in Canada’s Democratic Processes and Institutions (public version, PDF)", "National Security and Intelligence Committee of Parliamentarians", "https://www.nsicop-cpsnr.ca/reports/rp-2024-06-03/special-report-foreign-interference.pdf", "2024-06-03", True),
S("Final Report, Volume 4 — The NSICOP Report (PDF)", "Foreign Interference Commission", "https://foreigninterferencecommission.ca/fileadmin/PIFI_-_Final_Report_Vol._4__2025_.pdf", "2025-01-28", True),
S("Trudeau won’t say if Liberal MPs allegedly conspired with foreign states", "Global News", "https://globalnews.ca/news/10568744/trudeau-wont-say-if-liberal-mps-allegedly-conspired-with-foreign-states", "2024-06-13"),
]),

dict(
id="immigration-could-have-acted-quicker",
subject=PM, category="governance",
title="Immigration: “we could have acted quicker”",
date_start="2024-10-24", date_end="2024-11-17",
actors=["Justin Trudeau", "Marc Miller"],
summary=(
"On October 24, 2024 Immigration Minister Marc Miller cut the 2025 permanent-resident target to 395,000 from the "
"planned 500,000 and set a goal of reducing temporary residents to 5% of the population. Statistics Canada had "
"recorded population growth of 3.2% in 2023, the highest rate since 1957, and 3,049,277 non-permanent residents on "
"October 1, 2024, 7.4% of the population. In a video on November 17, 2024 Trudeau said that once the post-pandemic "
"labour need had cooled, “as a federal team we could have acted quicker and turned off the taps faster,” and "
"attributed abuses to employers and colleges that gamed the programs."
),
finding=dict(body="Justin Trudeau — public video statement", date="2024-11-17",
    result="ADMISSION", label="Admitted",
    quote="“As a federal team we could have acted quicker and turned off the taps faster.”"),
consequence_pm="None.",
consequence_others="None. Permanent-resident targets were cut by about a fifth over two years.",
public_cost=None,
status="Reduced targets remained in force through the change of government.",
sources=[
S("Government of Canada reduces immigration (2025–2027 Immigration Levels Plan)", "Immigration, Refugees and Citizenship Canada", "https://www.canada.ca/en/immigration-refugees-citizenship/news/2024/10/government-of-canada-reduces-immigration.html", "2024-10-24", True),
S("Canada’s population estimates, third quarter 2024", "Statistics Canada", "https://www150.statcan.gc.ca/n1/daily-quotidien/241217/dq241217c-eng.htm", "2024-12-17", True),
S("Trudeau says he could have acted faster to make immigration changes, blames ‘bad actors’", "CBC News", "https://www.cbc.ca/lite/story/1.7386023", "2024-11-18"),
]),

dict(
id="freeland-resignation",
subject=GOV, category="governance",
title="Chrystia Freeland resigns as Finance Minister",
date_start="2024-12-13", date_end="2024-12-16",
actors=["Chrystia Freeland", "Justin Trudeau", "Dominic LeBlanc"],
summary=(
"On December 16, 2024, the morning the Fall Economic Statement was due, Deputy Prime Minister and Finance Minister "
"Chrystia Freeland resigned by public letter. She wrote that Trudeau had told her the previous Friday that he no "
"longer wanted her as Finance Minister, that they were “at odds about the best path forward,” and that the "
"government should be “eschewing costly political gimmicks, which we can ill afford” — the GST holiday had begun two "
"days earlier and $250 cheques were proposed. The statement tabled that afternoon reported a 2023–24 deficit of "
"$61.9 billion against the $40.1-billion ceiling she had set. Trudeau announced his own resignation three weeks later."
),
finding=dict(body="Chrystia Freeland — resignation letter", date="2024-12-16",
    result="RESIGNATION", label="Resigned",
    quote="“On Friday, you told me you no longer want me to serve as your Finance Minister… we have been at odds about the best path forward for Canada… That means eschewing costly political gimmicks, which we can ill afford… keeping our fiscal powder dry today, so we have the reserves we may need.”"),
consequence_pm="Announced his resignation on January 6, 2025.",
consequence_others="Freeland left cabinet; Dominic LeBlanc was sworn in as Finance Minister the same day.",
public_cost="2023–24 deficit of $61.9 billion against the $40.1-billion guardrail.",
status="Closed.",
sources=[
S("Freeland resigns: calls for Trudeau to step down grow, as Liberals appoint new finance minister amid $62B deficit", "Yahoo Finance Canada", "https://ca.finance.yahoo.com/news/chrystia-freeland-sends-resignation-letter-to-trudeau-calls-out-costly-political-gimmicks-162749861.html", "2024-12-16"),
S("Fall economic update overshadowed by Freeland’s exit", "Global News", "https://globalnews.ca/news/10920897/fall-economic-update-chrystia-freeland-exit", "2024-12-16"),
]),

# ───────────────────────────── 2025 ─────────────────────────────
dict(
id="trudeau-resignation",
subject=PM, category="governance",
title="Trudeau announces his resignation",
date_start="2025-01-06", date_end="2025-03-14",
actors=["Justin Trudeau", "Mary Simon", "Mark Carney"],
summary=(
"By late 2024 at least two dozen Liberal MPs and three regional caucuses had asked Trudeau to step down; Freeland’s "
"resignation followed on December 16. On January 6, 2025, outside Rideau Cottage, Trudeau announced he would resign "
"as Liberal leader and Prime Minister once a successor was chosen: “If I’m having to fight internal battles, I cannot "
"be the best option in that election.” The Governor General prorogued Parliament until March 24. Mark Carney won the "
"leadership on March 9 and was sworn in on March 14, 2025."
),
finding=dict(body="Justin Trudeau — public announcement", date="2025-01-06",
    result="RESIGNATION", label="Resigned",
    quote="“This country deserves a real choice in the next election, and it’s become clear to me that if I’m having to fight internal battles, I cannot be the best option in that election.”"),
consequence_pm="Ceased to be Prime Minister on March 14, 2025.",
consequence_others="Parliament did not sit from January 6 to March 24, 2025.",
public_cost=None,
status="Closed.",
sources=[
S("Trudeau says he’s not the right choice to lead party in next election, promises to resign as PM", "CBC News", "https://www.cbc.ca/news/politics/trudeau-news-conference-1.7423680", "2025-01-06"),
S("Canada’s Trudeau resigns as Liberal Party leader in the face of rising discontent over his leadership", "PBS NewsHour / Associated Press", "https://www.pbs.org/newshour/amp/world/canadas-trudeau-to-announce-his-political-future-after-facing-growing-calls-to-resign", "2025-01-06"),
]),

dict(
id="prorogation-2025",
subject=PM, category="governance",
title="The January 2025 prorogation, upheld in Federal Court",
date_start="2025-01-06", date_end="2025-03-06",
actors=["Justin Trudeau", "Chief Justice Paul Crampton", "David MacKinnon", "Aris Lavranos", "Justice Centre for Constitutional Freedoms"],
summary=(
"Trudeau obtained a prorogation of Parliament from January 6 to March 24, 2025 to allow a Liberal leadership race. "
"Two Nova Scotia residents, backed by the Justice Centre for Constitutional Freedoms, sought judicial review. On "
"March 6, 2025 Chief Justice Paul Crampton dismissed the application: the exercise of the prorogation power is "
"reviewable by the courts, but the applicants had not shown the Prime Minister exceeded any constitutional limit. "
"An appeal was filed; the Federal Court of Appeal heard argument on whether it is moot in April 2026."
),
finding=dict(body="Federal Court, MacKinnon v. Canada (Attorney General), 2025 FC 422 (Crampton C.J.)", date="2025-03-06",
    result="COURT_FOR_GOVERNMENT", label="Upheld",
    quote="“The Applicants failed to demonstrate that the Prime Minister exceeded any of the limits established by the written Constitution or by the unwritten principles they identified.”"),
consequence_pm="None. The prorogation stood.",
consequence_others="None.",
public_cost=None,
status="Ruling for the government stands; no appeal decision located as of September 2026.",
sources=[
S("Decision on motion, T-60-25, MacKinnon et al. v. AGC, 2025 FC 105 (PDF)", "Federal Court of Canada", "https://www.fct-cf.ca/Content/assets/pdf/base/Decision-on-motion-T-60-25-MacKinnon-et-al.-v.-AGC.pdf", "2025-01-18", True),
S("A Lawful Prorogation: MacKinnon v. Canada (Attorney General), 2025 FC 422", "Paul Daly, Administrative Law Matters", "https://www.administrativelawmatters.com/blog/2025/03/07/a-lawful-prorogation-mackinnon-v-canada-attorney-general-2025-fc-422/", "2025-03-07"),
S("Court dismisses legal challenge to Trudeau’s prorogation decision", "CBC News", "https://www.cbc.ca/lite/story/1.7477263", "2025-03-06"),
]),

dict(
id="boil-water-advisories-promise",
subject=PM, category="commitments",
title="Long-term drinking-water advisories on reserves: the five-year promise",
date_start="2015-10", date_end="2021-03-31",
actors=["Justin Trudeau", "Marc Miller", "Indigenous Services Canada", "Karen Hogan (Auditor General)"],
summary=(
"In the 2015 campaign Trudeau promised to end every long-term drinking-water advisory on First Nations reserves "
"within five years of taking office, a deadline of March 2021. The Auditor General reported on February 25, 2021 "
"that Indigenous Services Canada “did not meet its commitment”: 60 long-term advisories remained as of November 1, "
"2020, 28 of them in place for more than a decade, and the department had not changed the formula that funds the "
"operation and maintenance of water systems in thirty years. When the deadline arrived, 58 advisories remained in "
"38 communities. The minister said the commitment “remains firm” and set no new date."
),
finding=dict(body="Auditor General of Canada — 2021 Report 3, Access to Safe Drinking Water in First Nations Communities", date="2021-02-25",
    result="BROKEN_COMMITMENT", label="Promise broken",
    quote="“Indigenous Services Canada did not meet its commitment to eliminate long-term drinking water advisories in First Nations communities.” As of November 1, 2020, 60 long-term advisories remained in effect, 28 of them for more than a decade; the operations-and-maintenance funding formula “had not been amended since it was first developed 30 years ago.”"),
consequence_pm="None. The deadline passed and no replacement date was set.",
consequence_others="None. Minister Marc Miller pledged more than $1.5 billion to finish the work.",
public_cost="More than $1.5 billion pledged in 2021 to finish the work.",
status="The March 2021 deadline passed with 58 advisories in place in 38 communities; no new date was set during the tenure.",
sources=[
S("Report 3—Access to Safe Drinking Water in First Nations Communities, 2021 Reports of the Auditor General of Canada", "Office of the Auditor General of Canada", "https://www.canada.ca/en/auditor-general/our-work/audit-reports/parl-oag-202102-03-e.html", "2021-02-25", True),
S("Appearance before the Standing Committee on Public Accounts on OAG Report 3 (April 29, 2021)", "Indigenous Services Canada", "https://www.sac-isc.gc.ca/eng/1624619832748/1624619978924", "2021-04-29", True),
S("Federal government vows again to end boil water advisories but offers no new target date", "CBC News", "https://amp.cbc.ca/lite/story/1.5943388", "2021-03-10"),
S("Too many First Nations lack clean drinking water and it’s Ottawa’s fault, says auditor general", "CBC News", "https://www.cbc.ca/news/politics/auditor-general-reports-2021-1.5927572", "2021-02-25"),
]),

dict(
id="pandemic-preparedness-audit",
subject=GOV, category="governance",
title="Pandemic preparedness: the early-warning system and quarantine",
date_start="2020-01", date_end="2021-03-25",
actors=["Public Health Agency of Canada", "Patty Hajdu", "Karen Hogan (Auditor General)"],
summary=(
"The Auditor General reported on March 25, 2021 that the Public Health Agency of Canada “was not adequately "
"prepared to respond to the pandemic, and it underestimated the potential impact of the virus at the onset of the "
"pandemic.” The Global Public Health Intelligence Network, built to give early warning of outbreaks, “did not issue "
"an alert” when COVID-19 emerged in Wuhan; the agency rated the risk to Canada “low” until March 12, 2020; it had not "
"completed a planned test of its pandemic plans; it did not know whether two-thirds of incoming travellers followed "
"quarantine orders; and it referred only 40 per cent of the travellers it flagged as high-risk to police."
),
finding=dict(body="Auditor General of Canada — 2021 Report 8, Pandemic Preparedness, Surveillance, and Border Control Measures", date="2021-03-25",
    result="AUDIT_ADVERSE", label="Audit: unprepared",
    quote="“The agency was not adequately prepared to respond to the pandemic, and it underestimated the potential impact of the virus at the onset of the pandemic.” The Global Public Health Intelligence Network “did not issue an alert to provide an early warning when COVID-19 first emerged in Wuhan, China.” The agency “did not know whether two-thirds of incoming travellers followed quarantine orders.”"),
consequence_pm="None.",
consequence_others="None to ministers. The agency accepted the recommendations.",
public_cost=None,
status="Closed as an audit matter.",
sources=[
S("Report 8—Pandemic Preparedness, Surveillance, and Border Control Measures, 2021 Reports of the Auditor General of Canada", "Office of the Auditor General of Canada", "https://www.canada.ca/en/auditor-general/our-work/audit-reports/parl-oag-202103-03-e.html", "2021-03-25", True),
S("Key information — Standing Committee on Public Accounts: OAG audit on Pandemic Preparedness, Surveillance and Border Control (April 20, 2021)", "Canada Border Services Agency", "https://cbsa-asfc.gc.ca/transparency-transparence/pd-dp/bbp-rpp/pacp/2021-04-20/keyinfo-infocle-eng.html", "2021-04-20", True),
S("Public Health Agency was unprepared for the pandemic and ‘underestimated’ the danger, auditor general says", "CBC News", "https://www.cbc.ca/lite/story/1.5963895", "2021-03-25"),
S("Misuse of pandemic early warning system, inaccurate risk assessments hurt Canada’s response to COVID-19, Auditor-General says", "The Globe and Mail", "https://www.theglobeandmail.com/politics/article-misuse-of-pandemic-early-warning-system-inaccurate-risk-assessments/", "2021-03-25"),
]),

dict(
id="khadr-settlement",
subject=GOV, category="spending",
title="The Omar Khadr settlement",
date_start="2017-07-05", date_end="2017-07-07",
actors=["Omar Khadr", "Ralph Goodale", "Jody Wilson-Raybould", "Justin Trudeau"],
summary=(
"On July 5, 2017 the government paid Omar Khadr $10.5 million, and on July 7 Public Safety Minister Ralph Goodale "
"and Justice Minister Jody Wilson-Raybould announced the settlement, and the government issued a written apology signed by "
"Goodale and Foreign Affairs Minister Chrystia Freeland. Khadr had been taken to "
"Guantanamo Bay at 15; the Supreme Court of Canada ruled in 2008 and 2010 that Canadian officials violated his "
"Charter rights by interrogating him there and sharing the results with the United States. His lawsuit had sought "
"$20 million."
),
finding=dict(body="Government of Canada — Statement of Apology to Mr. Omar Khadr, issued by Ministers Freeland and Goodale; settlement announced by Goodale and Wilson-Raybould", date="2017-07-07",
    result="RECORD", label="Cost on record",
    quote="“Today, we are announcing that the Government of Canada has reached a settlement with Mr. Omar Khadr, bringing this civil case to a close. On behalf of the Government of Canada, we wish to apologize to Mr. Khadr for any role Canadian officials may have played in relation to his ordeal abroad and any resulting harm. […] The details of the settlement are confidential between Mr. Khadr and the Government.” At the announcement, Wilson-Raybould: “A Canadian citizen’s charter rights were violated … there are serious costs when the government violates the rights of its citizens.” Goodale: “It is not about the battlefield in Afghanistan. It is about the acts or omissions of the Canadian government after Mr. Khadr was captured and detained.”"),
consequence_pm="None.",
consequence_others="None.",
public_cost="$10.5 million, paid July 5, 2017.",
status="Closed.",
sources=[
S("Statement of Apology to Mr. Omar Khadr", "Public Safety Canada", "https://www.canada.ca/en/public-safety-canada/news/2017/07/statement_of_apologytomromarkhadr.html", "2017-07-07", primary=True),
S("Government issues official apology, confirms settlement payout to Omar Khadr", "Global News", "https://globalnews.ca/news/3582295/government-issues-official-apology-to-omar-khadr/", "2017-07-07"),
S("Omar Khadr received $10.5M from Ottawa on Wednesday, government confirms", "CBC News", "https://www.cbc.ca/news/politics/omar-khadr-settlement-1.4194142", "2017-07-06"),
S("Government formally apologizes to Omar Khadr", "CBC News", "https://www.cbc.ca/news/politics/cabinet-explain-omar-khadr-settlement-1.4194467", "2017-07-07"),
]),

dict(
id="firearms-buyback-program",
subject=GOV, category="spending",
title="The firearms buyback program",
date_start="2020-05-01", date_end=None,
actors=["Bill Blair", "Marco Mendicino", "Dominic LeBlanc", "Public Safety Canada"],
summary=(
"On May 1, 2020 the cabinet banned about 1,500 models of firearm by order-in-council and told owners the government "
"would buy them back. Figures tabled in Parliament in response to an Order Paper question, reported by CTV News on "
"September 20, 2024, put the program’s cost at $67.2 million since 2020, with no firearms collected."
),
finding=dict(body="Public Safety Canada figures tabled in response to an Order Paper question", date="2024-09-20",
    result="RECORD", label="Cost on record",
    quote="“The federal firearm buyback program has cost taxpayers nearly $67.2 million since it was announced in 2020, but it still hasn’t collected a single gun.” — CTV News, reporting the tabled figures."),
consequence_pm="None.",
consequence_others="None.",
public_cost="$67.2 million to September 2024, with no firearms collected.",
status="Figures current to September 2024; later phases of the program are not verified in this record.",
sources=[
S("Federal firearm buyback program has cost $67M since 2020, still hasn’t collected guns", "CTV News", "https://www.ctvnews.ca/politics/article/federal-firearm-buyback-program-has-cost-67m-since-2020-still-hasnt-collected-guns/", "2024-09-20"),
S("Assault-Style Firearms Compensation Program", "Public Safety Canada", "https://www.canada.ca/en/public-safety-canada/campaigns/firearms-buyback.html", None, True),
]),

]


# Clean public-cost figures in CAD for machine use (null where no single figure exists).
COST_CAD = {
    "aga-khan-vacation": 215398, "india-trip-atwal": 1660000, "jamaica-vacation": 230442, "london-hotel-queen-funeral": 397843,
    "butts-telford-moving-expenses": 207052, "arrivecan": 59500000, "phoenix-pay-system": 5100000000,
    "covid-benefit-overpayments": 4600000000, "mckinsey-outsourcing": 209000000, "sdtc-green-fund": 123000000,
    "trans-mountain": 38700000000, "snap-election-2021": 574200000, "mark-norman-prosecution": 500000,
    "nuctech-standing-offer": 250000, "ng-pomp-circumstance": 22790, "hussen-constituency-contracts": 93050,
    "baylis-ventilators": 237000000, "david-johnston-rapporteur": 4496888, "khadr-settlement": 10500000,
    "firearms-buyback-program": 67200000, "fiscal-record-2015-promise": 637600000000,
}
