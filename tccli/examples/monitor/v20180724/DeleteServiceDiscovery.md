**Example 1: 删除服务发现**



Input: 

```
tccli monitor DeleteServiceDiscovery --cli-unfold-argument  \
    --InstanceId prom-sdfk2342a \
    --Yaml apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: go-demo    # 填写一个唯一名称
  namespace: cm-prometheus  # namespace固定，不要修改
spec:
  endpoints:
  - interval: 30s
    # 填写service yaml中Prometheus Exporter对应的Port的Name
    port: 2112
    # 填写Prometheus Exporter对应的Path的值，不填默认/metrics
    path: /metrics
    relabelings:
    # ** 必须要有一个 label 为 application，这里假设 k8s 有一个 label 为 app，
    # 我们通过 relabel 的 replace 动作把它替换成了 application
    - action: replace
      sourceLabels:  [__meta_kubernetes_pod_label_app]
      targetLabel: application
  # 选择要监控service所在的namespace
  namespaceSelector:
    matchNames:
    - golang-demo
    # 填写要监控service的Label值，以定位目标service
  selector:
    matchLabels:
      app: golang-app-demo \
    --Type 1 \
    --KubeClusterId cls-pwerf3k3 \
    --KubeType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

