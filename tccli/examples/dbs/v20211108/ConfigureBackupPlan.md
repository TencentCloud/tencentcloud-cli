**Example 1: 配置备份计划**



Input: 

```
tccli dbs ConfigureBackupPlan --cli-unfold-argument  \
    --BackupPlanId dbs-3enedogk \
    --BackupPlanName dbs-test \
    --UpperParallel 6
```

Output: 
```
{
    "Response": {
        "RequestId": "0f6dc02f-2eba-4f52-b016-c06f631a914e"
    }
}
```

