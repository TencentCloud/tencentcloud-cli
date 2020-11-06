**Example 1: Modifying the database backup configuration**



Input: 

```
tccli cdb ModifyBackupConfig --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --ExpireDays 10 \
    --BinlogExpireDays 8 \
    --StartTime 02:00-06:00 \
    --BackupMethod logical
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

