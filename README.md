# azure-kubernetes-infrastructure
This project contains a Terraform template to deploy a customizable Kubernetes cluster with Azure Kubernetes Service.

## Deploy AKS Cluster

Log into your Azure account
``` bash
az login 
```
``` bash 
az account set --subscription="SUBSCRIPTION_ID"
```

If it is the first time running the cluster run the following commands:

``` bash 
cd scripts
./createTFRemoteState.sh
```

Deploy the Kubernetes Cluster

``` bash 
cd scripts
./deployAksSolution.sh
```

Destroy the Kubernetes Cluster

``` bash 
cd terraform
terraform destroy
```
