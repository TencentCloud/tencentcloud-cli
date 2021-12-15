**Example 1: 查询主设备设备告警订阅状态**



Input: 

```
tccli iotvideoindustry DescribeSubscriptionStatus --cli-unfold-argument  \
    --DeviceId aaa_bbb
```

Output: 
```
{
    "Response": {
        "RequestId": "sss118",
        "AlarmStatus": 1
    }
}
```

