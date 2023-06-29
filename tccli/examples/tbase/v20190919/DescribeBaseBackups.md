**Example 1: 查询数据备份**



Input: 

```
tccli tbase DescribeBaseBackups --cli-unfold-argument  \
    --OrderBy xx \
    --BackupStrategy xx \
    --PageSize 0 \
    --InstanceId xx \
    --BackupType xx \
    --PageNumber 0 \
    --StartTime xx \
    --OrderByType xx \
    --EndTime xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "BaseBackups": [
            {
                "BackupStrategy": "xx",
                "InstanceId": "xx",
                "BackupPattern": "xx",
                "FileDir": "xx",
                "BackupType": "xx",
                "FileSize": "xx",
                "StartTime": "xx",
                "BackupId": 0,
                "EndTime": "xx",
                "InstanceName": "xx"
            }
        ]
    }
}
```

