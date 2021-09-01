**Example 1: 设置单IP默认告警阈值配置**



Input: 

```
tccli antiddos CreateDefaultAlarmThreshold --cli-unfold-argument  \
    --InstanceType bgp \
    --DefaultAlarmConfig.AlarmType 1 \
    --DefaultAlarmConfig.AlarmThreshold 2000
```

Output: 
```
{
    "Response": {
        "RequestId": "b7739a1e-837d-4248-bf9f-16a9bf77db22"
    }
}
```

