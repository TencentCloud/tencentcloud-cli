**Example 1: 查询自治功能开关情况**



Input: 

```
tccli dbbrain DescribeUserAutonomyProfile --cli-unfold-argument  \
    --ProfileType RedisAutoScaleUp \
    --InstanceId crs-1p8z8saa \
    --Product redis
```

Output: 
```
{
    "Response": {
        "ProfileInfo": {
            "Enabled": true,
            "MemoryUpperLimit": 512,
            "ThresholdRule": {
                "Duration": 900,
                "Metric": "mem_util",
                "Threshold": 50
            },
            "Uin": "100013717858"
        },
        "ProfileType": "RedisAutoScaleUp",
        "RequestId": "18c0c4ad-5f14-4609-9796-a0fb07e85918",
        "UpdateTime": "2025-03-14 10:32:25"
    }
}
```

