import json

with open('world_universities_and_domains.json') as f:
    r = json.load(f)

with open('reference.txt','w') as f:
    for x in r:
        f.writelines(['{}\n'.format(d) for d in x['domains']])