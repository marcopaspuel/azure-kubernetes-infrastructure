## Deploy the simplest RabbitMQ on K8S
.PHONY: rabbitmq
rabbitmq:
	kubectl apply --filename k8s/statefulset.yml

## Make simplest RabbitMQ on K8S public
.PHONY: public
public:
	kubectl apply --filename k8s/service.yml

## Run publisher Job
.PHONY: run-publisher-job
run-publisher-job:
	kubectl apply --filename k8s/producer-job.yaml

## Delete publisher Job
.PHONY: delete-publisher-job
delete-publisher-job:
	kubectl delete --filename k8s/producer-job.yaml

## Deploy consumer pod
.PHONY: deploy-consumer-pod
deploy-consumer-pod:
	kubectl apply --filename k8s/consumer-pod.yaml