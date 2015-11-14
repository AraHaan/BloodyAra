import requests
import json

def has_profanity(searchterm):
    r = requests.get('http://www.purgomalum.com/service/containsprofanity?text=' + searchterm)
    if (r.text == 'true'):
        return True
    r = requests.get('http://www.wdyl.com/profanity?q=' + searchterm)
    jsondata = json.loads(r.text)
    if(jsondata['response'] == 'true'):
        return True
    return False