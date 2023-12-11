**Example 1: 调整任务目标RPS**



Input: 

```
tccli pts AdjustJobSpeed --cli-unfold-argument  \
    --JobId job-61ovraba \
    --TargetRequestsPerSecond 10
```

Output: 
```
{
    "Response": {
        "RequestId": "70805f6a-d7e1-4247-9d5a-fde3afe2b377"
    }
}
```

