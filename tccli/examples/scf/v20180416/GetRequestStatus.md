**Example 1: 获取函数运行状态**



Input: 

```
tccli scf GetRequestStatus --cli-unfold-argument  \
    --FunctionName <FunctionName> \
    --FunctionRequestId <FunctionRequestId>
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [
            {
                "FunctionName": "function-demo",
                "RetMsg": "Hello",
                "RequestId": "96d91886-f49b-4962-825e-1b4b8a2585f7",
                "StartTime": "2024-12-25 19:50:07",
                "RetCode": 0,
                "Duration": 0,
                "MemUsage": 0,
                "RetryNum": 0
            }
        ],
        "RequestId": "a63607c3-581f-4be9-8c4b-631c75909f07"
    }
}
```

