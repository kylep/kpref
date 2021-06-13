Vault manages the secrets of the apps. Normally it should be deployed on a dedicated cluster,
but for dev purposes this setup works.

```bash
helm repo add hashicorp https://helm.releases.hashicorp.com
# helm search repo hashicorp/vault --versions

kubectl create namespace vault

helm install vault hashicorp/vault -n vault -f vault-values.yaml --version 0.12.0

```
