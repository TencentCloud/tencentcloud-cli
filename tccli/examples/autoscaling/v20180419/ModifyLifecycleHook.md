**Example 1: 修改生命周期挂钩至实例启动后进入挂钩时间**



Input: 

```
tccli as ModifyLifecycleHook --cli-unfold-argument  \
    --LifecycleHookId ash-je1esoo9 \
    --LifecycleTransition INSTANCE_LAUNCHING
```

Output: 
```
{
    "Response": {
        "RequestId": "4942c041-fc7f-4f50-b489-d01cdeb6638f"
    }
}
```

