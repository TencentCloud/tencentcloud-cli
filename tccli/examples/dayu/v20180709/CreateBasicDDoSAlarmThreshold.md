**Example 1: Setting DDoS alarm threshold for Anti-DDoS Basic**



Input: 

```
tccli dayu CreateBasicDDoSAlarmThreshold --cli-unfold-argument  \
    --Business bgpip\
    --Method set\
    --AlarmThreshold 1000\
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

