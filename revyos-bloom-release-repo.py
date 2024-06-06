#!/usr/bin/python3

import re
import sys
import yaml

release_repo_url=sys.argv[1]

yaml_file = 'tracks.yaml'

with open(yaml_file, 'r') as f:
    y = yaml.safe_load(f)

actions = y["tracks"]["humble"]["actions"][:]

for s in y["tracks"]["humble"]["actions"]:
    if re.search(r'(rhel|fedora|ubuntu)', s):
        actions.remove(s)
    if re.search('name debian', s):
        new_match = re.search(r'.*(?= )', s)
        actions[actions.index(s)] = new_match.group()

y["tracks"]["humble"]["actions"] = actions

y["tracks"]["humble"]["release_repo_url"] = release_repo_url

with open(yaml_file, 'w') as f:
    yaml.dump(y, f, default_flow_style=False, sort_keys=False)
