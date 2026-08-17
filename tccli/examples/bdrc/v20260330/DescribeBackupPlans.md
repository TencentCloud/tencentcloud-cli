**Example 1: 查询整机备份计划**



Input: 

```
tccli bdrc DescribeBackupPlans --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BackupPlanSet": [
            {
                "AutoBackupPolicyId": "abp-i55a3egv",
                "BackupCount": 0,
                "CreateTime": "2026-06-10T15:55:37+08:00",
                "InstanceId": "ins-az7px5xk",
                "LastTriggerError": "",
                "LastTriggerTime": null,
                "ModifyTime": "2026-06-10T15:55:37+08:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "982dc596-965b-4b36-9fea-34f2197e9717"
    }
}
```

