**Example 1: 获取指标采集基础监控配置信息**

获取指标采集基础监控配置信息

Input: 

```
tccli cls DescribeTopicBaseMetricConfigs --cli-unfold-argument  \
    --TopicId d7adf66d-88a7-4321-8b4b-6f2c7a9773b8 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Datas": [
            {
                "Configs": [
                    {
                        "ConfigId": "6886a667-77eb-4363-ad5a-906d1481fe04",
                        "CreateTime": 1724244707,
                        "Flag": 1,
                        "GroupIds": [
                            "43948ea4-f286-4636-adfd-92aa0fc8344e"
                        ],
                        "HonorLabels": false,
                        "Name": "node-exporter",
                        "Operate": 0,
                        "Scheme": "",
                        "ScrapeInterval": "",
                        "ScrapeTimeout": "",
                        "Source": 0,
                        "TopicIds": [
                            "d7adf66d-88a7-4321-8b4b-6f2c7a9773b8"
                        ],
                        "Type": 0,
                        "UpdateTime": 1724244707,
                        "YamlSpec": {
                            "Spec": "job_name: node-exporter\nhonor_timestamps: true\ntrack_timestamps_staleness: false\nmetrics_path: /metrics\nscheme: http\nenable_compression: true\nauthorization:\n  type: Bearer\n  credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token\ntls_config:\n  insecure_skip_verify: true\nfollow_redirects: true\nenable_http2: true\nhttp_headers: null\nrelabel_configs:\n- source_labels: [__meta_kubernetes_pod_node_name]\n  separator: ;\n  regex: (.*)\n  target_label: instance\n  replacement: $1\n  action: replace\n",
                            "Type": "ScrapeConfig-prometheus"
                        }
                    },
                    {
                        "ConfigId": "853fd8d1-77ec-4815-8696-5e2e029fba21",
                        "CreateTime": 1724244707,
                        "Flag": 1,
                        "GroupIds": [
                            "43948ea4-f286-4636-adfd-92aa0fc8344e"
                        ],
                        "HonorLabels": false,
                        "Name": "kube-state-metric",
                        "Operate": 0,
                        "Scheme": "",
                        "ScrapeInterval": "",
                        "ScrapeTimeout": "",
                        "Source": 0,
                        "TopicIds": [
                            "d7adf66d-88a7-4321-8b4b-6f2c7a9773b8"
                        ],
                        "Type": 0,
                        "UpdateTime": 1724244707,
                        "YamlSpec": {
                            "Spec": "job_name: kube-state-metric\nhonor_timestamps: true\ntrack_timestamps_staleness: false\nmetrics_path: /metrics\nscheme: http\nenable_compression: true\nauthorization:\n  type: Bearer\n  credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token\ntls_config:\n  insecure_skip_verify: true\nfollow_redirects: true\nenable_http2: true\nhttp_headers: null\nmetric_relabel_configs:\n- source_labels: [__name__, resource, unit]\n  separator: ;\n  regex: kube_pod_container_resource_requests;cpu;core\n  target_label: __name__\n  replacement: kube_pod_container_resource_requests_cpu_cores\n  action: replace\n- source_labels: [__name__, resource, unit]\n  separator: ;\n  regex: kube_pod_container_resource_limits;cpu;core\n  target_label: __name__\n  replacement: kube_pod_container_resource_limits_cpu_cores\n  action: replace\n- source_labels: [__name__, resource, unit]\n  separator: ;\n  regex: kube_pod_container_resource_requests;memory;byte\n  target_label: __name__\n  replacement: kube_pod_container_resource_requests_memory_bytes\n  action: replace\n- source_labels: [__name__, resource, unit]\n  separator: ;\n  regex: kube_pod_container_resource_limits;memory;byte\n  target_label: __name__\n  replacement: kube_pod_container_resource_limits_memory_bytes\n  action: replace\n- source_labels: [__name__, resource, unit]\n  separator: ;\n  regex: kube_node_status_capacity;cpu;core\n  target_label: __name__\n  replacement: kube_node_status_capacity_cpu_cores\n  action: replace\n- source_labels: [__name__, resource, unit]\n  separator: ;\n  regex: kube_node_status_capacity;memory;byte\n  target_label: __name__\n  replacement: kube_node_status_capacity_memory_bytes\n  action: replace\n- source_labels: [__name__, resource, unit]\n  separator: ;\n  regex: kube_node_status_allocatable;cpu;core\n  target_label: __name__\n  replacement: kube_node_status_allocatable_cpu_cores\n  action: replace\n- source_labels: [__name__, resource, unit]\n  separator: ;\n  regex: kube_node_status_allocatable;memory;byte\n  target_label: __name__\n  replacement: kube_node_status_allocatable_memory_bytes\n  action: replace\n",
                            "Type": "ScrapeConfig-prometheus"
                        }
                    },
                    {
                        "ConfigId": "1bac0b5b-7bbe-4612-8831-5d445da9553d",
                        "CreateTime": 1724244707,
                        "Flag": 1,
                        "GroupIds": [
                            "43948ea4-f286-4636-adfd-92aa0fc8344e"
                        ],
                        "HonorLabels": false,
                        "Name": "cadvisor",
                        "Operate": 0,
                        "Scheme": "",
                        "ScrapeInterval": "",
                        "ScrapeTimeout": "",
                        "Source": 0,
                        "TopicIds": [
                            "d7adf66d-88a7-4321-8b4b-6f2c7a9773b8"
                        ],
                        "Type": 0,
                        "UpdateTime": 1724244707,
                        "YamlSpec": {
                            "Spec": "job_name: cadvisor\nhonor_timestamps: false\ntrack_timestamps_staleness: false\nmetrics_path: /metrics\nscheme: https\nenable_compression: true\nauthorization:\n  type: Bearer\n  credentials_file: /var/run/secrets/kubernetes.io/serviceaccount/token\ntls_config:\n  ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt\n  insecure_skip_verify: false\nfollow_redirects: true\nenable_http2: true\nhttp_headers: null\nrelabel_configs:\n- source_labels: [__meta_kubernetes_node_name]\n  separator: ;\n  regex: (.*)\n  target_label: __address__\n  replacement: kubernetes.default.svc:443\n  action: replace\n- source_labels: [__meta_kubernetes_node_name]\n  separator: ;\n  regex: (.+)\n  target_label: __metrics_path__\n  replacement: /api/v1/nodes/${1}/proxy/metrics/cadvisor\n  action: replace\n- separator: ;\n  regex: __meta_kubernetes_node_label_(.+)\n  replacement: $1\n  action: labelmap\n- separator: ;\n  regex: eks_tke_cloud_tencent_com_(.+)\n  replacement: $1\n  action: labeldrop\nmetric_relabel_configs:\n- source_labels: [container_name]\n  separator: ;\n  regex: (.+)\n  target_label: container\n  replacement: $1\n  action: replace\n- source_labels: [pod_name]\n  separator: ;\n  regex: (.+)\n  target_label: pod\n  replacement: $1\n  action: replace\n- source_labels: [container]\n  separator: ;\n  regex: (.*)\n  replacement: $1\n  action: keep\n",
                            "Type": "ScrapeConfig-prometheus"
                        }
                    }
                ],
                "GroupId": "43948ea4-f286-4636-adfd-92aa0fc8344e"
            }
        ],
        "RequestId": "c8db920f-a681-44a6-a22b-c8d5d40a09fe",
        "TotalCount": 1
    }
}
```

