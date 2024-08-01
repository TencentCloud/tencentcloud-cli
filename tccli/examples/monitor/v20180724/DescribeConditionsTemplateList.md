**Example 1: 获取告警策略模板列表**



Input: 

```
tccli monitor DescribeConditionsTemplateList --cli-unfold-argument  \
    --ViewName cvm_device \
    --Module monitor \
    --UpdateTimeOrder desc \
    --GroupName test \
    --Limit 1 \
    --Offset 0 \
    --GroupID  1998658
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "TemplateGroupList": [
            {
                "Conditions": [
                    {
                        "AlarmNotifyPeriod": 0,
                        "AlarmNotifyType": 0,
                        "CalcType": "abc",
                        "CalcValue": "abc",
                        "ContinueTime": "abc",
                        "MetricID": 0,
                        "MetricDisplayName": "abc",
                        "Period": 0,
                        "RuleID": 0,
                        "Unit": "abc",
                        "IsAdvanced": 0,
                        "IsOpen": 0,
                        "ProductId": "abc",
                        "HierarchicalValue": {
                            "Remind": "abc",
                            "Warn": "abc",
                            "Serious": "abc"
                        }
                    }
                ],
                "EventConditions": [
                    {
                        "AlarmNotifyPeriod": "abc",
                        "AlarmNotifyType": "abc",
                        "EventID": "abc",
                        "EventDisplayName": "abc",
                        "RuleID": "abc",
                        "MetricName": "abc"
                    }
                ],
                "PolicyGroups": [
                    {
                        "CanSetDefault": true,
                        "GroupID": 0,
                        "GroupName": "abc",
                        "InsertTime": 0,
                        "IsDefault": 0,
                        "Enable": true,
                        "LastEditUin": 0,
                        "NoShieldedInstanceCount": 0,
                        "ParentGroupID": 0,
                        "ProjectID": 0,
                        "ReceiverInfos": [
                            {
                                "EndTime": 0,
                                "NeedSendNotice": 0,
                                "NotifyWay": [
                                    "abc"
                                ],
                                "PersonInterval": 0,
                                "ReceiverGroupList": [
                                    0
                                ],
                                "ReceiverType": "abc",
                                "ReceiverUserList": [
                                    0
                                ],
                                "RecoverNotify": [
                                    "abc"
                                ],
                                "RoundInterval": 0,
                                "RoundNumber": 0,
                                "SendFor": [
                                    "abc"
                                ],
                                "StartTime": 0,
                                "UIDList": [
                                    0
                                ]
                            }
                        ],
                        "Remark": "abc",
                        "UpdateTime": 0,
                        "TotalInstanceCount": 0,
                        "ViewName": "abc",
                        "IsUnionRule": 0
                    }
                ],
                "GroupID": 0,
                "GroupName": "abc",
                "InsertTime": 0,
                "LastEditUin": 0,
                "Remark": "abc",
                "UpdateTime": 0,
                "ViewName": "abc",
                "IsUnionRule": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

