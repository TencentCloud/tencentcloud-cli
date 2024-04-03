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
        "TotalCount": 0,
        "Policies": [
            {
                "PolicyId": "abc",
                "PolicyName": "abc",
                "Remark": "abc",
                "MonitorType": "abc",
                "Enable": 0,
                "UseSum": 0,
                "ProjectId": 0,
                "ProjectName": "abc",
                "Namespace": "abc",
                "ConditionTemplateId": "abc",
                "Condition": {
                    "IsUnionRule": 0,
                    "Rules": [
                        {
                            "MetricName": "abc",
                            "Period": 0,
                            "Operator": "abc",
                            "Value": "abc",
                            "ContinuePeriod": 0,
                            "NoticeFrequency": 0,
                            "IsPowerNotice": 0,
                            "Filter": {
                                "Type": "abc",
                                "Dimensions": "abc"
                            },
                            "Description": "abc",
                            "Unit": "abc",
                            "RuleType": "abc",
                            "IsAdvanced": 0,
                            "IsOpen": 0,
                            "ProductId": "abc",
                            "ValueMax": 0,
                            "ValueMin": 0,
                            "HierarchicalValue": {
                                "Remind": "abc",
                                "Warn": "abc",
                                "Serious": "abc"
                            }
                        }
                    ],
                    "ComplexExpression": "abc"
                },
                "EventCondition": {
                    "Rules": [
                        {
                            "MetricName": "abc",
                            "Period": 0,
                            "Operator": "abc",
                            "Value": "abc",
                            "ContinuePeriod": 0,
                            "NoticeFrequency": 0,
                            "IsPowerNotice": 0,
                            "Filter": {
                                "Type": "abc",
                                "Dimensions": "abc"
                            },
                            "Description": "abc",
                            "Unit": "abc",
                            "RuleType": "abc",
                            "IsAdvanced": 0,
                            "IsOpen": 0,
                            "ProductId": "abc",
                            "ValueMax": 0,
                            "ValueMin": 0,
                            "HierarchicalValue": {
                                "Remind": "abc",
                                "Warn": "abc",
                                "Serious": "abc"
                            }
                        }
                    ]
                },
                "NoticeIds": [
                    "abc"
                ],
                "Notices": [
                    {
                        "Id": "abc",
                        "Name": "abc",
                        "UpdatedAt": "abc",
                        "UpdatedBy": "abc",
                        "NoticeType": "abc",
                        "UserNotices": [
                            {
                                "ReceiverType": "abc",
                                "UserIds": [
                                    0
                                ],
                                "GroupIds": [
                                    0
                                ],
                                "StartTime": 0,
                                "EndTime": 0,
                                "NoticeWay": [
                                    "abc"
                                ],
                                "PhoneOrder": [
                                    0
                                ],
                                "PhoneCircleTimes": 0,
                                "PhoneInnerInterval": 0,
                                "PhoneCircleInterval": 0,
                                "NeedPhoneArriveNotice": 0,
                                "PhoneCallType": "abc",
                                "Weekday": [
                                    0
                                ],
                                "OnCallFormIDs": [
                                    "abc"
                                ]
                            }
                        ],
                        "URLNotices": [
                            {
                                "URL": "abc",
                                "IsValid": 0,
                                "ValidationCode": "abc",
                                "StartTime": 0,
                                "EndTime": 0,
                                "Weekday": [
                                    0
                                ]
                            }
                        ],
                        "IsPreset": 0,
                        "NoticeLanguage": "abc",
                        "PolicyIds": [
                            "abc"
                        ],
                        "AMPConsumerId": "abc",
                        "CLSNotices": [
                            {
                                "Enable": 0,
                                "Region": "abc",
                                "LogSetId": "abc",
                                "TopicId": "abc"
                            }
                        ],
                        "Tags": [
                            {
                                "Key": "abc",
                                "Value": "abc"
                            }
                        ]
                    }
                ],
                "TriggerTasks": [
                    {
                        "Type": "abc",
                        "TaskConfig": "abc"
                    }
                ],
                "ConditionsTemp": {
                    "TemplateName": "abc",
                    "Condition": {
                        "IsUnionRule": 0,
                        "Rules": [
                            {
                                "MetricName": "abc",
                                "Period": 0,
                                "Operator": "abc",
                                "Value": "abc",
                                "ContinuePeriod": 0,
                                "NoticeFrequency": 0,
                                "IsPowerNotice": 0,
                                "Filter": {
                                    "Type": "abc",
                                    "Dimensions": "abc"
                                },
                                "Description": "abc",
                                "Unit": "abc",
                                "RuleType": "abc",
                                "IsAdvanced": 0,
                                "IsOpen": 0,
                                "ProductId": "abc",
                                "ValueMax": 0,
                                "ValueMin": 0,
                                "HierarchicalValue": {
                                    "Remind": "abc",
                                    "Warn": "abc",
                                    "Serious": "abc"
                                }
                            }
                        ],
                        "ComplexExpression": "abc"
                    },
                    "EventCondition": {}
                },
                "LastEditUin": "abc",
                "UpdateTime": 0,
                "InsertTime": 0,
                "Region": [
                    "abc"
                ],
                "NamespaceShowName": "abc",
                "IsDefault": 0,
                "CanSetDefault": 0,
                "InstanceGroupId": 0,
                "InstanceSum": 0,
                "InstanceGroupName": "abc",
                "RuleType": "abc",
                "OriginId": "abc",
                "TagInstances": [
                    {
                        "Key": "abc",
                        "Value": "abc",
                        "InstanceSum": 0,
                        "ServiceType": "abc",
                        "RegionId": 0,
                        "BindingStatus": 0,
                        "TagStatus": 0
                    }
                ],
                "Filter": {
                    "Type": "abc",
                    "Expression": "abc",
                    "Dimensions": "abc"
                },
                "GroupBy": [
                    {
                        "Id": "abc",
                        "Name": "abc"
                    }
                ],
                "FilterDimensionsParam": "abc",
                "IsOneClick": 0,
                "OneClickStatus": 0,
                "AdvancedMetricNumber": 0,
                "IsBindAll": 0,
                "Tags": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "IsSupportAlarmTag": 0
            }
        ],
        "RequestId": "abc"
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
        "TotalCount": 0,
        "Policies": [
            {
                "PolicyId": "abc",
                "PolicyName": "abc",
                "Remark": "abc",
                "MonitorType": "abc",
                "Enable": 0,
                "UseSum": 0,
                "ProjectId": 0,
                "ProjectName": "abc",
                "Namespace": "abc",
                "ConditionTemplateId": "abc",
                "Condition": {
                    "IsUnionRule": 0,
                    "Rules": [
                        {
                            "MetricName": "abc",
                            "Period": 0,
                            "Operator": "abc",
                            "Value": "abc",
                            "ContinuePeriod": 0,
                            "NoticeFrequency": 0,
                            "IsPowerNotice": 0,
                            "Filter": {
                                "Type": "abc",
                                "Dimensions": "abc"
                            },
                            "Description": "abc",
                            "Unit": "abc",
                            "RuleType": "abc",
                            "IsAdvanced": 0,
                            "IsOpen": 0,
                            "ProductId": "abc",
                            "ValueMax": 0,
                            "ValueMin": 0,
                            "HierarchicalValue": {
                                "Remind": "abc",
                                "Warn": "abc",
                                "Serious": "abc"
                            }
                        }
                    ],
                    "ComplexExpression": "abc"
                },
                "EventCondition": {
                    "Rules": [
                        {
                            "MetricName": "abc",
                            "Period": 0,
                            "Operator": "abc",
                            "Value": "abc",
                            "ContinuePeriod": 0,
                            "NoticeFrequency": 0,
                            "IsPowerNotice": 0,
                            "Filter": {
                                "Type": "abc",
                                "Dimensions": "abc"
                            },
                            "Description": "abc",
                            "Unit": "abc",
                            "RuleType": "abc",
                            "IsAdvanced": 0,
                            "IsOpen": 0,
                            "ProductId": "abc",
                            "ValueMax": 0,
                            "ValueMin": 0,
                            "HierarchicalValue": {
                                "Remind": "abc",
                                "Warn": "abc",
                                "Serious": "abc"
                            }
                        }
                    ]
                },
                "NoticeIds": [
                    "abc"
                ],
                "Notices": [
                    {
                        "Id": "abc",
                        "Name": "abc",
                        "UpdatedAt": "abc",
                        "UpdatedBy": "abc",
                        "NoticeType": "abc",
                        "UserNotices": [
                            {
                                "ReceiverType": "abc",
                                "UserIds": [
                                    0
                                ],
                                "GroupIds": [
                                    0
                                ],
                                "StartTime": 0,
                                "EndTime": 0,
                                "NoticeWay": [
                                    "abc"
                                ],
                                "PhoneOrder": [
                                    0
                                ],
                                "PhoneCircleTimes": 0,
                                "PhoneInnerInterval": 0,
                                "PhoneCircleInterval": 0,
                                "NeedPhoneArriveNotice": 0,
                                "PhoneCallType": "abc",
                                "Weekday": [
                                    0
                                ],
                                "OnCallFormIDs": [
                                    "abc"
                                ]
                            }
                        ],
                        "URLNotices": [
                            {
                                "URL": "abc",
                                "IsValid": 0,
                                "ValidationCode": "abc",
                                "StartTime": 0,
                                "EndTime": 0,
                                "Weekday": [
                                    0
                                ]
                            }
                        ],
                        "IsPreset": 0,
                        "NoticeLanguage": "abc",
                        "PolicyIds": [
                            "abc"
                        ],
                        "AMPConsumerId": "abc",
                        "CLSNotices": [
                            {
                                "Enable": 0,
                                "Region": "abc",
                                "LogSetId": "abc",
                                "TopicId": "abc"
                            }
                        ],
                        "Tags": [
                            {
                                "Key": "abc",
                                "Value": "abc"
                            }
                        ]
                    }
                ],
                "TriggerTasks": [
                    {
                        "Type": "abc",
                        "TaskConfig": "abc"
                    }
                ],
                "ConditionsTemp": {
                    "TemplateName": "abc",
                    "Condition": {
                        "IsUnionRule": 0,
                        "Rules": [
                            {
                                "MetricName": "abc",
                                "Period": 0,
                                "Operator": "abc",
                                "Value": "abc",
                                "ContinuePeriod": 0,
                                "NoticeFrequency": 0,
                                "IsPowerNotice": 0,
                                "Filter": {
                                    "Type": "abc",
                                    "Dimensions": "abc"
                                },
                                "Description": "abc",
                                "Unit": "abc",
                                "RuleType": "abc",
                                "IsAdvanced": 0,
                                "IsOpen": 0,
                                "ProductId": "abc",
                                "ValueMax": 0,
                                "ValueMin": 0,
                                "HierarchicalValue": {
                                    "Remind": "abc",
                                    "Warn": "abc",
                                    "Serious": "abc"
                                }
                            }
                        ],
                        "ComplexExpression": "abc"
                    },
                    "EventCondition": {}
                },
                "LastEditUin": "abc",
                "UpdateTime": 0,
                "InsertTime": 0,
                "Region": [
                    "abc"
                ],
                "NamespaceShowName": "abc",
                "IsDefault": 0,
                "CanSetDefault": 0,
                "InstanceGroupId": 0,
                "InstanceSum": 0,
                "InstanceGroupName": "abc",
                "RuleType": "abc",
                "OriginId": "abc",
                "TagInstances": [
                    {
                        "Key": "abc",
                        "Value": "abc",
                        "InstanceSum": 0,
                        "ServiceType": "abc",
                        "RegionId": 0,
                        "BindingStatus": 0,
                        "TagStatus": 0
                    }
                ],
                "Filter": {
                    "Type": "abc",
                    "Expression": "abc",
                    "Dimensions": "abc"
                },
                "GroupBy": [
                    {
                        "Id": "abc",
                        "Name": "abc"
                    }
                ],
                "FilterDimensionsParam": "abc",
                "IsOneClick": 0,
                "OneClickStatus": 0,
                "AdvancedMetricNumber": 0,
                "IsBindAll": 0,
                "Tags": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "IsSupportAlarmTag": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

