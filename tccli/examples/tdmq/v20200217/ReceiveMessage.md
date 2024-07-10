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
        "MessageID": "abc",
        "MessagePayload": "abc",
        "AckTopic": "abc",
        "ErrorMsg": "abc",
        "SubName": "abc",
        "MessageIDList": "abc",
        "MessagesPayload": "abc",
        "RequestId": "abc"
    }
}
```

