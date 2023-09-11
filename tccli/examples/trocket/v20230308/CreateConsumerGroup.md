**Example 1: 创建消费组**

创建消费组

Input: 

```
tccli trocket CreateConsumerGroup --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --ConsumerGroup group \
    --MaxRetryTimes 16 \
    --ConsumeEnable True \
    --ConsumeMessageOrderly True \
    --Remark test
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ConsumerGroup": "group",
        "InstanceId": "rmq-72mo3a9o",
        "RequestId": "58f60891-002f-4b8a-b71f-3767a645c28e"
    }
}
```

**Example 2: 创建消费者组**

创建消费者组

Input: 

```
tccli trocket CreateConsumerGroup --cli-unfold-argument  \
    --InstanceId rmq-g83xq2jn \
    --ConsumerGroup group \
    --ConsumeMessageOrderly False \
    --MaxRetryTimes 16 \
    --ConsumeEnable True
```

Output: 
```
{
    "Response": {
        "RequestId": "60a1347e-e418-42f1-9f9e-00226a3a3c18",
        "InstanceId": "rmq-g83xq2jn",
        "ConsumerGroup": "group"
    }
}
```

