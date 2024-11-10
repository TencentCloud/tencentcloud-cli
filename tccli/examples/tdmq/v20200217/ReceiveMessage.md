**Example 1: 接收消息**



Input: 

```
tccli tdmq ReceiveMessage --cli-unfold-argument  \
    --Topic tenant/namespace/topic \
    --SubscriptionName "test-sub"
```

Output: 
```
{
    "Response": {
        "MessageID": "931087:81:0",
        "MessagePayload": "msg send",
        "AckTopic": "tenant/namespace/topic",
        "ErrorMsg": "success",
        "SubName": "test-sub",
        "MessageIDList": "931087:81:0",
        "MessagesPayload": "msg send",
        "RequestId": "bee03397-31dd-4688-8fe0-81c691c3c1ae"
    }
}
```

