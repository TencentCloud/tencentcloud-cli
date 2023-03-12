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
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Config": "xdfdfd",
        "ServiceMonitors": [
            {
                "Name": "sm1",
                "Config": "dfd"
            }
        ],
        "PodMonitors": [
            {
                "Name": "pm1",
                "Config": "fdfd"
            }
        ],
        "RawJobs": [
            {
                "Name": "job1",
                "Config": "fd"
            }
        ],
        "Probes": [
            {
                "Name": "job1",
                "Config": "fd"
            }
        ]
    }
}
```

