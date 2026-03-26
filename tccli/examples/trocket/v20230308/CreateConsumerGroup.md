**Example 1: 成功创建消费组**



Input: 

```
tccli trocket CreateConsumerGroup --cli-unfold-argument  \
    --InstanceId rmq-16ogwxoxmm \
    --MaxRetryTimes 16 \
    --ConsumeEnable True \
    --ConsumeMessageOrderly False \
    --ConsumerGroup test_group \
    --RetryPolicy.PolicyType EXPONENTIAL \
    --RetryPolicy.RetryInterval 120
```

Output: 
```
{
    "Response": {
        "ConsumerGroup": "test_group",
        "InstanceId": "rmq-16ogwxoxmm",
        "RequestId": "03ff82e0-631d-47aa-9bbd-6aa1949f1efd"
    }
}
```

