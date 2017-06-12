# ansible-prometheus-tests

This repository contains some tests of the ansible role [williamyeh.prometheus](https://github.com/William-Yeh/ansible-prometheus) implemented using [molecule](https://github.com/metacloud/molecule).

The test environment is composed by three vms:

1. Server VM. Which has installed the prometheus, the node_exporter service and the alarmexporter services.
2. Client VM. Which has only the node_exporter installed.
3. DockerHost VM. which has installed the docker server with [cadvisor](https://github.com/google/cadvisor) and Grafana containers.

All the metrics of each service can be retrieved at the url _http://[ip VM]:9100/metrics_ (node_exporter).

The prometheus server is running at _http://[Server_IP]:9090_

The Grafana frontend is at _http://[DockerVM_IP]:3000_

At the Grafana app some steps must be performed manually.

1. Login in Grafana (admin/foobar)
2. Add a data source of type `prometheus` pointing to the _http://[Server_IP]:9090_, direct access and without authentication
3. Import this three dashboards: [718](https://grafana.com/dashboards/718)  and [179](https://grafana.com/dashboards/179). (you can use only the id numbers to import the dashboards through the import wizard)

**Note: you can enter in a particular VM using the command `molecule login --host prometheus-idi-[server|client|docker]`**
