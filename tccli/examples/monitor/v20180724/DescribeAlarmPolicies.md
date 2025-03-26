**Example 1: 根据接收组搜索**

根据接收组搜索

Input: 

```
tccli monitor DescribeAlarmPolicies --cli-unfold-argument  \
    --Module monitor \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Policies": [
            {
                "AdvancedMetricNumber": 0,
                "CanSetDefault": 1,
                "Condition": {
                    "ComplexExpression": "",
                    "IsUnionRule": 0,
                    "Rules": [
                        {
                            "ContinuePeriod": 1,
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
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "1",
                            "ValueMax": 100,
                            "ValueMin": 0
                        },
                        {
                            "ContinuePeriod": 1,
                            "Description": "外网出带宽使用率",
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
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "1",
                            "ValueMax": 100,
                            "ValueMin": 0
                        },
                        {
                            "ContinuePeriod": 1,
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
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "1",
                            "ValueMax": 100,
                            "ValueMin": 0
                        },
                        {
                            "ContinuePeriod": 1,
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
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "1",
                            "ValueMax": 100,
                            "ValueMin": 0
                        },
                        {
                            "ContinuePeriod": 1,
                            "Description": "基础CPU利用率",
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
                            "MetricName": "BaseCpuUsage",
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "0",
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
                "Enable": 0,
                "EventCondition": {
                    "Rules": [
                        {
                            "ContinuePeriod": 0,
                            "Description": "机器重启",
                            "Filter": null,
                            "HierarchicalValue": null,
                            "IsAdvanced": 0,
                            "IsLatenessMetric": 0,
                            "IsOpen": 0,
                            "IsPowerNotice": 0,
                            "MetricName": "cvm:ErrorEvent:GuestReboot",
                            "NoticeFrequency": 0,
                            "Operator": "",
                            "Period": 0,
                            "ProductId": "",
                            "RuleType": "",
                            "Unit": "",
                            "Value": "",
                            "ValueMax": null,
                            "ValueMin": null
                        }
                    ]
                },
                "Filter": null,
                "FilterDimensionsParam": "",
                "GroupBy": null,
                "HierarchicalNotices": [
                    {
                        "Classification": [
                            ""
                        ],
                        "NoticeId": "notice-lnrxepp7",
                        "PolicyId": "policy-s5yso1am"
                    },
                    {
                        "Classification": [
                            ""
                        ],
                        "NoticeId": "notice-lzpys7tu",
                        "PolicyId": "policy-s5yso1am"
                    }
                ],
                "InsertTime": 1739863161,
                "InstanceGroupId": 0,
                "InstanceGroupName": "",
                "InstanceSum": 0,
                "IsBindAll": 0,
                "IsDefault": 0,
                "IsOneClick": 0,
                "IsSupportAlarmTag": 1,
                "LastEditUin": "700000233161",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "NamespaceShowName": "云服务器-基础监控",
                "NoticeContentTmplBindInfos": null,
                "NoticeIds": [
                    "notice-lnrxepp7",
                    "notice-lzpys7tu"
                ],
                "Notices": [
                    {
                        "AMPConsumerId": "",
                        "CLSNotices": [],
                        "Id": "notice-lnrxepp7",
                        "IsPreset": 1,
                        "Name": "系统预设通知模板",
                        "NoticeLanguage": "zh-CN",
                        "NoticeType": "ALL",
                        "PolicyIds": null,
                        "Tags": null,
                        "URLNotices": [],
                        "UpdatedAt": "2020-11-13 17:02:44",
                        "UpdatedBy": "1500000685",
                        "UserNotices": [
                            {
                                "EndTime": 86399,
                                "GroupIds": [],
                                "NeedPhoneArriveNotice": 0,
                                "NoticeWay": [
                                    "SMS",
                                    "EMAIL"
                                ],
                                "OnCallFormIDs": [
                                    ""
                                ],
                                "PhoneCircleInterval": 0,
                                "PhoneCircleTimes": 0,
                                "PhoneInnerInterval": 0,
                                "PhoneOrder": [],
                                "ReceiverType": "USER",
                                "StartTime": 0,
                                "UserIds": [
                                    1000909
                                ],
                                "Weekday": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6,
                                    7
                                ]
                            }
                        ]
                    },
                    {
                        "AMPConsumerId": "",
                        "CLSNotices": [],
                        "Id": "notice-lzpys7tu",
                        "IsPreset": 0,
                        "Name": "Eric-告警回调",
                        "NoticeLanguage": "zh-CN",
                        "NoticeType": "ALL",
                        "PolicyIds": null,
                        "Tags": null,
                        "URLNotices": [
                            {
                                "EndTime": 86399,
                                "IsValid": 0,
                                "StartTime": 0,
                                "URL": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=47483435-2b48-4706-b76e-ac56e98be374",
                                "ValidationCode": "",
                                "Weekday": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6,
                                    7
                                ]
                            },
                            {
                                "EndTime": 86399,
                                "IsValid": 0,
                                "StartTime": 0,
                                "URL": "http://123.com",
                                "ValidationCode": "",
                                "Weekday": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6,
                                    7
                                ]
                            }
                        ],
                        "UpdatedAt": "2023-05-08 20:47:39",
                        "UpdatedBy": "700000233161",
                        "UserNotices": []
                    }
                ],
                "OneClickStatus": 0,
                "OriginId": "2963911",
                "PolicyId": "policy-s5yso1am",
                "PolicyName": "Eric-新增收敛测试",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "Region": [
                    "bj",
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
                    "in",
                    "jkt",
                    "jnec",
                    "jp",
                    "kr",
                    "nj",
                    "qy",
                    "qyxa",
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
                    "xiyec"
                ],
                "Remark": "",
                "RuleType": "STATIC",
                "TagInstances": [],
                "TagOperation": "",
                "Tags": [],
                "TriggerTasks": [],
                "UpdateTime": 1741072433,
                "UseSum": 4
            }
        ],
        "RequestId": "cd403f27-3cea-4565-8856-36907e07a026",
        "TotalCount": 216
    }
}
```

**Example 2: 搜索一个云服务器绑定的告警策略**

按照实例过滤策略，需要填入监控类型、策略类型、实例的维度信息。我们以搜索两个云服务器为例，假设他们的实例 ID 分别为 `ins-qr8d555g`,  `ins-qr8d555h`。

MonitorTypes 指定为 `MT_QCE`

Namespaces 指定为 `cvm_device`

Dimensions 的 JSON 字符串为

```
[
    {
        "Dimensions": {
            "unInstanceId": "ins-qr8d555g"
        }
    },
     {
        "Dimensions": {
            "unInstanceId": "ins-qr8d555h"
        }
    }
]
```

不同云产品参数示例详见 [维度信息Dimensions列表](https://cloud.tencent.com/document/product/248/50397)

Input: 

```
tccli monitor DescribeAlarmPolicies --cli-unfold-argument  \
    --Module monitor \
    --PageSize 10 \
    --PageNumber 1 \
    --MonitorTypes MT_QCE \
    --Namespaces cvm_device \
    --Dimensions [{"Dimensions": { "unInstanceId": "ins-qr8d555g"}},{ "Dimensions": { "unInstanceId": "ins-qr8d555h"}}]
```

Output: 
```
{
    "Response": {
        "Policies": [
            {
                "AdvancedMetricNumber": 0,
                "CanSetDefault": 1,
                "Condition": {
                    "ComplexExpression": "",
                    "IsUnionRule": 0,
                    "Rules": [
                        {
                            "ContinuePeriod": 1,
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
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "1",
                            "ValueMax": 100,
                            "ValueMin": 0
                        },
                        {
                            "ContinuePeriod": 1,
                            "Description": "外网出带宽使用率",
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
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "1",
                            "ValueMax": 100,
                            "ValueMin": 0
                        },
                        {
                            "ContinuePeriod": 1,
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
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "1",
                            "ValueMax": 100,
                            "ValueMin": 0
                        },
                        {
                            "ContinuePeriod": 1,
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
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "1",
                            "ValueMax": 100,
                            "ValueMin": 0
                        },
                        {
                            "ContinuePeriod": 1,
                            "Description": "基础CPU利用率",
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
                            "MetricName": "BaseCpuUsage",
                            "NoticeFrequency": 300,
                            "Operator": "gt",
                            "Period": 60,
                            "ProductId": "",
                            "RuleType": "STATIC",
                            "Unit": "%",
                            "Value": "0",
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
                "Enable": 0,
                "EventCondition": {
                    "Rules": [
                        {
                            "ContinuePeriod": 0,
                            "Description": "机器重启",
                            "Filter": null,
                            "HierarchicalValue": null,
                            "IsAdvanced": 0,
                            "IsLatenessMetric": 0,
                            "IsOpen": 0,
                            "IsPowerNotice": 0,
                            "MetricName": "cvm:ErrorEvent:GuestReboot",
                            "NoticeFrequency": 0,
                            "Operator": "",
                            "Period": 0,
                            "ProductId": "",
                            "RuleType": "",
                            "Unit": "",
                            "Value": "",
                            "ValueMax": null,
                            "ValueMin": null
                        }
                    ]
                },
                "Filter": null,
                "FilterDimensionsParam": "",
                "GroupBy": null,
                "HierarchicalNotices": [
                    {
                        "Classification": [
                            ""
                        ],
                        "NoticeId": "notice-lnrxepp7",
                        "PolicyId": "policy-s5yso1am"
                    },
                    {
                        "Classification": [
                            ""
                        ],
                        "NoticeId": "notice-lzpys7tu",
                        "PolicyId": "policy-s5yso1am"
                    }
                ],
                "InsertTime": 1739863161,
                "InstanceGroupId": 0,
                "InstanceGroupName": "",
                "InstanceSum": 0,
                "IsBindAll": 0,
                "IsDefault": 0,
                "IsOneClick": 0,
                "IsSupportAlarmTag": 1,
                "LastEditUin": "700000233161",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "NamespaceShowName": "云服务器-基础监控",
                "NoticeContentTmplBindInfos": null,
                "NoticeIds": [
                    "notice-lnrxepp7",
                    "notice-lzpys7tu"
                ],
                "Notices": [
                    {
                        "AMPConsumerId": "",
                        "CLSNotices": [],
                        "Id": "notice-lnrxepp7",
                        "IsPreset": 1,
                        "Name": "系统预设通知模板",
                        "NoticeLanguage": "zh-CN",
                        "NoticeType": "ALL",
                        "PolicyIds": null,
                        "Tags": null,
                        "URLNotices": [],
                        "UpdatedAt": "2020-11-13 17:02:44",
                        "UpdatedBy": "1500000685",
                        "UserNotices": [
                            {
                                "EndTime": 86399,
                                "GroupIds": [],
                                "NeedPhoneArriveNotice": 0,
                                "NoticeWay": [
                                    "SMS",
                                    "EMAIL"
                                ],
                                "OnCallFormIDs": [
                                    ""
                                ],
                                "PhoneCircleInterval": 0,
                                "PhoneCircleTimes": 0,
                                "PhoneInnerInterval": 0,
                                "PhoneOrder": [],
                                "ReceiverType": "USER",
                                "StartTime": 0,
                                "UserIds": [
                                    1000909
                                ],
                                "Weekday": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6,
                                    7
                                ]
                            }
                        ]
                    },
                    {
                        "AMPConsumerId": "",
                        "CLSNotices": [],
                        "Id": "notice-lzpys7tu",
                        "IsPreset": 0,
                        "Name": "Eric-告警回调",
                        "NoticeLanguage": "zh-CN",
                        "NoticeType": "ALL",
                        "PolicyIds": null,
                        "Tags": null,
                        "URLNotices": [
                            {
                                "EndTime": 86399,
                                "IsValid": 0,
                                "StartTime": 0,
                                "URL": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=47483435-2b48-4706-b76e-ac56e98be374",
                                "ValidationCode": "",
                                "Weekday": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6,
                                    7
                                ]
                            },
                            {
                                "EndTime": 86399,
                                "IsValid": 0,
                                "StartTime": 0,
                                "URL": "http://123.com",
                                "ValidationCode": "",
                                "Weekday": [
                                    1,
                                    2,
                                    3,
                                    4,
                                    5,
                                    6,
                                    7
                                ]
                            }
                        ],
                        "UpdatedAt": "2023-05-08 20:47:39",
                        "UpdatedBy": "700000233161",
                        "UserNotices": []
                    }
                ],
                "OneClickStatus": 0,
                "OriginId": "2963911",
                "PolicyId": "policy-s5yso1am",
                "PolicyName": "Eric-新增收敛测试",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "Region": [
                    "bj",
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
                    "in",
                    "jkt",
                    "jnec",
                    "jp",
                    "kr",
                    "nj",
                    "qy",
                    "qyxa",
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
                    "xiyec"
                ],
                "Remark": "",
                "RuleType": "STATIC",
                "TagInstances": [],
                "TagOperation": "",
                "Tags": [],
                "TriggerTasks": [],
                "UpdateTime": 1741072433,
                "UseSum": 4
            }
        ],
        "RequestId": "cd403f27-3cea-4565-8856-36907e07a026",
        "TotalCount": 216
    }
}
```

