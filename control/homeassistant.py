import requests
import json

with open("config.json") as f:
   config = json.loads(f.read())

TOKEN = config['token']
DOMAIN = config['domain']

headers = {
        "Authorization": f"Bearer {TOKEN}",
        "content-type": "application/json"
    }

def lightToggle(lights, action):
    url = f"https://{DOMAIN}/api/services/light/{action}"

    data = {"entity_id": lights}
    requests.post(url, headers=headers, data=json.dumps(data))

def getState(light):
    url = f"https://{DOMAIN}/api/states/{light}"
    r = requests.get(url, headers=headers)
    entity = json.loads(r.text)

    return entity['state']