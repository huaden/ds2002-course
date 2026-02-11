#!/workspaces/ds2002-course/mywork/lab3/venv/bin/python

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

print(url)

r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)