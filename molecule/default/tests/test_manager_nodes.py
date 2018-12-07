testinfra_hosts = ['instance-1', 'instance-2']


def test_node_is_manager(docker_info):
    assert "Is Manager" in docker_info


def test_number_of_managers(docker_info):
    assert "Managers: 2" in docker_info


def test_number_of_workers(docker_info):
    assert "Nodes: 4" in docker_info
