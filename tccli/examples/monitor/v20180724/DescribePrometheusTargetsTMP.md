**Example 1: 获取targets列表**

获取targets列表

Input: 

```
tccli monitor DescribePrometheusTargetsTMP --cli-unfold-argument  \
    --InstanceId prom-xxx \
    --ClusterType tke \
    --ClusterId cls-xxx
```

Output: 
```
{
    "Response": {
        "Jobs": [
            {
                "Targets": [
                    {
                        "Url": "http://1.1.1.1:9000",
                        "State": "down"
                    }
                ],
                "Total": 1,
                "Up": 0,
                "JobName": "test-job"
            }
        ],
        "RequestId": "abc"
    }
}
```

