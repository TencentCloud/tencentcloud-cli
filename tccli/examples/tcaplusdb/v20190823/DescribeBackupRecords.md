**Example 1: 获取审批申请**



Input: 

```
tccli tcaplusdb DescribeBackupRecords --cli-unfold-argument  \
    --Limit 1 \
    --ClusterId xx \
    --TableGroupId xx \
    --TableName xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 92,
        "BackupRecords": [
            {
                "BackupBatchTime": "xx",
                "AppId": 1,
                "TableName": "xx",
                "ZoneId": 1,
                "BackupType": "xx",
                "FileTag": "xx",
                "ShardCount": 1,
                "BackupExpireTime": "xx",
                "BackupSuccRate": "xx",
                "BackupFileSize": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

