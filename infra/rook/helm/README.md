# Rook Implemented via Helm


Install the operator


These Helm manifests are used to *implement* Rook, not to distribute it. These can be considered
the IaC representation of how we want Rook to be deployed.

```
helm install -n rook-ceph -f rook-impl.yaml rook-impl rook-impl
```

Show the status

```
# Show the CRD
kubectl -n rook-ceph get cephclusters.ceph.rook.io

# Show ceph's status using the toolbox
kubectl -n rook-ceph exec -it deploy/rook-ceph-tools -- ceph -s
```


---

This was kind of helpful
https://www.cloudops.com/blog/the-ultimate-rook-and-ceph-survival-guide/

