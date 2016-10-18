import requests
from bs4 import BeautifulSoup
from search_engine_scraper import scraper

#url_base_yahoo = 'http://search.yahoo.com/search?p=%s'
#url_base_bing = 'http://www.bing.com/search?q=%s'
#url_base_ask = 'http://www.ask.com/web?q=%s'

urls = ['http://search.yahoo.com/search?p=%s', 'http://www.bing.com/search?q=%s', 'http://www.ask.com/web?q=%s']

queries = {
    'is it possible to increase the jazz audience': 'http://www.npr.org/sections/ablogsupreme/2012/05/23/153461410/it-cant-be-done-the-difficulty-of-growing-a-jazz-audience',
    'setup jupyterhub on server': 'https://github.com/jupyterhub/jupyterhub/wiki/Installation-of-Jupyterhub-on-remote-server'
}

for url in urls:
    for query in queries:
        print(scraper(url_base_bing % query))
