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
                "GroupName": "default-alarm-group",
                "IsOpen": true,
                "ViewName": "cvm_device",
                "LastEditUin": "100000001",
                "UpdateTime": 0,
                "InsertTime": 0,
                "UseSum": 0,
                "NoShieldedSum": 0,
                "IsDefault": 0,
                "CanSetDefault": true,
                "ParentGroupId": 0,
                "Remark": "默认告警策略组",
                "ProjectId": 0,
                "Conditions": [
                    {
                        "MetricShowName": "CPU利用率",
                        "Period": 0,
                        "MetricId": 0,
                        "RuleId": 0,
                        "Unit": "%",
                        "AlarmNotifyType": 0,
                        "AlarmNotifyPeriod": 0,
                        "CalcType": 0,
                        "CalcValue": "90",
                        "ContinueTime": 0,
                        "MetricName": "cpu_usage"
                    }
                ],
                "EventConditions": [
                    {
                        "EventId": 0,
                        "RuleId": 0,
                        "EventShowName": "磁盘只读",
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
                        "ReceiverType": "group",
                        "NotifyWay": [
                            "SMS"
                        ],
                        "UidList": [
                            0
                        ],
                        "RoundNumber": 0,
                        "RoundInterval": 0,
                        "PersonInterval": 0,
                        "NeedSendNotice": 0,
                        "SendFor": [
                            "ALARM"
                        ],
                        "RecoverNotify": [
                            "SMS"
                        ],
                        "ReceiveLanguage": "zh-CN"
                    }
                ],
                "ConditionsTemp": {
                    "GroupId": 0,
                    "GroupName": "default-alarm-group",
                    "ViewName": "cvm_device",
                    "Remark": "默认告警策略组",
                    "LastEditUin": "100000001",
                    "UpdateTime": 0,
                    "InsertTime": 0,
                    "IsUnionRule": 0
                },
                "InstanceGroup": {
                    "InstanceGroupId": 0,
                    "ViewName": "cvm_device",
                    "LastEditUin": "100000001",
                    "GroupName": "default-instance-group",
                    "InstanceSum": 0,
                    "UpdateTime": 0,
                    "InsertTime": 0
                },
                "IsUnionRule": 0
            }
        ],
        "Total": 0,
        "Warning": "",
        "RequestId": "wafdafasdfew-adfadfasfdeaf-erqer"
    }
}
```

