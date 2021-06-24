## Kubernetes Python Client

Using the kubernetes python client to post jobs.

### Prerequisites 
- [Kubernetes Python Client](https://github.com/kubernetes-client/python/)

List all the pods in the cluster 
``` bash 
python3 list_all_pods.py
```

Create a K8s Job with the throw dice pod
``` bash 
python3 job_creator_dice.py
```

Generate json configuration from yaml manifest 
``` bash 
kubectl create -f throw-dice-pod.yaml --dry-run=client -o json
```
