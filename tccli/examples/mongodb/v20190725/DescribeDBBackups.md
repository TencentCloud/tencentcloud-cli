**Example 1: 查询云数据库实例的备份文件信息**



Input: 

```
tccli mongodb DescribeDBBackups --cli-unfold-argument  \
    --InstanceId cmgo-f555zzzz \
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

