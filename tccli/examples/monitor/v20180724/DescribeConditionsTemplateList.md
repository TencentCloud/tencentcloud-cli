**Example 1: 获取告警策略模板列表**



Input: 

```
tccli monitor DescribeConditionsTemplateList --cli-unfold-argument  \
    --ViewName cvm_device \
    --Module monitor \
    --UpdateTimeOrder desc \
    --GroupName cpu \
    --Limit 1 \
    --Offset 0 \
    --GroupID  1998658
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "TemplateGroupList": [
            {
                "Conditions": [
                    {
                        "AlarmNotifyPeriod": 86400,
                        "AlarmNotifyType": 0,
                        "CalcType": "1",
                        "CalcValue": "95",
                        "ContinueTime": "300",
                        "MetricID": 33,
                        "MetricDisplayName": "CPU利用率",
                        "Period": 60,
                        "RuleID": 100001,
                        "Unit": "%",
                        "IsAdvanced": 0,
                        "IsOpen": 1,
                        "ProductId": "cvm",
                        "HierarchicalValue": {
                            "Remind": "80",
                            "Warn": "90",
                            "Serious": "95"
                        }
                    }
                ],
                "EventConditions": [
                    {
                        "AlarmNotifyPeriod": "86400",
                        "AlarmNotifyType": "0",
                        "EventID": "disk_readonly",
                        "EventDisplayName": "磁盘只读",
                        "RuleID": "200001",
                        "MetricName": "disk_readonly"
                    }
                ],
                "PolicyGroups": [
                    {
                        "CanSetDefault": true,
                        "GroupID": 4001,
                        "GroupName": "生产环境告警策略",
                        "InsertTime": 1719302400,
                        "IsDefault": 0,
                        "Enable": true,
                        "LastEditUin": 100012345,
                        "NoShieldedInstanceCount": 15,
                        "ParentGroupID": 3001,
                        "ProjectID": 0,
                        "ReceiverInfos": [
                            {
                                "EndTime": 86399,
                                "NeedSendNotice": 1,
                                "NotifyWay": [
                                    "SMS",
                                    "EMAIL",
                                    "WECHAT"
                                ],
                                "PersonInterval": 3600,
                                "ReceiverGroupList": [
                                    5001
                                ],
                                "ReceiverType": "group",
                                "ReceiverUserList": [
                                    100012345
                                ],
                                "RecoverNotify": [
                                    "SMS",
                                    "EMAIL"
                                ],
                                "RoundInterval": 60,
                                "RoundNumber": 3,
                                "SendFor": [
                                    "alarm",
                                    "ok"
                                ],
                                "StartTime": 0,
                                "UIDList": [
                                    100012345
                                ]
                            }
                        ],
                        "Remark": "生产环境核心主机告警",
                        "UpdateTime": 1719388800,
                        "TotalInstanceCount": 20,
                        "ViewName": "cvm_device",
                        "IsUnionRule": 0
                    }
                ],
                "GroupID": 3001,
                "GroupName": "CVM基础监控模板",
                "InsertTime": 1719302400,
                "LastEditUin": 100012345,
                "Remark": "适用于CVM实例的基础监控告警模板",
                "UpdateTime": 1719388800,
                "ViewName": "cvm_device",
                "IsUnionRule": 0
            }
        ],
        "RequestId": "f8a7e6d5-c4b3-2a19-8e7f-0d1c2b3a4e5f"
    }
}
```

