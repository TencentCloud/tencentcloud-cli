**Example 1: 查询实例所有备份计划**

查询postgres-xxxxxxxx实例的所有备份计划

Input: 

```
tccli postgres DescribeBackupPlans --cli-unfold-argument  \
    --DBInstanceId postgres-1xm16x1d
```

Output: 
```
{
    "Response": {
        "Plans": [
            {
                "BackupPeriod": "[\"monday\",\"tuesday\",\"wednesday\",\"thursday\",\"friday\",\"saturday\",\"sunday\"]",
                "BackupPeriodType": "week",
                "BaseBackupRetentionPeriod": 7,
                "LogBackupRetentionPeriod": 7,
                "MaxBackupStartTime": "05:16:05",
                "MinBackupStartTime": "01:16:05",
                "PlanId": "422a5f4d-52af-5cb1-9474-324d63ccc62c",
                "PlanName": "default",
                "PlanType": "default"
            },
            {
                "BackupPeriod": "[\"1\",\"2\"]",
                "BackupPeriodType": "month",
                "BaseBackupRetentionPeriod": 40,
                "LogBackupRetentionPeriod": 7,
                "MaxBackupStartTime": "02:00:00",
                "MinBackupStartTime": "01:00:00",
                "PlanId": "dfea3bb4-8ca7-5e79-aefb-9d231f2b66b6",
                "PlanName": "plan_test",
                "PlanType": "custom"
            }
        ],
        "RequestId": "0b6c3429-6dfc-4ecd-ab80-b25631f0821e"
    }
}
```

