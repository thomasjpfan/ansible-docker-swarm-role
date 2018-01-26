testinfra_hosts = ['tests_server1_1', 'tests_server2_1',
                   'tests_server3_1', 'tests_server4_1']


def test_docker_running(host):
    docker = host.service("docker")
    assert docker.is_enabled
    assert docker.is_running


def test_swarm_is_active(host):
    cmd = "docker info -f '{{ .Swarm.LocalNodeState }}'"
    output = host.check_output(cmd)
    assert output == "active"
