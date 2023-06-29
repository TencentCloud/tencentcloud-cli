**Example 1: 查询备份空间信息**



Input: 

```
tccli tbase DescribeBackupSpace --cli-unfold-argument  \
    --OrderBy xx \
    --OrderByType xx \
    --InstanceIds xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "BackupSpaces": [
            {
                "WALBackupCount": 1,
                "InstanceId": "tdpg-test123",
                "EngineType": "TbaseV2",
                "AutoBackupCount": 1,
                "ManualBackupCount": 1,
                "InstanceName": "tdpg-test123",
                "WALBackupSize": "1",
                "AutoBackupSize": "1",
                "ManualBackupSize": "1",
                "BackupTotalSize": "4",
                "BaseBackupSize": "1",
                "Status": "online",
                "BaseBackupCount": 4
            }
        ]
    }
}
```

