# install

```
helm repo add jenkinsci https://charts.jenkins.io
helm repo update
helm search repo jenkinsci
```

Grab the jenkins values:

```
helm inspect values jenkinsci/jenkins > all-jenkins-values.yaml
```

Write a jenkins.values.yaml file using the values from the above file for your instance.
Deploy it.

```
helm install jenkinstest jenkinsci/jenkins --values jenkinsci.values.yaml
```
