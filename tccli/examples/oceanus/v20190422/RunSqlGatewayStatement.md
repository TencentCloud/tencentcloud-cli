**Example 1: 执行Statement**

执行Statement

Input: 

```
tccli oceanus RunSqlGatewayStatement --cli-unfold-argument  \
    --ClusterId abc \
    --SessionId abc \
    --Sql abc
```

Output: 
```
{
    "Response": {
        "ErrorMessage": [
            "abc"
        ],
        "SessionId": "abc",
        "OperationHandleId": "abc",
        "RequestId": "abc"
    }
}
```

