**Example 1: 拉取模板列表**



Input: 

```
tccli tke DescribePrometheusTemp --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "Name": "abc",
                "Describe": "abc",
                "Level": "abc",
                "RecordRules": [
                    {
                        "Name": "abc",
                        "Config": "abc",
                        "TemplateId": "abc"
                    }
                ],
                "ServiceMonitors": [
                    {
                        "Name": "abc",
                        "Config": "abc",
                        "TemplateId": "abc"
                    }
                ],
                "PodMonitors": [
                    {
                        "Name": "abc",
                        "Config": "abc",
                        "TemplateId": "abc"
                    }
                ],
                "TemplateId": "abc",
                "UpdateTime": "abc",
                "Version": "abc",
                "IsDefault": true,
                "AlertDetailRules": [
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
                "TargetsTotal": 0
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

