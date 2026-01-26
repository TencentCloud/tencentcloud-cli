**Example 1: 示例**



Input: 

```
tccli mqtt DescribeMessageByTopic --cli-unfold-argument  \
    --InstanceId mqtt-mwe5jvvr \
    --Topic abc/1 \
    --StartTime 1769419861944
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ClientId": "client-1",
                "MessageId": "1539703B00486587524C8485D83769D5",
                "OriginTopic": "abc/1",
                "Qos": "1",
                "StoreTimestamp": 1769420164152
            }
        ],
        "RequestId": "242a41d4-65f2-4a6d-863e-8d8b7b00f0fb"
    }
}
```

