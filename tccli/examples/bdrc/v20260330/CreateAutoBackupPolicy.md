**Example 1: 创建备份策略**



Input: 

```
tccli bdrc CreateAutoBackupPolicy --cli-unfold-argument  \
    --Policy.0.DayOfWeek 1 \
    --Policy.0.Hour 3 \
    --IsPermanent False \
    --AutoBackupPolicyName test策略 \
    --IsActivated True \
    --RetentionDays 7 \
    --RetentionMonths 0 \
    --RetentionAmount 0 \
    --StorageType COMMON \
    --VaultId 
```

Output: 
```
{
    "Response": {
        "AutoBackupPolicyId": "abp-5zukg4nz",
        "RequestId": "4d34cfa0-104e-4db7-8da8-6d1dd794fa75"
    }
}
```

