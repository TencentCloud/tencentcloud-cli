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
                "ErrorMessage": "",
                "Success": true,
                "TaskId": "task-xx"
            }
        ],
        "RequestId": "720b3231-5a85-4f05-aaab-c9b9596xxxxx"
    }
}
```

