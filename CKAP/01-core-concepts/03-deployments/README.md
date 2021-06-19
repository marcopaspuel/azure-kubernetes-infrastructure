## Deploy a Deployment to the Cluster

Create
``` bash 
kubectl create -f deployment-definition.yaml -n default
```
Rolling Upgrade
``` bash
kubectl apply -f deployment-definition.yaml -n default
```
Describe
``` bash
kubectl describe deployment myapp-deployment -n default
```
