**Example 1: 开启自治功能**



Input: 

```
tccli dbbrain CreateUserAutonomyProfile --cli-unfold-argument  \
    --ProfileType RedisAutoScaleUp \
    --InstanceId crs-k1gjspdk \
    --Product redis \
    --ProfileInfo {
        "Strategy": "Threshold",
        "Enabled": true,
        "MemoryUpperLimit": 512,
        "ThresholdRule": {
            "Metric": "mem_util",
            "Threshold": 70,
            "Duration": 600
        }
    }
```

Output: 
```
{
    "Response": {
        "RequestId": "d98451b3-bff6-4ce8-9972-1e770534cac9"
    }
}
```

