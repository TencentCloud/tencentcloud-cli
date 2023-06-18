**Example 1: 查询默认数据治理规则**

查询默认数据治理规则

Input: 

```
tccli dlc DescribeGovernDefaultPolicy --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Threshold": {
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
        "RequestId": "abc"
    }
}
```

