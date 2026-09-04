**Example 1: 测试**



Input: 

```
tccli dlc BindApiKey --cli-unfold-argument  \
    --ApiKeyIds apikey-20260606184322-7o1x \
    --ServiceId svc-20260606162551-ols8
```

Output: 
```
{
    "Response": {
        "FailedList": [
            {
                "ApiKeyId": "apikey-20260606184322-7o1x",
                "Reason": "已被其他服务绑定"
            }
        ],
        "SuccessList": [],
        "RequestId": "643d163f-020f-4576-934c-c9d0cc8fcd76"
    }
}
```

