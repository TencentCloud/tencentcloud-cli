**Example 1: 发布RRPC消息**



Input: 

```
tccli iotcloud PublishRRPCMessage --cli-unfold-argument  \
    --ProductId ASBHKN121 \
    --DeviceName dev \
    --Payload 1234561
```

Output: 
```
{
    "Response": {
        "MessageId": 74,
        "PayloadBase64": "QUJDRA==",
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

