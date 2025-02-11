# Function converter for Open WebUI function plugin
# 
# author: Takashi Okamoto
#
# Currently(11/Feb/2025), Open WebUI can't import downloaded json from Open WebUI community site.
# This script convert downloaded function json to valid json to import.
# usage:
# $ python fix-openwebui-function.py < downloaded-function-json.json > function-to-import.json

import sys, json;


downloaded = json.load(sys.stdin)[0]
f = downloaded['function']
d = [{
  'id': downloaded['user']['id'].replace("-","_"),
  'name': f['name'],
  'meta': f['meta'],
  'content': f['content'],
  'userId': downloaded['user']['id'].replace("-","_"),
}
]

print(json.dumps(d))
