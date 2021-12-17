**Example 1: 删除拨测任务**



Input: 

```
tccli cat DeleteProbeTask --cli-unfold-argument  \
    --TaskIds xx
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
                "TaskId": "task-xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

