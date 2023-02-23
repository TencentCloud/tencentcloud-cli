**Example 1: 示例1**

通过该接口查询实例 crs-c7nuafdt 的备份列表。

Input: 

```
tccli redis DescribeInstanceBackups --cli-unfold-argument  \
    --Status 2 \
    --InstanceId crs-c7nuafdt \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "BackupSet": [
            {
                "BackupId": "154572601-1165734322-153731238",
                "BackupSize": 191,
                "BackupType": "0",
                "EndTime": "2022-12-23 16:25:18",
                "ExpireTime": "2022-12-30 16:24:41",
                "FileType": "RDB-Redis 4.0",
                "FullBackup": 0,
                "InstanceId": "crs-c7nuafdt",
                "InstanceName": "备份test",
                "InstanceType": 6,
                "Locked": 0,
                "Region": "ap-guangzhou",
                "Remark": "test001",
                "StartTime": "2022-12-23 16:24:41",
                "Status": 2
            }
        ],
        "RequestId": "2a95bfa4-ac8c-43cd-b7b1-5a93817d8de2",
        "TotalCount": 1
    }
}
```

