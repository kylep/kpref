# Rook

Rook provides PVs to the app.


## Deploy the Operator

The options for `rook-values.yaml` can be obtained by running
`helm inspect values rook-release/rook-ceph`.

```bash
helm repo add rook-release https://charts.rook.io/release
kubectl create namespace rook-ceph
helm install \
  --namespace rook-ceph \
  --values rook-operator-values.yaml \
  rook-ceph \
  rook-release/rook-ceph
```

Verify that the operator pod is now running:

```bash
kubectl -n rook-ceph get pods
```

## Add Disks to workers

On the worker nodes that will host Ceph, add some disks. You coud also use a partition or some
other block-type PV. Adding disks as Cinder volumes work well on Breqwatr OpenStack. Make them
the same size on each worker node.




