**Example 1: 删除任务**



Input: 

```
tccli cat DeleteProbeTask --cli-unfold-argument  \
    --TaskIds task-xxx
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
                "TaskId": "task-xxx"
            }
        ],
        "RequestId": "720b3231-5a85-4f05-aaab-c9b9596xxxxx"
    }
}
```

