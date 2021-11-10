#!/usr/bin/env python3
""" List the LUNS and their names """
import urllib3
import os
import sys
from storops import UnitySystem  # https://github.com/emc-openstack/storops
from storops.connection.exceptions import HTTPClientError

# Disable HTTPS warnings
urllib3.disable_warnings()

# get hostname from posargs

if len(sys.argv) != 2:
    sys.stderr.write('ERROR: expected a hostname pos arg\n')
    sys.exit(1)
hostname = sys.argv[1]
print(f"Finding luns on {hostname}")
print("")

# collect environment vars
def env(var):
    """ get an env var or error """
    if var not in os.environ:
        sys.stderr.write(f"ERROR: env var {var} is required\n")
        sys.exit(1)
    return os.environ[var]

san_ip = env("UNITY_IP")
username = env("UNITY_USER")
password = env("UNITY_PASS")
pool_name = env("UNITY_POOL")

unity = UnitySystem(host=san_ip, username=username, password=password, verify=False)
luns = unity.get_lun()

print("hostname - name - description - wwid")
for lun in luns:
    if not getattr(lun, "host_access"):
        continue
    bwhosts = [h.host.name for h in lun.host_access if hostname in h.host.name]
    if not bwhosts:
        continue
    wwid = lun.wwn.replace(":","").lower()
    print(f"{hostname} - {lun.name} - {lun.description} - {wwid}")
