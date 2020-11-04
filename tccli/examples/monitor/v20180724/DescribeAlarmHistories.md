**Example 1: 获取告警历史列表**



Input: 

```
tccli monitor DescribeAlarmHistories --cli-unfold-argument  \
    --Module monitor\
    --PageNumber 1\
    --PageSize 100\
    --Order DESC\
    --StartTime 1598976507\
    --EndTime 1599019707\
    --AlarmObject object\
    --MonitorTypes MT_QCE\
    --AlarmStatus ALARM\
    --ProjectIds 0\
    --InstanceGroupIds 0\
    --MetricNames mem_used\
    --PolicyName policy\
    --Content content\
    --ReceiverUids 10000\
    --ReceiverGroups 10000\
    --Namespaces.0.MonitorType MT_QCE\
    --Namespaces.0.Namespace cvm_device
```

Output: 
```
{
    "TotalCount": 2,
    "Histories": [
        {
            "AlarmId": "g34jgh3-t3cc3c23-cv23vc234c",
            "MonitorType": "MT_QCE_METRIC",
            "Namespace": "cvm_device",
            "AlarmObject": "9.142.151.35",
            "Content": "CPU 利用率 >= 99.99%",
            "FirstOccurTime": 1597240790,
            "LastOccurTime": 1597250790,
            "AlarmStatus": "ALARM",
            "PolicyId": "195491",
            "PolicyName": "告警策略",
            "VPC": "-",
            "ProjectId": 0,
            "ProjectName": "默认项目",
            "InstanceGroup": [
                {
                    "Id": 123,
                    "Name": "我是一个实例组"
                }
            ],
            "ReceiverUids": [
                1451455,
                125151,
                616677
            ],
            "ReceiverGroups": [],
            "NoticeWays": [
                "SMS",
                "EMAIL"
            ],
            "OriginId": "100"
        },
        {
            "AlarmId": "g34jgh3-t3cc3c23-ag4hg3y3h2",
            "MonitorType": "MT_CUSTOM",
            "Namespace": "custom_test_space",
            "AlarmObject": "host = 127.0.0.1",
            "Content": "告警",
            "FirstOccurTime": 1597240790,
            "LastOccurTime": 1597250790,
            "AlarmStatus": "ALARM",
            "PolicyId": "195492",
            "PolicyName": "告警策略",
            "VPC": "-",
            "ProjectId": -1,
            "ProjectName": "-",
            "InstanceGroup": [],
            "ReceiverUids": [],
            "ReceiverGroups": [
                12345,
                56789
            ],
            "NoticeWays": [
                "CALL"
            ],
            "OriginId": "policy-msjftixf"
        }
    ]
}
```

