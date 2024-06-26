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
        "Config": "abc",
        "ServiceMonitors": [
            {
                "Name": "abc",
                "Config": "abc",
                "TemplateId": "abc"
            }
        ],
        "PodMonitors": [
            {
                "Name": "abc",
                "Config": "abc",
                "TemplateId": "abc"
            }
        ],
        "RawJobs": [
            {
                "Name": "abc",
                "Config": "abc",
                "TemplateId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

