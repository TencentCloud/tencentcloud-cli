**Example 1: 终止任务实例**



Input: 

```
tccli batch TerminateTaskInstance --cli-unfold-argument  \
    --JobId job-rybewp57 \
    --TaskName A \
    --TaskInstanceIndex 0
```

Output: 
```
{
    "Response": {
        "RequestId": "72e9a712-1fed-4b57-be72-62e71eefd4c3"
    }
}
```

