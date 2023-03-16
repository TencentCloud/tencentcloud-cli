**Example 1: 查询函数异步事件状态**

查询函数异步事件状态

Input: 

```
tccli scf GetAsyncEventStatus --cli-unfold-argument  \
    --InvokeRequestId b379787f-8487-4bac-bd8c-17a20a9ce40e
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": "abc",
            "StatusCode": 0,
            "InvokeRequestId": "abc"
        },
        "RequestId": "abc"
    }
}
```

