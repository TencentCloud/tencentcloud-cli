**Example 1: 查询函数异步事件状态**



Input: 

```
tccli scf GetAsyncEventStatus --cli-unfold-argument  \
    --InvokeRequestId b379787f-8487-4bac-bd8c-17a20a9ce40e
```

Output: 
```
{
    "Response": {
        "RequestId": "ee33a89b-3825-4d2f-bd88-35a8fa27aae1",
        "Result": {
            "Status": "RUNNING",
            "InvokeRequestId": "xx",
            "StatusCode": 0
        }
    }
}
```

