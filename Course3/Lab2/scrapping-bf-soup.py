import urllib.request#, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url1 = r' http://py4e-data.dr-chuck.net/comments_42.html'
url2 = r'http://py4e-data.dr-chuck.net/comments_47839.html'

class ResultVal(object):
    def __init__(self, cnt, sum):
        self._cnt = cnt
        self._sum = sum

    @property
    def count (self): return self._cnt

    @property
    def sum (self): return self._sum

def scrapNumbers (urlFrom):
    html = None
    with urllib.request.urlopen(urlFrom) as webRc:
        html = webRc.read()

    htmlDom = BeautifulSoup(html, 'html.parser')
    tags = htmlDom('span')
    sum = 0
    count = 0
    for span in tags:
        value = span.contents[0].strip()
        if len(value) < 1: continue
        count = count + 1
        sum = sum + int(value)

    return ResultVal(count, sum)



res1 = scrapNumbers(url1)
res2 = scrapNumbers(url2)

print(f'Count = {res1.count}, sum = {res1.sum}')
print(f'Count = {res2.count}, sum = {res2.sum}')
