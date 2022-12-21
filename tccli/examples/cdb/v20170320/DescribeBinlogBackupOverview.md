**Example 1: DescribeBinlogBackupOverview**



Input: 

```
tccli cdb DescribeBinlogBackupOverview --cli-unfold-argument  \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "BinlogBackupCount": 15,
        "BinlogBackupVolume": 6000,
        "RemoteBinlogCount": 5,
        "RemoteBinlogVolume": 2000,
        "BinlogArchiveCount": 5,
        "BinlogArchiveVolume": 2000,
        "BinlogStandbyCount": 5,
        "BinlogStandbyVolume": 2000,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

