**Example 1: 列出服务发现列表**



Input: 

```
tccli monitor DescribeServiceDiscovery --cli-unfold-argument  \
    --InstanceId prom-sdfk2342a \
    --KubeClusterId cls-pwerf3k3 \
    --KubeType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0523dedd-1235-428d-885c-9443cf9175d1",
        "ServiceDiscoverySet": [
            {
                "Kind": "ServiceMonitor",
                "Name": "name",
                "Namespace": "namespace",
                "Selector": "{\"matchLabels\":{\"k8sapp\":\"mysql-exporter\"}}",
                "Yaml": "apiVersion: monitoring.coreos.com...",
                "NamespaceSelector": "{\"matchNames\":[\"demo-ns\"]}",
                "Endpoints": "[{\"port\":\"tcp-port\",\"path\":\"/metrics\",\"interval\":\"30s\",\"bearerTokenSecret\":{\"key\":\"\"}}]"
            }
        ]
    }
}
```

