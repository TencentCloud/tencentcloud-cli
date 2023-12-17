**Example 1: 查询全局告警通知渠道**

查询全局告警通知渠道

Input: 

```
tccli monitor DescribePrometheusGlobalNotification --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "Notification": {
            "Enabled": true,
            "Type": "abc",
            "WebHook": "abc",
            "AlertManager": {
                "ClusterType": "abc",
                "ClusterId": "abc",
                "Url": "abc"
            },
            "RepeatInterval": "abc",
            "TimeRangeStart": "abc",
            "TimeRangeEnd": "abc",
            "NotifyWay": [
                "abc"
            ],
            "ReceiverGroups": [
                "abc"
            ],
            "PhoneNotifyOrder": [
                1
            ],
            "PhoneCircleTimes": 0,
            "PhoneInnerInterval": 0,
            "PhoneCircleInterval": 0,
            "PhoneArriveNotice": true
        },
        "RequestId": "abc"
    }
}
```

