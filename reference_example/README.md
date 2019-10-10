## Building a reference set (example)

Use `parse_edu_json.py` to build a reference set of .edu domains based off the 
`world_universities_and_domains.json` dataset [1].

```
$ curl -o world_universities_and_domains.json https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json
$ python parse_edu_json.py
# generates reference.txt for use in domain-validator -r [file]
```

[1] https://github.com/Hipo/university-domains-list