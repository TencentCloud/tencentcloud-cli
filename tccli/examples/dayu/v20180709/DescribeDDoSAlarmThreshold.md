**Example 1: Getting DDoS alarm threshold**



Input: 

```
tccli dayu DescribeDDoSAlarmThreshold --cli-unfold-argument  \
    --Business bgpip \
    --RsId net-0000002h
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "DDoSAlarmThreshold": {
            "AlarmType": 1,
            "AlarmThreshold": 1000
        }
    }
}
```

