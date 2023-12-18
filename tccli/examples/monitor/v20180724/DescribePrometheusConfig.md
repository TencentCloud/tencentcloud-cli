**Example 1: 拉取prometheus配置**

拉取prometheus配置

Input: 

```
tccli monitor DescribePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --ClusterType tke \
    --ClusterId cls-xxx
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
        "ImageNeedUpdate": true,
        "RequestId": "abc"
    }
}
```

