**Example 1: 自动快照策略跨账号复制**

自动快照策略跨账号复制

Input: 

```
tccli cbs CopyAutoSnapshotPolicyCrossAccount --cli-unfold-argument  \
    --AutoSnapshotPolicyIds asp-1h6gs2 \
    --TargetAccountUin 1044849112
```

Output: 
```
{
    "Response": {
        "AutoSnapshotPolicyIds": [
            "asp-1h6gs2"
        ],
        "TargetAccountUin": "1044849112",
        "RequestId": "sfqw134-fcdsf21-e534f42-12few"
    }
}
```

