import os, requests, json

API="http://api.dev.catalogueoflife.org"
USER="frank"
PASS="xyz"


def update(d):
    print("Update {}".format(d.name))
    for f in os.scandir(d):
        if f.is_file() and f.name.endswith("latest.yaml"):
            key=f.name[:4]
            print("  PUT Dataset {}".format(key))
            headers = {'Accept' : 'application/json', 'Content-Type' : 'application/x-yaml'}
            r=requests.put(API+"/dataset/"+key, data=open(f, 'rb'), headers=headers, auth=(USER, PASS))
            print(r.status_code)

print("Updating datasets from latest YAML metadata...\n")
for f in os.scandir("."):
    if f.is_dir() and not f.name.startswith("."):
        update(f)
