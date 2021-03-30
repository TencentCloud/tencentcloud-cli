**Example 1: 创建备份下载任务**



Input: 

```
tccli mongodb CreateBackupDownloadTask --cli-unfold-argument  \
    --InstanceId cmgo-dygv1rnp \
    --BackupName 'cmgo-dygv1rnp_2021-03-26 10:44' \
    --BackupSets.0.ReplicaSetId cmgo-dygv1rnp_0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ed8d110-67be-4650-83b0-5df5a897e9e6",
        "Tasks": [
            {
                "ReplicaSetId": "cmgo-dygv1rnp_0",
                "Status": 2
            }
        ]
    }
}
```

