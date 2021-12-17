**Example 1: 恢复拨测任务**



Input: 

```
tccli cat ResumeProbeTask --cli-unfold-argument  \
    --TaskIds task-xx
```

Output: 
```
{
    "Response": {
        "SuccessCount": 0,
        "Total": 0,
        "Results": [
            {
                "ErrorMessage": "xx",
                "Success": true,
                "TaskId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

