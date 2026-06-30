**Example 1: 查询告警策略详情**



Input: 

```
tccli monitor DescribeAlarmPolicy --cli-unfold-argument  \
    --Module monitor \
    --PolicyId policy-1b842bhh
```

Output: 
```
{
    "Response": {
        "Policy": {
            "AdvancedMetricNumber": 0,
            "CanSetDefault": 1,
            "Condition": {
                "ComplexExpression": "",
                "IsUnionRule": 0,
                "Rules": [
                    {
                        "ContinuePeriod": 5,
                        "Description": "CPU利用率",
                        "Filter": {
                            "Dimensions": "",
                            "Type": ""
                        },
                        "HierarchicalValue": {
                            "Remind": "",
                            "Serious": "",
                            "Warn": ""
                        },
                        "IsAdvanced": 0,
                        "IsLatenessMetric": 0,
                        "IsOpen": 1,
                        "IsPowerNotice": 0,
                        "MetricName": "CpuUsage",
                        "NoticeFrequency": 7200,
                        "Operator": "gt",
                        "Period": 60,
                        "ProductId": "",
                        "RuleType": "STATIC",
                        "Unit": "%",
                        "Value": "95",
                        "ValueMax": 100,
                        "ValueMin": 0
                    },
                    {
                        "ContinuePeriod": 5,
                        "Description": "外网出带宽使用率（适用于非上移账户）",
                        "Filter": {
                            "Dimensions": "",
                            "Type": ""
                        },
                        "HierarchicalValue": {
                            "Remind": "",
                            "Serious": "",
                            "Warn": ""
                        },
                        "IsAdvanced": 0,
                        "IsLatenessMetric": 0,
                        "IsOpen": 1,
                        "IsPowerNotice": 0,
                        "MetricName": "Outratio",
                        "NoticeFrequency": 7200,
                        "Operator": "gt",
                        "Period": 60,
                        "ProductId": "",
                        "RuleType": "STATIC",
                        "Unit": "%",
                        "Value": "95",
                        "ValueMax": 100,
                        "ValueMin": 0
                    },
                    {
                        "ContinuePeriod": 5,
                        "Description": "内存利用率",
                        "Filter": {
                            "Dimensions": "",
                            "Type": ""
                        },
                        "HierarchicalValue": {
                            "Remind": "",
                            "Serious": "",
                            "Warn": ""
                        },
                        "IsAdvanced": 0,
                        "IsLatenessMetric": 0,
                        "IsOpen": 1,
                        "IsPowerNotice": 0,
                        "MetricName": "MemUsage",
                        "NoticeFrequency": 7200,
                        "Operator": "gt",
                        "Period": 60,
                        "ProductId": "",
                        "RuleType": "STATIC",
                        "Unit": "%",
                        "Value": "95",
                        "ValueMax": 100,
                        "ValueMin": 0
                    },
                    {
                        "ContinuePeriod": 5,
                        "Description": "磁盘利用率",
                        "Filter": {
                            "Dimensions": "",
                            "Type": ""
                        },
                        "HierarchicalValue": {
                            "Remind": "",
                            "Serious": "",
                            "Warn": ""
                        },
                        "IsAdvanced": 0,
                        "IsLatenessMetric": 0,
                        "IsOpen": 1,
                        "IsPowerNotice": 0,
                        "MetricName": "CvmDiskUsage",
                        "NoticeFrequency": 7200,
                        "Operator": "gt",
                        "Period": 60,
                        "ProductId": "",
                        "RuleType": "STATIC",
                        "Unit": "%",
                        "Value": "95",
                        "ValueMax": 100,
                        "ValueMin": 0
                    }
                ]
            },
            "ConditionTemplateId": "",
            "ConditionsTemp": {
                "Condition": null,
                "EventCondition": null,
                "TemplateName": ""
            },
            "Enable": 1,
            "EventCondition": {
                "Rules": []
            },
            "Filter": null,
            "FilterDimensionsParam": "",
            "GroupBy": null,
            "HierarchicalNotices": [
                {
                    "Classification": [
                        ""
                    ],
                    "NoticeId": "notice-qvq836vc",
                    "PolicyId": "policy-1b842bhh"
                }
            ],
            "InsertTime": 1781493760,
            "InstanceGroupId": 0,
            "InstanceGroupName": "",
            "InstanceSum": 0,
            "IsBindAll": 0,
            "IsDefault": 0,
            "IsOneClick": 0,
            "IsSupportAlarmTag": 0,
            "LastEditUin": "100026263254",
            "MonitorType": "MT_QCE",
            "Namespace": "cvm_device",
            "NamespaceShowName": "云服务器-基础监控",
            "NoticeContentTmplBindInfos": [],
            "NoticeIds": [
                "notice-qvq836vc"
            ],
            "Notices": [
                {
                    "AMPConsumerId": "",
                    "CLSNotices": [],
                    "Id": "notice-qvq836vc",
                    "IsPreset": 1,
                    "Name": "系统预设通知模板",
                    "NoticeLanguage": "zh-CN",
                    "NoticeType": "OK",
                    "PolicyIds": null,
                    "Tags": null,
                    "URLNotices": [
                        {
                            "EndTime": 1,
                            "GroupMembers": "",
                            "IsValid": 0,
                            "StartTime": 0,
                            "URL": "https://qq.com?no-user-no-alarm-please-use-custom-notice",
                            "ValidationCode": "",
                            "Weekday": [
                                7
                            ]
                        }
                    ],
                    "UpdatedAt": "2025-09-25 15:21:35",
                    "UpdatedBy": "1500000688",
                    "UserNotices": []
                }
            ],
            "OneClickStatus": 0,
            "OriginId": "15225159",
            "PolicyId": "policy-1b842bhh",
            "PolicyName": "cvm告警",
            "PredefinedConfigID": "",
            "ProjectId": 0,
            "ProjectName": "默认项目",
            "Region": [
                "bj",
                "bjhldycft",
                "bjjr",
                "cd",
                "cgoec",
                "cq",
                "csec",
                "de",
                "fzec",
                "gz",
                "gzopen",
                "gzwxzf",
                "hfeec",
                "hk",
                "hzec",
                "jkt",
                "jnec",
                "jp",
                "kr",
                "nj",
                "osa",
                "qy",
                "qyxa",
                "sa",
                "sao",
                "sg",
                "sh",
                "shadc",
                "sheec",
                "shhqcft",
                "shjr",
                "shwxzf",
                "sjwec",
                "szjr",
                "szjxcft",
                "szsycft",
                "szx",
                "th",
                "tpe",
                "tsn",
                "use",
                "usw",
                "whec",
                "xbec",
                "xiyec",
                "zw",
                "zwadc"
            ],
            "Remark": "",
            "RuleType": "STATIC",
            "TagInstances": [],
            "TagOperation": "",
            "Tags": [],
            "TriggerTasks": [],
            "UpdateTime": 1781493761,
            "UseSum": 1
        },
        "RequestId": "11d9550a-f3c3-441f-a0f5-21d8e7d00b0e"
    }
}
```

