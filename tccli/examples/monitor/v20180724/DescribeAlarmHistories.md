**Example 1: 查询告警历史**



Input: 

```
tccli monitor DescribeAlarmHistories --cli-unfold-argument  \
    --Module monitor \
    --PolicyName policy \
    --PageNumber 1 \
    --PageSize 10 \
    --StartTime 1598976507 \
    --EndTime 1599019707
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
                "MetricsInfo": null
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

