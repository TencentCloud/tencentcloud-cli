**Example 1: 新增、删除、修改备份过期策略**

新增、删除、修改备份过期策略

Input: 

```
tccli tcaplusdb SetBackupExpireRule --cli-unfold-argument  \
    --ClusterId 21312 \
    --BackupExpireRules.0.ExpireDay 1 \
    --BackupExpireRules.0.OperType 1 \
    --BackupExpireRules.0.TableGroupId 213213 \
    --BackupExpireRules.0.TableName nametest \
    --BackupExpireRules.0.FileTag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "12312-1231",
        "TaskId": "23132"
    }
}
```

