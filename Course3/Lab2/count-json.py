import urllib.request, urllib.parse
import json

url1 = r'http://py4e-data.dr-chuck.net/comments_42.json'
url2 = r'http://py4e-data.dr-chuck.net/comments_47842.json'

def processJson (urlFrom):    
    doc = None
    with urllib.request.urlopen(urlFrom) as reader:
        doc = json.load(reader)

    if not 'comments' in doc:
        raise Exception('Json document has been not recognized')

    count = 0
    sum = 0
    for el in doc['comments']:        
        count = count + 1
        sum = sum + int(el['count'])

    return (count, sum)


count, sum = processJson(url1)
print(f'1: {count} = {sum}')

count, sum = processJson(url2)
print(f'2: {count} = {sum}')
