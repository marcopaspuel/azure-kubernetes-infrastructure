.PHONY: k9s
k9s: ## Interact with K8S via terminal UI
	k9s --namespace default

.PHONY: rabbitmq
rabbitmq: ## Deploy the simplest RabbitMQ on K8S
	kubectl apply --filename k8s/statefulset.yml

.PHONY: rabbitmq-rm
rabbitmq-rm: ## Delete RabbitMQ and all linked resources
	kubectl delete --ignore-not-found=true --filename k8s

.PHONY: shell
shell: ## Open shell in RabbitMQ node
	kubectl exec -it rabbitmq-0 -- /bin/bash

.PHONY: persistent
persistent: ## Give RabbitMQ on K8S persistent storage
	kubectl apply --filename k8s/persistentvolumeclaim.yml
	yq eval-all 'select(fileIndex == 0) * select(fileIndex == 1)' k8s/statefulset* | kubectl apply --filename -

.PHONY: public
public: ## Make simplest RabbitMQ on K8S public
	kubectl apply --filename k8s/service.yml

.PHONY: benchmark
benchmark: ## Benchmark simplest RabbitMQ on K8S
	kubectl create --filename k8s/benchmark.job

.PHONY: all
all: rabbitmq public benchmark ## Deploy RabbitMQ, make public & [persistent], then benchmark

.PHONY: clean
clean: rabbitmq-rm ## Delete RabbitMQ and all linked resources.
