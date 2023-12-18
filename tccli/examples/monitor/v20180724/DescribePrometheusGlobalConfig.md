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
                "TemplateId": "abc",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "PodMonitors": [
            {
                "Name": "abc",
                "Config": "abc",
                "TemplateId": "abc",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "Probes": [
            {
                "Name": "abc",
                "Config": "abc",
                "TemplateId": "abc",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "RawJobs": [
            {
                "Name": "abc",
                "Config": "abc",
                "TemplateId": "abc",
                "Targets": {
                    "Total": 1,
                    "Up": 1,
                    "Down": 1,
                    "Unknown": 1
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

