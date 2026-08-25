**Example 1: 创建备份计划**



Input: 

```
tccli bdrc CreateFileBackupPlan --cli-unfold-argument  \
    --PolicyId abp-peu8v28r \
    --BackupStorageId vault-hrvkughn \
    --Resources.0.ResourceId cfs-o5vnh8qh \
    --Resources.0.BackupPaths /mnt \
    --Resources.0.ExcludeSystemDirectories True \
    --Resources.0.ExecuteImmediately False \
    --ResourceType CFS_AGENT
```

Output: 
```
{
    "Response": {
        "PlanIds": [
            "bplan-pij7q4vk"
        ],
        "RequestId": "5533b400-2d05-4649-952b-3e523de60561"
    }
}
```

