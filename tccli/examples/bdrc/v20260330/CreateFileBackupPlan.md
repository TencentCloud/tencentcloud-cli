**Example 1: 创建备份计划**



Input: 

```
tccli bdrc CreateFileBackupPlan --cli-unfold-argument  \
    --PolicyId abp-5c5l02gj \
    --PlanName test-new-plan \
    --BackupStorageId vault-qjhn63ku \
    --Resources.0.ResourceId ins-7630gzfm \
    --Resources.0.BackupPaths /var/log \
    --Resources.0.IncludeFileTypes *.log \
    --Resources.0.ExcludeSystemDirectories True \
    --Resources.0.ExecuteImmediately False
```

Output: 
```
{
    "Response": {
        "PlanIds": [
            "fbp-d66961s5"
        ],
        "RequestId": "e7b880e6-f80d-43b5-a080-26d595b1f83d"
    }
}
```

