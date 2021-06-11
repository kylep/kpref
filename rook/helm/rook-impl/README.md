# STOP - Helm is not the right tool for this job!

Helm is, it seems, a bad way to implement your rook resources.

You can't cleanly delete Ceph's stuff without cleaning up on the host, plus you had to add vols
to the host in the first place which is very not-helm-ish.

Instead, run things part by part. You need to wait a bit, anways.


## Deploy the cluster

from `templates/` with your current'context in `rook-ceph`:

```bash
# Start the cluster
kubectl apply -f cluster.yaml

# get the name of the operator
kubectl get pods | grep operator

# watch the cluster build and make sure it doesn't error out
kubectl logs -f <operator pod>

# you can also get the cephclusters.ceph.rook.io CRD to see the status
kubectl get cephclusters.ceph.rook.io

# once the cluster is up, add the toolbox
kubectl create -f toolbox.yaml

# Use the toolbox to show some ceph status details
kubectl exec -it deploy/rook-ceph-tools -- ceph -s
kubectl exec -it deploy/rook-ceph-tools -- ceph osd tree
kubectl exec -it deploy/rook-ceph-tools -- ceph osd lspools
```

## Deploy ceph-fs

```
# Deploy a filesystem
kubectl create -f filesytem-myfs.yaml

# Deploy a storageclass to use the filesystem
kubectl create -f cephfs-storageclass.yaml
```

### Confirm Ceph-FS works

Make a volume claim
```
kubctl create -f cephfs-pvc.yaml
```
If the volume is bound, that works.

Make a pod via a deployment with 2 replicas to show that it mounts and gets shared

```
kubectl create -f cephfs-pvc-sample-consumer-deployment.yaml
```


## Configure object storage

Make a CephObjectStore
```
kubectl create -f object.yaml
kubectl get CephObjectStore
```

## Deploy the web dashboard

It isn't really needed but it's kind of neat.

```
kubectl create -f dashboard-ingress-https.yaml
kubectl get ingress
```

Update your /etc/hosts file and point rook.local to the ingress IP.
Browse to https://rook.local in your browser to get to a login page.

Get the credentials:
```
kubectl get secret rook-ceph-dashboard-password -o jsonpath="{['data']['password']}" | base64 --decode && echo
```
