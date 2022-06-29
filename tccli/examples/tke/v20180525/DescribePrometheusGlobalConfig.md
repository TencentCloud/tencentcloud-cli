**Example 1: 获得实例级别监控配置**



Input: 

```
tccli tke DescribePrometheusGlobalConfig --cli-unfold-argument  \
    --InstanceId prom-xxx
```

Output: 
```
{
    "Response": {
        "PodMonitors": [
            {
                "Config": "xx",
                "Name": "xx",
                "TemplateId": "xx"
            }
        ],
        "Config": "xx",
        "RawJobs": [
            {
                "Config": "xx",
                "Name": "xx",
                "TemplateId": "xx"
            }
        ],
        "RequestId": "xx",
        "ServiceMonitors": [
            {
                "Config": "xx",
                "Name": "xx",
                "TemplateId": "xx"
            }
        ]
    }
}
```

