**Example 1: DescribeDataBackupOverview**



Input: 

```
tccli cdb DescribeDataBackupOverview --cli-unfold-argument  \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "AutoBackupCount": 3,
        "AutoBackupVolume": 3000,
        "DataBackupCount": 5,
        "DataBackupVolume": 5000,
        "ManualBackupCount": 2,
        "ManualBackupVolume": 2000,
        "RemoteBackupVolume": 1000,
        "RemoteBackupCount": 1,
        "DataBackupArchiveVolume": 1000,
        "DataBackupArchiveCount": 1,
        "DataBackupStandbyVolume": 1000,
        "DataBackupStandbyCount": 1,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

