**Example 1: 暂停任务**



Input: 

```
tccli cat SuspendProbeTask --cli-unfold-argument  \
    --TaskIds task-xxx
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "Total": 1,
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

