**Example 1: 获取头两个基础策略告警组列表**



Input: 

```
tccli monitor DescribePolicyGroupList --cli-unfold-argument  \
    --Limit 2 \
    --Module monitor \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "GroupList": [
            {
                "GroupId": 0,
                "GroupName": "abc",
                "IsOpen": true,
                "ViewName": "abc",
                "LastEditUin": "abc",
                "UpdateTime": 0,
                "InsertTime": 0,
                "UseSum": 0,
                "NoShieldedSum": 0,
                "IsDefault": 0,
                "CanSetDefault": true,
                "ParentGroupId": 0,
                "Remark": "abc",
                "ProjectId": 0,
                "Conditions": [
                    {
                        "MetricShowName": "abc",
                        "Period": 0,
                        "MetricId": 0,
                        "RuleId": 0,
                        "Unit": "abc",
                        "AlarmNotifyType": 0,
                        "AlarmNotifyPeriod": 0,
                        "CalcType": 0,
                        "CalcValue": "abc",
                        "ContinueTime": 0,
                        "MetricName": "abc"
                    }
                ],
                "EventConditions": [
                    {
                        "EventId": 0,
                        "RuleId": 0,
                        "EventShowName": "abc",
                        "AlarmNotifyPeriod": 0,
                        "AlarmNotifyType": 0
                    }
                ],
                "ReceiverInfos": [
                    {
                        "ReceiverGroupList": [
                            0
                        ],
                        "ReceiverUserList": [
                            0
                        ],
                        "StartTime": 0,
                        "EndTime": 0,
                        "ReceiverType": "abc",
                        "NotifyWay": [
                            "abc"
                        ],
                        "UidList": [
                            0
                        ],
                        "RoundNumber": 0,
                        "RoundInterval": 0,
                        "PersonInterval": 0,
                        "NeedSendNotice": 0,
                        "SendFor": [
                            "abc"
                        ],
                        "RecoverNotify": [
                            "abc"
                        ],
                        "ReceiveLanguage": "abc"
                    }
                ],
                "ConditionsTemp": {
                    "GroupId": 0,
                    "GroupName": "abc",
                    "ViewName": "abc",
                    "Remark": "abc",
                    "LastEditUin": "abc",
                    "UpdateTime": 0,
                    "InsertTime": 0,
                    "IsUnionRule": 0
                },
                "InstanceGroup": {
                    "InstanceGroupId": 0,
                    "ViewName": "abc",
                    "LastEditUin": "abc",
                    "GroupName": "abc",
                    "InstanceSum": 0,
                    "UpdateTime": 0,
                    "InsertTime": 0
                },
                "IsUnionRule": 0
            }
        ],
        "Total": 0,
        "Warning": "abc",
        "RequestId": "abc"
    }
}
```

