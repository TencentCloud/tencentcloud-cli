**Example 1: 告警列表**

告警列表

Input: 

```
tccli monitor DescribePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId xxx \
    --Limit 1 \
    --Filters.0.Name Name \
    --Filters.0.Values alert-test \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "AlertRules": [
            {
                "Name": "xxx",
                "Rules": [
                    {
                        "Describe": "xxx",
                        "Name": "xxx",
                        "For": "xxx",
                        "Labels": [
                            {
                                "Name": "xxx",
                                "Value": "xxx"
                            }
                        ],
                        "Rule": "xxx",
                        "Template": "xxx",
                        "Annotations": [
                            {
                                "Name": "xxx",
                                "Value": "xxx"
                            }
                        ]
                    }
                ],
                "Notification": {
                    "AlertManager": {
                        "Url": "xxx",
                        "ClusterId": "xxx",
                        "ClusterType": "xxx"
                    },
                    "RepeatInterval": "xxx",
                    "WebHook": "xxx",
                    "Enabled": true,
                    "PhoneNotifyOrder": [
                        1
                    ],
                    "PhoneInnerInterval": 0,
                    "PhoneCircleInterval": 0,
                    "NotifyWay": [
                        "xxx"
                    ],
                    "ReceiverGroups": [
                        "1"
                    ],
                    "PhoneArriveNotice": true,
                    "PhoneCircleTimes": 0,
                    "TimeRangeStart": "xxx",
                    "Type": "xxx",
                    "TimeRangeEnd": "xxx"
                },
                "TemplateId": "xxx",
                "ClusterId": "xxx",
                "UpdatedAt": "xxx",
                "Id": "xxx"
            }
        ],
        "Total": 1,
        "RequestId": "xxx"
    }
}
```

