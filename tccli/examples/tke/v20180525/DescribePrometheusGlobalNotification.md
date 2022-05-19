**Example 1: 查询全局告警通知渠道**



Input: 

```
tccli tke DescribePrometheusGlobalNotification --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "Notification": {
            "AlertManager": {
                "Url": "xx",
                "ClusterId": "xx",
                "ClusterType": "xx"
            },
            "RepeatInterval": "xx",
            "WebHook": "xx",
            "Enabled": true,
            "PhoneNotifyOrder": [
                1
            ],
            "PhoneInnerInterval": 0,
            "PhoneCircleInterval": 0,
            "NotifyWay": [
                "xx"
            ],
            "ReceiverGroups": [
                "xx"
            ],
            "PhoneArriveNotice": true,
            "PhoneCircleTimes": 0,
            "TimeRangeStart": "xx",
            "Type": "xx",
            "TimeRangeEnd": "xx"
        },
        "RequestId": "xx"
    }
}
```

