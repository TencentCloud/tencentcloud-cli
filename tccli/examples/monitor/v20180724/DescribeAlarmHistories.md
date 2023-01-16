**Example 1: 查询告警历史**



Input: 

```
tccli monitor DescribeAlarmHistories --cli-unfold-argument  \
    --Module monitor \
    --PageNumber 1 \
    --PageSize 10 \
    --StartTime 1598976507 \
    --EndTime 1599019707
```

Output: 
```
{
    "Response": {
        "TotalCount": 486,
        "Histories": [
            {
                "Dimensions": "xx",
                "LastOccurTime": 1603162964,
                "Namespace": "xx",
                "Content": "xx",
                "PolicyId": "xx",
                "AlarmStatus": "xx",
                "ReceiverGroups": [
                    1544
                ],
                "VPC": "xx",
                "FirstOccurTime": 1603117860,
                "EventId": 0,
                "PolicyName": "xx",
                "ProjectId": 0,
                "Region": "xx",
                "AlarmObject": "xx",
                "AlarmId": "xx",
                "ReceiverUids": [
                    0
                ],
                "OriginId": "xx",
                "NoticeWays": [
                    "SMS",
                    "EMAIL",
                    "WECHAT"
                ],
                "ProjectName": "xx",
                "InstanceGroup": [
                    {
                        "Id": 430,
                        "Name": "xx"
                    }
                ],
                "MetricsInfo": [
                    {
                        "Description": "xx",
                        "QceNamespace": "xx",
                        "Period": 60,
                        "Value": "xx",
                        "MetricName": "xx"
                    }
                ],
                "MonitorType": "xx",
                "PolicyExists": 1,
                "AlarmType": "xx"
            },
            {
                "Dimensions": "xx",
                "LastOccurTime": 1603162964,
                "Namespace": "xx",
                "Content": "xx",
                "PolicyId": "xx",
                "AlarmStatus": "xx",
                "ReceiverGroups": [
                    0
                ],
                "VPC": "xx",
                "FirstOccurTime": 1603117860,
                "EventId": 0,
                "PolicyName": "xx",
                "ProjectId": 0,
                "Region": "xx",
                "AlarmObject": "xx",
                "AlarmId": "xx",
                "ReceiverUids": [
                    0
                ],
                "OriginId": "xx",
                "NoticeWays": [
                    "xx"
                ],
                "ProjectName": "xx",
                "InstanceGroup": [
                    {
                        "Id": 430,
                        "Name": "xx"
                    }
                ],
                "MetricsInfo": [
                    {
                        "Description": "xx",
                        "QceNamespace": "xx",
                        "Period": 0,
                        "Value": "xx",
                        "MetricName": "xx"
                    }
                ],
                "MonitorType": "xx",
                "PolicyExists": 1,
                "AlarmType": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: 查询“云服务器-基础监控”的告警历史**

监控类型是一级概念，策略类型是二级概念，因此在 Namespaces 字段中只有在指定监控类型后，策略类型才有意义。

如果要查询“云服务器-基础监控”的告警历史，这里的过滤条件应为：监控类型=“云产品监控”，策略类型=“云服务器-基础监控”

MonitorTypes 作为一级过滤条件应填入 `["MT_QCE"]`

Namespaces 作为二级过滤条件应填入 `[{"MonitorType": "MT_QCE", "Namespace": "cvm_device"}]`

Input: 

```
tccli monitor DescribeAlarmHistories --cli-unfold-argument  \
    --Module monitor \
    --PageNumber 1 \
    --PageSize 10 \
    --StartTime 1598976507 \
    --EndTime 1599019707 \
    --MonitorTypes MT_QCE \
    --Namespaces.0.MonitorType MT_QCE \
    --Namespaces.0.Namespace cvm_device
```

Output: 
```
{
    "Response": {
        "Histories": [
            {
                "AlarmId": "c36494f8-ae38-45cb-8089-e14006bcfc67",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "AlarmObject": "10.104.126.8 (内) | 服务器01 | 基础网络",
                "Content": "CPU利用率 >0%",
                "FirstOccurTime": 1603117860,
                "LastOccurTime": 1603162964,
                "AlarmStatus": "ALARM",
                "PolicyId": "policy-abc01",
                "PolicyName": "CVM告警策略1",
                "VPC": "0",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "InstanceGroup": [
                    {
                        "Id": 430,
                        "Name": "example-instance-group"
                    }
                ],
                "ReceiverUids": [],
                "ReceiverGroups": [
                    1544
                ],
                "NoticeWays": [
                    "SMS",
                    "EMAIL",
                    "WECHAT"
                ],
                "EventId": 0,
                "AlarmType": "METRIC",
                "OriginId": "1278441",
                "Region": "gz",
                "PolicyExists": 1,
                "MetricsInfo": [
                    {
                        "QceNamespace": "qce/cvm",
                        "MetricName": "CpuUsage",
                        "Period": 60,
                        "Value": "86.5",
                        "Description": "CPU利用率"
                    }
                ]
            },
            {
                "AlarmId": "779d129a-40a1-4acf-b226-d9c2ae26e63b",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "AlarmObject": "10.104.126.9 (内) | 服务器02 | 基础网络",
                "Content": "CPU利用率 >0%",
                "FirstOccurTime": 1603117860,
                "LastOccurTime": 1603162964,
                "AlarmStatus": "ALARM",
                "PolicyId": "policy-abc02",
                "PolicyName": "CVM告警策略2",
                "VPC": "0",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "InstanceGroup": [
                    {
                        "Id": 430,
                        "Name": "example-instance-group"
                    }
                ],
                "ReceiverUids": [],
                "ReceiverGroups": [],
                "NoticeWays": [],
                "EventId": 0,
                "AlarmType": "METRIC",
                "OriginId": "1276973",
                "Region": "gz",
                "PolicyExists": 1,
                "MetricsInfo": null
            }
        ],
        "RequestId": "4bzogxhgsgs95hgmxne5ei6y9jjxvi1f",
        "TotalCount": 486
    }
}
```

