import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('server')


def test_node_exporter_service(Service):
    node_exporter = Service("node_exporter")
    assert node_exporter.is_running
    assert node_exporter.is_enabled

def test_node_exporter_port(Socket):
    ne_port = Socket("tcp://:::9100")
    assert ne_port.is_listening

def test_prometheus_service(Service):
    prometheus = Service("prometheus")
    assert prometheus.is_running
    assert prometheus.is_enabled

def test_prometheus_port(Socket):
    p_port = Socket("tcp://:::9090")
    assert p_port.is_listening

def test_alertmanager_service(Service):
    alertmanager = Service("alertmanager")
    assert alertmanager.is_running
    assert alertmanager.is_enabled

def test_alertmanager_port(Socket):
    a_port = Socket("tcp://:::9093")
    assert a_port.is_listening
