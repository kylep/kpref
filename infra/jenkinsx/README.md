# jenkins-x

Jenkins-X will handle the CICD of the app.

## Install

https://jenkins-x.io/docs/resources/guides/managing-jx/old/install-on-cluster/

### Get the jx CLI tool

Install the `jx` command. On mac run
```
brew install jenkins-x/jx/jx
```

See [here](https://jenkins-x.io/docs/install-setup/install-binary/) for other OS steps.


### Check compliance


```
# This takes like an hour, skip it if you're sure it'll pass
jx compliance run
jx compliance status

# Compliance tests are still running, it can take up to 60 minutes. ... wait
while true; do date; jx compliance status; sleep 60; done

jx compliance results

jx compliance delete
```

### Run the install

`jx` REALLY wants to be used on GKE, so this will fail.

```
jx boot
```

Edit `jx-requirements.yml` and set `provider: kubernetes`. Try it again. It'll still fail, but
further along the install this time.

The current `jx boot` command is defective and does not work with the new format of GitHub tokens
that are now issued. Run the command then fix it up. Once this [bug](https://github.com/jenkins-x/jx/issues/7633)
is closed, the issue will be resolved.

```
jx boot
```

Now it will error out when you try and pass your GitHub token saying that it doesn't match the
regex. From inside the `jenkins-x-boot-config` directory, fix the defect.

`vi ./env/parameters.tmpl.schema.json`

Change `"pattern": "^[0-9a-f]{40}$` to `"pattern": "^[0-9a-zA-Z_]{40}$"`

Then re-run the boot wizard

```
jx boot
```

Then it will fail with

```
error: failed to lint the chart '/var/folders/95/31l7sb597p3107yds9lky4tc0000gn/T/jx-helm-apply-584207017/env': failed to run 'helm lint --set tags.jx-lint=true --set global.jxLint=true --set-string global.jxTypeEnv=lint' command in directory '/var/folders/95/31l7sb597p3107yds9lky4tc0000gn/T/jx-helm-apply-584207017/env', output: '==> Linting .
[ERROR] templates/: render error in "env/charts/jenkins-x-platform/templates/ssh-config-secret.yaml": template: env/charts/jenkins-x-platform/templates/ssh-config-secret.yaml:3:14: executing "env/charts/jenkins-x-platform/templates/ssh-config-secret.yaml" at <.Values.PipelineSecrets.SSHConfig>: nil pointer evaluating interface {}.SSHConfig

Error: 1 chart(s) linted, 1 chart(s) failed'
error: failed to interpret pipeline file jenkins-x.yml: failed to run '/bin/sh -c jx step helm apply --boot --remote --name jenkins-x --provider-values-dir ../kubeProviders' command in directory 'env', output: ''
```

At this point, you might decide that Jenkins X is not ready for production and use something else.
That seems like a good idea to me, too. It probably works on GKE, which is of zero use for private
clouds.

