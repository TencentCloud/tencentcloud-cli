**Example 1: 修改告警服务默认阈值**



Input: 

```
tccli teo ModifyAlarmDefaultThreshold --cli-unfold-argument  \
    --Threshold 100 \
    --ServiceType ddos \
    --ZoneId zone-28569s6od5na
```

Output: 
```
{
    "Response": {
        "RequestId": "46c32ba8-06d8-447e-a8e2-c39619535723"
    }
}
```

