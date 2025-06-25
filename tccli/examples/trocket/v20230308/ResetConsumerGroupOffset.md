**Example 1: 重置消费位点**



Input: 

```
tccli trocket ResetConsumerGroupOffset --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --ConsumerGroup test_group \
    --Topic test_topic \
    --ResetTimestamp -1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "707a78e5-019d-41f6-80fc-15743d99c81a"
    }
}
```

