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
                "FunctionName": "abc",
                "RetMsg": "abc",
                "RequestId": "abc",
                "StartTime": "abc",
                "RetCode": 0,
                "Duration": 0,
                "MemUsage": 0,
                "RetryNum": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

