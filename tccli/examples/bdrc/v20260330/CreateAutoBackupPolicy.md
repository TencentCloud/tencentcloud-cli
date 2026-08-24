**Example 1: 创建备份库备份策略**



Input: 

```
tccli bdrc CreateAutoBackupPolicy --cli-unfold-argument  \
    --Policy.0.DayOfWeek 5 \
    --Policy.0.Hour 2 3 \
    --Policy.0.IntervalDays 3 \
    --IsPermanent False \
    --AutoBackupPolicyName test-policy \
    --IsActivated True \
    --RetentionDays 3 \
    --StorageType VAULT \
    --VaultId vault-qjhn63ku
```

Output: 
```
{
    "Response": {
        "AutoBackupPolicyId": "abp-p5ylj73z",
        "RequestId": "7b50a8c7-1685-4136-96fe-f18fcde35414"
    }
}
```

