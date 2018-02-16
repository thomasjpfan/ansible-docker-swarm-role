.PHONY: setup_test clean_up build test cycle

TAG ?= 1.0.0-docker-18.01.0-ce-py3
CLI_COMMAND := docker run --rm -v $(PWD):/etc/ansible/roles/role_to_test \
	--name runner -v /var/run/docker.sock:/var/run/docker.sock:ro
DOCKER_HUB_REPO ?= thomasjpfan/ansible-docker-runner

build:
	docker build -t $(DOCKER_HUB_REPO):$(TAG) -f python$(PY_VERSION)/Dockerfile .

test:
	$(CLI_COMMAND) -ti $(DOCKER_HUB_REPO):$(TAG) cli all

cli:
	$(CLI_COMMAND) -ti $(DOCKER_HUB_REPO):$(TAG) /bin/sh

setup_test:
	docker-compose -f tests/docker-compose.yml up -d

clean_up:
	docker-compose -f tests/docker-compose.yml down

cycle: setup_test test clean_up
