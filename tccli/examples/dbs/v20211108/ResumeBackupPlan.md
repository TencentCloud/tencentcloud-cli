**Example 1: 恢复备份计划**



Input: 

```
tccli dbs ResumeBackupPlan --cli-unfold-argument  \
    --BackupPlanId dbs-xxxxxxxx \
    --BackupNow 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ce31a435-eb3d-4508-b6e9-1b96cf86c8c7"
    }
}
```

