from bs4 import BeautifulSoup
import requests

print('Please enter URL: ')
url = 'https://search.yahoo.com/search;_ylc=X3oDMTFiN25laTRvBF9TAzIwMjM1MzgwNzUEaXRjAzEEc2VjA3NyY2hfcWEEc2xrA3NyY2h3ZWI-?p=cats&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8'
r = requests.get(url)
data = r.content

soup = BeautifulSoup(data,'html.parser')

list = []

if 'yahoo' in url:
    for x in soup.find_all('ol', class_= 'mb-15 reg searchCenterMiddle'):
        for y in x.find_all('a'):
            print(y.get('href'))


#yahoo class=:"mb-15 reg searchCenterMiddle"
