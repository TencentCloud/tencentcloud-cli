**Example 1: 查看etcd快照策略**



Input: 

```
tccli cetcd DescribeEtcdSnapshotPolicies --cli-unfold-argument  \
    --InstanceId etcd-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "13b59a2d-dd68-48ab-845e-8cba577eca6d",
        "SnapshotPolicies": [
            {
                "Name": "test",
                "BackupSettings": {
                    "BackupInterval": 3600,
                    "MaxBackupCount": 24
                }
            }
        ]
    }
}
```

