**Example 1: 开启 Grafana 单点登录**

开启 Grafana 单点登录

Input: 

```
tccli monitor EnableGrafanaSSO --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --EnableSSO True
```

Output: 
```
{
    "Response": {
        "RequestId": "qmunlpf51noe13qp5vyvg7mq5t4t4w6u"
    }
}
```

