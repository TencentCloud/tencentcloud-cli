**Example 1: 查询备份统计信息**



Input: 

```
tccli postgres DescribeBackupSummaries --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "BackupSummarySet": [
            {
                "AutoBaseBackupCount": 3,
                "AutoBaseBackupSize": 3535342436352,
                "DBInstanceId": "postgres-lsw5y0bp",
                "LogBackupCount": 2,
                "LogBackupSize": 167792640,
                "ManualBaseBackupCount": 1,
                "ManualBaseBackupSize": 1178447478784,
                "TotalBackupCount": 6,
                "TotalBackupSize": 4713957707776
            }
        ],
        "RequestId": "3929dd3a-d95d-4ec2-ae69-a98317ce24fa",
        "TotalCount": 10
    }
}
```

