**Example 1: 查询备份计划预校验结果**



Input: 

```
tccli dbs DescribeBackupCheckJob --cli-unfold-argument  \
    --BackupPlanId dbs-qcloudtest
```

Output: 
```
{
    "Response": {
        "Status": "finished",
        "Progress": 100,
        "CheckFlag": 1,
        "ErrMessage": "success",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

