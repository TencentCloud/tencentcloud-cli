**Example 1: 创建消费组**

创建消费组成功

Input: 

```
tccli trocket CreateConsumerGroup --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --ConsumerGroup test_group \
    --MaxRetryTimes 16 \
    --ConsumeEnable True \
    --ConsumeMessageOrderly True \
    --Remark remark info
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ConsumerGroup": "test_group",
        "InstanceId": "rmq-72mo3a9o",
        "RequestId": "58f60891-002f-4b8a-b71f-3767a645c28e"
    }
}
```

