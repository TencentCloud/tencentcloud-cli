**Example 1: 列出 Grafana 的设置**



Input: 

```
tccli monitor DescribeGrafanaConfig --cli-unfold-argument  \
    --InstanceId grafana-12345678
```

Output: 
```
{
    "Response": {
        "Config": "{\"server\":{\"root_url\":\"http://balababbb\"}}",
        "RequestId": "zcv6drxckn53gb61anxndsckjdwgfw6j"
    }
}
```

