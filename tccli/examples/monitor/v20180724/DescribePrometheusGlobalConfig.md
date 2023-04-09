**Example 1: 获得实例级别监控配置**

获得实例级别监控配置

Input: 

```
tccli monitor DescribePrometheusGlobalConfig --cli-unfold-argument  \
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
        "Probes": [
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

