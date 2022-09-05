**Example 1: 列出 Grafana 已安装的集成**



Input: 

```
tccli monitor DescribeGrafanaIntegrations --cli-unfold-argument  \
    --IntegrationId xx \
    --InstanceId xx \
    --Kind xx
```

Output: 
```
{
    "Response": {
        "IntegrationSet": [
            {
                "IntegrationId": "xx",
                "Content": "xx",
                "Kind": "xx",
                "Description": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

