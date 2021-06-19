## Create a Namespace on the Cluster

Create
``` bash 
kubectl create -f namespace-dev.yml 
```

Create POD (with Namespace)
``` bash 
kubectl create -f pod-definition.yml
```

## Deploy Compute Quota
Rolling Upgrade
``` bash
kubectl create -f compute-quota.yaml
```
