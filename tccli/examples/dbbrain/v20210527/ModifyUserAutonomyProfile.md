**Example 1: 关闭自治功能（实例级）**



Input: 

```
tccli dbbrain ModifyUserAutonomyProfile --cli-unfold-argument  \
    --ProfileType RedisAutoScaleUp \
    --InstanceId crs-1p8z8saa \
    --Product redis \
    --NewProfileInfo 	{
    "MemoryUpperLimit": 512,
    "Version": 0,
    "Enabled": true,
    "Uin": "100013717858",
    "ThresholdRule": {
        "Duration": 900,
        "Metric": "mem_util",
        "Threshold": 50
    }
}
```

Output: 
```
{
    "Response": {
        "RequestId": "c1ed2569-7c73-4ed5-bec8-4aab9f9b0a77"
    }
}
```

