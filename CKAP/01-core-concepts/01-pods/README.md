## Deploy a POD to the Cluster

Imperative
``` bash
kubectl run nginx --image=nginx --dry-run=client -o yaml > nginx-pod.yaml
```
With YAML
``` bash 
kubectl create -f nginx-pod.yaml -n default
```
