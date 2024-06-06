#!/usr/bin/python3

import sys
import yaml

pkg_name = sys.argv[1]
repo_url = sys.argv[2]
new_version = sys.argv[3]

yaml_path = 'humble/distribution.yaml'
with open(yaml_path, 'r') as f:
    y = yaml.safe_load(f)

y['repositories'][pkg_name]['release']['url'] = repo_url
y['repositories'][pkg_name]['release']['version'] = new_version

with open(yaml_path, 'w') as f:
    yaml.dump(y, f, default_flow_style=False, sort_keys=False)

