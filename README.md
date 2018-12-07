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
server1
server2

[docker_swarm_worker]
server3
server4
```

### Docker Swarm Labels

Swarm labels can be added to nodes by setting the `docker_swarm_label` to a list of strings:

```ini
...
[docker_swarm_manager]
server1 docker_swarm_labels="{'db':'true'}"
server2 docker_swarm_labels="{'dog':'big'}"

[docker_swarm_worker]
server3 docker_swarm_labels="{'docker':'17.12', 'type':'queue'}"
server4
...
```

## License

MIT
