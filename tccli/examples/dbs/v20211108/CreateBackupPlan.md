**Example 1: 购买备份计划**



Input: 

```
tccli dbs CreateBackupPlan --cli-unfold-argument  \
    --DatabaseType mysql \
    --BackupMethod logical \
    --InstanceClass large \
    --Period 3 \
    --PayType prepay \
    --Count 1 \
    --AutoRenew 1
```

Output: 
```
{
    "Response": {
        "BackupPlanIds": [
            "dbs-3enedogk"
        ],
        "OrderId": "20251216711021858208781",
        "RequestId": "ce31a435-eb3d-4508-b6e9-1b96cf86c8c7"
    }
}
```

