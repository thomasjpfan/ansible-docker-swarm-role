import json
import pytest

testinfra_hosts = ['tests_server1_1']

HOST_LABELS = [('tests_server1_1', {
    'db': 'true'
}), ('tests_server3_1', {
    'dog': 'big'
}), ('tests_server2_1', {
    'docker': '18.06',
    'type': 'queue'
}), ('tests_server4_1', {})]


@pytest.mark.parametrize('hostname, labels', HOST_LABELS)
def test_labels(host, hostname, labels):
    cmd = "docker inspect -f '{{  json .Spec.Labels }}' %s"
    label_json = host.check_output(cmd, hostname)
    labels_dict = json.loads(label_json)

    assert labels == labels_dict
