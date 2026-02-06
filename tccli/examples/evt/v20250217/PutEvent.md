**Example 1: 推送事件**



Input: 

```
tccli evt PutEvent --cli-unfold-argument  \
    --PluginId plugin-D******* \
    --Data ** \
    --Source 操作审计 \
    --TargetUin 10000
```

Output: 
```
{
    "Response": {
        "RequestId": "76db4f4c-9d32-4156-87a6-32a6b7d0a4d9"
    }
}
```

