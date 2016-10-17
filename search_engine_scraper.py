from bs4 import BeautifulSoup
import requests

url = input()
r = requests.get('https://search.yahoo.com/search;_ylc=X3oDMTFiN25laTRvBF9TAzIwMjM1MzgwNzUEaXRjAzEEc2VjA3NyY2hfcWEEc2xrA3NyY2h3ZWI-?p=cats&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8')
data = r.content

soup = BeautifulSoup(data)

list = []

for link in soup.find_all('a'):
    list.append(link.get('href'))

for link in list:
    if 'yahoo' not in link:
        print(link)
