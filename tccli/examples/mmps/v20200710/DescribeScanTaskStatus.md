**Example 1: 获取小程序隐私诊断任务状态(失败)**



Input: 

```
tccli mmps DescribeScanTaskStatus --cli-unfold-argument  \
    --Platform 2 \
    --Source 0 \
    --TaskID 273051273836630016 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "b1c3418e-fe02-45be-9de0-498b4dfb7907",
        "Result": 0,
        "Status": 5,
        "FlowSteps": [],
        "ErrMsg": "FAIL GENERATE REPORT."
    }
}
```

