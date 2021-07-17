#! /bin/bash
set -euo pipefail

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# RabbitMQ
helm upgrade rabbitmq bitnami/rabbitmq \
  --install \
  --set auth.username=user \
  --set auth.password=PASSWORD \
  --namespace rabbitmq-system \
  --create-namespace
