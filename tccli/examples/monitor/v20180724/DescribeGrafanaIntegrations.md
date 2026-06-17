**Example 1: 列出 Grafana 已安装的集成**



Input: 

```
tccli monitor DescribeGrafanaIntegrations --cli-unfold-argument  \
    --IntegrationId integration-abcd1234 \
    --InstanceId grafana-abcd1234 \
    --Kind tencent-managed-promestheus
```

Output: 
```
{
    "Response": {
        "IntegrationSet": [
            {
                "IntegrationId": "integration-abcd1234",
                "Content": "{\"type\":\"prometheus\"}",
                "Kind": "tencent-managed-promestheus",
                "Description": "managed prometheus integration",
                "GrafanaURL": "http://<grafana root url>"
            }
        ],
        "RequestId": "requestId"
    }
}
```

