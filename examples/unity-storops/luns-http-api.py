#!/usr/bin/env python3
""" List the LUNS and their names """
import base64
import urllib3
import os
import sys
import requests
from pprint import pprint

# I intercepted the storops query to see what it was doing then replayed it here. - Kyle

# Disable HTTPS warnings
urllib3.disable_warnings()


# Set fiddler proxy env vars
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:8866'
os.environ['http_proxy'] = 'http://127.0.0.1:8866'
os.environ['HTTPS_PROXY'] = 'https://127.0.0.1:8866'
os.environ['https_proxy'] = 'https://127.0.0.1:8866'


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

# unity = UnitySystem(host=san_ip, username=username, password=password, verify=False)
# luns = unity.get_lun()
# len(luns)

auth_bytes = bytes(f"{username}:{password}", "ascii")
basic_auth_header = base64.b64encode(auth_bytes).decode("ascii")

url = f"https://{san_ip|/api/types/lun/instances?compact=True&fields=auSize,creationTime,currentNode,dataReductionPercent,dataReductionRatio,dataReductionSizeSaved,defaultNode,description,effectiveIoLimitMaxIOPS,effectiveIoLimitMaxKBPS,familyBaseLun,familyCloneCount,familySizeAllocatedTotal,familySnapCount,health,hostAccess,hostAccess.host.name,id,instanceId,ioLimitPolicy,isAdvancedDedupEnabled,isDataReductionEnabled,isReplicationDestination,isSnapSchedulePaused,isThinClone,isThinEnabled,lunGroupObjectId,lunNumber,metadataSize,metadataSizeAllocated,modificationTime,moveSession,name,nonBaseSize,nonBaseSizeAllocated,objectId,operationalStatus,originalParentLun,parentSnap,perTierSizeUsed,pool,pool.isFASTCacheEnabled,pool.name,pool.raidType,sizeAllocated,sizeAllocatedTotal,sizePreallocated,sizeTotal,sizeUsed,smpBackendId,snapCount,snapSchedule,snapWwn,snapsSize,snapsSizeAllocated,storageResource,storageResource.type,tieringPolicy,type,wwn"

headers = {
    "User-agent": "EMC-OpenStack",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Accept_Language": "en_US",
    "Visibility": "Engineering",
    "X-EMC-REST-CLIENT": "true",
    "Authorization": f"Basic {basic_auth_header}"
}

# Get the data, print the names
resp = requests.get(url, headers=headers)
data = resp2.json()
luns = data["entries"]
for lun_dict in luns:
    lun = lun_dict["content"]
    print(lun["name"])

