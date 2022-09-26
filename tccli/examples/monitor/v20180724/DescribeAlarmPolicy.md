**Example 1: 查询告警策略详情**



Input: 

```
tccli monitor DescribeAlarmPolicy --cli-unfold-argument  \
    --Module monitor \
    --PolicyId policy-t1pvz47f
```

Output: 
```
{
    "Response": {
        "Policy": {
            "NamespaceShowName": "xx",
            "LastEditUin": "xx",
            "Namespace": "xx",
            "InstanceGroupName": "xx",
            "AdvancedMetricNumber": 0,
            "Notices": [
                {
                    "AMPConsumerId": "xx",
                    "URLNotices": [
                        {
                            "ValidationCode": "xx",
                            "URL": "xx",
                            "IsValid": 0,
                            "Weekday": [
                                0
                            ],
                            "StartTime": 0,
                            "EndTime": 0
                        }
                    ],
                    "Name": "xx",
                    "NoticeType": "xx",
                    "CLSNotices": [
                        {
                            "TopicId": "xx",
                            "Region": "xx",
                            "Enable": 0,
                            "LogSetId": "xx"
                        }
                    ],
                    "UpdatedBy": "xx",
                    "PolicyIds": [
                        "xx"
                    ],
                    "UserNotices": [
                        {
                            "NoticeWay": [
                                "SMS",
                                "EMAIL"
                            ],
                            "NeedPhoneArriveNotice": 0,
                            "PhoneOrder": [
                                0
                            ],
                            "PhoneCallType": "xx",
                            "UserIds": [
                                1001357
                            ],
                            "ReceiverType": "xx",
                            "PhoneCircleInterval": 0,
                            "GroupIds": [
                                0
                            ],
                            "StartTime": 0,
                            "PhoneCircleTimes": 0,
                            "EndTime": 86399,
                            "PhoneInnerInterval": 0,
                            "Weekday": [
                                0
                            ]
                        }
                    ],
                    "IsPreset": 1,
                    "UpdatedAt": "xx",
                    "NoticeLanguage": "xx",
                    "Id": "xx"
                }
            ],
            "TriggerTasks": [
                {
                    "Type": "xx",
                    "TaskConfig": "xx"
                }
            ],
            "ConditionTemplateId": "xx",
            "UpdateTime": 1608197675,
            "Enable": 1,
            "TagInstances": [
                {
                    "ServiceType": "xx",
                    "RegionId": 0,
                    "Value": "xx",
                    "InstanceSum": 0,
                    "Key": "xx",
                    "BindingStatus": 0,
                    "TagStatus": 0
                }
            ],
            "Condition": {
                "IsUnionRule": 0,
                "Rules": [
                    {
                        "NoticeFrequency": 86400,
                        "RuleType": "xx",
                        "IsAdvanced": 0,
                        "Description": "xx",
                        "IsOpen": 0,
                        "Period": 60,
                        "Value": "xx",
                        "Filter": {
                            "Type": "xx",
                            "Dimensions": "xx"
                        },
                        "IsPowerNotice": 0,
                        "ContinuePeriod": 1,
                        "Operator": "xx",
                        "ProductId": "xx",
                        "Unit": "xx",
                        "MetricName": "xx"
                    }
                ]
            },
            "PolicyName": "xx",
            "Remark": "xx",
            "ConditionsTemp": {
                "EventCondition": {
                    "Rules": [
                        {
                            "NoticeFrequency": 0,
                            "RuleType": "xx",
                            "IsAdvanced": 0,
                            "Description": "xx",
                            "IsOpen": 0,
                            "Period": 0,
                            "Value": "xx",
                            "Filter": {
                                "Type": "xx",
                                "Dimensions": "xx"
                            },
                            "IsPowerNotice": 0,
                            "ContinuePeriod": 0,
                            "Operator": "xx",
                            "ProductId": "xx",
                            "Unit": "xx",
                            "MetricName": "xx"
                        }
                    ]
                },
                "Condition": {
                    "IsUnionRule": 0
                },
                "TemplateName": "xx"
            },
            "ProjectId": 0,
            "Region": [
                "bj",
                "ca",
                "cd",
                "cgoec",
                "cq",
                "de",
                "fzec",
                "gz",
                "gzopen",
                "hfeec",
                "hk",
                "hzec",
                "in",
                "jnec",
                "jp",
                "kr",
                "nj",
                "ru",
                "sg",
                "sh",
                "sheec",
                "shjr",
                "szjr",
                "szx",
                "th",
                "tpe",
                "tsn",
                "use",
                "usw",
                "xbec",
                "xiyec"
            ],
            "FilterDimensionsParam": "xx",
            "EventCondition": {
                "Rules": [
                    {
                        "NoticeFrequency": 0,
                        "RuleType": "xx",
                        "IsAdvanced": 0,
                        "Description": "xx",
                        "IsOpen": 0,
                        "Period": 0,
                        "Value": "xx",
                        "Filter": {
                            "Type": "xx",
                            "Dimensions": "xx"
                        },
                        "IsPowerNotice": 0,
                        "ContinuePeriod": 0,
                        "Operator": "xx",
                        "ProductId": "xx",
                        "Unit": "xx",
                        "MetricName": "xx"
                    }
                ]
            },
            "InsertTime": 1608197675,
            "InstanceGroupId": 6155,
            "NoticeIds": [
                "notice-rwudonte"
            ],
            "OriginId": "xx",
            "IsDefault": 0,
            "PolicyId": "xx",
            "UseSum": 1,
            "InstanceSum": 1,
            "ProjectName": "xx",
            "RuleType": "xx",
            "OneClickStatus": 0,
            "IsOneClick": 0,
            "CanSetDefault": 0,
            "MonitorType": "xx"
        },
        "RequestId": "xx"
    }
}
```

