## Deploy a replicaSet to the Cluster

Create
``` bash 
kubectl create -f replica-definition.yaml -n default
```
Scale
``` bash
kubectl scale rs myapp-replicaset --replicas=3 -n default
```
