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
        "TotalCount": 1,
        "Data": [
            {
                "MemUsage": 0.0,
                "RetCode": 0,
                "RetMsg": "xx",
                "RequestId": "xx",
                "StartTime": "xx",
                "Duration": 0.0,
                "RetryNum": 0,
                "FunctionName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

