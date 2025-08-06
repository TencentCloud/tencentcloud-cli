**Example 1: CreateLifecycleDataTask**



Input: 

```
tccli cfs CreateLifecycleDataTask --cli-unfold-argument  \
    --FileSystemId cfs-4agcdretg \
    --Type archive \
    --TaskPath /cfs/data \
    --TaskName dataarchive
```

Output: 
```
{
    "Response": {
        "TaskId": "task-abcdefg",
        "RequestId": "req-gagagagagag"
    }
}
```

