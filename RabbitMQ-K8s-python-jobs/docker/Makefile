OWNER := marcopaspuel
PROJECT := python-rmq-test
VERSION := 1.0.0
OPV := $(OWNER)/$(PROJECT):$(VERSION)

# builds docker image
docker-build:
	docker build -f Dockerfile -t $(OPV) .

## cleans docker image
clean:
	docker image rm $(OPV) | true

## pushes to docker hub
docker-push:
	docker push $(OPV)
