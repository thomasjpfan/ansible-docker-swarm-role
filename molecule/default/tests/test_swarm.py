def test_docker_running(host):
    docker = host.service("docker")
    assert docker.is_enabled
    assert docker.is_running


def test_swarm_is_active(docker_info):
    assert "Swarm: active" in docker_info
