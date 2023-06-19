**Example 1: 查询数据库列表**

查询数据库列表

Input: 

```
tccli dlc DescribeDatabases --cli-unfold-argument  \
    --DatasourceConnectionName DataLakeCatalog \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "DatabaseList": [
            {
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
                    "GovernEngine": "abc"
                },
                "DatabaseId": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

