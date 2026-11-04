import sys
from playwright.sync_api import sync_playwright
base=sys.argv[1]; pre=sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,vp,mob in [('desktop',{'width':1440,'height':900},False),('mobile',{'width':390,'height':844},True)]:
        pg=b.new_page(viewport=vp,is_mobile=mob,device_scale_factor=2 if mob else 1)
        r=pg.goto(base+'/',wait_until='networkidle'); print(name,r.status, pg.title())
        pg.screenshot(path=f'shots/{pre}home-{name}.png'); pg.screenshot(path=f'shots/{pre}home-{name}-full.png',full_page=True)
        print('hscroll', pg.evaluate('document.documentElement.scrollWidth>innerWidth'))
    for path in ['/window-tint','/quote','/faq','/blog','/blank','/blank-1','/sitemap.xml','/robots.txt']:
        print(path, b.new_page().goto(base+path).status)
    b.close()
