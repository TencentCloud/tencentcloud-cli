**Example 1: 获取审批申请**



Input: 

```
tccli tcaplusdb DescribeBackupRecords --cli-unfold-argument  \
    --ClusterId 1345225 \
    --Limit 0 \
    --Offset 0 \
    --TableGroupId 2313 \
    --TableName testname
```

Output: 
```
{
    "Response": {
        "BackupRecords": [
            {
                "ZoneId": 1,
                "TableName": "testname",
                "BackupType": "1",
                "FileTag": "2",
                "ShardCount": 1,
                "BackupBatchTime": "17844564",
                "BackupFileSize": 1,
                "BackupSuccRate": "1",
                "BackupExpireTime": "17844564",
                "AppId": 1
            }
        ],
        "TotalCount": 0,
        "RequestId": "213123-2131"
    }
}
```

