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
                "AlarmObject": "10.104.126.8 (内)  | 同环比告警1 | 基础网络",
                "Content": "CPU利用率 >0%",
                "FirstOccurTime": 1603117860,
                "LastOccurTime": 1603162964,
                "AlarmStatus": "ALARM",
                "PolicyId": "bd010610-cfd1-4bdd-9e2d-83421ce2f3ce",
                "PolicyName": "gao",
                "VPC": "0",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "InstanceGroup": [
                    {
                        "Id": 430,
                        "Name": "test-instance-group"
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
                "Region": "test-master",
                "PolicyExists": 1
            },
            {
                "AlarmId": "779d129a-40a1-4acf-b226-d9c2ae26e63b",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "AlarmObject": "10.104.126.8 (内)  | 同环比告警1 | 基础网络",
                "Content": "CPU利用率 >0%",
                "FirstOccurTime": 1603117860,
                "LastOccurTime": 1603162964,
                "AlarmStatus": "ALARM",
                "PolicyId": "91cd9e02-4846-4f90-a04e-ff0343798063",
                "PolicyName": "迁移测试2",
                "VPC": "0",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "InstanceGroup": [
                    {
                        "Id": 430,
                        "Name": "test-instance-group"
                    }
                ],
                "ReceiverUids": [],
                "ReceiverGroups": [],
                "NoticeWays": [],
                "EventId": 0,
                "AlarmType": "METRIC",
                "OriginId": "1276973",
                "Region": "test-master",
                "PolicyExists": 1
            }
        ],
        "RequestId": "4bzogxhgsgs95hgmxne5ei6y9jjxvi1f",
        "TotalCount": 486
    }
}
```

