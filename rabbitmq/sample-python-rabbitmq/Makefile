OWNER := marcopaspuel
PROJECT := python-rmq-test
VERSION := 1.0.0
OPV := $(OWNER)/$(PROJECT):$(VERSION)

## cannot be evaluated in target and used in ifdef, ifdef evaluated during parse of makefile
ISRUNNING := $(shell docker ps -a -f name=my-rabbit --format='{{.Names}}' | wc -l )

# builds docker image
docker-build:
	docker build -f Dockerfile -t $(OPV) .

## cleans docker image
clean:
	docker image rm $(OPV) | true

## runs container in foreground, using default args
docker-test:
	docker run -it --rm $(OPV)

## runs container in foreground, override entrypoint to use use shell
docker-test-cli:
	docker run -it --rm --entrypoint "/bin/bash" $(OPV)

## runs with parameters passed from command line, examples:
## make docker-run CMD="./producer.py --host=192.168.1.100"
## make docker-run CMD="./consumer.py --host=192.168.1.100"
## make docker-run CMD="./get_ip.py"
docker-run: 
	docker run -it --rm $(OPV) $(CMD)

## pushes to docker hub
docker-push:
	docker push $(OPV)


## convenience tasks for running produer/consumer against privateIP of rmq
docker-run-producer: get-rabbitmq-ip
	docker run -it --rm $(OPV) ./producer.py --host=$(RMQ) $(CMD)
docker-run-consumer: get-rabbitmq-ip
	docker run -it --rm $(OPV) ./consumer.py --host=$(RMQ) $(CMD)

## gets IP address of running rabbit server
get-rabbitmq-ip:
	$(eval RMQ=$(shell docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-rabbit))


# runs rabbitmq server
run-rabbitmq-background:
	@echo ISRUNNING = $(ISRUNNING)
ifeq ($(ISRUNNING),1)
	@echo RabbitMQ server is already running, no need to startup container
else
	docker run --rm -it -d --hostname my-rabbit --name my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
	@echo
	@echo RabbitMQ server starting...
	sleep 20
	docker logs my-rabbit | grep startup
endif
	@echo
	$(eval RMQ=$(shell docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-rabbit))
	@echo RabbitMQ server listening at $(RMQ):5672 and also host server:5672
	@echo RabbitMQ web admin gui listening at $(RMQ):15672 and also host server:15672

# stops rabbitmq server
stop-rabbitmq:
	docker stop my-rabbit
