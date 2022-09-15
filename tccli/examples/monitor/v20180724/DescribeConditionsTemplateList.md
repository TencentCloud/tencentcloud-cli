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
        "RequestId": "853dafdc-22d4-4e9d-88a7-ebc43abf7cef",
        "TemplateGroupList": [
            {
                "Conditions": [
                    {
                        "AlarmNotifyPeriod": 0,
                        "AlarmNotifyType": 0,
                        "CalcType": "",
                        "CalcValue": "",
                        "ContinueTime": "",
                        "MetricDisplayName": "机器重启",
                        "MetricID": 25,
                        "Period": 60,
                        "RuleID": 5001158,
                        "Unit": ""
                    }
                ],
                "EventConditions": [
                    {
                        "AlarmNotifyPeriod": "0",
                        "AlarmNotifyType": "0",
                        "EventDisplayName": "ping不可达",
                        "EventID": "42",
                        "RuleID": "5001160"
                    }
                ],
                "GroupID": 1998664,
                "GroupName": "test",
                "InsertTime": 1567074714,
                "LastEditUin": 1500000687,
                "IsUnionRule": 0,
                "PolicyGroups": [
                    {
                        "CanSetDefault": true,
                        "Enable": true,
                        "GroupID": 1998665,
                        "GroupName": "test2",
                        "InsertTime": 1567075011,
                        "IsDefault": 0,
                        "LastEditUin": 1500000687,
                        "NoShieldedInstanceCount": 1,
                        "ParentGroupID": 1998664,
                        "ProjectID": 0,
                        "ReceiverInfos": [
                            {
                                "EndTime": 57599,
                                "NeedSendNotice": 1,
                                "NotifyWay": [
                                    "EMAIL",
                                    "SMS"
                                ],
                                "PersonInterval": 60,
                                "ReceiverGroupList": null,
                                "ReceiverType": "group",
                                "ReceiverUserList": null,
                                "RecoverNotify": [
                                    "SMS"
                                ],
                                "RoundInterval": 60,
                                "RoundNumber": 2,
                                "SendFor": null,
                                "StartTime": 57600,
                                "UIDList": null
                            }
                        ],
                        "Remark": "test2",
                        "TotalInstanceCount": 1,
                        "UpdateTime": 1567075012,
                        "ViewName": "cvm_device"
                    }
                ],
                "Remark": "test",
                "UpdateTime": 1567074881,
                "ViewName": "cvm_device"
            }
        ],
        "Total": 1
    }
}
```

