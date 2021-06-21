**Example 1: 获取单IP默认告警阈值配置**



Input: 

```
tccli antiddos DescribeDefaultAlarmThreshold --cli-unfold-argument  \
    --InstanceType bgp \
    --FilterAlarmType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a7df6626-fb01-4c9e-b43a-7af1db3fe998",
        "DefaultAlarmConfigList": [
            {
                "AlarmType": 1,
                "AlarmThreshold": 1000
            }
        ]
    }
}
```

