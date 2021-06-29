import os, requests, json
from pathlib import Path

API="http://api.catalogueoflife.org"
USER="markus"
PASS=""


def update(d):
    print("Update {}".format(d.name))
    for f in os.scandir(d):
        if f.is_file() and f.name.endswith("latest.yaml"):
            key=f.name[:4]
            print("  PUT Dataset {}".format(key))
            headers = {'Accept' : 'application/json', 'Content-Type' : 'application/x-yaml'}
            r=requests.put(API+"/dataset/"+key, data=open(f, 'rb'), headers=headers, auth=(USER, PASS))
            if r.status_code != 204:
                print(r.status_code)
                print(r.json())

update(Path("Species Fungorum Plus"))

#print("Updating datasets from latest YAML metadata...\n")
#for f in os.scandir("."):
#    if f.is_dir() and not f.name.startswith("."):
#        update(f)
