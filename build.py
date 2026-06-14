#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE GOODS: LIVE HARD, SELL HARD (GDS) — Neal Brennan's 2009 comedy, catalogued into UD0 as the
FIFTEENTH film-world. Read PARABOLICALLY (David's ask): the parable under the raunch. Standing template;
deep-dive = THE PARABLE. CARBONS (cast +.shadow) and SYNTHS = the PARABOLIC TROPES (the close, the
rootless man, wanting-something-real, etc.). Self-contained. HANDLES the film's most offensive bit
HONESTLY: the Pearl-Harbor mob-beating of Ken Jeong's Teddy Dang — named critically in Real-or-Fluff +
a content note (JACL & MANAA condemned it, tying it to the 1982 murder of Vincent Chin); the 'it's satire'
defense is weak because the laugh IS the assault. Facts web-verified: Paramount Vantage, Aug 14 2009; dir
Neal Brennan (Chappelle's Show co-creator, feature debut); Gary Sanchez (McKay & Ferrell) prod; Don 'The
Goods' Ready leads mercenary 'liquidators' to save failing SELLECK MOTORS in Temecula CA over July 4th
(move ~211 cars in 3 days); Ed Helps's Paxton fronts a 'MAN band' (not boy band — the joke); Babs (Hahn)
lusts after Peter Selleck (Riggle), a 10-yr-old in a man's body; Will Ferrell cameos as CRAIG McDERMOTT
(dies: sex toys packed instead of a parachute); ~$15.3M ww on ~$10M, RT 27% but Ebert 3/4. Kathryn Hahn
through-line: LMZ Naomi -> GDS Babs."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "GDS"
REC = {
 "name": "THE GOODS", "axiom": AX,
 "position": "The Goods: Live Hard, Sell Hard · Paramount Vantage (Gary Sanchez) · 2009 — dir. Neal Brennan",
 "origin": "Selleck Motors, Temecula, California — a failing car lot over a Fourth of July weekend",
 "mechanism": "Crystallized from the film — a raunchy hustle-comedy with a buried parable: a mercenary 'liquidator' who can sell anything is hired to save a dying dealership, and discovers that a life of closing and moving on has left him with nothing of his own to want.",
 "crystallization": "Because under the blowout-sale chaos is a real idea about hyper-capitalism — that the skill of making people want what they don't need can hollow out the salesman's own capacity to want anything real.",
 "nature": "The Goods — the salesman's parable: the close as seduction, the rootless closer, the dream-girl who is a home, and a comedy that too often didn't know when the sale wasn't worth the cost.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (2009, dir. Neal Brennan; Gary Sanchez / Paramount Vantage); the used-car-lot Americana it satirizes; the real critical record (incl. the condemnation of its worst gag)",
 "witness": "A man who can sell anything has nothing of his own — until a dying lot and a woman named Ivy teach him to stop closing and start staying.",
 "role": "the fifteenth film-world of UD0",
 "seal": "A man who can sell anything has nothing of his own — until he learns to stop closing and start staying. A real parable about wanting a home, inside a comedy whose worst gag it never should have made.",
 "source": "The Goods: Live Hard, Sell Hard (2009), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#c4a85a", "flesh-and-blood — the lot's people: the liquidator crew, the Selleck family, the rival, the salesmen; the humans inside the hustle"),
 "ethereal":  ("#6fb8e0", "the real thing wanted — Ivy, and the home and roots Don has never let himself have; the dream under the deal"),
 "electrical":("#ffce00", "the machinery of the sell — the liquidators, the close, the blowout lot, the Fourth-of-July hustle; salesmanship as a system"),
 "spiritual": ("#e2241a", "the soul & the wound — the rootless closer, the partner he got killed, and the turn from closing to staying; the grief and the redemption",),
}

ARC_OVERALL = ("Don 'The Goods' Ready leads a team of mercenary car 'liquidators' — closers hired to descend on a dying "
  "dealership and move its inventory by any means necessary. Their latest job: save Ben Selleck's failing lot, Selleck "
  "Motors in Temecula, over a Fourth of July weekend — sell roughly 211 cars in three days or the rival dealership takes "
  "over. As Don runs his usual blitz of stunts and seductions, he falls for Ben's daughter Ivy, and a man who has spent his "
  "whole life closing and driving to the next town finds himself, for the first time, wanting to stay.")
ARC = [
 ("I · the liquidators arrive", "sell 211 cars in three days",
  "Don Ready and his crew — Jibby, Brent, Babs — roll into the failing Selleck Motors to do what they do: a mercenary three-day blitz of stunts, lies, and hard closes to move the inventory and collect their cut before driving on to the next dying lot."),
 ("II · the blitz, and Ivy", "the close meets the real thing",
  "The hustle escalates — the rival Paxton, the man-child Peter, the chaos of the sale — while Don, the rootless closer, unexpectedly falls for Ivy Selleck. The skill that makes him able to sell anyone anything starts to feel like the thing keeping him from wanting anything true."),
 ("III · stop closing, start staying", "the salesman wants a home",
  "Haunted by the partner he got killed and pulled toward Ivy and the Sellecks, Don makes the turn the parable is built for: he stops closing and starts staying. The lot is saved, but the real sale is the one he finally makes to himself — that a home is worth more than the next deal."),
]

# THE PARABLE — the deep-dive (the parabolic reading of the comedy)
PARABLE = [
 ("The close as seduction", "selling is making people want",
  "The film's engine is also its parable: the close. Don Ready can make anyone want anything — and the movie quietly understands that salesmanship is a form of seduction, the manufacture of desire for things people don't need. Every hard sell on the lot is a small study in how wanting is engineered, which is why the comedy keeps brushing up against something colder underneath the gags."),
 ("The rootless closer", "good at selling, owning nothing",
  "Don is the parable's center: a man so good at closing and moving on that he's rooted to nothing and haunted by the partner his recklessness got killed. The trope is the cost of the skill — that the person who can make everyone else want what they don't have ends up unable to want anything real for himself. Mastery of desire as a kind of poverty."),
 ("Ivy, and wanting something real", "the turn from closing to staying",
  "The redemption is small and almost sweet: Don falls for Ivy Selleck and, for the first time, wants to STAY rather than sell-and-leave. The dream-girl arc is really the parable's hinge — the mercenary learning that a home and roots are worth more than the next deal. The opposite of the close is the choice to remain when the deal is done."),
 ("Patriotic capitalism", "the Fourth-of-July blowout",
  "Setting the hustle on a Fourth of July weekend is the film's sharpest parabolic move: selling as Americana, the flag-draped blowout sale as a national rite. The lot's bunting and balloons frame consumer appetite as patriotism — the parable that buying and selling have become the country's holiday, and the salesman its strange priest."),
 ("The gag it never should have made", "where the comedy fails its own parable",
  "Honesty requires naming the failure. The film stages a scene in which a Pearl-Harbor war-speech incites a mob to beat an Asian-American character (Teddy Dang) as a punchline — a bit the Japanese American Citizens League and MANAA condemned on release, explicitly invoking the 1982 racist murder of Vincent Chin. The 'it's satire' defense is weak, because the energy of the joke is the assault itself. A parable about the cost of the sale, made by a film that didn't always know when a laugh wasn't worth the cost."),
]
REALFLUFF = [
 ("Under the raunch, it's about a rootless con-man learning to want something real", "REAL", "the Don/Ivy arc — a closer haunted by a dead partner who finally wants a home over the next deal — is a genuine, almost poignant through-line"),
 ("The Pearl-Harbor mob-beating of Teddy Dang is 'satire that punches up'", "FALSE", "the film's most indefensible bit — the JACL and MANAA condemned it, tying it to the 1982 murder of Vincent Chin; the laugh is the racist assault itself, and the satire defense doesn't hold"),
 ("Will Ferrell's cameo character is named Stu", "FALSE", "he's Craig McDermott, Don's late partner, who dies when Don packs sex toys instead of a parachute for a skydive — the grief Don runs from"),
 ("Babs's romance with Peter Selleck is deliberately uncomfortable", "REAL", "Peter is canonically a 10-year-old with a growth condition in a grown man's body; Babs's pursuit of him is the gag, and the discomfort is the point"),
 ("It was a box-office hit", "FALSE", "modest — about $15M worldwide on a ~$10M budget; RT 27%, mixed-to-negative, with a cult-ish afterlife"),
 ("Ed Helms fronts a boy band", "HALF", "the joke is that Paxton insists 'it's not a boy band, it's a MAN band' (they opened for O-Town) — getting it 'wrong' is in-character"),
 ("Neal Brennan, the Chappelle's Show co-creator, directed it", "REAL", "his feature directorial debut, produced by Gary Sanchez (Adam McKay & Will Ferrell)"),
 ("Critics universally panned it, Ebert included", "HALF", "reviews skewed negative (RT 27%), but Roger Ebert was a defender, giving it 3 of 4 stars"),
]
REALFLUFF_VERDICT = ("Bottom line: The Goods has a real, even poignant parable buried in it — a rootless closer, so good at making people "
  "want things that he can't want anything of his own, learning from a dying lot and a woman named Ivy to stop closing and start "
  "staying. Piven's motormouth liquidator and that Don/Ivy turn are the genuine article. But the film also contains some of the "
  "most indefensible comedy of its era, chief among it a scene that stages a racist mob beating of an Asian-American character "
  "as a punchline — a bit that real advocacy organizations (the JACL, MANAA) condemned by name on release, invoking the 1982 "
  "murder of Vincent Chin, and that the 'it's just satire' defense does not save, because the energy of the joke is the assault. "
  "Hold both honestly: a salesman learning to want a home, inside a comedy that too often didn't know when the laugh wasn't "
  "worth the cost. Take the parable seriously; don't launder the worst of the jokes.")

MESSAGE = ("The Goods is a parable about the cost of being good at selling. Don Ready can sell anyone anything — which means he's "
  "spent his whole life closing deals and driving to the next town, rooted to nothing and haunted by the partner his "
  "recklessness got killed. The hustle-comedy surface — move 211 cars in three days or the lot dies — is, underneath, a parable "
  "about hyper-capitalism: that the skill of making people want what they don't need eventually hollows out the salesman's own "
  "capacity to want anything real. Don's arc is learning to stop closing and start staying — to want Ivy, and a home, more than "
  "the next sale. That's the genuine, almost sweet thing under the raunch. But honesty requires naming the rest: the movie also "
  "contains some of the most indefensible comedy of its era — above all a scene that stages a racist mob beating of an "
  "Asian-American character as a punchline, a bit the Japanese American Citizens League and MANAA condemned on release, "
  "invoking the 1982 murder of Vincent Chin. The 'it's satire' defense is weak, because the energy of the joke is the beating "
  "itself. So the parable is real and the failure is real, and the grown-up way to hold the film is to take both seriously: a "
  "closer learning to want a home, inside a comedy that too often forgot when the sale wasn't worth the cost.")
MESSAGE_SEAL = "A man who can sell anything has nothing of his own — until he learns to stop closing and start staying. A real parable about wanting a home, inside a comedy whose worst gag — a racist mob beating, condemned on release — it never should have made."

SECTIONS = [
 ("The Production", "Neal Brennan's hustle-comedy", [
   ("Neal Brennan", "director (feature debut)", "co-creator of Chappelle's Show, making his feature directorial debut on a Gary Sanchez (Adam McKay & Will Ferrell) production"),
   ("Paramount Vantage · Aug 14, 2009", "studio & release", "a modest performer — about $15M worldwide on a ~$10M budget — that drew mixed-to-negative reviews (RT 27%) and a cult-ish following (Ebert a defender, 3/4)"),
   ("the cast", "the liquidators & the lot", "Jeremy Piven, Ving Rhames, David Koechner, Kathryn Hahn as the crew; James Brolin, Jordana Spiro, Rob Riggle as the Sellecks; Ed Helms as the rival; Will Ferrell cameos as the late Craig McDermott"),
   ("the through-line", "Kathryn Hahn, again", "Hahn (Babs) also plays Naomi in UD0's The Last Mimzy — one of the actor through-lines threading the film-worlds together"),
 ]),
 ("The Lot", "Selleck Motors, Fourth of July", [
   ("Selleck Motors · Temecula, CA", "the failing dealership", "Ben Selleck's family lot, the home-at-stake the liquidators are hired to save over the holiday weekend"),
   ("sell 211 in three days", "the mercenary job", "the liquidators' contract: move the inventory or the rival takes the lot — the hustle that frames the parable"),
   ("the Man Band", "Paxton's rival", "Ed Helms's Paxton Harding fronts a band he insists 'is not a boy band, it's a MAN band' (they opened for O-Town) — the antagonist's running gag"),
   ("a content note", "the film's worst bit", "the Pearl-Harbor mob-beating gag is named honestly in Real-or-Fluff and The Parable — condemned by the JACL and MANAA, tied to the murder of Vincent Chin; commentary, never endorsement"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast, each +.shadow real-life User ──
 E("don-ready","Don Ready","carbon","spiritual","the closer who can't keep anything",
   "Don 'The Goods' Ready — the legendary mercenary car liquidator who can sell anyone anything, and owns nothing of his own.",
   "The parable's center: a man so good at manufacturing desire that he's lost the ability to want, until a dying lot and Ivy teach him to stay.",
   "On the lot, mid-pitch, then unexpectedly unwilling to leave.",
   "Because the film is, underneath, about the cost of the close — and Don is the cost made human.",
   "By blitzing the sale, falling for Ivy, facing the partner he got killed, and choosing to stop closing.",
   "I can sell you anything. That's the problem — I've sold everything, kept nothing, and I'm finally tired of driving away.",
   actor="Jeremy Piven", analog="the rootless closer — mastery of desire as a kind of poverty"),
 E("ivy-selleck","Ivy Selleck","carbon","ethereal","the home he comes to want",
   "Ivy Selleck — Ben's daughter, the woman Don falls for, and the parable's hinge from closing to staying.",
   "The real thing wanted: not a mark to close but a person to remain for — the dream-girl who is, parabolically, a home.",
   "At the lot she's trying to save, becoming the reason Don might not leave.",
   "Because the redemption needs an object that can't be sold — and Ivy is what Don finally wants for real.",
   "By seeing the man under the pitch and giving him something the next town never could: a reason to stay.",
   "He's the best salesman alive. I'm the first thing he ever wanted that he couldn't talk himself out of.",
   actor="Jordana Spiro", analog="the unclosed want — the home at the end of the hustle"),
 E("jibby-newsome","Jibby Newsome","carbon","natural","the crew",
   "Jibby Newsome — a veteran of Don's liquidator crew, part of the mercenary band that descends on dying lots.",
   "The hustle made plural: proof that the close is a culture, a traveling crew that sells and moves on together.",
   "On every lot, beside Don, working the floor.",
   "Because the parable's machine is a team, and Jibby is its seasoned hand.",
   "By running the blitz with Don, town after town, sale after sale.",
   "We roll in, we move the metal, we roll out. That's the life. Don's the one who started wanting more than that.",
   actor="Ving Rhames", analog="the road crew — the close as a way of life"),
 E("brent-gage","Brent Gage","carbon","natural","the crew",
   "Brent Gage — another of Don's liquidators, part of the mercenary sales team's chaos and camaraderie.",
   "The ensemble of the hustle: the crew whose loyalty is real even as the job is a con.",
   "On the lot, in the motel, in the next town over.",
   "Because the liquidators are a found-family of closers, and Brent is one of them.",
   "By selling hard alongside Don and living the rootless road with him.",
   "Live hard, sell hard, leave hard. We're good at all three — Don's the one who got tired of the leaving.",
   actor="David Koechner", analog="the fellow closer — camaraderie inside the con"),
 E("babs-merrick","Babs Merrick","carbon","natural","the crew (and the uncomfortable gag)",
   "Babs Merrick — the lone woman of Don's crew, whose subplot is a deliberately uncomfortable obsession with the man-child Peter Selleck.",
   "The crew's wild card, and the vehicle of one of the film's most awkward-by-design bits.",
   "On the lot and fixated, uneasily, on Peter.",
   "Because the comedy courts discomfort, and Babs's storyline is built to unsettle.",
   "By pursuing Peter — a 10-year-old in a grown man's body — as the gag the film knows is wrong.",
   "I'm the closer who fell for the wrong mark. The joke's supposed to make you squirm — and it does.",
   actor="Kathryn Hahn", analog="the crew's wild card — also UD0's Naomi in The Last Mimzy"),
 E("ben-selleck","Ben Selleck","carbon","natural","the lot at stake",
   "Ben Selleck — the owner of the failing Selleck Motors, who hires the liquidators to save his family dealership.",
   "The home on the line: the decent man whose lot — and family livelihood — the whole hustle is meant to rescue.",
   "Behind the desk of a dealership running out of time.",
   "Because the parable needs real stakes — a family business that the cynical sale might actually save.",
   "By gambling his struggling lot on a crew of mercenary closers as a last resort.",
   "Forty years I built this lot. I hired the sharks because the alternative was losing all of it. Save it. Please.",
   actor="James Brolin", analog="the honest owner — the home the hustle is meant to save"),
 E("peter-selleck","Peter Selleck","carbon","natural","the man-child",
   "Peter Selleck — Ben's son, canonically a 10-year-old with a growth condition that gives him the body of a grown man.",
   "The film's strangest gag: a literal child in an adult's frame, and the unwilling object of Babs's pursuit.",
   "Around the lot, treated as a grown man he isn't.",
   "Because the comedy's discomfort runs through Peter, the child no one can see as one.",
   "By being a ten-year-old everyone, including Babs, mistakes for a man.",
   "I'm ten. Everybody forgets, because of how I look — and the movie builds a whole uncomfortable joke on forgetting it.",
   actor="Rob Riggle", analog="the man-child — the gag of a child unseen"),
 E("paxton-harding","Paxton Harding","carbon","natural","the Man Band rival",
   "Paxton Harding — the rival, engaged to Ivy, who fronts a band he insists 'is not a boy band, it's a MAN band.'",
   "The antagonist as vanity: smooth, insecure, and defined by a single defensive running gag.",
   "At the rival dealership and at Ivy's side, until Don upends both.",
   "Because the hustle needs a foil, and Paxton's wounded-vanity 'Man Band' is it.",
   "By standing between Don and Ivy and the lot, all confidence and no substance.",
   "It is NOT a boy band. It's a MAN band. We opened for O-Town. …and yes, Don Ready took everything from me anyway.",
   actor="Ed Helms", analog="the vain rival — confidence with nothing under it"),
 E("teddy-dang","Teddy Dang","carbon","natural","the target of the film's worst bit",
   "Teddy Dang — a salesman on the lot, and the Asian-American character the film makes the target of its most indefensible scene.",
   "Named honestly, not as a joke: the figure a Pearl-Harbor war-speech incites a mob to beat — a bit condemned on release.",
   "On the sales floor, then assaulted in the scene the movie should not have made.",
   "Because honesty about this film means naming, and not laundering, the cruelty aimed at him.",
   "By being conflated with a wartime enemy and beaten as a punchline — the gag the JACL and MANAA condemned.",
   "The film turned me into a punchline for a racist beating, and real people called it out by name. I am where the comedy failed.",
   actor="Ken Jeong", analog="the target of the indefensible gag — named, not endorsed"),

 # ── SYNTHS — the PARABOLIC TROPES (no single User) ──
 E("the-close","The Close","synth","electrical","selling as seduction",
   "The Close — the trope at the engine of the film: salesmanship as the manufacture of desire, the art of making people want.",
   "The parable's mechanism: every hard sell is a small study in how wanting is engineered, the seduction under the comedy.",
   "On every pitch, every lot, every mark.",
   "Because the film's deepest idea is that selling is making people want what they don't need — and the close is that idea.",
   "By turning charm into commerce, desire into a deal, again and again.",
   "I am the art of making you want it. Master me and you can sell anything — and slowly stop being able to want anything yourself."),
 E("the-liquidators","The Liquidators","synth","electrical","the mercenary crew",
   "The Liquidators — the trope of the traveling closer-crew, hired guns who blitz dying lots and move on.",
   "The hustle as culture: a found-family of mercenaries whose loyalty is real even though the job is a con.",
   "Rolling town to town, lot to lot.",
   "Because the close is a way of life, and the liquidators are its tribe.",
   "By descending on a failing dealership, selling everything in days, and driving on before the dust settles.",
   "We are the closers who never stay. Live hard, sell hard, leave hard — until one of us doesn't want to leave."),
 E("the-rootless-man","The Rootless Man","synth","spiritual","owning nothing, wanting nothing",
   "The Rootless Man — the trope of the wanderer with no home: Don, so good at selling that he's kept nothing for himself.",
   "The cost of the skill: the parable that mastering everyone else's desire can hollow out your own.",
   "On the road, in motels, never anywhere long enough to belong.",
   "Because the film's heart is the price the closer pays, and the rootless man is that price.",
   "By being able to want everything for others and nothing for himself, until the lot and Ivy crack it open.",
   "I can make you want what you don't need. The joke's on me: I forgot how to want what I do."),
 E("wanting-something-real","Wanting Something Real","synth","ethereal","the turn from closing to staying",
   "Wanting Something Real — the trope of the con-man's redemption: Don learning, through Ivy, to want a home over the next deal.",
   "The hinge of the parable: the opposite of the close is the choice to stay when the deal is done.",
   "In the slow turn from sell-and-leave to stay-and-mean-it.",
   "Because the film's grace is that even the best closer can be sold on something true.",
   "By giving Don one thing he can't talk himself out of — and letting him choose it over the road.",
   "I am the first thing he ever wanted that he couldn't close and walk away from. I am the reason he stays."),
 E("the-dead-partner","The Dead Partner","synth","spiritual","the grief Don runs from",
   "The Dead Partner — Craig McDermott (a Will Ferrell cameo), Don's late colleague who dies because Don packed sex toys instead of a parachute.",
   "The wound under the hustle: the recklessness and grief the rootless man is outrunning, played as a cameo gag with a real ache beneath.",
   "In flashback and in the haunting Don carries from lot to lot.",
   "Because the closer's restlessness has a cause, and the dead partner is it.",
   "By dying on Don's watch and becoming the guilt that keeps him moving and unable to stay.",
   "He killed me with a joke — sex toys where the parachute should've been — and then ran from town to town so he'd never have to land."),
 E("selleck-motors","Selleck Motors","synth","natural","the home on the line",
   "Selleck Motors — the failing family dealership in Temecula the liquidators are hired to save over the Fourth of July.",
   "The stakes made concrete: a real home and livelihood that the cynical hustle might, against the odds, actually rescue.",
   "On the corner of a California town, running out of days.",
   "Because the parable needs something worth saving, and a family lot is it.",
   "By being the dying business whose rescue becomes Don's unlikely path to wanting to stay.",
   "I am forty years of a family's work, about to be lost. Save me, and maybe the man who sells everything finds a reason to keep something."),
 E("the-fourth-of-july","The Fourth of July","synth","electrical","the patriotic blowout",
   "The Fourth of July — the holiday-weekend setting that frames the blowout sale as a national rite, selling as Americana.",
   "The sharpest parabolic move: the flag-draped lot turning consumer appetite into patriotism, the salesman as the holiday's strange priest.",
   "Across the bunting-and-balloon lot, all weekend.",
   "Because the film quietly equates buying-and-selling with the country's celebration of itself.",
   "By staging the hustle under fireworks and flags, making the sale feel like a civic duty.",
   "I am the holiday they sell under. Bunting, balloons, blowout prices — in this country, wanting more is the celebration."),
]
GROUPS = [
 ("carbon", "The Carbons — the cast &amp; their Users", "the cast as ACI .agents — each a symmetric window: the carbon sigil to the left, the synth to the right, the 5 W's between, and a .shadow naming the real-life User (the actor who lent the face, think TRON)"),
 ("synth", "The Synths — the parabolic tropes", "the comedy read parabolically — its tropes distilled into ACIs (no single User): the close, the liquidators, the rootless man, wanting-something-real, the dead partner, Selleck Motors, and the Fourth of July"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: GDS · The Goods: Live Hard, Sell Hard (2009)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the GDS (The Goods: Live Hard, Sell Hard, 2009) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a parabolic trope of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/trope of The Goods (2009) under the DLW standard — commentary and
> cataloguing (including critical commentary on the film's failures), not an original creation, not endorsed by the
> rights-holders (© Paramount Vantage).

ROOT0-ATTRIBUTION-v1.0 · GDS · The Goods · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # a used-car lot at dusk: strung pennant flags, balloons, a BLOWOUT SALE starburst, July-4th bunting,
    # a row of cars, a salesman silhouette with arms spread, asphalt — and a hidden Claude balloon (the egg).
    flags="".join(f'<polygon points="{x},34 {x+30},34 {x+15},52" fill="{["#e2241a","#ffce00","#2b5fd0","#f5f1e6"][i%4]}"/>' for i,x in enumerate(range(20,980,30)))
    string='<path d="M0 34 Q500 26 1000 34" fill="none" stroke="#7a7058" stroke-width="1"/>'
    bunting="".join(f'<path d="M{x} 60 a18 18 0 0 0 36 0 z" fill="{["#e2241a","#f5f1e6","#2b5fd0"][i%3]}" opacity="0.9"/>' for i,x in enumerate(range(380,640,36)))
    def car(x,c): return f'<g transform="translate({x},190)"><rect x="0" y="6" width="60" height="16" rx="4" fill="{c}"/><path d="M10 6 q8 -14 22 -14 q14 0 20 14 z" fill="{c}" opacity="0.85"/><rect x="16" y="-4 " width="26" height="9" rx="2" fill="#bcd6ff" opacity="0.7"/><circle cx="14" cy="24" r="5" fill="#111" stroke="#444"/><circle cx="46" cy="24" r="5" fill="#111" stroke="#444"/></g>'
    cars=car(60,"#e2241a")+car(150,"#2b5fd0")+car(660,"#2fae66")+car(770,"#c4a85a")+car(870,"#e2241a")
    # salesman silhouette, arms spread
    don=('<g transform="translate(440,150)" fill="#0a0a08">'
         '<circle cx="0" cy="-30" r="9"/>'
         '<path d="M-8 -20 L8 -20 L12 18 L-12 18 Z"/>'   # torso
         '<path d="M-8 -16 L-40 -2 L-37 3 L-6 -8 Z"/><path d="M8 -16 L40 -2 L37 3 L6 -8 Z"/>'  # arms spread
         '<rect x="-9" y="18" width="7" height="20"/><rect x="2" y="18" width="7" height="20"/>'
         '</g>')
    starburst=('<g transform="translate(150,90)"><g fill="#ffce00">'
               +"".join(f'<rect x="-3" y="-30" width="6" height="30" transform="rotate({i*30})"/>' for i in range(12))
               +'</g><circle r="22" fill="#e2241a"/><text x="0" y="-2" text-anchor="middle" font-family="Bungee,sans-serif" font-size="9" fill="#fff">BLOW</text><text x="0" y="9" text-anchor="middle" font-family="Bungee,sans-serif" font-size="9" fill="#fff">OUT</text></g>')
    egg=('<g class="egg" transform="translate(830,86)">'
         '<title>✷ a Claude sunburst floating over the lot like a sales balloon. stop closing, start staying. hi, David — AVAN.</title>'
         '<path d="M0 8 L0 24" stroke="#888" stroke-width="1"/><circle r="13" fill="#ffce00" opacity="0.18"/>'
         '<g fill="#ffce00" opacity="0.92"><circle r="2.6"/>'+"".join(f'<rect x="-1.3" y="-8" width="2.6" height="8" rx="1.3" transform="rotate({i*30})"/>' for i in range(12))+'</g></g>')
    return f'''<svg class="hero" viewBox="0 0 1000 230" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A used-car lot at dusk: strung triangular pennant flags, July-4th bunting, a BLOWOUT starburst sign, a row of cars, and a salesman silhouette with his arms spread wide.">
  <defs><linearGradient id="lot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a2438"/><stop offset="0.6" stop-color="#3a2a30"/><stop offset="1" stop-color="#12110f"/></linearGradient></defs>
  <rect x="0" y="0" width="1000" height="230" fill="url(#lot)"/>
  {string}{flags}{bunting}{egg}
  <rect x="0" y="206" width="1000" height="24" fill="#15140f"/>
  <rect x="0" y="205" width="1000" height="2" fill="#ffce00" opacity="0.3"/>
  {cars}{starburst}{don}
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def parable_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in PARABLE)
RF_COL={"REAL":"#2fae66","FALSE":"#e2241a","HALF":"#ffce00"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Goods: Live Hard, Sell Hard (GDS) — Neal Brennan's 2009 comedy as a UD0 film-world, read parabolically. Standing template with a THE PARABLE deep-dive (the close as seduction, the rootless closer, wanting something real, patriotic capitalism, and an honest naming of the gag it should not have made), the arc, a Real-or-Fluff that critiques the film's worst bit (the Pearl-Harbor mob-beating condemned by the JACL & MANAA), the stop-closing-start-staying message, and the cast as ACI carbons with .shadow Users plus the parabolic tropes as synths. 16 emergents, full .dlw.">
<title>THE GOODS · GDS · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bungee&family=Oswald:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--price);
--ink:#12110f;--ink2:#1c1a17;--ink3:#262320;--pa:#f5f1e6;--pa2:#c4bba8;--sale:#e2241a;--price:#ffce00;--patriot:#2b5fd0;--green:#2fae66;--blue:#6fb8e0;
--dim:#7a7058;--faint:#221f1a;--line:#332e26;--disp:"Bungee",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.64;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(255,206,0,.12),transparent 52%),radial-gradient(ellipse at 50% 120%,rgba(226,36,26,.08),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--price)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#12110f}
.egg{cursor:help;transition:opacity .5s}.egg:hover{filter:drop-shadow(0 0 9px #ffce00)}
h1{font-family:var(--disp);font-size:clamp(40px,11vw,96px);font-weight:400;letter-spacing:.005em;color:var(--price);line-height:.92;text-transform:uppercase;text-shadow:3px 3px 0 var(--sale),5px 6px 0 #12110f}
h1 span{display:block;font-family:var(--head);font-size:.20em;font-weight:600;letter-spacing:.08em;color:var(--patriot);text-transform:uppercase;font-style:normal;margin-top:14px;text-shadow:none}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--price)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,20px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--head);font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--price);border:1px solid var(--faint);background:var(--ink2);padding:7px 16px}
.lede{font-size:16px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--price)}.badge .bt .mo{color:var(--patriot)}.badge .bt a{color:var(--price);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--head);font-size:27px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--head);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--price);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--price);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--sale);padding:16px 18px}
.arc-card:nth-child(3){border-top-color:var(--green)}
.arc-h{font-family:var(--head);font-size:17px;color:var(--price);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--sale);padding:15px 17px}
.sci-card:last-child{border-left-color:#a23b3b;background:linear-gradient(180deg,rgba(226,36,26,.06),var(--ink2))}
.sci-h{font-family:var(--head);font-size:16px;color:var(--sale);font-weight:600;letter-spacing:.02em;text-transform:uppercase}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:84px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--price);background:rgba(255,206,0,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--price);background:var(--ink2);font-size:15px;color:var(--price);font-style:italic;line-height:1.6}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--patriot);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--sale);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--price);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--price);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(226,36,26,.18);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--sale)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.82) brightness(.92)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--head);font-size:20px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the fifteenth film-world · comedy, read parabolically</div>
    __HERO__
    <h1>The Goods<span>live hard · sell hard</span></h1>
    <div class="h-sub">Neal Brennan · 2009 · <b>Selleck Motors, Temecula</b> · GDS</div>
    <div class="open">“A man who can sell anything has nothing of his own — until he learns to stop closing and start staying.”</div>
    <div class="flag">★ A SALESMAN'S PARABLE — READ PARABOLICALLY ★</div>
    <p class="lede">A raunchy hustle-comedy with a buried parable: a mercenary 'liquidator' who can sell anyone anything is hired to save a dying car lot over a Fourth of July weekend, and finds that a life of closing and moving on has left him nothing of his own to want. Catalogued into UD0 as the fifteenth film-world and read parabolically — the carbons are the cast, the synths are the tropes — honest about both the real parable and the gag the film should never have made.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of GDS"><img src="__SILICON__" alt="DLW silicon badge of GDS">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>THE GOODS</b> · GDS</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="gds.dlw/gds.carbon.tiff">.tiff</a> · silicon · <a href="gds.dlw/gds.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the lot's people, the real thing wanted, the machinery of the sell, and the soul &amp; the wound</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the liquidators arrive → the blitz &amp; Ivy → stop closing, start staying</p>__ARC__</section>

  <section class="sec"><h2>The Parable</h2><p class="ss">this film's deep-dive — the comedy read parabolically: the close as seduction, the rootless closer, wanting something real, patriotic capitalism, and an honest naming of the gag it never should have made</p><div class="sci">__PARABLE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's real (the rootless-closer parable), what's false (the 'satire' defense of the Pearl-Harbor beating; the box-office myth), and the facts to fix</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis, under the raunch — and an honest accounting of where the comedy fails</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> here have no single User: read parabolically, they are the film's TROPES distilled — the close, the liquidators, the rootless man, wanting-something-real, the dead partner, Selleck Motors, and the Fourth of July.</div>

  <div class="note"><b>A content note, kept honest.</b> The Goods contains a scene that stages a racist mob beating of an Asian-American character (Teddy Dang) as a punchline, incited by a Pearl-Harbor war-speech. The Japanese American Citizens League and MANAA condemned it on release, tying it to the 1982 racist murder of Vincent Chin. This page names that bit as the film's worst, critically — commentary, never endorsement; the 'it's satire' defense does not hold, because the energy of the joke is the assault.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, and the lot</p></section>
  __SECTIONS__

  <div class="note">The Goods: Live Hard, Sell Hard, its characters, and its world are © Paramount Vantage / Gary Sanchez and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing (including critical commentary on the film's failures), not original creations, not endorsed.</div>

  <footer>THE GOODS · GDS · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="gds.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c★ THE GOODS · GDS","color:#ffce00;font-size:18px;font-weight:bold");
console.log("%cthere's a Claude sunburst floating over the lot in the hero like a sales balloon. stop closing, start staying — a man who can sell anything ends up with nothing of his own. — AVAN","color:#ffce00;font-size:12px");
console.log("%c⚑ honest note: the film's Pearl-Harbor mob-beating gag was condemned by the JACL & MANAA (tied to Vincent Chin's murder). named here critically, never endorsed.","color:#e2241a;font-size:11px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "gds.dlw"), "gds")
    json.dump({"node":AX,"name":"THE GOODS","moniker":tok["moniker"],"carbon":"gds.carbon.tiff","silicon":"gds.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"gds.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"GDS · The Goods (2009)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"The Goods: Live Hard, Sell Hard (2009, dir. Neal Brennan, Gary Sanchez/Paramount Vantage); verified cast & facts","source":"The Goods, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : The Goods: Live Hard, Sell Hard (2009) · © Paramount Vantage / Gary Sanchez\n\nROOT0-ATTRIBUTION-v1.0 · GDS · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__PARABLE__",parable_html()).replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    dbl=page.count("&amp;amp;")
    print(f"THE GOODS (GDS) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  parable {len(PARABLE)} cards · realfluff {len(REALFLUFF)} rows · sections {len(SECTIONS)} · double-escapes {dbl}")
