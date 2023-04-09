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
                "UpdateTime": "xxx",
                "RecordRules": [
                    {
                        "Config": "xxx",
                        "Name": "xxx",
                        "TemplateId": "xxx"
                    }
                ],
                "Version": "xxx",
                "Name": "xxx",
                "Level": "xxx",
                "Describe": "xxx",
                "TargetsTotal": 0,
                "RawJobs": [
                    {
                        "Config": "xxx",
                        "Name": "xxx",
                        "TemplateId": "xxx"
                    }
                ],
                "PodMonitors": [
                    {
                        "Config": "xxx",
                        "Name": "xxx",
                        "TemplateId": "xxx"
                    }
                ],
                "TemplateId": "xxx",
                "AlertDetailRules": [
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
                                "xxx"
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
                "IsDefault": true,
                "ServiceMonitors": [
                    {
                        "Config": "xxx",
                        "Name": "xxx",
                        "TemplateId": "xxx"
                    }
                ]
            }
        ],
        "Total": 1,
        "RequestId": "xxx"
    }
}
```

