**Example 1: 创建文件存储生命周期策略**

创建文件存储生命周期策略

Input: 

```
tccli cfs CreateLifecyclePolicy --cli-unfold-argument  \
    --LifecyclePolicyName default \
    --LifecycleRules.0.StorageType InfrequentAccess \
    --LifecycleRules.0.Interval DEFAULT_ATIME_14 \
    --LifecycleRules.0.FileType ALL \
    --LifecycleRules.0.Action Release \
    --LifecycleRules.0.FileMaxSize 10240 \
    --LifecycleRules.0.FileMinSize 64
```

Output: 
```
{
    "Response": {
        "LifecyclePolicyID": "policy-13epvfrn",
        "RequestId": "req-acb"
    }
}
```

