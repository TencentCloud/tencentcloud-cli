**Example 1: 创建 Grafana 集成配置**



Input: 

```
tccli monitor CreateGrafanaIntegration --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --Content xx \
    --Kind tencent-cloud-prometheus
```

Output: 
```
{
    "Response": {
        "IntegrationId": "xx",
        "RequestId": "xx"
    }
}
```

