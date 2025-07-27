**Example 1: 查询数据备份**



Input: 

```
tccli tbase DescribeBaseBackups --cli-unfold-argument  \
    --OrderBy start_time \
    --BackupStrategy Manual \
    --PageSize 20 \
    --InstanceId tdpg-mdi2stas \
    --BackupType physical \
    --PageNumber 1 \
    --StartTime 2025-07-01 17:09:17 \
    --OrderByType DESC \
    --EndTime 2025-07-24 19:09:17
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "80504340-ad95-4124-a1d8-e7442ac598b2",
        "BaseBackups": [
            {
                "BackupId": 49827,
                "BackupPattern": "full",
                "BackupStrategy": "Auto",
                "BackupType": "physical",
                "EndTime": "2025-07-24 00:15:36",
                "FileDir": "/backupDev/tdpg-f5jk3et8/base_bkp_2025_07_24",
                "FileSize": "280.29 MB",
                "InstanceId": "tdpg-f5jk3et8",
                "InstanceName": "tdpg-f5jk3et8",
                "StartTime": "2025-07-24 00:00:35"
            }
        ]
    }
}
```

