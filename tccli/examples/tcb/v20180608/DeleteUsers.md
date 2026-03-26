**Example 1: 删除用户**



Input: 

```
tccli tcb DeleteUsers --cli-unfold-argument  \
    --EnvId testenv-123 \
    --Uids 19837204372934434
```

Output: 
```
{
    "Response": {
        "Data": {
            "FailedCount": 0,
            "SuccessCount": 1
        },
        "RequestId": "563b4e8e-7898-401d-95b1-c86bbaecc6b3"
    }
}
```

