**Example 1: 修改云硬盘的自动备份策略**



Input: 

```
tccli lighthouse ModifyDisksAutomaticBackupPolicy --cli-unfold-argument  \
    --DiskIds lhdisk-0p3m7jkr \
    --AutomaticBackupPolicy.Hours 20
```

Output: 
```
{
    "Response": {
        "RequestId": "0d5e192e-10a2-44a6-a6ce-2ac6b01f7646"
    }
}
```

