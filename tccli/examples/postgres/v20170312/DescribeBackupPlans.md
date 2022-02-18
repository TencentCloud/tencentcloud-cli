**Example 1: 查询实例所有备份计划**

查询postgres-xxxxxxxx实例的所有备份计划

Input: 

```
tccli postgres DescribeBackupPlans --cli-unfold-argument  \
    --DBInstanceId postgres-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Plans": [
            {
                "BackupPeriod": "[\"monday\",\"thursday\",\"friday\"]",
                "BaseBackupRetentionPeriod": 3,
                "MaxBackupStartTime": "10:00:00",
                "MinBackupStartTime": "08:00:00"
            }
        ],
        "RequestId": ""
    }
}
```

