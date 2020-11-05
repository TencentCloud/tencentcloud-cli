**Example 1: Querying backup overview**



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
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

