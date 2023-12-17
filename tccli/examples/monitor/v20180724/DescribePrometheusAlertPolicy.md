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
                "Id": "abc",
                "Name": "abc",
                "TemplateId": "abc",
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
                "Rules": [
                    {
                        "Name": "abc",
                        "Rule": "abc",
                        "Labels": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "Template": "abc",
                        "For": "abc",
                        "Describe": "abc",
                        "Annotations": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "RuleState": 0
                    }
                ],
                "UpdatedAt": "abc",
                "ClusterId": "abc"
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

