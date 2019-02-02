CONTAINER_NAME := "napalm-inspector"


.PHONY: docker
docker:
	docker build . --tag napalm-inspector:latest


.PHONY: start
start: stop
	docker run -it --name $(CONTAINER_NAME) -p 5000:5000 napalm-inspector:latest


.PHONY: stop
stop:
	@docker rm $(CONTAINER_NAME) -f || exit 0