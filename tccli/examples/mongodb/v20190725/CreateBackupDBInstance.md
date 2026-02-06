**Example 1: 发起备份任务**



Input: 

```
tccli mongodb CreateBackupDBInstance --cli-unfold-argument  \
    --InstanceId cmgo-xxxxxx \
    --BackupMethod 0
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "1750660112000249",
        "RequestId": "fa4e07a8-4452-4490-94f4-bbac1f220256"
    }
}
```

