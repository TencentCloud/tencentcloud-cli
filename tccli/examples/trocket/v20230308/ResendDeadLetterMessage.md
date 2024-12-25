**Example 1: 重发死信消息**



Input: 

```
tccli trocket ResendDeadLetterMessage --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --ConsumerGroup test_group \
    --MessageIds 01963F0B14BAF09F27077D244F00000000
```

Output: 
```
{
    "Response": {
        "RequestId": "f4f1d3ba-3ed2-4e03-b741-9f6f696b9689"
    }
}
```

