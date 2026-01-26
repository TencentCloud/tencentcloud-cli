**Example 1: 示例**



Input: 

```
tccli mqtt DescribeMessageDetails --cli-unfold-argument  \
    --InstanceId mqtt-mwe5jvvr \
    --MessageId 1539703B00486587524C8485D83769D5 \
    --Subscription abc/1
```

Output: 
```
{
    "Response": {
        "Body": "{\n  \"msg\": \"hello\"\n}",
        "ClientId": "client-1",
        "ContentType": "",
        "CorrelationData": "",
        "MessageExpiryInterval": 0,
        "MessageId": "1539703B00486587524C8485D83769D5",
        "OriginTopic": "abc/1",
        "PayloadFormatIndicator": 0,
        "Qos": "1",
        "ResponseTopic": "",
        "StoreTimestamp": 1769420164152,
        "SubscriptionIdentifier": "",
        "UserProperties": [],
        "RequestId": "6e12518d-ea5e-47e5-b837-73fe1616bbf7"
    }
}
```

