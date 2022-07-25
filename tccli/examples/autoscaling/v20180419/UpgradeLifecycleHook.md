**Example 1: 升级生命周期挂钩**



Input: 

```
tccli as UpgradeLifecycleHook --cli-unfold-argument  \
    --DefaultResult CONTINUE \
    --LifecycleHookName hook-updated \
    --LifecycleHookId ash-8azjzxj9 \
    --LifecycleTransition INSTANCE_LAUNCHING \
    --HeartbeatTimeout 240
```

Output: 
```
{
    "Response": {
        "RequestId": "db656d36-ed6b-4795-bdc4-94e7a7e04acb"
    }
}
```

