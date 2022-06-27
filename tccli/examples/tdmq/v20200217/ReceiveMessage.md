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
        "RequestId": "36713f94-d07d-4b96-babf-42d139276f23",
        "MessageID": "71:12:0:0",
        "MessageIDList": "",
        "MessagesPayload": "",
        "MessagePayload": "hello TDMQ",
        "SubName": "xx",
        "AckTopic": "persistent://tenant/namespace/topic",
        "ErrorMsg": "xx"
    }
}
```

