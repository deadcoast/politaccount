# -*- coding: utf-8 -*-
"""Plain-language layer for every case. Voice: flat, concrete, no adjectives, no section numbers.
Fields: headline · plain · found · him · others · cost · label (tag) · big (headline case)"""

PLAIN = {

"fiscal-record-2015-promise": dict(
 headline="Promised small deficits and a balanced budget by 2019. Never balanced one.",
 plain="In 2015 he promised deficits under $10 billion for two years and a balanced budget in 2019. He ran a deficit every year he was in office. The federal debt roughly doubled, from about $629 billion when he took over to about $1.27 trillion when he left, and interest on it now costs more than $50 billion a year.",
 found="Finance Canada's own books: no balanced budget in any year, 2015–2025.",
 him="Nothing. The target was replaced with a 'debt-to-GDP anchor'.",
 others="Nothing.",
 cost="Debt up about $640 billion; interest costs $53 billion in 2024–25.",
 label="Promise broken"),

"electoral-reform": dict(
 headline="Promised 2015 would be the last election under first past the post. Killed the promise in 2017.",
 plain="The 2015 platform said 2015 'will be the last federal election conducted under the first-past-the-post voting system'. A committee studied it and recommended a referendum on proportional representation. In February 2017 his mandate letter to the new minister said the change 'will not be in your mandate'. Three more elections were held under the old system. The day he resigned he called it his one regret.",
 found="His own mandate letter cancelled the promise.",
 him="Nothing.",
 others="Nothing.",
 cost=None,
 label="Promise broken"),

"phoenix-pay-system": dict(
 headline="Switched on a pay system that failed hundreds of thousands of public servants. The fix has cost $5 billion.",
 plain="Phoenix was bought under Harper and switched on by Trudeau's government in 2016. Public servants went unpaid, underpaid or overpaid for years. The Auditor General called it 'an incomprehensible failure of project management and oversight'. Fixing it has cost $5.1 billion so far; at the end of 2025 more than 233,000 pay problems were still open. The replacement is budgeted at another $4.2 billion.",
 found="Auditor General: 'an incomprehensible failure of project management and oversight'.",
 him="Nothing.",
 others="No minister or deputy minister lost their job.",
 cost="$5.1 billion to fix so far; $4.2 billion for the replacement.",
 label="Audit: failure", big=True),

"elbowgate": dict(
 headline="Grabbed one MP and elbowed another on the floor of the House.",
 plain="During a stalled vote in May 2016 he walked across the floor, took the Conservative whip by the arm to pull him through a group of NDP MPs and elbowed NDP MP Ruth Ellen Brosseau in the chest. She left the chamber and missed the vote. He apologized twice. The committee that looked at it dropped the matter once she accepted the apology.",
 found="Referred to a committee, which dropped it after the apology was accepted.",
 him="Two apologies. Nothing else.",
 others="Nothing.",
 cost=None,
 label="Apologized"),

"cash-for-access-fundraisers": dict(
 headline="Sold face time at $1,500 a ticket in private homes, including to a Chinese billionaire who then gave $200,000 to the Trudeau Foundation.",
 plain="Through 2016 he headlined Liberal fundraisers in private homes at up to $1,525 a ticket. One, in May 2016, was attended by Chinese businessman Zhang Bin; weeks later Zhang and a partner announced $200,000 for the Pierre Elliott Trudeau Foundation and $50,000 for a statue of his father. The ethics commissioner called the practice 'not very savoury' and found no breach of the rules as written. He ended the format in 2017 and the rules were tightened.",
 found="Ethics commissioner: 'not very savoury'; no breach found.",
 him="Nothing. Investigated and cleared.",
 others="Nothing.",
 cost=None,
 label="Cleared"),

"tootoo-resignation": dict(
 headline="Fisheries minister quit cabinet and caucus over an 'inappropriate relationship' with a staffer.",
 plain="Hunter Tootoo resigned as fisheries minister and left the Liberal caucus in May 2016 and went into treatment for alcohol addiction. That August he admitted to a 'consensual but inappropriate relationship' in the workplace. He sat as an Independent for the rest of the Parliament.",
 found="No investigation. He resigned.",
 him="Nothing.",
 others="Tootoo left cabinet and caucus for good.",
 cost=None,
 label="Quit"),

"trudeau-foundation-donation": dict(
 headline="Beijing directed a $200,000 gift to the Trudeau Foundation, CSIS intercepts showed. The whole board quit.",
 plain="In 2016 two Chinese businessmen pledged $200,000 to the foundation named for his father. In 2023 the Globe and Mail reported that CSIS had intercepted a Chinese diplomat instructing the donor to make the gift, with Beijing reimbursing him. The foundation moved to return the money; its president and entire board resigned. The Auditor General said she had no power to look into private donations. Trudeau said he cut ties with the foundation when he became prime minister.",
 found="Never investigated. The Auditor General declined; nobody else had jurisdiction.",
 him="Nothing. He had no role in running the foundation while in office.",
 others="The foundation's CEO and board resigned.",
 cost=None,
 label="Never investigated"),

"butts-telford-moving-expenses": dict(
 headline="His two top aides billed $207,000 to move from Toronto to Ottawa.",
 plain="Principal secretary Gerald Butts and chief of staff Katie Telford claimed $207,000 in moving expenses under a decades-old policy, part of $1.1 million in relocation costs for 47 political staff. After the Globe reported it they repaid $65,000 and apologized. The rest stayed paid.",
 found="No investigation. Partial repayment.",
 him="Nothing. Ordered a policy review.",
 others="Butts and Telford repaid $65,000 of $207,000.",
 cost="$142,000 kept; $1.1 million for staff moves overall.",
 label="Partly repaid"),

"aga-khan-vacation": dict(
 headline="Took a free holiday on a billionaire's private island while the billionaire's foundation lobbied his office. Broke the ethics law. Paid nothing.",
 plain="Over Christmas 2016 he, his family and friends stayed on the Aga Khan's private island in the Bahamas, flying in on the Aga Khan's helicopter. At the time the Aga Khan's foundation was registered to lobby the Prime Minister's Office and had a $15-million federal grant in the pipeline. The ethics commissioner ruled he broke four sections of the Conflict of Interest Act, the first prime minister ever found to have broken it. Security for the trip cost taxpayers $215,000. The RCMP looked at a fraud charge and dropped it in 2019, partly because it couldn't tell whether a prime minister can legally give himself permission to accept a gift.",
 found="Ethics commissioner: broke four sections of the Conflict of Interest Act. RCMP: considered a fraud charge, closed the file.",
 him="Nothing. The sections he broke carry no penalty. He said he accepted the report.",
 others="Nothing.",
 cost="$215,398 in security and travel.",
 label="Broke the ethics law", big=True),

"mark-norman-prosecution": dict(
 headline="His government prosecuted a vice-admiral for leaking, after Trudeau twice predicted the case would go to court before any charge existed. The case collapsed.",
 plain="Vice-Admiral Mark Norman was suspended in 2017 over an alleged leak about a shipbuilding contract. Trudeau said publicly, twice, that the matter would end up in court, the second time a month before the RCMP laid a charge. Norman's lawyers said officials withheld records and used code names to discuss him. In May 2019 the Crown dropped the charge: 'no reasonable prospect of conviction'. The House of Commons unanimously apologized to Norman; Trudeau left the chamber before the vote. The government paid Norman's legal bills and settled with him.",
 found="Charge stayed by the Crown. Unanimous House apology.",
 him="Nothing. He said the prosecution was 'entirely independent of my office'.",
 others="Norman's career ended; legal fees paid by taxpayers; settlement confidential.",
 cost="Norman's legal fees, reported above $500,000, plus a confidential settlement.",
 label="Case collapsed", big=True),

"sajjan-operation-medusa": dict(
 headline="Defence minister claimed to be 'the architect' of a major Afghan battle. He wasn't.",
 plain="In 2017 Harjit Sajjan told an audience in India he was 'the architect' of Operation Medusa, the 2006 battle in Kandahar. The operation was commanded by Brig.-Gen. David Fraser; Sajjan was a reservist intelligence liaison. After veterans objected he retracted it and apologized. Trudeau refused calls to fire him.",
 found="Retracted and apologized.",
 him="Nothing. Kept Sajjan in the job.",
 others="Sajjan kept the Defence portfolio.",
 cost=None,
 label="Retracted"),

"julie-payette": dict(
 headline="Skipped the vetting committee and picked a governor general who quit over a toxic workplace. She keeps a $150,000 pension for life.",
 plain="He appointed Julie Payette in 2017 without using the advisory committee set up to vet vice-regal candidates. Reporters quickly found a 2011 assault charge (dropped and expunged) and a 2011 fatal collision she had been involved in; neither had surfaced. In 2020 staff described a 'toxic, verbally abusive workplace' at Rideau Hall; an independent review agreed and she resigned in January 2021. By law she keeps a pension of about $150,000 a year and can bill up to $206,000 a year in expenses for life.",
 found="Independent review: she 'belittled, berated and publicly humiliated' staff. She resigned.",
 him="Nothing. He said vetting would be strengthened.",
 others="Payette and her secretary resigned; her pension and expense account continue.",
 cost="About $150,000 a year in pension plus up to $206,000 a year in expenses, for life.",
 label="Resigned"),

"kang-harassment": dict(
 headline="Liberal MP found to have harassed a constituency staffer. Left caucus.",
 plain="In 2017 a staffer in Calgary MP Darshan Kang's office alleged unwanted touching, an attempt to get into her hotel room and an offer of money to keep quiet. Kang left the Liberal caucus. The House of Commons investigation found the complaint 'partially substantiated' and that some of his conduct 'represented harassment'. He was never let back in.",
 found="House investigation: harassment, partially substantiated.",
 him="Nothing.",
 others="Kang out of caucus for good.",
 cost=None,
 label="Left caucus; harassment found"),

"morneau-french-villa": dict(
 headline="Finance minister didn't declare the company holding his villa in France for two years. Fined $200.",
 plain="Bill Morneau owned a villa in Provence through a French private company and didn't disclose the company to the ethics commissioner until CBC asked, two years into the job. His office blamed 'administrative confusion'. He paid a $200 penalty, the only fine anyone in the Trudeau ministry ever paid, sold his Morneau Shepell shares and put his assets in a blind trust.",
 found="Ethics commissioner: $200 penalty for failing to disclose.",
 him="Nothing.",
 others="Morneau paid $200 and stayed finance minister.",
 cost=None,
 label="Fined $200"),

"hehr-resignation": dict(
 headline="Sport minister quit cabinet over sexual harassment allegations. The report was never released.",
 plain="Kent Hehr resigned from cabinet in January 2018 after a woman said he had made sexual comments to women at the Alberta legislature when he was an MLA; a second woman alleged inappropriate touching. The PMO hired an investigator. In June 2018 the PMO said Hehr would not return to cabinet and would stay in the Liberal caucus. The report was kept private.",
 found="PMO-commissioned investigation; report withheld.",
 him="Nothing.",
 others="Hehr out of cabinet, kept in caucus.",
 cost=None,
 label="Quit cabinet"),

"india-trip-atwal": dict(
 headline="A man convicted of trying to murder an Indian cabinet minister got invited to Trudeau's reception in India.",
 plain="During his 2018 India trip, Jaspal Atwal, convicted in the 1986 attempted murder of a Punjab minister, attended a reception hosted by the Prime Minister and was photographed with Trudeau's wife. A Liberal MP took the blame for the invitation. Trudeau's national security adviser then briefed reporters, anonymously, that factions in the Indian government might have set it up. A parliamentary committee with security clearance found the PMO had failed to screen its guests and the RCMP had failed to flag Atwal's record. The trip cost $1.66 million, including $17,000 to fly a celebrity chef over.",
 found="Security-cleared committee: the PMO 'should have more properly addressed' its screening failures; the RCMP erred; no evidence the PMO ordered the media briefing.",
 him="Nothing. Nobody in the PMO was disciplined.",
 others="MP Randeep Sarai took responsibility. The RCMP admitted its error.",
 cost="$1.66 million for the trip.",
 label="Inquiry: PMO failed to vet"),

"leblanc-surf-clam": dict(
 headline="Fisheries minister handed a lucrative clam licence to a company run by his wife's cousin. Broke the ethics law. Kept his job.",
 plain="In 2018 Dominic LeBlanc awarded a new Arctic surf clam licence, a quarter of the whole catch, to a company whose planned general manager was his wife's first cousin, who had lobbied him on it beforehand. The ethics commissioner found he broke the Conflict of Interest Act. The licence was cancelled and re-run. LeBlanc stayed in cabinet until the end.",
 found="Ethics commissioner: broke the Conflict of Interest Act.",
 him="Nothing. Kept LeBlanc in cabinet through 2025.",
 others="LeBlanc: no penalty, the law has none. Licence withdrawn.",
 cost=None,
 label="Broke the ethics law"),

"vance-allegations-2018": dict(
 headline="Told in 2018 that the top general faced a misconduct allegation, his defence minister refused to look at the evidence. The general stayed three more years.",
 plain="In March 2018 the military ombudsman told Defence Minister Harjit Sajjan there was an allegation of inappropriate behaviour against Gen. Jonathan Vance, the chief of the defence staff. When the ombudsman reached for the evidence, Sajjan 'pushed back from the table and said, No'. The PMO was told the next day that a complaint existed; Trudeau's chief of staff testified nobody asked what it was and the prime minister wasn't told. Vance ran the military until 2021. He later pleaded guilty to obstructing justice for pressuring a complainant to lie to investigators.",
 found="Vance pleaded guilty to obstruction of justice. No body made a finding against Sajjan or the PMO.",
 him="Nothing. He said he still had confidence in Sajjan.",
 others="Sajjan: moved to another ministry. Vance: conditional discharge, probation, community service, no criminal record.",
 cost=None,
 label="Vance pleaded guilty", big=True),

"trans-mountain": dict(
 headline="Bought a pipeline for $4.5 billion. The expansion cost $34 billion. Taxpayers will likely take a loss.",
 plain="In 2018 his government bought the Trans Mountain pipeline from Kinder Morgan for $4.5 billion after the company gave up on the expansion. The expansion's cost climbed from an estimated $21 billion to $34 billion. The Parliamentary Budget Officer says the pipeline is worth less than what's on the books, so a sale would likely record a loss. Ottawa still owns it.",
 found="Parliamentary Budget Officer: a sale at current valuations would record a loss.",
 him="Nothing.",
 others="Nothing. Ottawa still owns and finances it.",
 cost="$4.5 billion purchase; $34.2 billion expansion; valued below book.",
 label="Likely loss"),

"kokanee-summit-allegation": dict(
 headline="A 2000 editorial said he groped a reporter at a festival. In 2018 the reporter confirmed it happened. Nobody investigated.",
 plain="In 2000 a small B.C. newspaper published an editorial saying Trudeau, then 28, groped a female reporter at the Kokanee Summit and apologized the next day, reportedly saying he wouldn't have 'been so forward' had he known she wrote for a national paper. It resurfaced in 2018. He said he didn't remember 'any negative interactions', then that he was 'confident I did not act inappropriately' and that a woman 'can experience it differently'. The reporter then confirmed: 'The incident referred to in the editorial did occur, as reported.' She asked to be left alone. No complaint, no investigation.",
 found="Never investigated. The reporter confirmed the account; Trudeau denied acting inappropriately.",
 him="Nothing.",
 others="Nothing.",
 cost=None,
 label="Never investigated"),

"grewal-charges": dict(
 headline="Liberal MP quit over gambling debts, was charged with breach of trust, and was acquitted.",
 plain="Raj Grewal left caucus in 2018 after disclosing a gambling problem and large debts. In 2020 the RCMP charged him with breach of trust and fraud, alleging he traded access to the prime minister and immigration help for loans. The Crown dropped most counts before trial; on the rest a judge directed a not-guilty verdict in 2023.",
 found="Acquitted (directed verdict), March 2023.",
 him="Nothing.",
 others="Grewal: out of politics, acquitted.",
 cost=None,
 label="Charged, acquitted"),

"snc-lavalin-affair": dict(
 headline="Leaned on his attorney general to spare SNC-Lavalin a criminal trial. Broke the ethics law. Two ministers who wouldn't go along were pushed out.",
 plain="In 2018 the prosecution service refused to give SNC-Lavalin a deal that would let it avoid a fraud trial. Trudeau, his staff, the finance minister's office and the top civil servant then pressed Attorney General Jody Wilson-Raybould, over months, to overrule that decision. When the Globe reported it in February 2019 she resigned; so did his principal secretary Gerald Butts and, later, minister Jane Philpott. The clerk of the Privy Council retired. Trudeau expelled Wilson-Raybould and Philpott from the party. The ethics commissioner ruled he broke the law: he used his position to improperly influence the attorney general, against prosecutorial independence and the rule of law. SNC-Lavalin pleaded guilty to fraud anyway and was fined $280 million.",
 found="Ethics commissioner: broke the Conflict of Interest Act. RCMP: not enough evidence for a charge; cabinet secrecy blocked much of the investigation and Trudeau was never interviewed.",
 him="Nothing. The section he broke carries no penalty. He said he took responsibility and would not apologize 'for standing up for Canadian jobs'.",
 others="Wilson-Raybould and Philpott lost cabinet and their party. Butts resigned. Wernick retired. SNC-Lavalin paid $280 million.",
 cost=None,
 label="Broke the ethics law", big=True),

"liberalist-judicial-vetting": dict(
 headline="His office ran would-be judges through the Liberal Party's voter database before appointing them.",
 plain="In 2019 the Globe reported that the PMO checked candidates for judgeships, people already recommended by independent committees, against Liberalist, the party's database of supporters and donors. The PMO said appointments were 'merit-based'. The Canadian Bar Association said political vetting threatened faith in the courts. The practice was reported stopped in 2021; the justice minister said the government would keep reviewing candidates' partisan history from other sources.",
 found="Never investigated.",
 him="Nothing.",
 others="Nothing.",
 cost=None,
 label="Never investigated"),

"ng-pomp-circumstance": dict(
 headline="Trade minister gave $23,000 in contracts to her friend's PR firm. Broke the ethics law. Kept her job.",
 plain="Mary Ng awarded two media-training contracts, worth $22,790, to a public-relations firm co-founded by a friend of twenty years. The ethics commissioner ruled she broke the Conflict of Interest Act by not recusing herself. She apologized. Nothing was repaid and Trudeau kept her in cabinet.",
 found="Ethics commissioner: broke the Act by failing to recuse. 'The Conflict of Interest Act does not provide for any sanctions.'",
 him="Nothing. Kept her in cabinet.",
 others="Ng: apology; no penalty; no repayment.",
 cost="$22,790 of public money to the friend's firm.",
 label="Broke the ethics law"),

"winnipeg-lab-documents": dict(
 headline="Two scientists with ties to Chinese military researchers were fired from Canada's top-security lab. His government fought Parliament in court to keep the files secret.",
 plain="Xiangguo Qiu and Keding Cheng were walked out of the National Microbiology Lab in Winnipeg in 2019 and fired in 2021. Parliament ordered the records; the government refused, the head of the Public Health Agency was formally reprimanded at the bar of the House, and the government sued the Speaker in Federal Court to block the order, a first. The lawsuit died when Trudeau called the 2021 election. The files came out in 2024: CSIS had assessed that Qiu had an 'extensive relationship' with Chinese state institutions, an agreement with the Wuhan Institute of Virology, and had hidden it from her employer. The health minister called the lapses 'unacceptable'.",
 found="Health minister: 'unacceptable', 'lax adherence to the security protocols'. Documents withheld two and a half years, then released.",
 him="Nothing.",
 others="Both scientists fired; no charges. Public Health Agency president reprimanded by the House.",
 cost=None,
 label="Files withheld, then released"),

"blackface-images": dict(
 headline="Wore blackface at least three times. Couldn't say how many.",
 plain="Mid-campaign in 2019, Time published a 2001 photo of him in dark makeup at an 'Arabian Nights' party at the private school where he taught. He apologized that night and admitted a second instance from high school. The next day a video from the early 1990s surfaced showing a third. Asked how many times, he said he couldn't say. He won the election a month later.",
 found="Admitted it. No investigation.",
 him="Two apologies. Nothing else.",
 others="Nothing.",
 cost=None,
 label="Admitted", big=True),

"covid-benefit-overpayments": dict(
 headline="$4.6 billion in pandemic benefits went to people who weren't eligible, and $27 billion more needs checking. The tax agency said checking wasn't worth it.",
 plain="The Auditor General found the government paid $4.6 billion in COVID benefits to people who didn't qualify and flagged at least $27.4 billion more in payments to individuals and businesses that should be investigated, because the agencies 'did not develop rigorous and comprehensive plans to verify the eligibility of recipients'. The head of the Canada Revenue Agency told MPs a full review of the flagged wage subsidies wasn't worth the effort. By the end of 2025 more than $10 billion was still owed.",
 found="Auditor General: $4.6 billion overpaid; $27.4 billion needs investigation; no rigorous eligibility checks.",
 him="Nothing.",
 others="Nothing to ministers. Collection letters to individuals started in 2023.",
 cost="$4.6 billion confirmed overpaid; $10.35 billion still outstanding.",
 label="Audit: $4.6B overpaid", big=True),

"baylis-ventilators": dict(
 headline="A $237-million ventilator contract went to a firm that subcontracted to a company co-owned by a former Liberal MP.",
 plain="In spring 2020 the government ordered 10,000 ventilators for about $237 million from a company that subcontracted the manufacturing to Baylis Medical, co-owned by Frank Baylis, a Liberal MP until 2019. The ethics commissioner said Baylis, as a former MP, wasn't covered by the rules and the contract wasn't with him personally. Baylis told a committee he never approached anyone in government for it. Canada later sat on a large surplus of unused ventilators.",
 found="Never investigated: the ethics commissioner said the rules don't cover a former MP.",
 him="Nothing.",
 others="Nothing.",
 cost="About $237 million.",
 label="Never investigated"),

"we-charity": dict(
 headline="Handed a $912-million student program to a charity that had paid his mother and brother over $280,000 in speaking fees. Didn't recuse. Cleared, and now the courts get to check that.",
 plain="In 2020 cabinet chose WE Charity to run the new Canada Student Service Grant, worth up to $912 million, with an administration fee of up to $43.5 million. Trudeau didn't step out of the decision even though WE had paid his mother about $250,000 and his brother about $32,000 for speeches. When it came out, WE pulled out, Trudeau apologized for not recusing, and finance minister Bill Morneau, whose family had taken free WE trips, resigned. Trudeau then prorogued Parliament, shutting down four committee investigations, and later turned a motion for a special committee into a confidence vote to kill it. In 2021 the ethics commissioner ruled Trudeau hadn't broken the law, because his relatives' income wasn't legally his 'private interest'. Morneau, he ruled, had broken it three ways.",
 found="Ethics commissioner: Trudeau cleared; Morneau broke the Act. Supreme Court, July 2026: the clause that shielded that clearance from the courts is unconstitutional; the Federal Court of Appeal now decides whether the clearance was lawful.",
 him="Nothing. Cleared. Apologized. Prorogued Parliament.",
 others="Morneau resigned and was found to have broken the law. WE Charity shut down in Canada.",
 cost="Program cancelled; up to $43.5 million in fees never paid.",
 label="Cleared, now under court review", big=True),

"lucki-nova-scotia-call": dict(
 headline="After the Nova Scotia massacre, the RCMP commissioner said she'd promised his office details on the guns to help sell gun legislation. Inquiry found no interference.",
 plain="Eleven days after the 2020 mass shooting, RCMP Commissioner Brenda Lucki told Nova Scotia commanders, according to a superintendent's notes, that she had promised the public safety minister's office and the PMO that the force would release details of the killer's weapons to support the government's coming gun bill. Lucki and minister Bill Blair denied any interference; Trudeau said Ottawa 'had a lot of questions' but didn't interfere. The public inquiry found her remarks 'ill-timed and poorly expressed' but not political interference.",
 found="Mass Casualty Commission: no attempted political interference; Lucki's remarks 'ill-timed and poorly expressed'.",
 him="Nothing.",
 others="Lucki retired before the report came out.",
 cost=None,
 label="Inquiry: no interference"),

"arrivecan": dict(
 headline="An app first estimated at $80,000 ended up costing about $60 million. A two-man firm got $19 million. Nobody has been charged.",
 plain="ArriveCAN, the pandemic border app, was first pegged at $80,000. The Auditor General estimated it cost $59.5 million and said the border agency's records were so bad the real number can't be known: 'glaring disregard for basic management and contracting practices'. GC Strategies, a company of two people who did no IT work themselves, collected about $19 million. The procurement watchdog found that in three-quarters of the contracts it checked, some or all of the people the winning bidder promised never did any work. One of the two owners was hauled before the bar of the House of Commons and reprimanded, the first time since 1913 anyone has been questioned there. The firm is banned from federal contracts until 2032. As of September 2026 the RCMP investigation has produced no charges.",
 found="Auditor General: 'glaring disregard for basic management and contracting practices'; true cost unknowable. Procurement ombud: in 76% of contracts, paid-for people did no work.",
 him="Nothing. No minister was sanctioned.",
 others="GC Strategies banned from federal contracts for seven years; owner reprimanded by the House; two border-agency executives suspended without pay. No charges.",
 cost="About $59.5 million, against an $80,000 estimate.",
 label="Audit: rules ignored", big=True),

"morneau-we-charity": dict(
 headline="Finance minister took free trips from WE, let his staff run interference for WE's funding, then helped hand WE a $912-million program. Broke the law three ways. Resigned.",
 plain="Bill Morneau and his family took WE-hosted trips to Kenya and Ecuador in 2017 worth $41,000, which he said he thought he'd paid for; he wrote the cheque in July 2020, the week the scandal broke. His family had also given WE $100,000 and one daughter worked there. His office gave WE 'unfettered access' while it sought federal money, and he sat in on the cabinet decision to hand WE the student grant program. He resigned in August 2020. The ethics commissioner ruled he broke three sections of the Conflict of Interest Act.",
 found="Ethics commissioner: preferential treatment, a decision made in a conflict, failure to recuse.",
 him="Nothing.",
 others="Morneau resigned as minister and MP; no penalty, the law has none.",
 cost=None,
 label="Broke the ethics law"),

"nuctech-standing-offer": dict(
 headline="Awarded a Chinese state-linked firm the contract to supply X-ray scanners for Canadian embassies. Reversed after it hit the news.",
 plain="In July 2020 the procurement department signed a standing offer worth up to $6.8 million with Nuctech, a company tied to the Chinese state, for X-ray machines and metal detectors at 170 embassies. After reporters found it, Global Affairs paid Deloitte $250,000 to review the deal; the review found security experts had been left out of the process. Global Affairs said it wouldn't use the offer; no equipment was bought.",
 found="Reversed. Deloitte: security experts were not part of the procurement.",
 him="Nothing.",
 others="Nothing.",
 cost="$250,000 for the review.",
 label="Reversed"),

"access-to-information-decline": dict(
 headline="Canada's information watchdog: the access-to-information system 'no longer serves its intended purpose', and transparency 'is not a priority for the government'.",
 plain="Caroline Maynard, the officer of Parliament who polices freedom-of-information requests, warned the government in 2021 that the system 'could soon be beyond repair'. The government's review ended in 2022 with no changes to the law. In 2023 she reported that over her tenure she had watched 'the steady decline of the access-to-information system to the point where it no longer serves its intended purpose', and said transparency was 'not a priority for the government'. Liberal MPs on the committee voted against reform.",
 found="Information Commissioner: the system 'no longer serves its intended purpose'.",
 him="Nothing. The law was left unchanged.",
 others="Nothing.",
 cost=None,
 label="Watchdog: system failing"),

"michael-chong-zhao-wei": dict(
 headline="CSIS knew in 2021 that a Chinese diplomat was targeting MP Michael Chong's family in Hong Kong. Chong found out from a newspaper two years later.",
 plain="After Chong led a Commons vote calling China's treatment of Uyghurs a genocide, CSIS learned a Chinese diplomat in Toronto was gathering information on Chong and his relatives in Hong Kong. CSIS sent the public safety minister a memo in 2021; it never reached him. Chong got a vague briefing that left out the diplomat. The Globe published the CSIS assessment in May 2023; the public inquiry later confirmed that Trudeau, his senior staff and the minister all learned of it from that article. The diplomat was expelled a week later.",
 found="Hogue inquiry: the information 'did not flow as it should have'; the memo 'never reached the Minister'; nobody acted with intent.",
 him="Nothing. Found to have learned about it from the newspaper.",
 others="Diplomat Zhao Wei expelled. No official disciplined.",
 cost=None,
 label="Inquiry: warning never delivered"),

"blair-csis-warrant-delay": dict(
 headline="A CSIS spy warrant sat in the public safety minister's office for 54 days. The inquiry called it 'unacceptable'.",
 plain="In 2021 CSIS asked for urgent sign-off on a Federal Court warrant application; the agency wanted it back within six days. It sat with Bill Blair's chief of staff for weeks, and Blair signed it on day 54. Blair testified he didn't know it was waiting until two or three days before. The inquiry kept the target's name secret; the Globe reported it was Liberal organizer Michael Chan.",
 found="Hogue inquiry: delay 'unacceptable', 'everyone involved dropped the ball'; no wrongdoing beyond lack of diligence.",
 him="Nothing.",
 others="Blair stayed in cabinet until 2025.",
 cost=None,
 label="Inquiry: 'unacceptable' delay"),

"afghanistan-evacuation-2021": dict(
 headline="Called an election the day Kabul fell. The airlift ended eleven days later with people left behind.",
 plain="On August 15, 2021, as the Taliban took Kabul, Trudeau went to the Governor General and dissolved Parliament for an election. Canada's airlift got about 3,700 people out before the last flight left on August 26; the government never gave a firm count of who was left behind. A Commons committee later documented the failures in planning and coordination. The general running the evacuation called leaving people behind 'heartbreaking'.",
 found="Commons special committee: planning and coordination failures.",
 him="Nothing.",
 others="No minister resigned; two were shuffled.",
 cost=None,
 label="Committee: planning failures"),

"snap-election-2021": dict(
 headline="Called a $600-million pandemic election two years early and got the same Parliament back.",
 plain="He triggered the September 2021 election halfway through a minority mandate, during the fourth wave of COVID. It was the most expensive in Canadian history; Elections Canada's final count is $574 million plus $150 million in readiness costs. The Liberals went from 157 seats to 160, still a minority.",
 found="Cost on the record. No finding.",
 him="Nothing.",
 others="Nothing.",
 cost="$574 million plus $150 million in readiness (Elections Canada).",
 label="Cost on record"),

"sajjan-afghan-sikhs": dict(
 headline="During the Kabul evacuation, the defence minister reportedly told special forces to go rescue 225 Afghan Sikhs with no ties to Canada. The mission failed.",
 plain="Three military sources told the Globe in 2024 that as Kabul fell, Harjit Sajjan pressed Canadian special forces to rescue a group of about 225 Afghan Sikhs, fed the military their location and texted commanders during the attempt. The sources said the group had no link to Canada, the tasking pulled resources from evacuating Canadians, and none of the group got out on a Canadian flight. Sajjan said he passed on information and never gave an order. His father had sat on the board of the Sikh organization pushing for the rescue.",
 found="Never investigated.",
 him="Nothing.",
 others="Sajjan stayed in cabinet until 2025.",
 cost=None,
 label="Never investigated"),

"tofino-truth-reconciliation-day": dict(
 headline="Spent the first National Day for Truth and Reconciliation surfing in Tofino while his schedule said 'private meetings' in Ottawa.",
 plain="On September 30, 2021, the first day set aside to remember residential-school victims, his public itinerary listed private meetings in Ottawa. He was in Tofino with his family. The Tk'emlúps te Secwépemc, who had announced 215 suspected unmarked graves at the Kamloops residential school that spring, had invited him twice. The itinerary was corrected after Global News asked. He called the chief to apologize, said 'travelling on September 30th was a mistake', and went to Kamloops three weeks later.",
 found="Admitted it: 'a mistake'.",
 him="Apology. Nothing else.",
 others="Nothing.",
 cost=None,
 label="Admitted"),

"emergencies-act-2022": dict(
 headline="Invoked the Emergencies Act against the convoy protests and froze people's bank accounts. Two courts have ruled it was illegal. Nobody paid for it.",
 plain="In February 2022 his cabinet declared a national emergency over the trucker protests, the first use of the Emergencies Act in its history, and ordered banks to freeze accounts without a court order: more than 200 accounts, about $7.8 million. A public inquiry led by Justice Rouleau concluded, 'with reluctance', that the legal bar had been met. Then the Federal Court ruled in 2024 that there was no national emergency, the invocation was 'unreasonable' and beyond the government's legal power, and the account freezes violated the Charter. The government appealed. In January 2026 the Federal Court of Appeal unanimously agreed with the lower court. Ottawa is now asking the Supreme Court to hear it.",
 found="Federal Court (2024) and Federal Court of Appeal (2026): no national emergency; the invocation was unreasonable and beyond the government's power; Charter breaches. Rouleau inquiry (2023): bar met, 'with reluctance'.",
 him="Nothing. No minister resigned. Freeland: 'We believed we were doing something necessary and something legal at the time. That continues to be my belief today.'",
 others="Nothing. The next government kept appealing.",
 cost="More than 200 bank accounts, about $7.8 million, frozen.",
 label="Court: illegal, upheld on appeal", big=True),

"mendicino-police-request-claim": dict(
 headline="Public safety minister said police asked for the Emergencies Act. The police said they didn't.",
 plain="Marco Mendicino told MPs 'the advice we received was to invoke the Emergencies Act' and repeated that the government acted on police advice. The RCMP commissioner and Ottawa's police chief then testified they never asked for it. His own deputy minister told a committee the minister had been 'misunderstood'.",
 found="Walked back by his deputy minister. Police chiefs testified no request was made.",
 him="Nothing.",
 others="Mendicino was dropped from cabinet a year later, over a different matter.",
 cost=None,
 label="Walked back"),

"boissonnault-global-health-imports": dict(
 headline="A minister's business partner texted about 'Randy' during a deal while the minister was in cabinet. Then his claim to be Cree fell apart. He left cabinet.",
 plain="Randy Boissonnault co-owned Global Health Imports and kept half of it after joining cabinet. In 2024 Global News published texts his partner sent during a 2022 deal referring to 'Randy'. Boissonnault denied any involvement; the partner blamed autocorrect and later admitted lying about a second Randy. The ethics commissioner closed his review without a formal investigation, citing no evidence. Separately, Boissonnault had called himself 'non-status adopted Cree' and the party listed him as Indigenous; in November 2024 he said his adoptive mother and brother are Métis and apologized. He stepped out of cabinet that month and didn't run again. His old company was later banned from federal contracts for calling itself Indigenous-owned.",
 found="Ethics commissioner: closed by letter, no evidence of a breach, no formal investigation.",
 him="Nothing. Said Boissonnault was stepping away to clear his name.",
 others="Boissonnault out of cabinet and politics. His former company barred from contracts until 2030; police investigating it.",
 cost=None,
 label="Cleared; left cabinet"),

"london-hotel-queen-funeral": dict(
 headline="Stayed in a $6,000-a-night hotel suite for the Queen's funeral, and his office wouldn't say who was in it.",
 plain="The Canadian delegation to Queen Elizabeth's funeral spent $398,000 on London hotels, including one suite at $6,089 a night for five nights. Records released under access-to-information law blacked out who stayed there; the PMO didn't answer. Two months later it confirmed it was Trudeau and his wife, and said hotel prices had spiked.",
 found="Cost on the record. No finding.",
 him="Nothing.",
 others="Nothing.",
 cost="$398,000 in hotels; about $30,000 for the suite.",
 label="Cost on record"),

"foreign-interference-response": dict(
 headline="Warned by CSIS about Chinese interference in two elections, his government was 'slow to act' and 'insufficiently transparent', in a public inquiry's words.",
 plain="From late 2022, leaked CSIS documents showed China had worked to influence the 2019 and 2021 elections, including through a network around candidates in Toronto. Trudeau said he hadn't been briefed on candidates getting Chinese money, then appointed a 'special rapporteur' who recommended against a public inquiry and quit within three months. The inquiry he finally agreed to found the interference didn't change who won, may have swung a few ridings, and badly hurt public trust, and that most Canadians learned about it from the press, not their government. It found no 'traitors' in Parliament.",
 found="Hogue inquiry: the government 'has sometimes taken too long to act', is 'a poor communicator and insufficiently transparent'. Security-cleared MPs' committee: 'expected the government to act. It was slow to do so.'",
 him="Nothing. No finding of personal wrongdoing.",
 others="No minister resigned. A new foreign-interference law passed in 2024.",
 cost=None,
 label="Inquiry: slow, not transparent", big=True),

"mckinsey-outsourcing": dict(
 headline="Federal contracts to McKinsey went from $2 million under Harper to more than $100 million under Trudeau. The Auditor General found the rules were routinely ignored.",
 plain="Radio-Canada found McKinsey's federal contracts jumped from $2.2 million over nine Harper years to $66 million in seven Trudeau years, later topping $100 million. McKinsey's former global boss, Dominic Barton, had chaired Trudeau's economic advisory council and was made ambassador to China. The Auditor General examined 97 McKinsey contracts worth $209 million: 70% were awarded without competition and most lacked the required justification. Federal spending on outside consultants hit a record $20.7 billion in 2023–24.",
 found="Auditor General: 'frequent disregard for procurement policies and guidance'.",
 him="Nothing. Asked ministers to review the contracts.",
 others="Nobody sanctioned.",
 cost="$209 million to McKinsey, 2011–2023; $20.7 billion a year in outsourcing by 2023–24.",
 label="Audit: rules ignored"),

"hussen-constituency-contracts": dict(
 headline="A minister's office paid $93,000 to a firm run by his policy director's sister.",
 plain="Global News found Ahmed Hussen's constituency office had paid $93,050 over two years to a communications firm whose director is the sister of his director of policy. His office said it was disclosed to the ethics commissioner and the rules were followed. Nobody investigated.",
 found="Never investigated.",
 him="Nothing.",
 others="Hussen stayed in cabinet.",
 cost="$93,050 from his taxpayer-funded office budget.",
 label="Never investigated"),

"han-dong": dict(
 headline="CSIS warned the Liberals in 2019 that Beijing had bused students to a nomination vote. Trudeau kept the candidate.",
 plain="Two days before the 2019 campaign, his campaign director briefed him that CSIS believed Chinese officials had arranged buses of international students to vote for Han Dong at a Toronto Liberal nomination. Trudeau decided the intelligence wasn't solid enough to drop Dong. In 2023 Global News reported the bus story plus a claim that Dong had told a Chinese official to delay freeing the two Michaels; Dong quit caucus and sued. The inquiry found the classified record backed Dong's denial on the Michaels and said it couldn't determine what happened at the nomination, but that nominations are 'gateways' for foreign interference. Dong and Global settled in 2025.",
 found="Hogue inquiry: the Michaels allegation is not supported; the nomination irregularities are undetermined; 'nomination contests may be gateways for foreign states'.",
 him="Nothing. His decision to keep Dong was recorded without criticism.",
 others="Dong lost his party, sat as an Independent, left politics.",
 cost=None,
 label="Inquiry: undetermined"),

"mendicino-bernardo-transfer": dict(
 headline="His public safety minister's office was told months ahead that Paul Bernardo was moving to a medium-security prison. The minister said he found out from the news.",
 plain="Corrections moved serial killer Paul Bernardo to medium security in May 2023. The prison service said Mendicino's office was notified in March and again in May, and the PMO the day it happened. Mendicino said his staff never told him, called the transfer 'shocking and incomprehensible', and blamed a staff error. Trudeau dropped him from cabinet two months later.",
 found="Never formally investigated. Corrections' records show the office was told.",
 him="Nothing. His own office had been briefed the day of the move.",
 others="Mendicino dropped from cabinet; left politics in 2025.",
 cost=None,
 label="Dropped from cabinet"),

"david-johnston-rapporteur": dict(
 headline="To head off a public inquiry into Chinese interference, he appointed a family friend and Trudeau Foundation member to review it. The House voted him out within three months.",
 plain="In March 2023 he named David Johnston, a former governor general, family friend and Trudeau Foundation member, as 'special rapporteur' on foreign interference. Johnston's lawyer was a Liberal donor. Johnston recommended against a public inquiry. The House voted 174–150 for him to step aside; his office hired the crisis-PR firm Navigator, then fired it on learning Navigator had also worked for Han Dong. He resigned in June, blaming the 'highly partisan atmosphere'. The public inquiry he'd advised against was called three months later.",
 found="House of Commons vote, 174–150, to remove him. He resigned.",
 him="Nothing. His alternative to an inquiry collapsed and he called the inquiry anyway.",
 others="Johnston resigned.",
 cost="Legal contract for the review capped at $4.5 million; Johnston paid $1,600 a day.",
 label="Forced out"),

"hunka-recognition": dict(
 headline="Parliament gave a standing ovation to a Waffen-SS veteran during Zelenskyy's visit. The Speaker resigned; Trudeau apologized for Parliament.",
 plain="During President Zelenskyy's address in September 2023, Speaker Anthony Rota introduced 98-year-old Yaroslav Hunka as a 'Canadian hero' who fought the Russians. Hunka had served in the 14th Waffen-SS Division. The House, Zelenskyy and Trudeau all applauded. The PMO said it never saw the Speaker's guest list. Rota resigned four days later; the House struck the tribute from the record; Trudeau apologized on behalf of Parliament. Poland said it was looking at extradition.",
 found="Speaker resigned. Trudeau: 'a mistake that has deeply embarrassed Parliament and Canada'.",
 him="An apology on Parliament's behalf. Nothing else.",
 others="Rota resigned as Speaker.",
 cost=None,
 label="Speaker resigned"),

"sdtc-green-fund": dict(
 headline="The government's billion-dollar green-tech fund gave $59 million to ineligible projects and $76 million in deals where board members had conflicts. Parliament seized up for four months over the documents.",
 plain="Sustainable Development Technology Canada handed out federal money to clean-tech startups. After a whistleblower complaint, the Auditor General found $59 million went to projects that didn't qualify and nearly $76 million was approved in 90 decisions where the board's conflict-of-interest rules were ignored, directors voting money to companies they were connected to. The chair, Annette Verschuren, was found to have broken the Conflict of Interest Act. The fund was shut down and folded into the National Research Council. When the House ordered the documents sent to the RCMP and the government didn't fully comply, the resulting privilege fight froze all House business from late September 2024 until Trudeau prorogued Parliament in January 2025.",
 found="Auditor General: $59 million to ineligible projects; $76 million in 90 conflicted decisions; the department failed to monitor. Ethics commissioner: the chair broke the Act.",
 him="Nothing.",
 others="Chair resigned and was found in breach (no penalty). Minister Champagne: nothing. RCMP: investigation confirmed, no charges.",
 cost="About $123 million in ineligible or conflicted funding.",
 label="Audit: conflicts, ineligible grants", big=True),

"carbon-charge-heating-oil": dict(
 headline="Exempted home heating oil from the carbon tax, a fuel used mostly in Atlantic Liberal ridings. A minister then told the Prairies to 'elect more Liberals' if they wanted the same.",
 plain="In October 2023, with his Atlantic MPs in revolt, he paused the carbon charge on home heating oil for three years, mainly benefiting Atlantic Canada. Asked why the Prairies got nothing, minister Gudie Hutchings said on CTV: 'Perhaps they need to elect more Liberals in the Prairies so that we can have that conversation as well.' Days later Trudeau said there would 'absolutely not' be any more carve-outs. Saskatchewan stopped collecting the charge on natural gas in response.",
 found="Policy reversal, on the record.",
 him="Nothing.",
 others="Hutchings kept her job.",
 cost=None,
 label="Reversed"),

"jamaica-vacation": dict(
 headline="Took a free luxury vacation at a family friend's Jamaica estate. His office gave three different stories about who paid.",
 plain="Over Christmas 2023 he and his family stayed at Prospect Estate in Jamaica, owned by the Green family, where villas rent for around $9,000 a night. The PMO first said the family was paying; then that they stayed 'at no cost at a location owned by family friends'; then that they stayed 'with family friends'. His office had checked with the ethics commissioner beforehand, and the commissioner told MPs the host was a genuine friend with no government dealings: 'They consulted us. We gave advice. They went to Jamaica.' Security and flights cost $230,000.",
 found="Cleared in advance by the ethics commissioner.",
 him="Nothing. Cleared.",
 others="Nothing.",
 cost="$230,442 in security and flights.",
 label="Cleared in advance"),

"nsicop-2024-parliamentarians": dict(
 headline="A committee with top-secret clearance said some MPs were 'witting' helpers of foreign governments. Trudeau wouldn't name them. The inquiry later said the claim overshot the evidence.",
 plain="In June 2024 the National Security and Intelligence Committee of Parliamentarians reported that some parliamentarians were 'semi-witting or witting participants' in foreign states' interference, and that the government had been 'slow' to act. Trudeau refused to release names and questioned how the committee reached its conclusions. The Hogue inquiry then read the raw intelligence and concluded the report's claims were 'more definitive than the underlying intelligence could support': poor judgment and questionable ethics by some MPs, yes; 'traitors', no.",
 found="Hogue inquiry: the claims were 'more definitive than the underlying intelligence could support'; no evidence of MPs conspiring with foreign states.",
 him="Nothing.",
 others="No MP named or sanctioned.",
 cost=None,
 label="Inquiry: overstated"),

"immigration-could-have-acted-quicker": dict(
 headline="After population growth hit its highest rate since 1957, he admitted his government 'could have acted quicker and turned off the taps faster'.",
 plain="Canada's population grew 3.2% in 2023, almost all from immigration, and by late 2024 there were three million temporary residents, 7.4% of the country. In October 2024 his immigration minister cut the permanent-resident target by a fifth and set out to shrink the temporary population. In a video three weeks later Trudeau said that once the post-pandemic labour shortage eased, 'as a federal team we could have acted quicker and turned off the taps faster', and blamed 'bad actors', employers and colleges gaming the programs.",
 found="Admitted it, on video.",
 him="Nothing.",
 others="Nothing.",
 cost=None,
 label="Admitted"),

"freeland-resignation": dict(
 headline="His finance minister quit the morning of the fiscal update, calling his spending plans 'costly political gimmicks'.",
 plain="On December 16, 2024, hours before she was due to deliver the fall economic statement, Chrystia Freeland resigned by public letter. He'd told her the Friday before that he was moving her out of Finance. She wrote that they were 'at odds about the best path forward for Canada' and that the country should be 'eschewing costly political gimmicks, which we can ill afford'; the GST holiday had started two days earlier and $250 cheques were on the table. The update she didn't deliver showed a $62-billion deficit, against the $40-billion ceiling she'd promised. He announced his own resignation three weeks later.",
 found="Resignation letter, on the record.",
 him="Announced his resignation on January 6, 2025.",
 others="Freeland out; LeBlanc in as finance minister the same day.",
 cost="$61.9-billion deficit against a $40.1-billion guardrail.",
 label="Quit"),

"trudeau-resignation": dict(
 headline="With his own MPs demanding he go, he quit and prorogued Parliament to give the party time to replace him.",
 plain="By late 2024 at least two dozen Liberal MPs and three regional caucuses had told him to leave. Freeland's resignation followed. On January 6, 2025 he announced he would step down as leader and prime minister once a successor was chosen, and had Parliament prorogued until March 24: 'if I'm having to fight internal battles, I cannot be the best option in that election'. Mark Carney was sworn in on March 14, 2025.",
 found="Resigned.",
 him="Left office March 14, 2025.",
 others="Parliament closed from January 6 to March 24, 2025.",
 cost=None,
 label="Resigned"),

"prorogation-2025": dict(
 headline="Shut down Parliament for eleven weeks to run a leadership race. A court said that was within his power.",
 plain="The January 2025 prorogation kept Parliament closed from January 6 to March 24 while the Liberals picked a new leader. Two Nova Scotians backed by a legal-advocacy group sued. The chief justice of the Federal Court ruled in March 2025 that courts can review a prorogation, but that these applicants hadn't shown he'd crossed any constitutional line.",
 found="Federal Court: within his power. Upheld.",
 him="Nothing. Upheld.",
 others="Nothing.",
 cost=None,
 label="Upheld by court"),
}

# Plain names for the finding classes (tags and groups)
CLASS_PLAIN = {
    "critical":   "Broke the law, or ruled illegal",
    "warning":    "Audit or inquiry found fault",
    "proceeding": "Quit, forced out, or charged",
    "good":       "Investigated and cleared",
    "neutral":    "Admitted, on the record, or never investigated",
}

# Groups for the full list, in the order they appear (most damning first)
GROUPS = [
    ("law",      "Broke the ethics law",              "The ethics commissioner ruled the Conflict of Interest Act was broken. The Act has no penalty for any of it.",
                 lambda e: e["finding"]["result"] == "VIOLATION_FOUND"),
    ("court",    "Ruled illegal by the courts",        "Two courts, one matter. Still under appeal to the Supreme Court.",
                 lambda e: e["finding"]["result"] == "COURT_AGAINST_GOVERNMENT"),
    ("audit",    "Audits: money wasted, rules ignored", "Findings by the Auditor General of Canada.",
                 lambda e: e["finding"]["result"] == "AUDIT_ADVERSE"),
    ("inquiry",  "What the inquiries found",           "Public inquiries, security-cleared committees and officers of Parliament. Each label says what they found.",
                 lambda e: e["finding"]["result"] == "INQUIRY_FINDING"),
    ("promise",  "Promises broken",                    "Made in writing in 2015. Not delivered.",
                 lambda e: e["finding"]["result"] == "BROKEN_COMMITMENT"),
    ("exit",     "Quit, forced out, charged",          "Resignations, removals and criminal cases, with the outcome.",
                 lambda e: e["finding"]["result"] in ("RESIGNATION", "CHARGES", "CHARGES_STAYED")),
    ("admit",    "Admitted, apologized, reversed",     "On the record, in their own words. Nobody investigated.",
                 lambda e: e["finding"]["result"] == "ADMISSION"),
    ("never",    "Never investigated",                 "Reported by major outlets, answered by the people involved, examined by no one.",
                 lambda e: e["finding"]["result"] == "UNADJUDICATED"),
    ("cost",     "Costs on the record",                "No finding. The bill is the record.",
                 lambda e: e["finding"]["result"] == "RECORD"),
    ("cleared",  "Investigated and cleared",           "Looked at and found clean, or upheld by a court. Same weight as everything above.",
                 lambda e: e["finding"]["result"] in ("CLEARED", "COURT_FOR_GOVERNMENT")),
]
