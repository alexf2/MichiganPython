import urllib.request
from bs4 import BeautifulSoup
import re

url1 = r'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url2 = r'http://py4e-data.dr-chuck.net/known_by_Caelyn.html'
regexName = re.compile(r'_([A-Za-z\d]+)\.html?$')

def navigateAndExtract(urlTo, linkIndex):
    html = None
    with urllib.request.urlopen(urlTo) as webRc:
        html = webRc.read()

    htmlDom = BeautifulSoup(html, 'html.parser')
    tags = htmlDom('a')    
    return tags[ linkIndex ].get('href', None)

def navigate (urlStart, linkIndex, repeatCount):
    for i in range(1, repeatCount + 1):
        urlStart = navigateAndExtract(urlStart, linkIndex)

    res = regexName.search(urlStart).groups()    
    return res[0] if len(res) > 0 else ''

print(f'3-->4: {navigate(url1, 2, 4)}')
print(f'18-->7: {navigate(url2, 17, 7)}')
