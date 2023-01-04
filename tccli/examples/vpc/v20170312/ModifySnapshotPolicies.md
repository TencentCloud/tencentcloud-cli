**Example 1: 修改快照策略**



Input: 

```
tccli vpc ModifySnapshotPolicies --cli-unfold-argument  \
    --SnapshotPoliciesInfo.0.SnapshotPolicyId sspolicy-aart89ip \
    --SnapshotPoliciesInfo.0.SnapshotPolicyName new_name
```

Output: 
```
{
    "Response": {
        "RequestId": "fdba6828-e317-4bd8-940f-6e12b09ecf1b"
    }
}
```

