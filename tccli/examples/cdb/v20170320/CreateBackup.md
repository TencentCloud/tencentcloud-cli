**Example 1: Creating database backup**



Input: 

```
tccli cdb CreateBackup --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv\
    --BackupMethod logical\
    --BackupDBTableList '[{"Db": "db1", "Table": "tb1"}, {"Db": "db1", "Table": "tb2"}, {"Db": "db2"} ]'
```

Output: 
```
{
    "Response": {
        "BackupId": 102996666,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

