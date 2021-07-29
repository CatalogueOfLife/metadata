import os, requests, json
from pathlib import Path

API="http://api.catalogueoflife.org"
USER="markus"
PASS="xxx"


def update(f):
    key=f.name[:4]
    print("  PUT Dataset {}".format(key))
    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/x-yaml'}
    r=requests.put(API+"/dataset/"+key, data=open(f, 'rb'), headers=headers, auth=(USER, PASS))
    if r.status_code != 204:
        print(r.status_code)
        print(r.json())


update(Path("1010-metadata.yaml"))
update(Path("1019-metadata.yaml"))
update(Path("1021-metadata.yaml"))
update(Path("1026-metadata.yaml"))
update(Path("1061-metadata.yaml"))
update(Path("1065-metadata.yaml"))
update(Path("1076-metadata.yaml"))
update(Path("1089-metadata.yaml"))
update(Path("1133-metadata.yaml"))
update(Path("1158-metadata.yaml"))
update(Path("1167-metadata.yaml"))
update(Path("1168-metadata.yaml"))
update(Path("1170-metadata.yaml"))
update(Path("1173-metadata.yaml"))
update(Path("1192-metadata.yaml"))
update(Path("2144-metadata.yaml"))


#print("Updating datasets from latest YAML metadata...\n")
#for f in os.scandir("."):
#    if f.is_file() and f.name.endswith("-metadata.yaml"):
#        update(f)

