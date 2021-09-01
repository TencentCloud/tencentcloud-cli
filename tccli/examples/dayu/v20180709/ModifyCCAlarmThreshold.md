**Example 1: 设置CC告警阈值**



Input: 

```
tccli dayu ModifyCCAlarmThreshold --cli-unfold-argument  \
    --Business bgpip \
    --IpList 212.64.63.57 129.28.240.128 \
    --RsId net-0000002h \
    --AlarmThreshold 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

