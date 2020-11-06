**Example 1: 获取CC告警阈值**



Input: 

```
tccli dayu DescribeCCAlarmThreshold --cli-unfold-argument  \
    --Business bgpip \
    --RsId net-0000002h
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "CCAlarmThreshold": {
            "AlarmThreshold": 1000
        }
    }
}
```

