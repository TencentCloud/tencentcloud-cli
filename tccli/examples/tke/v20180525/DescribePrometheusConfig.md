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
        "Probes": [
            {
                "Name": "probe-xxx",
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

**Example 2: 获取集群采集配置**



Input: 

```
tccli tke DescribePrometheusConfig --cli-unfold-argument  \
    --InstanceId prom-2tghe0lv \
    --ClusterId cls-9cgtidkr \
    --ClusterType tke
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
        "Probes": [],
        "RequestId": "abc"
    }
}
```

