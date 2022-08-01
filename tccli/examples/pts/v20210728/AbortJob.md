**Example 1: 停止任务**



Input: 

```
tccli pts AbortJob --cli-unfold-argument  \
    --ProjectId xx \
    --ScenarioId xx \
    --JobId xx \
    --AbortReason 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

