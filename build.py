import os, json
OUT='public'; BASE='https://www.tintsquad.com'; BOOK='https://tint-squad.onrender.com/book/'
TEL='tel:+13154185442'; PH='(315) 418-5442'
LD={"@context":"https://schema.org","@type":["AutoRepair","LocalBusiness"],"name":"Tint Squad","url":BASE+"/",
"telephone":"+1-315-418-5442","image":BASE+"/img/hero-1600.jpg","priceRange":"$$",
"address":{"@type":"PostalAddress","streetAddress":"1130 West Genesee Street","addressLocality":"Syracuse","addressRegion":"NY","postalCode":"13204","addressCountry":"US"},
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Tuesday","Wednesday","Thursday","Friday"],"opens":"10:00","closes":"18:00"}],
"areaServed":"Syracuse, NY","description":"Automotive window tint for pickup trucks and SUVs in Syracuse, NY. LLumar film, lifetime warranty."}
NAV=[('/','Home'),('/window-tint','Window Tint'),('/quote','Pricing & Quote'),('/faq','FAQ'),('/blog','Blog'),('/blank','Contact')]
def page(path,title,desc,body,extra_ld=None):
    nav=''.join(f'<a href="{h}"{" aria-current=page" if h==path else ""}>{t}</a>' for h,t in NAV)
    lds=f'<script type="application/ld+json">{json.dumps(LD)}</script>'
    if extra_ld: lds+=f'<script type="application/ld+json">{json.dumps(extra_ld)}</script>'
    url=BASE+path
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Tint Squad"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/img/og.jpg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0d"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css">
<link rel="preload" as="image" href="/img/hero-1600.webp" imagesrcset="/img/hero-800.webp 800w, /img/hero-1600.webp 1600w" imagesizes="100vw">
{lds}</head><body>
<header class="top"><div class="wrap bar"><a class="logo" href="/" aria-label="Tint Squad home"><img src="/img/logo-white.svg" alt="Tint Squad" width="180" height="33"></a>
<input type="checkbox" id="m" aria-label="Menu"><label for="m" class="burger" aria-hidden="true"><i></i><i></i><i></i></label>
<nav>{nav}</nav><div class="hcta"><a class="ph" href="{TEL}">{PH}</a><a class="btn" href="{BOOK}">Book Now</a></div></div></header>
<main>{body}</main>
<footer><div class="wrap fgrid"><div><a class="logo" href="/" aria-label="Tint Squad home"><img src="/img/logo-white.svg" alt="Tint Squad" width="180" height="33"></a><p>Automotive window tint in Syracuse, NY for 16 years. LLumar film. Lifetime warranty.</p></div>
<div><h4>Visit</h4><p>1130 West Genesee Street<br>Syracuse, NY 13204</p><p><a href="{TEL}">{PH}</a></p></div>
<div><h4>Hours</h4><p>Tue–Fri: 10am–6pm<br>Sat–Mon: Closed</p></div>
<div><h4>Links</h4><p>{" · ".join(f'<a href="{h}">{t}</a>' for h,t in NAV)}</p><p><a class="btn sm" href="{BOOK}">Book or Get a Quote</a></p></div></div>
<p class="wrap copy">© Tint Squad · Syracuse, NY</p></footer>
<a class="callbar" href="{TEL}">📞 Call {PH}</a><a class="bookbar" href="{BOOK}">Book / Quote</a>
</body></html>'''
    d=OUT+(path if path!='/' else '/'); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w').write(html)

def pic(name,alt,cls='',sizes='(max-width:800px) 100vw, 50vw',lazy=True,w=1200,h=900):
    return f'<picture><source type="image/webp" srcset="/img/{name}-800.webp 800w, /img/{name}-1600.webp 1600w" sizes="{sizes}"><img class="{cls}" src="/img/{name}-1600.jpg" srcset="/img/{name}-800.jpg 800w, /img/{name}-1600.jpg 1600w" sizes="{sizes}" alt="{alt}" width="{w}" height="{h}" {"loading=lazy" if lazy else "fetchpriority=high"} decoding="async"></picture>'

PRICING=f'''<section class="sec" id="pricing"><div class="wrap"><p class="eyebrow">Straight pricing</p><h2>Flat prices. No deposit.</h2>
<div class="cards price">
<div class="card hot"><span class="tag">Special</span><h3>Two Fronts + Windshield Strip</h3><p class="amt">$150</p><p>Trucks &amp; SUVs: two front windows matched to your rear glass plus a windshield sun strip.</p><a class="btn" href="{BOOK}">Book the Special</a></div>
<div class="card"><h3>Two Fronts</h3><p class="amt">$100</p><p>Trucks &amp; SUVs: we match your fronts to your factory rear privacy glass. Wait in our waiting room.</p><a class="btn ghost" href="{BOOK}">Book Two Fronts</a></div>
<div class="card"><h3>Windshield Strip</h3><p class="amt">$50</p><p>A sun strip across the top of the windshield to cut glare from the sun and the snow.</p><a class="btn ghost" href="{BOOK}">Book a Strip</a></div>
<div class="card"><h3>Full Windshield</h3><p class="amt">$150</p><p>Full windshield film. Ask us about NY rules before you choose a shade.</p><a class="btn ghost" href="{BOOK}">Book Windshield</a></div>
<div class="card"><h3>Full Vehicle &amp; Everything Else</h3><p class="amt sm">Quoted by vehicle</p><p>Pickups, SUVs, sunroofs and more. Pick your vehicle on the booking page for a price.</p><a class="btn ghost" href="{BOOK}">Get My Quote</a></div>
</div><p class="note">Every job uses LLumar film and comes with a lifetime warranty. Shade choice doesn't change the price.</p></div></section>'''
SHADES='''<div class="shades" role="list"><div role="listitem" style="--o:.92"><b>5%</b><span>Limo dark</span></div><div role="listitem" style="--o:.8"><b>15%</b><span>Very dark</span></div><div role="listitem" style="--o:.7"><b>20%</b><span>Dark</span></div><div role="listitem" style="--o:.5"><b>35%</b><span>Medium</span></div></div>'''
FAQS=[
("Can I roll my windows down after tint?","Leave your windows rolled up for at least 48 hours after the film is installed so it can set."),
("What are the tint laws in New York?","For most passenger vehicles, New York requires front side windows to let in at least 70% of light, and the windshield can only have non-reflective tint on the top 6 inches. On SUVs, pickup trucks and vans, the rear side windows and rear window can be darker; on sedans, the rear side windows also have to meet the 70% rule. Limited medical exemptions exist. Laws change, so check the NY DMV for the current rules before choosing a shade, and ask us if you have questions."),
("What film do you use?","LLumar, a dyed automotive film, in 5%, 15%, 20% and 35%. It's backed by a lifetime warranty against manufacturer defects like bubbling, peeling, fading or color change."),
("Why don't you carry ceramic tint?","We've built our shop around one film we trust and stand behind: LLumar. Ceramic is a different, higher-priced product line that we simply don't offer. If ceramic is a must-have for you, another shop may be a better fit."),
("Does the shade percentage affect the price?","No. Your shade choice doesn't change the price."),
("How long does it take?","Two front windows are a quick job and you can wait in our waiting room. For a full vehicle, plan to drop it off for about 3 hours."),
("Do I need a deposit?","No deposit. Book online and show up."),
("Does tint go on the inside or the outside?","On the inside. Sometimes the film is laid on the outside first so it can be heat-shrunk to the curve of the glass, then it's installed on the inside."),
("How do I clean tinted windows?","Use a soft microfiber cloth with mild soapy water or an ammonia-free glass cleaner."),
]
def faqhtml(items): return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)
FAQLD={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQS]}
HOW=f'''<section class="sec alt"><div class="wrap"><p class="eyebrow">How it works</p><h2>Three steps. Done.</h2><ol class="steps">
<li><b>Book online</b><span>Pick your vehicle and service on our <a href="{BOOK}">booking page</a> and get your price. No deposit.</span></li>
<li><b>Come in</b><span>Two fronts? Hang out in the waiting room. Full vehicle? Drop it off; plan on about 3 hours.</span></li>
<li><b>Drive off tinted</b><span>Keep the windows up for 48 hours. Your LLumar film is covered by a lifetime warranty.</span></li></ol></div></section>'''
MAP='<iframe title="Map to Tint Squad, 1130 West Genesee Street, Syracuse NY" src="https://www.google.com/maps?q=1130+West+Genesee+Street,+Syracuse,+NY+13204&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
CONTACT=f'''<section class="sec" id="contact"><div class="wrap cgrid"><div><p class="eyebrow">Visit the shop</p><h2>Tint Squad, Syracuse</h2>
<p class="big">1130 West Genesee Street<br>Syracuse, NY 13204</p><p><a class="btn" href="{TEL}">Call {PH}</a> <a class="btn ghost" href="{BOOK}">Book Online</a></p>
<table class="hours"><caption>Hours</caption><tr><th>Tue–Fri</th><td>10:00am – 6:00pm</td></tr><tr><th>Sat, Sun, Mon</th><td>Closed</td></tr></table></div><div class="map">{MAP}</div></div></section>'''

home=f'''<section class="hero">{pic("hero","White full-size pickup truck with dark tinted windows","bg","100vw",False,1600,900)}
<div class="wrap hin"><p class="eyebrow">Syracuse, NY · 16 years in business</p><h1>Truck &amp; SUV<br>window tint, <em>done right.</em></h1>
<p class="lead"><b>Special: Two Fronts + Windshield Strip $150</b>. LLumar film, lifetime warranty, no deposit.</p>
<div class="ctas"><a class="btn lg" href="{BOOK}">Book or Get a Quote</a><a class="btn ghost lg" href="{TEL}">Call {PH}</a></div>
<ul class="chips"><li>LLumar film</li><li>Lifetime warranty</li><li>No deposit</li><li>Tue–Fri 10–6</li></ul></div></section>
<section class="sec"><div class="wrap split"><div><p class="eyebrow">Two Fronts to Match · $100</p><h2>Your rear glass is dark. Your fronts aren't.</h2>
<p>Most pickups and SUVs leave the factory with dark rear privacy glass and clear front windows. We meter your back glass to see whether our 15% or 20% matches best, then tint your two fronts so the whole truck looks right. It's a quick job, so you can wait in our waiting room.</p>
<p><a class="btn" href="{BOOK}">Book Two Fronts – $100</a></p></div><div class="callout"><p class="eyebrow">Trucks &amp; SUVs</p><p class="amt">$100</p><h3>Two Fronts</h3><ul class="ticks"><li>We meter your back glass</li><li>15% or 20% to match</li><li>Wait in our waiting room</li><li>LLumar film, lifetime warranty</li></ul></div></div></section>
{PRICING}
<section class="sec"><div class="wrap split"><div><p class="eyebrow">Tint simulator</p><h2>See your tint before you book</h2><p>Pick your year, make, model, paint color and shades, and we'll show you an AI preview of your vehicle with tint in about 10 seconds.</p><p><a class="btn" href="/tint-simulator">Try the Tint Simulator</a></p></div>{pic("colorado","Red Chevrolet Colorado pickup truck with dark tinted windows")}</div></section>
<section class="sec alt"><div class="wrap"><p class="eyebrow">Why Tint Squad</p><h2>One shop. One film. 16 years.</h2><div class="cards why">
<div class="card"><h3>16 years in Syracuse</h3><p>Same shop on West Genesee Street, standing behind every install.</p></div>
<div class="card"><h3>LLumar film</h3><p>Dyed automotive film in 5, 15, 20 and 35% shades.</p></div>
<div class="card"><h3>Lifetime warranty</h3><p>Covers manufacturer defects like bubbling, peeling, fading or color change.</p></div>
<div class="card"><h3>Built for trucks &amp; SUVs</h3><p>Pickups, SUVs and two-front matches are what we do every day.</p></div></div>
<h3 class="mt">Pick your shade</h3>{SHADES}</div></section>
{HOW}
<section class="sec"><div class="wrap split rev">{pic("suv","White full-size SUV with dark tinted windows")}<div><p class="eyebrow">Tint in any season</p><h2>Syracuse glare doesn't wait for summer.</h2><p>Low winter sun off fresh snow is brutal. Tint cuts glare all year, and booking in the off-season beats the summer rush.</p><p><a class="btn ghost" href="/blog">Read the blog</a></p></div></div></section>
<section class="sec alt"><div class="wrap narrow"><p class="eyebrow">FAQ</p><h2>Quick answers</h2>{faqhtml(FAQS[:5])}<p><a href="/faq">All FAQs →</a></p></div></section>
<section class="sec alt"><div class="wrap gift"><picture><source type="image/webp" srcset="/img/gift-certificate.webp"><img src="/img/gift-certificate.png" alt="Tint Squad gift certificates" width="155" height="92" loading="lazy" decoding="async"></picture><div><p class="eyebrow">Gift certificates</p><h2>Give the Gift of Tint</h2><p>Tint Squad gift certificates, available at the shop.</p><p><a class="btn" href="{TEL}">Call to Buy</a></p></div></div></section>
{CONTACT}'''
page('/','Truck & SUV Window Tint Syracuse NY | Tint Squad','Window tint for pickup trucks and SUVs in Syracuse, NY. Two front windows $100. LLumar film, lifetime warranty, no deposit. Call (315) 418-5442.',home,FAQLD)

wt=f'''<section class="phero"><div class="wrap"><p class="eyebrow">Automotive window tint · Syracuse, NY</p><h1>Window tint for pickups &amp; SUVs</h1><p class="lead">LLumar film, computer-cut patterns and a lifetime warranty.</p><a class="btn lg" href="{BOOK}">Quote My Vehicle</a></div></section>
<section class="sec"><div class="wrap split"><div><h2>A factory-finished look</h2><p>We tint pickup trucks and SUVs every day, from a quick two-front match to the whole vehicle. Our installs go to the top of your windows, and every rear windshield is one full piece.</p>
<h3>Computer-cut patterns</h3><p>Our cutting system uses a large pattern database covering virtually any vehicle, so film lines up precisely every time.</p>
<h3>Lifetime warranty</h3><p>LLumar automotive film is covered for manufacturer defects such as bubbling, fading, peeling or color change.</p></div><div class="callout"><p class="eyebrow">Every install</p><ul class="ticks"><li>Computer-cut patterns</li><li>Film to the top of the window</li><li>One-piece rear windshield</li><li>Lifetime warranty</li></ul></div></div></section>
<section class="sec alt"><div class="wrap"><h2>Shades we carry</h2><p>LLumar dyed film only, in four shades. Price is the same whichever you choose.</p>{SHADES}<p class="note">Check New York's tint rules before picking a shade for your front windows. See our <a href="/faq">FAQ</a>.</p>
<h3 class="mt">Add-ons</h3><ul class="ticks"><li>Windshield sun strip ($50)</li><li>Full windshield ($150)</li><li>Sunroof (quoted by vehicle)</li></ul></div></section>
{PRICING}{HOW}'''
page('/window-tint','Truck & SUV Window Tinting Syracuse NY | Tint Squad','Professional window tint for pickups and SUVs in Syracuse, NY. LLumar film in 5/15/20/35%, computer-cut patterns, lifetime warranty.',wt)

q=f'''<section class="phero"><div class="wrap"><p class="eyebrow">Pricing &amp; quotes</p><h1>Get your price in a minute</h1><p class="lead">Flat prices for the common jobs. Everything else is quoted by vehicle on our booking page.</p><a class="btn lg" href="{BOOK}">Start My Quote</a></div></section>{PRICING}{HOW}'''
page('/quote','Window Tint Prices & Quote Syracuse NY | Tint Squad','Window tint prices in Syracuse, NY: two front windows $100, windshield strip $50, full windshield $150. Get a quote by vehicle. No deposit.',q)

f=f'''<section class="phero"><div class="wrap"><p class="eyebrow">FAQ</p><h1>Window tint questions, answered</h1></div></section><section class="sec"><div class="wrap narrow">{faqhtml(FAQS)}<p class="mt">Still have a question? <a href="{TEL}">Call {PH}</a>.</p></div></section>'''
page('/faq','Window Tint FAQ Syracuse NY | Tint Squad','Answers about window tint in Syracuse, NY: New York tint law basics, LLumar film, timing, pricing, warranty and aftercare.',f,FAQLD)

posts=[("The \"Factory Match\"","Why your truck looks unfinished without it: dark factory rear glass, clear fronts, and the $100 fix.","the-factory-match"),
("Why Tinting in Syracuse Winters is Smarter","Snow glare on 690 and I-81 is real, and winter is the best time to beat the summer rush.","why-tinting-in-syracuse-winters-is-smarter"),
("The \"Buyer Beware\" Post","Why a clean, professional install needs a real shop, and why a warranty is only as good as who stands behind it.","the-buyer-beware-post"),
("Is Ceramic Tint a Scam? (The Honest Truth)","Mike's honest take on the marketing claims you see in tint ads.","is-ceramic-tint-a-scam-the-honest-truth")]
b='<section class="phero"><div class="wrap"><p class="eyebrow">Blog</p><h1>Straight talk on window tint</h1><p class="lead">From Mike Canestrare at Tint Squad.</p></div></section><section class="sec"><div class="wrap cards blog">'+''.join(f'<a class="card" href="{BASE}/post/{s}"><h3>{t}</h3><p>{d}</p><span>Read post →</span></a>' for t,d,s in posts)+'</div></div></section>'
page('/blog','Window Tint Blog | Tint Squad Syracuse NY','Honest window tint advice from Tint Squad in Syracuse, NY: factory matching, winter tinting and how to avoid tint scams.',b)

c=f'<section class="phero"><div class="wrap"><p class="eyebrow">Contact</p><h1>Call, book, or stop by</h1></div></section>{CONTACT}'
page('/blank','Contact Tint Squad | Window Tint Syracuse NY','Contact Tint Squad, 1130 West Genesee Street, Syracuse, NY 13204. Call (315) 418-5442. Open Tuesday to Friday, 10am to 6pm.',c)
bk=f'<section class="phero"><div class="wrap"><p class="eyebrow">Book online</p><h1>Book your tint appointment</h1><p class="lead">Pick your vehicle and service, see your price, choose a time. No deposit.</p><a class="btn lg" href="{BOOK}">Open Booking Page</a> <a class="btn ghost lg" href="{TEL}">Call {PH}</a></div></section>{HOW}'
page('/blank-1','Book a Window Tint Appointment Syracuse NY | Tint Squad','Book your truck or SUV window tint appointment at Tint Squad in Syracuse, NY. LLumar film with a lifetime warranty. No deposit.',bk)
SIMBODY=f'''<section class="phero"><div class="wrap"><p class="eyebrow">Window tint simulator</p><h1>See your tint before you book</h1><p class="lead">Pick your vehicle, paint color and shades. We'll show you a preview in about 10 seconds.</p></div></section>
<section class="sec"><div class="wrap"><form id="sim" class="sim" novalidate>
<fieldset><legend>1. Your vehicle</legend><label>Year<select id="year" required></select></label><label>Make<select id="make" disabled required></select></label><label>Model<select id="model" disabled required></select></label><label id="bodyw" hidden>Body style<select id="body"></select></label><label>Paint color<select id="color" disabled required></select></label></fieldset>
<fieldset><legend>2. Your shades</legend><label>Front side windows<select id="front"></select></label><label>Rear side windows<select id="rear"></select></label><label>Back glass<select id="back"></select></label><label>Full windshield<select id="full"></select></label><label class="chk"><input type="checkbox" id="strip"> Windshield sun strip (5%)</label></fieldset>
<fieldset><legend>3. Where should we send your quote?</legend><label>Name<input type="text" id="name" autocomplete="name" required></label><label>Phone<input type="tel" id="phone" autocomplete="tel" required></label><input class="hp" id="website" tabindex="-1" autocomplete="off" aria-hidden="true"></fieldset>
<p class="err" id="err" role="alert"></p><p><button class="btn lg" id="go" type="submit">Show My Tint</button></p>
<p class="note">Previews are AI illustrations to help you compare shades. Your real vehicle and film may look different. Check New York's tint rules before choosing front-window shades (<a href="/faq">FAQ</a>).</p></form>
<div class="simout" id="out" hidden><div class="wait" id="wait"><div class="spin"></div>Creating your preview… <span id="secs">0</span>s</div>
<div id="res" hidden><img id="img" alt="AI preview of your vehicle with the selected window tint" width="1376" height="768"><p class="note" id="cap"></p><p class="note">AI illustration, not a photo of your vehicle.</p><p><a class="btn lg" href="{BOOK}">Book This Tint</a> <a class="btn ghost lg" href="{TEL}">Call {PH}</a></p></div></div>
</div></section><script src="/tint-simulator/sim.js" defer></script>'''
page('/tint-simulator','Window Tint Simulator | See Your Tint | Tint Squad Syracuse NY','Preview window tint on your truck or SUV before you book. Pick your vehicle, color and shades. Tint Squad, Syracuse NY.',SIMBODY)
page('/404','Page Not Found | Tint Squad','Page not found.',f'<section class="phero"><div class="wrap"><h1>Page not found</h1><p><a class="btn" href="/">Go home</a></p></div></section>')
os.rename(OUT+'/404/index.html',OUT+'/404.html'); os.rmdir(OUT+'/404')
paths=['/','/window-tint','/tint-simulator','/quote','/faq','/blog','/blank','/blank-1']
open(OUT+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{p}</loc><lastmod>2026-11-04</lastmod></url>' for p in paths)+'</urlset>\n')
# preview: block indexing so it won't compete with live site; flip for production
open(OUT+'/robots.txt','w').write(f'# PREVIEW: change to "Allow: /" when this replaces the live site\nUser-agent: *\nDisallow: /\nSitemap: {BASE}/sitemap.xml\n')
open(OUT+'/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#0b0b0d"/><path d="M6 10h20v4H18v12h-4V14H6z" fill="#e10600"/></svg>')
