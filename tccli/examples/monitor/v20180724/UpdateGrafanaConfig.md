**Example 1: 更新 Grafana 配置**



Input: 

```
tccli monitor UpdateGrafanaConfig --cli-unfold-argument  \
    --InstanceId xx \
    --Config {"server":{"root_url":"http://balaba"},"server_haha":"heihei"}
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

