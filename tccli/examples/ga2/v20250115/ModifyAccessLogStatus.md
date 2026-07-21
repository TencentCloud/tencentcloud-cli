**Example 1: 启停日志任务示例**



Input: 

```
tccli ga2 ModifyAccessLogStatus --cli-unfold-argument  \
    --LogPushTaskId galog-8ezkdjm9 \
    --Status START \
    --GlobalAcceleratorId ga-8sreohed
```

Output: 
```
{
    "Response": {
        "RequestId": "a2a67495-96a3-436a-b9bc-3e879facc94f"
    }
}
```

