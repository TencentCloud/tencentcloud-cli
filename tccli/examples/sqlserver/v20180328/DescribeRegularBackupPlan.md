**Example 1: 查询实例mssql-j8kv137v定期备份保留计划**



Input: 

```
tccli sqlserver DescribeRegularBackupPlan --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v \
    --RegularBackupCounts 1 \
    --RegularBackupSaveDays 365 \
    --RegularBackupStrategy month \
    --RegularBackupStartTime 2022-10-10 \
    --BackupCycle 1 2 3
```

Output: 
```
{
    "Response": {
        "RequestId": "a62cac28-1656-4115-bf8d-189bef5e1102",
        "SaveModePeriod": [
            "2022-10-24 00:00:00"
        ],
        "SaveModeRegular": [
            "2022-10-26 00:00:00"
        ]
    }
}
```

