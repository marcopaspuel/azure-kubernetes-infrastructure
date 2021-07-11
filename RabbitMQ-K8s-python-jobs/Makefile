## Deploy the simplest RabbitMQ on K8S
.PHONY: rabbitmq
rabbitmq:
	kubectl apply --filename k8s/statefulset.yml

## Make simplest RabbitMQ on K8S public
.PHONY: public
public:
	kubectl apply --filename k8s/service.yml
