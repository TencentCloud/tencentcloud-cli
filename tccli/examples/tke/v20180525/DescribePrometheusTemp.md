**Example 1: 拉取模板列表**



Input: 

```
tccli tke DescribePrometheusTemp --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "UpdateTime": "xx",
                "RecordRules": [
                    {
                        "Config": "xx",
                        "Name": "xx",
                        "TemplateId": "xx"
                    }
                ],
                "Version": "xx",
                "Name": "xx",
                "Level": "xx",
                "Describe": "xx",
                "TargetsTotal": 0,
                "RawJobs": [
                    {
                        "Config": "xx",
                        "Name": "xx",
                        "TemplateId": "xx"
                    }
                ],
                "PodMonitors": [
                    {
                        "Config": "xx",
                        "Name": "xx",
                        "TemplateId": "xx"
                    }
                ],
                "TemplateId": "xx",
                "AlertDetailRules": [
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
                                "Template": "xx",
                                "Annotations": [
                                    {
                                        "Name": "xx",
                                        "Value": "xx"
                                    }
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
                                "xx"
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
                "IsDefault": true,
                "ServiceMonitors": [
                    {
                        "Config": "xx",
                        "Name": "xx",
                        "TemplateId": "xx"
                    }
                ]
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

