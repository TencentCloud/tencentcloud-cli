**Example 1: 创建指标采集**

创建基础监控指标采集配置

Input: 

```
tccli cls CreateMetricConfig --cli-unfold-argument  \
    --TopicId d7adf66d-88a7-4321-8b4b-6f2c7a9773b8 \
    --Source 1 \
    --GroupIds 886bf7a8-7340-4314-8d64-b360da0ffd78 \
    --Type 1 \
    --Flag 1 \
    --YamlSpec.Type ScrapeConfig-prometheus \
    --YamlSpec.Spec scrape_configs:
- job_name: cadvisor
  honor_timestamps: false
  metrics_path: /metrics
  scheme: https
  kubernetes_sd_configs:
  - role: node
  bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
  tls_config:
    ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
  relabel_configs:
  - source_labels: [__meta_kubernetes_node_name]
    separator: ;
    regex: (.*)
    target_label: __address__
    replacement: kubernetes.default.svc:443
    action: replace
  - source_labels: [__meta_kubernetes_node_name]
    separator: ;
    regex: (.+)
    target_label: __metrics_path__
    replacement: /api/v1/nodes/${1}/proxy/metrics/cadvisor
    action: replace
  - separator: ;
    regex: __meta_kubernetes_node_label_(.+)
    replacement: $1
    action: labelmap
  - separator: ;
    regex: eks_tke_cloud_tencent_com_(.+)
    replacement: $1
    action: labeldrop
  metric_relabel_configs:
  - source_labels: [container_name]
    separator: ;
    regex: (.+)
    target_label: container
    replacement: $1
    action: replace
  - source_labels: [pod_name]
    separator: ;
    regex: (.+)
    target_label: pod
    replacement: $1
    action: replace
  - source_labels: [container]
    separator: ;
    regex: (.*)
    replacement: $1
    action: keep
---
scrape_configs:
- job_name: kube-state-metric
  honor_timestamps: true
  metrics_path: /metrics
  scheme: http
  kubernetes_sd_configs:
  - role: endpoints
    namespaces:
      names:
      - kube-system
    selectors:
      - label: "app.kubernetes.io/name==kube-state-metrics"
        role: endpoints
  bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
  tls_config:
    insecure_skip_verify: true
  metric_relabel_configs:
  - source_labels: [__name__, resource, unit]
    separator: ;
    regex: kube_pod_container_resource_requests;cpu;core
    target_label: __name__
    replacement: kube_pod_container_resource_requests_cpu_cores
    action: replace
  - source_labels: [__name__, resource, unit]
    separator: ;
    regex: kube_pod_container_resource_limits;cpu;core
    target_label: __name__
    replacement: kube_pod_container_resource_limits_cpu_cores
    action: replace
  - source_labels: [__name__, resource, unit]
    separator: ;
    regex: kube_pod_container_resource_requests;memory;byte
    target_label: __name__
    replacement: kube_pod_container_resource_requests_memory_bytes
    action: replace
  - source_labels: [__name__, resource, unit]
    separator: ;
    regex: kube_pod_container_resource_limits;memory;byte
    target_label: __name__
    replacement: kube_pod_container_resource_limits_memory_bytes
    action: replace
  - source_labels: [__name__, resource, unit]
    separator: ;
    regex: kube_node_status_capacity;cpu;core
    target_label: __name__
    replacement: kube_node_status_capacity_cpu_cores
    action: replace
  - source_labels: [__name__, resource, unit]
    separator: ;
    regex: kube_node_status_capacity;memory;byte
    target_label: __name__
    replacement: kube_node_status_capacity_memory_bytes
    action: replace
  - source_labels: [__name__, resource, unit]
    separator: ;
    regex: kube_node_status_allocatable;cpu;core
    target_label: __name__
    replacement: kube_node_status_allocatable_cpu_cores
    action: replace
  - source_labels: [__name__, resource, unit]
    separator: ;
    regex: kube_node_status_allocatable;memory;byte
    target_label: __name__
    replacement: kube_node_status_allocatable_memory_bytes
    action: replace
---
scrape_configs:
- job_name: node-exporter
  honor_timestamps: true
  metrics_path: /metrics
  scheme: http
  kubernetes_sd_configs:
  - role: endpoints
    namespaces:
      names:
      - kube-system
    selectors:
    - label: "app.kubernetes.io/name==node-exporter"
      role: endpoints
  bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
  tls_config:
    insecure_skip_verify: true
  relabel_configs:
  - separator: ;
    action: replace
    regex: (.*)
    replacement: $1
    source_labels: [__meta_kubernetes_pod_node_name]
    target_label: instance
```

Output: 
```
{
    "Response": {
        "ConfigIds": [
            "1bfadff7-9c5d-48c2-b985-21670d9d007e",
            "82182b27-7997-439d-bcc3-22a5c9da3bc4",
            "b8c24595-6fce-489c-8488-9d2db440fd9d"
        ],
        "RequestId": "e163af1b-fd31-4cef-b820-cb897e4644cf"
    }
}
```

