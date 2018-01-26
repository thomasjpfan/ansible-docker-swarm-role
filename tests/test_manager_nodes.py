testinfra_hosts = ['tests_server1_1', 'tests_server3_1']


def test_node_is_manager(host):
    cmd = "docker info -f '{{ .Swarm.ControlAvailable }}'"
    output = host.check_output(cmd)
    assert output == "true"


def test_number_of_managers(host):
    cmd = "docker info -f '{{ .Swarm.Managers }}'"
    output = host.check_output(cmd)

    assert output == "2"


def test_number_of_workers(host):
    cmd = "docker info -f '{{ .Swarm.Nodes }}'"
    output = host.check_output(cmd)

    assert output == "4"
