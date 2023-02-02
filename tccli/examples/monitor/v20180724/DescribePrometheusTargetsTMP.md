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
            {}
        ],
        "RequestId": "xx"
    }
}
```

