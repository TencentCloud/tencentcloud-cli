**Example 1: 更新 Grafana 集成配置**



Input: 

```
tccli monitor UpdateGrafanaIntegration --cli-unfold-argument  \
    --IntegrationId integration-abcd1234 \
    --InstanceId grafana-12345678 \
    --Kind tencent-cloud-prometheus \
    --Content xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

