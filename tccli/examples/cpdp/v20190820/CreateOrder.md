**Example 1: 消费请求正常示例**

消费请求正常示例

Input: 

```
tccli cpdp CreateOrder --cli-unfold-argument  \
    --ChannelCode ZSB2B \
    --MerchantAppId 1c6f41570498301d85fc4589a5435b54 \
    --Amount 200.56 \
    --TraceNo 46eed0ce0edc3b11bc1056b97dbc734c \
    --NotifyUrl http://aaa.aaa.aaa \
    --ReturnUrl http://bbb.bbb.bbb
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0",
        "MerchantAppId": "1c6f41570498301d85fc4589a5435b54",
        "TraceNo": "46eed0ce0edc3b11bc1056b97dbc734c",
        "OrderNo": "847f33d665d83eecaf0a8805a2ee6c7a",
        "PayUrl": "http://ccc.ccc.ccc"
    }
}
```

