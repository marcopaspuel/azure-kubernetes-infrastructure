## Deploy a Multi-Container POD to the Cluster

Create
``` bash 
kubectl create -f yellow-pod.yaml -n default
```
Get the logs from the container
``` bash
kubectl -n elastic-stack exec -it app cat /log/app.log
```
