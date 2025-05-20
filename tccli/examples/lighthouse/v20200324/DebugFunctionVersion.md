**Example 1: 调试函数版本**

调试函数function-001的版本2，body为test。

Input: 

```
tccli lighthouse DebugFunctionVersion --cli-unfold-argument  \
    --InstanceId lhins-gtn3ojxp \
    --FunctionName function-001 \
    --FunctionVersion 2 \
    --Body test
```

Output: 
```
{
    "Response": {
        "Body": "Body: test",
        "CostTime": 15624,
        "RequestId": "e9dda6d6-9d24-403d-a38a-d7fbdf5b0669",
        "StatusCode": 200
    }
}
```

