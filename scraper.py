import scraperwiki

# Blank Python

import scraperwiki           
import lxml.html           

urls = ["http://www.amazon.com/Best-Sellers-Patio-Lawn-Garden/zgbs/lawn-garden/ref=zg_bs_nav_0"]

for wurl in urls:
    error = True
    while error:
        try:
            html = scraperwiki.scrape(wurl)
            root = lxml.html.fromstring(html)
            for tr in root.cssselect("div[class='zg_title'] a"):    
                url = tr.get("href")
                html = scraperwiki.scrape(url ).lower()
                scraperwiki.sqlite.save(unique_keys=['url'],data=data)
            error = False
        except:
            error = True
