**Example 1: 创建etcd快照策略**



Input: 

```
tccli cetcd CreateEtcdSnapshotPolicy --cli-unfold-argument  \
    --InstanceId etcd-abcd1234 \
    --SnapshotPolicyName test \
    --BackupSettings.BackupInterval 3600 \
    --BackupSettings.MaxBackupCount 24
```

Output: 
```
{
    "Response": {
        "RequestId": "13b59a2d-dd68-48ab-845e-8cba577eca6d"
    }
}
```

