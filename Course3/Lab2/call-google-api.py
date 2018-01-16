import urllib.request, urllib.parse
import json

apiUrl = r'http://py4e-data.dr-chuck.net/geojson'

class GoogleClient(object):
    def __init__(self, baseUrl):
        self._baseUrl = baseUrl + ('' if baseUrl.endswith('?') else '?')

    @property
    def baseUrl (self): return self._baseUrl

    def makeCall (self, argumentsDic):
        url = self._baseUrl + urllib.parse.urlencode(argumentsDic)        
        with urllib.request.urlopen(url) as reader:
            data = reader.read().decode()

        try:
            doc = json.loads(data)
            exc = None
        except Exception as e:
            doc = None
            exc = e

        if not doc or 'status' not in doc or doc['status'] != 'OK':
            raise Exception('Can not prase JSON response') from exc

        return doc

client = GoogleClient(apiUrl)
#result = client.makeCall({'address': 'South Federal University'})
#print(json.dumps(result, indent=4))
#print(result['results'][0]['place_id'])

result = client.makeCall({'address': 'Czech Technical University in Prague'})
print(result['results'][0]['place_id'])
        
