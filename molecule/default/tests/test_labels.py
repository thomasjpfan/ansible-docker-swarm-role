import json
import pytest

testinfra_hosts = ['instance-1']

HOST_LABELS = [('instance-1', {
    'db': 'true'
}), ('instance-3', {
    'dog': 'big'
}), ('instance-2', {
    'docker': '18.06',
    'type': 'queue'
}), ('instance-4', {})]


@pytest.mark.parametrize('hostname, labels', HOST_LABELS)
def test_labels(host, hostname, labels):
    cmd = "docker inspect %s"
    inspect_str = host.check_output(cmd, hostname)
    inspect_dict = json.loads(inspect_str)

    assert inspect_dict[0]["Spec"]["Labels"] == labels
