testinfra_hosts = ['tests_server2_1', 'tests_server4_1']


def test_node_is_worker(host):
    cmd = "docker info -f '{{ .Swarm.ControlAvailable }}'"
    output = host.check_output(cmd)
    assert output == "false"
