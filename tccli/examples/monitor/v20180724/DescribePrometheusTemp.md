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
                "Name": "test",
                "Describe": "test",
                "Level": "instance",
                "RecordRules": [
                    {
                        "Name": "testRule",
                        "Config": "abc",
                        "TemplateId": "temp-asdj",
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
                        "Name": "test-sm",
                        "Config": "abc",
                        "TemplateId": "temp-asdj",
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
                        "Name": "test-pm",
                        "Config": "abc",
                        "TemplateId": "temp-asdj",
                        "Targets": {
                            "Total": 1,
                            "Up": 1,
                            "Down": 1,
                            "Unknown": 1
                        }
                    }
                ],
                "TemplateId": "temp-asdj",
                "UpdateTime": "2024-07-16T08:28:54Z",
                "Version": "v1",
                "IsDefault": true,
                "AlertDetailRules": [
                    {
                        "Id": "rule-asdk",
                        "Name": "testAlert",
                        "TemplateId": "temp-asdj",
                        "Notification": {
                            "Enabled": true,
                            "Type": "amp",
                            "WebHook": "abc",
                            "AlertManager": {
                                "ClusterType": "tke",
                                "ClusterId": "cls-askj",
                                "Url": "http://asasdkfh:9000"
                            },
                            "RepeatInterval": "5m",
                            "TimeRangeStart": "00:00:00",
                            "TimeRangeEnd": "23:59:59",
                            "NotifyWay": [
                                "abc"
                            ],
                            "ReceiverGroups": [
                                "notice-yakj"
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
                                "Name": "rule-ajdb",
                                "Rule": "avg by (abc) skdj",
                                "Labels": [
                                    {
                                        "Name": "label-name",
                                        "Value": "label-value"
                                    }
                                ],
                                "Template": "temp-asdj",
                                "For": "5m",
                                "Describe": "test-temp",
                                "Annotations": [
                                    {
                                        "Name": "label-name",
                                        "Value": "label-value"
                                    }
                                ],
                                "RuleState": 0
                            }
                        ],
                        "UpdatedAt": "2024-07-16 16:28:54",
                        "ClusterId": "cls-djfb"
                    }
                ],
                "TargetsTotal": 0
            }
        ],
        "Total": 1,
        "RequestId": "skdh-afbri"
    }
}
```

