#!/bin/bash
# be root

# install kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.0/kind-linux-amd64
chmod +x ./kind
mv ./kind /usr/bin/kind

# install docker and kubectl
apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/nul
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io kubectl

# install clusterctl
curl -L https://github.com/kubernetes-sigs/cluster-api/releases/download/v0.3.18/clusterctl-linux-amd64 -o clusterctl
chmod +x ./clusterctl
mv ./clusterctl /usr/local/bin/clusterctl
clusterctl version

# install openstack client (optional)
apt-get  install -y python3-pip
pip install python-openstackclient
mkdir -p /etc/openstack

# get the env config tools/script
snap install yq
wget https://raw.githubusercontent.com/kubernetes-sigs/cluster-api-provider-openstack/master/templates/env.rc -O /tmp/env.rc
