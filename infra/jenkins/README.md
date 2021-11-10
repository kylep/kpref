# Jenkins

Since JenkinsX is not supported on private clouds, the old plugin-based Jenkins is what we've got.

## Install

```
kubectl create ns kpref-jenkins
kubectl config set-context --current --namespace=kpref-jenkins

helm repo add jenkinsci https://charts.jenkins.io
helm install kpref-jenkins jenkinsci/jenkins --values jenkins-values.yaml --namespace kpref-jenkins
```

## Get the admin user

```
kubectl exec --namespace kpref-jenkins -it svc/kpref-jenkins -c jenkins -- /bin/cat /run/secrets/chart-admin-password && echo
```


