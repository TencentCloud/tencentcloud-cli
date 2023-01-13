**Example 1: 告警列表**

告警列表

Input: 

```
tccli monitor DescribePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId xx \
    --Limit 1 \
    --Filters.0.Type xx \
    --Filters.0.Key xx \
    --Filters.0.Value xx \
    --Offset 1
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
                            {}
                        ],
                        "Rule": "xx",
                        "Template": "xx",
                        "Annotations": [
                            {}
                        ]
                    }
                ],
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
                        1
                    ],
                    "PhoneArriveNotice": true,
                    "PhoneCircleTimes": 0,
                    "TimeRangeStart": "xx",
                    "Type": "xx",
                    "TimeRangeEnd": "xx"
                },
                "TemplateId": "xx",
                "ClusterId": "xx",
                "UpdatedAt": "xx",
                "Id": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

