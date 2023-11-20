**Example 1: 检查实例变配**



Input: 

```
tccli sqlserver DescribeUpgradeInstanceCheck --cli-unfold-argument  \
    --InstanceId mssql-30vft2ix \
    --Cpu 2 \
    --Memory 16 \
    --Storage 256 \
    --DBVersion 2017 \
    --HAType CLUSTER \
    --MultiZones SameZones
```

Output: 
```
{
    "Response": {
        "CheckItems": [
            {
                "CheckName": "CK_CPU",
                "CurrentValue": "0",
                "IsAffect": 0,
                "Msg": "",
                "MsgCode": 0,
                "Passed": 1
            },
            {
                "CheckName": "CK_MASTER_STORAGE",
                "CurrentValue": "",
                "IsAffect": 0,
                "Msg": "",
                "MsgCode": 0,
                "Passed": 1
            },
            {
                "CheckName": "CK_MEMORY",
                "CurrentValue": "0",
                "IsAffect": 0,
                "Msg": "",
                "MsgCode": 0,
                "Passed": 1
            },
            {
                "CheckName": "CK_STORAGE",
                "CurrentValue": "0",
                "IsAffect": 0,
                "Msg": "",
                "MsgCode": 0,
                "Passed": 1
            },
            {
                "CheckName": "CK_UPGRATE",
                "CurrentValue": "MIGRATE",
                "IsAffect": 1,
                "Msg": "version 2008 -> 2017 upgrade requires data migration",
                "MsgCode": 5,
                "Passed": 1
            }
        ],
        "IsAffect": 1,
        "ModifyMode": "up",
        "Passed": 1,
        "RequestId": "44416ab3-794e-47e2-840c-f645efc3481c"
    }
}
```

