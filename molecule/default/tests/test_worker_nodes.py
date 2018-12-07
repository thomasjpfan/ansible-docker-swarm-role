testinfra_hosts = ['instance-3', 'instance-4']


def test_node_is_worker(docker_info):
    assert "Is Manager: false" in docker_info
