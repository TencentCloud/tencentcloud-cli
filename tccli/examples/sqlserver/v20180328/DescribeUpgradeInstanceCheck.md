**Example 1: 实例变配前的检查**



Input: 

```
tccli sqlserver DescribeUpgradeInstanceCheck --cli-unfold-argument  \
    --InstanceId mssql-8lv5lbnn \
    --Cpu 4 \
    --Memory 16 \
    --Storage 200 \
    --DBVersion 2019 \
    --ThroughputPerformance 100
```

Output: 
```
{
    "Response": {
        "IsAffect": 1,
        "Passed": 1,
        "ModifyMode": "up",
        "CheckItems": [
            {
                "CheckName": "CPU",
                "CurrentValue": "2",
                "Passed": 1,
                "IsAffect": 1,
                "Msg": "CPU will be upgraded from 2 to 4",
                "MsgCode": 0
            },
            {
                "CheckName": "Memory",
                "CurrentValue": "8",
                "Passed": 1,
                "IsAffect": 1,
                "Msg": "Memory will be upgraded from 8GB to 16GB",
                "MsgCode": 0
            },
            {
                "CheckName": "Storage",
                "CurrentValue": "100",
                "Passed": 1,
                "IsAffect": 1,
                "Msg": "Storage will be upgraded from 100GB to 200GB",
                "MsgCode": 0
            },
            {
                "CheckName": "MasterStorage",
                "CurrentValue": "",
                "Passed": 1,
                "IsAffect": 0,
                "Msg": "",
                "MsgCode": 0
            },
            {
                "CheckName": "UpGradeType",
                "CurrentValue": "",
                "Passed": 1,
                "IsAffect": 1,
                "Msg": "Instance will be migrated during the upgrade",
                "MsgCode": 0
            }
        ],
        "RequestId": "5d2b4b33-11f3-4e70-835f-3478e6575371"
    }
}
```

