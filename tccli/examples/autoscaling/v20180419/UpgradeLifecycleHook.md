**Example 1: Upgrading a lifecycle hook**



Input: 

```
tccli as UpgradeLifecycleHook --cli-unfold-argument  \
    --LifecycleHookId ash-8azjzxj9 \
    --DefaultResult CONTINUE \
    --HeartbeatTimeout 240 \
    --LifecycleHookName hook-updated \
    --LifecycleTransition INSTANCE_LAUNCHING
```

Output: 
```
{
    "Response": {
        "RequestId": "db656d36-ed6b-4795-bdc4-94e7a7e04acb"
    }
}
```

