**Example 1: 查询数据库详细配置信息**

查询数据库详细配置信息

Input: 

```
tccli sqlserver DescribeDatabasesNormal --cli-unfold-argument  \
    --InstanceId mssql-ds3p26cv
```

Output: 
```
{
    "Response": {
        "DBList": [
            {
                "CollationName": "Chinese_PRC_CI_AS",
                "CreateTime": "2023-09-21 21:37:47.327",
                "IsAutoCleanupOn": "",
                "IsBrokerEnabled": "0",
                "IsCdcEnabled": "0",
                "IsDbChainingOn": "0",
                "IsEncrypted": "0",
                "IsFullTextEnabled": "",
                "IsFulltextEnabled": "1",
                "IsMirroring": "0",
                "IsPublished": "0",
                "IsReadCommittedSnapshotOn": "0",
                "IsSubscribed": "0",
                "IsTrustworthyOn": "0",
                "MirroringState": "",
                "Name": "test_db3",
                "RecoveryModelDesc": "FULL",
                "RetentionPeriod": "",
                "StateDesc": "ONLINE",
                "UserAccessDesc": "MULTI_USER"
            },
            {
                "CollationName": "Chinese_PRC_CI_AS",
                "CreateTime": "2023-09-20 20:21:50.360",
                "IsAutoCleanupOn": "",
                "IsBrokerEnabled": "0",
                "IsCdcEnabled": "1",
                "IsDbChainingOn": "0",
                "IsEncrypted": "0",
                "IsFullTextEnabled": "",
                "IsFulltextEnabled": "1",
                "IsMirroring": "0",
                "IsPublished": "0",
                "IsReadCommittedSnapshotOn": "0",
                "IsSubscribed": "0",
                "IsTrustworthyOn": "0",
                "MirroringState": "",
                "Name": "test_db",
                "RecoveryModelDesc": "FULL",
                "RetentionPeriod": "",
                "StateDesc": "ONLINE",
                "UserAccessDesc": "MULTI_USER"
            },
            {
                "CollationName": "Chinese_PRC_CI_AS",
                "CreateTime": "2023-09-21 15:49:47.903",
                "IsAutoCleanupOn": "1",
                "IsBrokerEnabled": "0",
                "IsCdcEnabled": "0",
                "IsDbChainingOn": "1",
                "IsEncrypted": "0",
                "IsFullTextEnabled": "",
                "IsFulltextEnabled": "1",
                "IsMirroring": "0",
                "IsPublished": "0",
                "IsReadCommittedSnapshotOn": "0",
                "IsSubscribed": "0",
                "IsTrustworthyOn": "0",
                "MirroringState": "",
                "Name": "test_db2",
                "RecoveryModelDesc": "FULL",
                "RetentionPeriod": "3",
                "StateDesc": "ONLINE",
                "UserAccessDesc": "MULTI_USER"
            }
        ],
        "RequestId": "0cc5e70b-6abe-4e42-8486-68f4348a0568",
        "TotalCount": 3
    }
}
```

