**Example 1: Querying the backup file information of a TencentDB instance**



Input: 

```
tccli mongodb DescribeDBBackups --cli-unfold-argument  \
    --InstanceId cmgo-f555zzzz\
    --BackupMethod 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "BackupList": [],
        "TotalCount": 0
    }
}
```

