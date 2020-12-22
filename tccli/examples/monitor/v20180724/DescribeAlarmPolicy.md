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
            "PolicyId": "policy-t1pvz47f",
            "PolicyName": "云服务器基础监控告警策略",
            "UseSum": 1,
            "Remark": "",
            "MonitorType": "MT_QCE",
            "Enable": 1,
            "IsDefault": 0,
            "ProjectId": 0,
            "ProjectName": "默认项目",
            "Namespace": "cvm_device",
            "ConditionTemplateId": "",
            "Condition": {
                "IsUnionRule": 0,
                "Rules": [
                    {
                        "MetricName": "CpuUsage",
                        "Description": "CPU利用率",
                        "Unit": "%",
                        "Period": 60,
                        "AggregateType": "",
                        "AggregationDimensions": null,
                        "Operator": "gt",
                        "Value": "0",
                        "ContinuePeriod": 1,
                        "NoticeFrequency": 86400,
                        "IsPowerNotice": 0,
                        "Filter": {
                            "Type": "",
                            "Expression": "",
                            "Dimensions": "[]"
                        },
                        "RuleType": ""
                    }
                ]
            },
            "EventCondition": {
                "Rules": []
            },
            "NoticeIds": [
                "notice-rwudonte"
            ],
            "Notices": [
                {
                    "Id": "notice-rwudonte",
                    "Name": "系统预设通知模板",
                    "UpdatedAt": "2020-12-04 19:22:30",
                    "UpdatedBy": "1500000686",
                    "NoticeType": "ALL",
                    "UserNotices": [
                        {
                            "ReceiverType": "USER",
                            "UserIds": [
                                1001357
                            ],
                            "GroupIds": null,
                            "StartTime": 0,
                            "EndTime": 86399,
                            "NoticeWay": [
                                "SMS",
                                "EMAIL"
                            ],
                            "PhoneOrder": null,
                            "PhoneCircleTimes": 0,
                            "PhoneInnerInterval": 0,
                            "PhoneCircleInterval": 0,
                            "NeedPhoneArriveNotice": 0
                        }
                    ],
                    "URLNotices": [],
                    "IsPreset": 1,
                    "NoticeLanguage": "zh-CN"
                }
            ],
            "TriggerTasks": [],
            "OriginId": "1319514",
            "ConditionsTemp": {
                "ConditionId": 0,
                "TemplateName": "",
                "Condition": null,
                "EventCondition": null
            },
            "LastEditUin": "1500000686",
            "UpdateTime": 1608197675,
            "InsertTime": 1608197675,
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
            "NamespaceShowName": "云服务器-基础监控",
            "CanSetDefault": 0,
            "InstanceGroupId": 6155,
            "InstanceGroupName": "mingc_instance",
            "InstanceSum": 1,
            "RuleType": "STATIC"
        },
        "RequestId": "546f55d8-80d1-4668-a43e-11490491d62e"
    }
}
```

