# -*- coding: utf-8 -*-
"""Said vs. the record. Only statements with a date and a document behind them.
said: [{date, who, quote (verbatim) or said (paraphrase, no quote marks), src_title, src_url}]
record: what the evidence shows, plain."""

SAID = {

"aga-khan-vacation": dict(said=[
 dict(date="2017-01-10", who="Trudeau", quote="The Aga Khan has been a long-time family friend. He was a pallbearer for my father’s funeral. He has known me since I was a toddler. And this was our family vacation.", src_title="Global News, January 2017", src_url="https://globalnews.ca/news/3174207/justin-trudeau-conflict-of-interest-ethics-vacation-aga-khan/amp/"),
], record="The ethics commissioner found there had been no private interactions between the two men until Trudeau became Liberal leader, and that “their relationship cannot be described as one of friends for the purposes of the Act.” The friendship exception failed; four sections of the law were broken."),

"snc-lavalin-affair": dict(said=[
 dict(date="2019-02-07", who="Trudeau, Vaughan, Ont.", quote="The allegations in the Globe story this morning are false. Neither the current, nor the previous attorney general was ever directed by me or by anyone in my office to take a decision in this matter.", src_title="Canada’s National Observer, February 7, 2019", src_url="https://www.nationalobserver.com/2019/02/07/news/trudeau-denies-directing-wilson-raybould-intervene-prosecution-snc-lavalin"),
 dict(date="2019-08-14", who="Trudeau", said="Said he took responsibility for what happened and could not apologize “for standing up for Canadian jobs.”", src_title="Al Jazeera, August 15, 2019", src_url="https://www.aljazeera.com/news/2019/8/15/canadas-pm-trudeau-found-guilty-by-ethics-commissioner"),
], record="His denial used the word “directed.” The ethics commissioner found “there were many ways in which Mr. Trudeau, either directly or through the actions of those under his direction, sought to influence the Attorney General,” and that this broke section 9 of the Act."),

"we-charity": dict(said=[
 dict(date="2020-06-29", who="Trudeau", quote="When our public servants looked at the potential partners, only the WE organization had the capacity to deliver the ambitious program that young people need for the summer.", src_title="CBC News, June 29, 2020", src_url="https://www.cbc.ca/lite/story/1.5631278"),
 dict(date="2020-07-13", who="Trudeau", said="Apologized for not recusing himself from the decision and said he was “sincerely sorry.”", src_title="Global News, July 13, 2020", src_url="https://globalnews.ca/news/7170235/trudeau-apologizes-not-recusing-we-charity"),
 dict(date="2020-07-30", who="Trudeau, Finance committee", said="Testified that he had “pushed back” on the recommendation in May and let it proceed without recusing.", src_title="CBC News, July 30, 2020", src_url="https://www.cbc.ca/news/politics/trudeau-testimony-finance-committee-we-charity-scheer-1.5668889"),
], record="Cabinet approved WE on May 22, 2020 with Trudeau and Morneau at the table. The ethics commissioner cleared Trudeau because his relatives’ fees were not legally his “private interest,” and found Morneau broke the law three ways over the same decision. In July 2026 the Supreme Court sent the Trudeau clearance back to the courts for review."),

"emergencies-act-2022": dict(said=[
 dict(date="2022-02-14", who="Trudeau", said="Said the measures “will be time-limited, geographically targeted, as well as reasonable and proportionate to the threats they are meant to address.”", src_title="PBS NewsHour / Associated Press, February 14, 2022", src_url="https://www.pbs.org/newshour/amp/world/canadian-prime-minister-trudeau-invokes-emergency-powers-to-quell-covid-restriction-protests"),
 dict(date="2024-01-23", who="Freeland, after the Federal Court ruling", quote="We believed we were doing something necessary and something legal at the time. That continues to be my belief today.", src_title="CBC News, January 23, 2024", src_url="https://www.cbc.ca/lite/story/1.7091891"),
], record="Federal Court: no national emergency existed; the decision was “unreasonable and ultra vires”; the account freezes breached the Charter. Federal Court of Appeal, January 2026: the government “did not demonstrate that it had reasonable grounds to believe that a threat to national security or a national emergency existed,” and the freezing process was “ad hoc and fraught with confusion.”"),

"india-trip-atwal": dict(said=[
 dict(date="2018-02-27", who="Trudeau, House of Commons", quote="When one of our top diplomats and security officials says something to Canadians it’s because they know it to be true.", src_title="CBC News, February 27, 2018", src_url="https://www.cbc.ca/lite/story/1.4553946"),
], record="The security-cleared committee of parliamentarians found the adviser briefed reporters “under difficult circumstances,” consulted no department first, and told the committee himself that he should have spoken on the record. It found the PMO “should have more properly addressed” its own failure to screen invitees. Its findings on Indian involvement are redacted."),

"julie-payette": dict(said=[
 dict(date="2020-09-02", who="Trudeau, RED FM interview", quote="We have an excellent governor general right now and I think on top of the COVID crisis, nobody is looking at any constitutional crises.", src_title="Global News, September 2, 2020", src_url="https://globalnews.ca/news/7311912/justin-trudeau-defends-julie-payette/amp"),
], record="The independent review his own Privy Council Office commissioned found she “belittled, berated and publicly humiliated” staff in a “toxic, verbally abusive workplace.” She resigned four and a half months after he called her excellent."),

"trans-mountain": dict(said=[
 dict(date="2018-05-29", who="Department of Finance, announcing the purchase", quote="It is not, however, the intention of the Government of Canada to be a long-term owner of this project.", src_title="Department of Finance Canada, May 29, 2018", src_url="https://www.canada.ca/en/department-finance/news/2018/05/agreement-reached-to-create-and-protect-jobs-build-trans-mountain-expansion-project0.html"),
], record="Eight years on, Ottawa still owns it. The Parliamentary Budget Officer says a sale at current valuations records a loss."),

"trudeau-resignation": dict(said=[
 dict(date="2024-10-24", who="Trudeau, after the caucus meeting", said="Told reporters he would stay on as leader and take the Liberals into the next election.", src_title="CBC News, October 24, 2024", src_url="https://www.cbc.ca/news/politics/trudeau-staying-on-as-leader-1.7362000"),
 dict(date="2025-01-06", who="Trudeau", quote="This country deserves a real choice in the next election, and it’s become clear to me that if I’m having to fight internal battles, I cannot be the best option in that election.", src_title="CBC News, January 6, 2025", src_url="https://www.cbc.ca/news/politics/trudeau-news-conference-1.7423680"),
], record="Resigned 74 days after saying he would stay."),

"access-to-information-decline": dict(said=[
 dict(date="2015-10", who="Liberal platform, p. 24", quote="Government data and information should be open by default, in formats that are modern and easy to use. […] We will update the Access to Information Act to meet this standard.", src_title="Real Change (2015 platform)", src_url="https://liberal.ca/wp-content/uploads/sites/292/2020/09/New-plan-for-a-strong-middle-class.pdf"),
], record="The Act was amended once, in 2019. In 2023 the Information Commissioner reported the system “no longer serves its intended purpose” and that transparency was “not a priority for the government.”"),

"freeland-resignation": dict(said=[
 dict(date="2023-11-21", who="Freeland, Fall Economic Statement", said="Committed to keeping the 2023–24 deficit at or below the spring budget’s $40.1 billion.", src_title="Global News, November 21, 2023", src_url="https://globalnews.ca/news/10106753/fall-economic-statement-2023-deficit"),
 dict(date="2024-12-16", who="Freeland, resignation letter", quote="That means eschewing costly political gimmicks, which we can ill afford.", src_title="Yahoo Finance Canada, December 16, 2024", src_url="https://ca.finance.yahoo.com/news/chrystia-freeland-sends-resignation-letter-to-trudeau-calls-out-costly-political-gimmicks-162749861.html"),
], record="The 2023–24 deficit came in at $61.9 billion, $21.8 billion over her own ceiling."),

"michael-chong-zhao-wei": dict(said=[
 dict(date="2023-05", who="Trudeau", said="Said CSIS had decided the report did not meet “a threshold that required them to pass it up – up out of CSIS.”", src_title="Foreign Interference Commission, Final Report Vol. 4", src_url="https://foreigninterferencecommission.ca/fileadmin/PIFI_-_Final_Report_Vol._4__2025_.pdf"),
], record="The inquiry found CSIS sent the intelligence to the Public Safety minister’s office in May 2021 specifically to make him aware of it, and that “the information never reached the Minister.” It left CSIS. It stalled inside the government."),

"tofino-truth-reconciliation-day": dict(said=[
 dict(date="2021-09-30", who="Prime Minister’s Office, public itinerary", said="Listed “private meetings” in Ottawa.", src_title="Global News, October 6, 2021", src_url="https://globalnews.ca/news/8247262/trudeau-tofino-truth-reconciliation-apology-mistake"),
 dict(date="2021-10-06", who="Trudeau", quote="Travelling on September 30th was a mistake, and I regret it.", src_title="Global News, October 6, 2021", src_url="https://globalnews.ca/news/8247262/trudeau-tofino-truth-reconciliation-apology-mistake"),
], record="He was in Tofino. The itinerary was corrected after Global News asked."),

"blackface-images": dict(said=[
 dict(date="2019-09-18", who="Trudeau", quote="I shouldn’t have done that. I should have known better… I’m really sorry.", src_title="CBC News, September 18, 2019", src_url="https://amp.cbc.ca/lite/story/1.5289165"),
 dict(date="2019-09-19", who="Trudeau, Winnipeg", said="Asked how many times he had worn blackface or brownface, said he could not say definitively.", src_title="PBS NewsHour / Associated Press, September 19, 2019", src_url="https://www.pbs.org/newshour/amp/world/canadian-prime-minister-justin-trudeau-apologizes-for-2001-brownface-photo"),
], record="He acknowledged two instances on the 18th. A third surfaced on video on the 19th."),

"kokanee-summit-allegation": dict(said=[
 dict(date="2018-07-01", who="Trudeau", quote="I remember that day in Creston well… I don’t remember any negative interactions that day at all.", src_title="Vice, July 6, 2018", src_url="https://www.vice.com/en/article/the-woman-who-accused-trudeau-of-groping-speaks-out/"),
 dict(date="2018-07-05", who="Trudeau", said="Said he was “confident I did not act inappropriately” and that a woman, “particularly in a professional context, can experience it differently.”", src_title="Vice, July 6, 2018", src_url="https://www.vice.com/en/article/the-woman-who-accused-trudeau-of-groping-speaks-out/"),
], record="The reporter, July 6, 2018: “The incident referred to in the editorial did occur, as reported… Mr. Trudeau did apologize the next day.”"),

"mark-norman-prosecution": dict(said=[
 dict(date="2018-02-02", who="Trudeau, Edmonton town hall", said="Said the matter would “inevitably” lead to “court processes.” No charge existed; the RCMP laid one a month later.", src_title="CBC News, February 2, 2018", src_url="https://www.cbc.ca/lite/story/1.4516573"),
 dict(date="2019-05-08", who="Trudeau", quote="The process involved in a public prosecution like this is entirely independent of my office.", src_title="Global News, May 8, 2019", src_url="https://globalnews.ca/news/5253178/mark-norman-charges-dropped"),
], record="The Crown stayed the charge: “There is no reasonable prospect of conviction.” The House of Commons apologized to Norman unanimously."),

"sajjan-operation-medusa": dict(said=[
 dict(date="2017-04-18", who="Sajjan, New Delhi", quote="I became the architect of an operation called Operation Medusa, where we removed about 1,500 fighters, Taliban fighters, off the battlefield.", src_title="The Globe and Mail, April 2017", src_url="https://www.theglobeandmail.com/news/national/defence-minister-sajjan-apologizes-for-claiming-he-was-architect-of-operation-medusa/article34858041/"),
 dict(date="2017-04-29", who="Sajjan", quote="I made a mistake in describing my role. I wish to retract that description and apologize for it. I am truly sorry.", src_title="The Globe and Mail, April 2017", src_url="https://www.theglobeandmail.com/news/national/defence-minister-sajjan-apologizes-for-claiming-he-was-architect-of-operation-medusa/article34858041/"),
], record="Operation Medusa was commanded by Brig.-Gen. David Fraser. Sajjan was a reservist intelligence liaison."),

"vance-allegations-2018": dict(said=[
 dict(date="2021-03", who="Sajjan", said="Said any allegations were “very quickly put forward to the proper authorities.”", src_title="Global News, March 3, 2021", src_url="https://globalnews.ca/news/7673801/vance-investigation-walbourne-testify"),
 dict(date="2021-05-07", who="Katie Telford, chief of staff", quote="We didn’t know the nature of the allegation.", src_title="Global News, May 7, 2021", src_url="https://globalnews.ca/news/7842824/canadian-forces-sexual-misconduct-justin-trudeau-katie-telford"),
], record="The ombudsman, under oath: “I reached into my pocket to show him the evidence I was holding. He pushed back from the table and said, No.” Vance stayed in command until 2021 and later pleaded guilty to obstructing justice."),

"mendicino-police-request-claim": dict(said=[
 dict(date="2022-04", who="Mendicino, parliamentary committee", quote="The advice we received was to invoke the Emergencies Act.", src_title="CTV News, June 7, 2022", src_url="https://www.ctvnews.ca/politics/mendicino-was-misunderstood-in-saying-police-asked-for-emergencies-act-deputy-minister-1.5937524"),
 dict(date="2022-06-07", who="Rob Stewart, his deputy minister", quote="I believe that the intention that he was trying to express was that law enforcement asked for the tools that were contained in the Emergencies Act.", src_title="CTV News, June 7, 2022", src_url="https://www.ctvnews.ca/politics/mendicino-was-misunderstood-in-saying-police-asked-for-emergencies-act-deputy-minister-1.5937524"),
], record="The RCMP commissioner and Ottawa’s interim police chief testified they never asked for the Act. The commissioner’s email to his office the day before invocation said police had not yet exhausted the tools they already had."),

"mendicino-bernardo-transfer": dict(said=[
 dict(date="2023-06", who="Mendicino", said="Said he learned of the transfer only after it happened and called it “shocking and incomprehensible.”", src_title="The Globe and Mail, June 2023", src_url="https://www.theglobeandmail.com/canada/article-corrections-head-questioned-how-mendicino-was-kept-in-dark-over/"),
], record="Correctional Service Canada: his office was notified in early March and again in late May; the Prime Minister’s Office was briefed the day of the move."),

"jamaica-vacation": dict(said=[
 dict(date="2023-12", who="Prime Minister’s Office", said="Said the family was covering the cost of the stay.", src_title="The Canadian Press, January 3, 2024", src_url="https://lethbridgenewsnow.com/2024/01/03/pmo-clarifies-trudeau-and-family-stayed-at-no-cost-during-vacation-in-jamaica/"),
 dict(date="2024-01-03", who="Prime Minister’s Office", said="Said the family stayed “at no cost at a location owned by family friends.”", src_title="The Canadian Press, January 3, 2024", src_url="https://lethbridgenewsnow.com/2024/01/03/pmo-clarifies-trudeau-and-family-stayed-at-no-cost-during-vacation-in-jamaica/"),
 dict(date="2024-01", who="Prime Minister’s Office", said="Then said the family stayed “with family friends, rather than at a location owned by the friends.”", src_title="Global News, January 30, 2024", src_url="https://globalnews.ca/news/10259902/justin-trudeau-jamaica-trip-committee"),
], record="The ethics commissioner had cleared the trip in advance: “They consulted us. We gave advice. They went to Jamaica.” On the three descriptions: “I’m not responsible for the spokesman of the prime minister and the way he characterizes our interaction.”"),

"boissonnault-global-health-imports": dict(said=[
 dict(date="2018", who="Boissonnault", said="Described himself as “non-status adopted Cree.” The Liberal Party listed him as Indigenous.", src_title="The Canadian Press via CP24, November 20, 2024", src_url="https://www.cp24.com/news/canada/2024/11/20/randy-boissonnault-leaves-liberal-cabinet-after-shifting-indigenous-identity-claims/"),
 dict(date="2024-11", who="Boissonnault", said="Said his adoptive mother and brother are Métis, and apologized.", src_title="The Canadian Press via CP24, November 20, 2024", src_url="https://www.cp24.com/news/canada/2024/11/20/randy-boissonnault-leaves-liberal-cabinet-after-shifting-indigenous-identity-claims/"),
], record="His former company described itself as “wholly Indigenous-owned” in federal bids and was barred from contracts until 2030. On the “Randy” texts, the ethics commissioner found no evidence he was running the company and closed the file."),

"electoral-reform": dict(said=[
 dict(date="2015-10", who="Liberal platform, p. 27", quote="We are committed to ensuring that 2015 will be the last federal election conducted under the first-past-the-post voting system.", src_title="Real Change (2015 platform)", src_url="https://liberal.ca/wp-content/uploads/sites/292/2020/09/New-plan-for-a-strong-middle-class.pdf"),
 dict(date="2017-02-01", who="Trudeau, mandate letter to the Minister of Democratic Institutions", quote="Changing the electoral system will not be in your mandate.", src_title="Prime Minister of Canada, February 1, 2017", src_url="https://www.pm.gc.ca/en/mandate-letters/2017/02/01/archived-minister-democratic-institutions-mandate-letter"),
 dict(date="2025-01-06", who="Trudeau", quote="I do wish that we’d been able to change the way we elect our governments in this country so that people could simply choose a second choice or a third choice on the same ballot.", src_title="CBC News, January 7, 2025", src_url="https://amp.cbc.ca/lite/story/1.7426407"),
], record="Three elections since, all under first past the post."),

"fiscal-record-2015-promise": dict(said=[
 dict(date="2015-10", who="Liberal platform", said="Promised deficits “of less than $10 billion in each of the next two fiscal years” and a “balanced budget in 2019.”", src_title="Real Change (2015 platform)", src_url="https://liberal.ca/wp-content/uploads/sites/292/2020/09/New-plan-for-a-strong-middle-class.pdf"),
], record="Deficits of $19 billion, $19 billion and $14 billion in the three years before the pandemic, then $39 billion in 2019–20. No balanced budget in any year of the tenure."),

"carbon-charge-heating-oil": dict(said=[
 dict(date="2023-10-26", who="Trudeau", quote="We are nothing if not a government that listens to people, that is focused on our goals and is willing to adjust as necessary.", src_title="Global News, October 26, 2023", src_url="https://globalnews.ca/news/10051832/trudeau-affordability-heating-oil-carbon-price"),
 dict(date="2023-10-29", who="Gudie Hutchings, minister, on CTV", quote="Perhaps they need to elect more Liberals in the Prairies so that we can have that conversation as well.", src_title="CTV News, October 29, 2023", src_url="https://www.ctvnews.ca/politics/prairies-should-elect-more-liberals-if-they-want-voices-heard-on-carbon-pricing-rural-economic-development-minister-1.6621490"),
 dict(date="2023-11-01", who="Trudeau", quote="There will absolutely not be any other carve-outs or suspensions of the price on pollution.", src_title="The Canadian Press, November 1, 2023", src_url="https://www.620ckrm.com/2023/11/01/absolutely-not-no-more-carve-outs-when-it-comes-to-carbon-pricing-trudeau-says/"),
], record="The pause applied to heating oil only, the fuel used mostly in Atlantic Canada. Saskatchewan stopped remitting the charge on natural gas in response. The consumer charge was abolished altogether in April 2025."),

"foreign-interference-response": dict(said=[
 dict(date="2022-11-20", who="Trudeau", quote="I do not have any information, nor have I been briefed on any federal candidates receiving any money from China.", src_title="Global News, November 20, 2022", src_url="https://globalnews.ca/news/9293238/justin-trudeau-china-interference-allegations"),
], record="On that point the inquiry backed him: “there is no intelligence that the $250,000 went to any of the 11 candidates.” On the government as a whole it found it “has sometimes taken too long to act” and was “a poor communicator and insufficiently transparent when it comes to foreign interference.”"),

"morneau-we-charity": dict(said=[
 dict(date="2020-07-22", who="Morneau", said="Said he had believed the costs of his family’s WE trips were already paid. He repaid $41,366 that day.", src_title="House of Commons ETHI Report 2, p. 51", src_url="https://www.ourcommons.ca/documentviewer/en/43-2/ETHI/report-2/page-51"),
], record="The ethics commissioner found he gave WE “preferential treatment,” made a decision while in a conflict of interest and failed to recuse. Three sections broken."),

"butts-telford-moving-expenses": dict(said=[
 dict(date="2016-09-22", who="Gerald Butts and Katie Telford", quote="While the rules were clear and we followed them, we both know that’s not always enough.", src_title="CBC News, September 22, 2016", src_url="https://amp.cbc.ca/lite/story/1.3774979"),
], record="They repaid $65,000 of the $207,000. The rest stayed paid."),

"sajjan-afghan-sikhs": dict(said=[
 dict(date="2024-07-03", who="Sajjan", said="Said he passed on information, never ordered the operation, and did not prioritize Sikhs above others.", src_title="CBC News, July 3, 2024", src_url="https://www.cbc.ca/news/politics/sajjan-relayed-information-sikhs-in-afghanistan-1.7248417"),
], record="Three military sources told the Globe he “instructed Canadian special forces to rescue about 225 Afghan Sikhs” and relayed their location. No body has examined it."),
}
