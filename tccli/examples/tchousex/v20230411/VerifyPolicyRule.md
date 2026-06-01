**Example 1: 校验行过滤策略**



Input: 

```
tccli tchousex VerifyPolicyRule --cli-unfold-argument  \
    --InstanceId instance-gpzb9mp1 \
    --PolicyType 2 \
    --Table orders
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "ReturnData": "{\"Total\":0,\"SuccessList\":[{\"Condition\":\"order_id \\u003e 101\",\"users\":[\"100006811818\"],\"roles\":[\"\"],\"ErrMessage\":\"\"}],\"FailedList\":[]}",
        "RequestId": "111691b6-e9e1-41c1-af2a-b10c2aa9265b"
    }
}
```

