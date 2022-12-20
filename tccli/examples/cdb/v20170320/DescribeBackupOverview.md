**Example 1: 查询备份概览**



Input: 

```
tccli cdb DescribeBackupOverview --cli-unfold-argument  \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "BackupCount": 15,
        "BackupVolume": 90000,
        "BillingVolume": 20000,
        "FreeVolume": 70000,
        "RemoteBackupVolume": 1000,
        "BackupArchiveVolume": 1000,
        "BackupStandbyVolume": 1000,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

