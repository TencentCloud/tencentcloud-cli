**Example 1: 查询数据库详细配置信息**

查询数据库详细配置信息

Input: 

```
tccli sqlserver DescribeDBsNormal --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DBList": [
            {
                "IsFulltextEnabled": "0",
                "UserAccessDesc": "MULTI_USER",
                "IsMirroring": "1",
                "CollationName": "Chinese_PRC_CI_AS",
                "RecoveryModelDesc": "FULL",
                "IsSubscribed": "1",
                "StateDesc": "ONLINE",
                "IsCdcEnabled": "1",
                "MirroringState": "SYNCHRONIZED",
                "IsPublished": "1",
                "RetentionPeriod": "20",
                "IsDbChainingOn": "1",
                "IsEncrypted": "0",
                "IsTrustworthyOn": "1",
                "IsReadCommittedSnapshotOn": "0",
                "IsBrokerEnabled": "1",
                "IsAutoCleanupOn": "1",
                "Name": "db_test"
            }
        ],
        "RequestId": "9607d890-db08-11eb-9f54-a9df121c01af"
    }
}
```

