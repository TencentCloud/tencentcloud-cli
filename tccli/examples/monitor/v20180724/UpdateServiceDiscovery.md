**Example 1: 更新服务发现**



Input: 

```
tccli monitor UpdateServiceDiscovery --cli-unfold-argument  \
    --InstanceId prom-sdfk2342a \
    --KubeClusterId cls-pwerf3k3 \
    --KubeType 1 \
    --Type 1 \
    --Yaml yaml
```

Output: 
```
{
    "Response": {
        "ServiceDiscovery": {
            "Kind": "ServiceMonitor",
            "Name": "name",
            "Namespace": "namespace",
            "Selector": "{\"matchLabels\":{\"k8sapp\":\"mysql-exporter\"}}",
            "Yaml": "apiVersion: monitoring.coreos.com...",
            "NamespaceSelector": "{\"matchNames\":[\"demo-ns\"]}",
            "Endpoints": "[{\"port\":\"tcp-port\",\"path\":\"/metrics\",\"interval\":\"30s\",\"bearerTokenSecret\":{\"key\":\"\"}}]"
        },
        "RequestId": "nrtlca1qmunlpf51noe13qp5vyvg7mq5"
    }
}
```

