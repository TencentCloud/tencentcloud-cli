**Example 1: 示例 1**



Input: 

```
tccli redis DescribeInstanceBackups --cli-unfold-argument  \
    --InstanceId crs-ei43p3gr
```

Output: 
```
{
    "Response": {
        "BackupSet": [
            {
                "BackupId": "165706342-5832225-1641692389",
                "BackupSize": 537,
                "BackupType": "1",
                "Encrypted": false,
                "EndTime": "2026-06-01 02:01:09",
                "ExpireTime": "2026-06-08 02:00:48",
                "FileType": "RDB-Redis 6.2",
                "FullBackup": 0,
                "InstanceId": "crs-ei43p3gr",
                "InstanceName": "testbackup",
                "InstanceType": 16,
                "Locked": 0,
                "Region": "ap-guangzhou",
                "Remark": "",
                "StartTime": "2026-06-01 02:00:48",
                "Status": 2
            }
        ],
        "TotalCount": 6,
        "RequestId": "66bb2e15-b864-46ea-894d-529885087fb8"
    }
}
```

