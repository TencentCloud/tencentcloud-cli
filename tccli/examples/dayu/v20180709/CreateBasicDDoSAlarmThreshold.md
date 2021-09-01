**Example 1: 设置基础防护的DDoS告警阈值**



Input: 

```
tccli dayu CreateBasicDDoSAlarmThreshold --cli-unfold-argument  \
    --Business bgpip \
    --Method set \
    --AlarmThreshold 1000 \
    --AlarmType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "AlarmThreshold": 1000,
        "AlarmType": 1
    }
}
```

