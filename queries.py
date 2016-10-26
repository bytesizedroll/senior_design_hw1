import requests
import random
from bs4 import BeautifulSoup
from search_engine_scraper import scraper
from grader import grader

# url_base_yahoo = 'http://search.yahoo.com/search?p=%s'
# url_base_bing = 'http://www.bing.com/search?q=%s'
# url_base_ask = 'http://www.ask.com/web?q=%s'

urls = [('yahoo','http://search.yahoo.com/search?p=%s'), ('bing','http://www.bing.com/search?q=%s'), ('ask','http://www.ask.com/web?q=%s')]
totals = {'yahoo':0, 'bing':0, 'ask':0}

queries = {
    'google AI justice': 'https://www.wired.com/2016/09/inside-googles-internet-justice-league-ai-powered-war-trolls/',
    'police facial recognition tougher oversight': 'http://www.nytimes.com/2016/10/19/us/a-virtual-lineups-of-average-citizens-created-by-software.html',
    'Rahm Emanuel\'s Speech violence chicago': 'https://www.dnainfo.com/chicago/20160922/downtown/rahm-emanuel-chicago-violence-speech-four-ps-parenting',
    'utah random clowns hysteria': 'http://www.independent.co.uk/news/world/americas/utah-orem-police-creepy-clown-sightings-shoot-random-illegal-criminal-charges-facebook-a7345311.html',
    'assessing google smartphone': 'http://www.nytimes.com/2016/10/20/technology/personaltech/google-pixel-review-assessing-the-new-smartphone.html'
}

results = {}
random.shuffle(urls)
for i, query in enumerate(queries):
    print('query %d: %s' % (i + 1, query))
    for x, url in enumerate(urls):
        query_results = scraper(url[1] % query)
        results['query_%s' % str(i)] = query_results
        grade = grader(query_results, queries[query])
        totals[url[0]] += grade
        print('Search engine %s: %d' % (x + 1, grade))
    print('\n')

print('totals:')
print(totals)
print('Search engines: \n 1: %s \n 2: %s \n 3: %s\n' % (urls[0][0], urls[1][0], urls[2][0]))
print('Winner: %s' % max(totals, key=totals.get))
