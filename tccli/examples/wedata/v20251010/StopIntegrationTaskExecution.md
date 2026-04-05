**Example 1: 停止数据接入调试任务**



Input: 

```
tccli wedata StopIntegrationTaskExecution --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --TaskId f5aaa5c0-5ace-4904-8ee3-79f9b6869bc1 \
    --JobId 6820260107162129021
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorMessage": "",
            "JobId": "6820260107162129021",
            "OpStatus": true,
            "TaskId": "f5aaa5c0-5ace-4904-8ee3-79f9b6869bc1"
        },
        "RequestId": "67ca1dd3-cdf3-418a-819c-7515f5e30836"
    }
}
```

