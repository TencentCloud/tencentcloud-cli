**Example 1: 跳过同步校验检查项**



Input: 

```
tccli dts SkipSyncCheckItem --cli-unfold-argument  \
    --JobId sync-4ddgid2 \
    --StepIds OptimizeCheck
```

Output: 
```
{
    "Response": {
        "RequestId": "46b45da1-3e8e-4ef2-8de8-b1bffa027385"
    }
}
```

