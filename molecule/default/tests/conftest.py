import pytest


@pytest.fixture(scope="module")
def docker_info(host):
    cmd = "docker info"
    output = host.check_output(cmd)
    return output
