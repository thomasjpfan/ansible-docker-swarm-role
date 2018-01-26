# Ansible Docker Swarm

[![Build Status](https://travis-ci.org/thomasjpfan/ansible-docker-swarm-role.svg?branch=master)](https://travis-ci.org/thomasjpfan/ansible-docker-swarm-role)

Configures a Docker Swarm cluster.

## Requirements

- `docker` installed on hosts

## Role Variables

```yaml
# Port docker swarm will communicate on
docker_swarm_port: 2377

# Network interface to use
docker_swarm_network_interface: "eth0"
```

## Usage

When starting a docker swarm the following ports must be open:

- 2377/tcp (`docker_swarm_port`)
- 7946/tcp
- 7946/udp
- 4789/udp
- 50/esp

This information can be found on docker's [documentation](https://docs.docker.com/engine/swarm/swarm-tutorial/#open-protocols-and-ports-between-the-hosts).

### Docker Manager and Workers

This role configures hosts in group `docker_swarm_manager` to be manager nodes and hosts in group `docker_swarm_worker` to be worker nodes:

```ini
[docker_swarm_manager]
tests_server1_1
tests_server3_1

[docker_swarm_worker]
tests_server2_1
tests_server4_1
```

### Docker Swarm Labels

Swarm labels can be added to nodes by setting the `docker_swarm_label` to a list of strings:

```ini
...
[docker_swarm_manager]
tests_server1_1 docker_swarm_labels="{'db':'true'}"
tests_server3_1 docker_swarm_labels="{'dog':'big'}"

[docker_swarm_worker]
tests_server2_1 docker_swarm_labels="{'docker':'17.12', 'type':'queue'}"
tests_server4_1
...
```

## Testing

This project uses [ansible-ubuntu-local-runner)](https://github.com/thomasjpfan/ansible-ubuntu-local-runner) to run tests in a docker container.

1. Start Container for testing:

```bash
make setup_test
```

2. Run Tests

```bash
make test
```

3. Stop up container

```bash
make clean_up
```

## License

MIT