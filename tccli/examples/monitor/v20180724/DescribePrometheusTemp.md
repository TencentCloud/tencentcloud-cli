**Example 1: 拉取模板列表**

拉取模板列表

Input: 

```
tccli monitor DescribePrometheusTemp --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Name ID \
    --Filters.0.Values alert-test \
    --Offset 1
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
                        "TemplateId": "abc",
                        "Targets": {
                            "Total": 1,
                            "Up": 1,
                            "Down": 1,
                            "Unknown": 1
                        }
                    }
                ],
                "RawJobs": [
                    {
                        "Name": "abc",
                        "Config": "abc",
                        "TemplateId": "abc",
                        "Targets": {
                            "Total": 1,
                            "Up": 1,
                            "Down": 1,
                            "Unknown": 1
                        }
                    }
                ],
                "ServiceMonitors": [
                    {
                        "Name": "abc",
                        "Config": "abc",
                        "TemplateId": "abc",
                        "Targets": {
                            "Total": 1,
                            "Up": 1,
                            "Down": 1,
                            "Unknown": 1
                        }
                    }
                ],
                "PodMonitors": [
                    {
                        "Name": "abc",
                        "Config": "abc",
                        "TemplateId": "abc",
                        "Targets": {
                            "Total": 1,
                            "Up": 1,
                            "Down": 1,
                            "Unknown": 1
                        }
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

