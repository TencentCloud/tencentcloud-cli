**Example 1: 调整任务目标RPS**



Input: 

```
tccli pts AdjustJobSpeed --cli-unfold-argument  \
    --JobId xx \
    --TargetRequestsPerSecond 10
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

