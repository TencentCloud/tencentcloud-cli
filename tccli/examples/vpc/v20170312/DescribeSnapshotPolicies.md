**Example 1: 查询快照策略**



Input: 

```
tccli vpc DescribeSnapshotPolicies --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name snapshot-policy-id \
    --Filters.0.Values sspolicy-g6jwvm35
```

Output: 
```
{
    "Response": {
        "SnapshotPolicySet": [
            {
                "SnapshotPolicyId": "sspolicy-g6jwvm35",
                "SnapshotPolicyName": "test2",
                "KeepTime": 180,
                "CosRegion": "ap-guangzhou",
                "CosBucket": "test1-251197522",
                "CreateTime": "2021-10-08 16:09:46",
                "Enable": true,
                "BackupType": "operate",
                "CreateNewCos": false
            }
        ],
        "TotalCount": 1,
        "RequestId": "a38579de-a046-4d68-b24a-b629c8d0ae57"
    }
}
```

