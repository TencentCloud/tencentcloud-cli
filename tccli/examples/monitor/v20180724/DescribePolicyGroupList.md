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
                "CanSetDefault": true,
                "Conditions": [
                    {
                        "AlarmNotifyPeriod": 86400,
                        "AlarmNotifyType": 0,
                        "CalcType": 1,
                        "CalcValue": "0",
                        "ContinueTime": 60,
                        "MetricId": 33,
                        "MetricShowName": "CPU利用率",
                        "Period": 60,
                        "RuleId": 1111111,
                        "Unit": "%"
                    }
                ],
                "ConditionsTemp": null,
                "EventConditions": [
                    {
                        "AlarmNotifyPeriod": 0,
                        "AlarmNotifyType": 0,
                        "EventId": 42,
                        "EventShowName": "ping不可达",
                        "RuleId": 1111112
                    }
                ],
                "GroupId": 1111111,
                "GroupName": "复制-test",
                "InsertTime": 1531122504,
                "InstanceGroup": null,
                "IsDefault": 0,
                "IsOpen": true,
                "LastEditUin": "1500000000",
                "NoShieldedSum": 0,
                "ParentGroupId": 0,
                "ProjectId": 0,
                "ReceiverInfos": [
                    {
                        "EndTime": 86400,
                        "NeedSendNotice": 1,
                        "NotifyWay": [
                            "EMAIL",
                            "SMS"
                        ],
                        "PersonInterval": 60,
                        "ReceiverGroupList": [
                            1111
                        ],
                        "ReceiverType": "group",
                        "ReceiverUserList": [],
                        "RecoverNotify": [
                            "SMS"
                        ],
                        "RoundInterval": 60,
                        "RoundNumber": 2,
                        "SendFor": [],
                        "StartTime": 0,
                        "UidList": null
                    }
                ],
                "Remark": "",
                "UpdateTime": 1577689096,
                "UseSum": 0,
                "ViewName": "cvm_device"
            },
            {
                "CanSetDefault": false,
                "Conditions": [
                    {
                        "AlarmNotifyPeriod": 0,
                        "AlarmNotifyType": 0,
                        "CalcType": 1,
                        "CalcValue": "0.85",
                        "ContinueTime": 300,
                        "MetricId": 1220,
                        "MetricShowName": "磁盘使用百分比",
                        "Period": 60,
                        "RuleId": 1111113,
                        "Unit": ""
                    }
                ],
                "ConditionsTemp": null,
                "EventConditions": null,
                "GroupId": 1111112,
                "GroupName": "默认",
                "InsertTime": 1565792922,
                "InstanceGroup": null,
                "IsDefault": 1,
                "IsOpen": true,
                "LastEditUin": "1500000687",
                "NoShieldedSum": 1,
                "ParentGroupId": 0,
                "ProjectId": 0,
                "ReceiverInfos": null,
                "Remark": "",
                "UpdateTime": 1565792922,
                "UseSum": 1,
                "ViewName": "CKAFKA_INSTANCE"
            }
        ],
        "RequestId": "5fdf1257-6024-4b59-b924-2b995080f0bd",
        "Total": 142,
        "Warning": "This method is deprecated! Use `DescribeAlarmPolicies` instead!"
    }
}
```

