import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('dockerhost')


def test_node_exporter_service(Service):
    node_exporter = Service("node_exporter")
    assert node_exporter.is_running
    assert node_exporter.is_enabled

def test_node_exporter_port(Socket):
    ne_port = Socket("tcp://9100")
    assert ne_port.is_listening

