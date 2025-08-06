**Example 1: 更新生命周期管理策略**

更新生命周期管理策略

Input: 

```
tccli cfs ModifyLifecyclePolicy --cli-unfold-argument  \
    --LifecyclePolicyName mypolicy-abc \
    --LifecycleRules.0.StorageType InfrequentAccess \
    --LifecycleRules.0.Interval DEFAULT_ATIME_14 \
    --LifecycleRules.0.FileType All \
    --LifecycleRules.0.Action Archive \
    --LifecycleRules.0.FileMaxSize 1G \
    --LifecycleRules.0.FileMinSize 1M \
    --LifecyclePolicyID policy-4cqyxcma
```

Output: 
```
{
    "Response": {
        "LifecyclePolicyID": "policy-4cqyxcma",
        "RequestId": ""
    }
}
```

