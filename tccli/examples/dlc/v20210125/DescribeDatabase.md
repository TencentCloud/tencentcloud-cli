**Example 1: 查询数据库详细信息**



Input: 

```
tccli dlc DescribeDatabase --cli-unfold-argument  \
    --DatasourceConnectionName DataLakeCatalog \
    --DatabaseName testDb
```

Output: 
```
{
    "Response": {
        "DatabaseInfo": {
            "DatabaseName": "abc",
            "Comment": "abc",
            "Properties": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "CreateTime": "abc",
            "ModifiedTime": "abc",
            "Location": "abc",
            "UserAlias": "abc",
            "UserSubUin": "abc",
            "GovernPolicy": {
                "RewriteDataPolicy": {
                    "RewriteDataEnable": "abc",
                    "Engine": "abc",
                    "MinInputFiles": 0,
                    "TargetFileSizeBytes": 0,
                    "IntervalMin": 0
                },
                "ExpiredSnapshotsPolicy": {
                    "ExpiredSnapshotsEnable": "abc",
                    "Engine": "abc",
                    "RetainLast": 0,
                    "BeforeDays": 0,
                    "MaxConcurrentDeletes": 0,
                    "IntervalMin": 0
                },
                "RemoveOrphanFilesPolicy": {
                    "RemoveOrphanFilesEnable": "abc",
                    "Engine": "abc",
                    "BeforeDays": 0,
                    "MaxConcurrentDeletes": 0,
                    "IntervalMin": 0
                },
                "MergeManifestsPolicy": {
                    "MergeManifestsEnable": "abc",
                    "Engine": "abc",
                    "IntervalMin": 0
                },
                "InheritDataBase": "abc",
                "RuleType": "abc",
                "GovernEngine": "abc",
                "Mode": 0,
                "PrimaryKeys": "abc"
            },
            "DatabaseId": "abc"
        },
        "RequestId": "abc"
    }
}
```

