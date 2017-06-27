import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('client')


def test_node_exporter_service(Service):
    node_exporter = Service("node_exporter")
    assert node_exporter.is_running
    assert node_exporter.is_enabled
