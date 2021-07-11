#! /bin/bash
set -euo pipefail

helm repo add kedacore https://kedacore.github.io/charts
helm repo update

# KEDA
# https://keda.sh/docs/2.0/deploy/
helm upgrade keda kedacore/keda \
  --install \
  --version 2.3.2 \
  --namespace keda \
  --create-namespace
