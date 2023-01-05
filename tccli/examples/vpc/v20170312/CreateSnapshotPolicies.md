**Example 1: 创建快照策略**



Input: 

```
tccli vpc CreateSnapshotPolicies --cli-unfold-argument  \
    --SnapshotPolicies.0.KeepTime 180 \
    --SnapshotPolicies.0.CosRegion ap-guangzhou \
    --SnapshotPolicies.0.CosBucket test-12345678 \
    --SnapshotPolicies.0.CreateNewCos true \
    --SnapshotPolicies.0.SnapshotPolicyName test_name \
    --SnapshotPolicies.0.BackupType operate
```

Output: 
```
{
    "Response": {
        "SnapshotPolicies": [
            {
                "SnapshotPolicyId": "sspolicy-n08du1g3",
                "SnapshotPolicyName": "test_name",
                "KeepTime": 180,
                "CosRegion": "ap-guangzhou",
                "CosBucket": "test-12345678",
                "Enable": true,
                "BackupType": "operate",
                "CreateNewCos": true
            }
        ],
        "RequestId": "fdba6828-e317-4bd8-940f-6e12b09ecf1b"
    }
}
```

