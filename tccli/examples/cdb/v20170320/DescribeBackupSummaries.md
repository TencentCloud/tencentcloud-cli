**Example 1: 查询备份实时统计**

查询备份实时统计

Input: 

```
tccli cdb DescribeBackupSummaries --cli-unfold-argument  \
    --Product mysql \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AutoBackupCount": 5,
                "AutoBackupVolume": 10000,
                "BackupVolume": 50000,
                "BinlogBackupCount": 2,
                "BinlogBackupVolume": 20000,
                "DataBackupCount": 15,
                "DataBackupVolume": 30000,
                "InstanceId": "cdb-01wa5l0v",
                "ManualBackupCount": 10,
                "ManualBackupVolume": 20000
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 50
    }
}
```

