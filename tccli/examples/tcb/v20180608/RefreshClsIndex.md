**Example 1: 刷新索引**



Input: 

```
tccli tcb RefreshClsIndex --cli-unfold-argument  \
    --EnvId lowcode-4gs26nnz095f6f4d \
    --RebuildIndex True \
    --RebuildTime -1 \
    --IndexFields.0.Key log \
    --IndexFields.0.Type text
```

Output: 
```
{
    "Response": {
        "RequestId": "99649fbd-1b4f-4581-b0f3-881707f6c521"
    }
}
```

