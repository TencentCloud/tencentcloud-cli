**Example 1: 查询备份空间信息**



Input: 

```
tccli tbase DescribeBackupSpace --cli-unfold-argument  \
    --OrderBy total_capacity \
    --OrderByType DESC \
    --InstanceIds tdpg-test123
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "68458160-670f-11ee-922e-a382ae347b69",
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

