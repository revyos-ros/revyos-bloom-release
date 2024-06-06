#!/usr/bin/python3

import sys
import yaml

yaml_path = sys.argv[1]
pkg_name = sys.argv[2]

with open(yaml_path, 'r') as f:
    y = yaml.safe_load(f)

# sometimes pkg_name in yaml is different from upstream_repo_name
real_pkg_name = 'ERR'
upstream_owner = 'ERR'
upstream_repo = 'ERR'

if pkg_name in y['repositories']:
    upstream_link = y['repositories'][pkg_name]['release']['url']
    # sample: https://github.com/revyos-ros/aerostack2-release.git
    # real_pkg_name: aerostack2
    # upstream_owner: revyos-ros
    # upstream_repo: aerostack2-release
    real_pkg_name = pkg_name
    upstream_owner = upstream_link.split('/')[-2]
    upstream_repo = upstream_link.split('/')[-1].split('.')[-1]
else:
    # 'repositories' -> PKG -> 'release' -> 'packages'
    for pkg in y['repositories']:
        found = False
        if 'release' not in y['repositories'][pkg]:
            continue
        if 'packages' in y['repositories'][pkg]['release']:
            for sub_pkg in y['repositories'][pkg]['release']['packages']:
                if pkg_name == sub_pkg:
                    upstream_link = y['repositories'][pkg]['release']['url']
                    real_pkg_name = pkg
                    upstream_owner = upstream_link.split('/')[-2]
                    upstream_repo = upstream_link.split('/')[-1].split('.')[-2]
                    found = True
                    break
        if found:
            break

print('{0} {1} {2}'.format(real_pkg_name, upstream_owner, upstream_repo))
