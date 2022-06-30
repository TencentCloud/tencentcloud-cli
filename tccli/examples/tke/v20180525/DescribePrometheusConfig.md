**Example 1: 拉取prometheus配置**



Input: 

```
tccli tke DescribePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --ClusterType tke \
    --ClusterId cls-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Config": "xxxx",
        "ServiceMonitors": [
            {
                "Name": "sm1",
                "Config": "xxx"
            }
        ],
        "PodMonitors": [
            {
                "Name": "pm1",
                "Config": "ddd"
            }
        ],
        "RawJobs": [
            {
                "Name": "job1",
                "Config": "xxx"
            }
        ]
    }
}
```

