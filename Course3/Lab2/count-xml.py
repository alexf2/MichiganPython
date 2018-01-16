import urllib.request
import xml.etree.cElementTree as ET

url1 = r'http://py4e-data.dr-chuck.net/comments_42.xml'
url2 = r'http://py4e-data.dr-chuck.net/comments_47841.xml'

def processXml (urlFrom, selector):
    doc = ET.ElementTree(file = urllib.request.urlopen(urlFrom))
    count = 0
    sum = 0
    for el in doc.findall(selector):
        count = count + 1
        sum = sum + int(el.text)
    return (count, sum)


count, sum = processXml(url1, './/count')
print(f'1: {count} = {sum}')

count, sum = processXml(url2, './/count')
print(f'2: {count} = {sum}')
