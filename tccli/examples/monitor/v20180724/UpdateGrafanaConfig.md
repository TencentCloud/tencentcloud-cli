**Example 1: 更新 Grafana 配置**



Input: 

```
tccli monitor UpdateGrafanaConfig --cli-unfold-argument  \
    --InstanceId grafana-abcd1234 \
    --Config {"server":{"root_url":"http://abc"},"server_a":"abc"}
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId"
    }
}
```

