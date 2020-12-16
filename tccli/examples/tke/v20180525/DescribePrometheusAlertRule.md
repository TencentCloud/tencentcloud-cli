**Example 1: 告警列表**



Input: 

```
tccli tke DescribePrometheusAlertRule --cli-unfold-argument  \
    --InstanceId prom-xxx
```

Output: 
```
{
    "Response": {
        "AlertRules": [
            {
                "Name": "xx",
                "Rules": [
                    {
                        "Describe": "xx",
                        "Name": "xx",
                        "For": "xx",
                        "Labels": [
                            {
                                "Name": "xx",
                                "Value": "xx"
                            }
                        ],
                        "Rule": "xx",
                        "Template": "xx"
                    }
                ],
                "Notification": {
                    "WebHook": "xx",
                    "RepeatInterval": "xx",
                    "TimeRangeStart": "xx",
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
                        1
                    ],
                    "PhoneArriveNotice": true,
                    "PhoneCircleTimes": 0,
                    "Type": "xx",
                    "TimeRangeEnd": "xx"
                },
                "UpdatedAt": "xx",
                "TemplateId": "xx",
                "Id": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

