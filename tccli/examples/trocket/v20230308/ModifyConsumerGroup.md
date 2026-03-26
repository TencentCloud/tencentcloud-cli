**Example 1: 成功修改消费组**



Input: 

```
tccli trocket ModifyConsumerGroup --cli-unfold-argument  \
    --InstanceId rmq-16ogwxoxmm \
    --ConsumeEnable True \
    --ConsumeMessageOrderly False \
    --ConsumerGroup test_group \
    --MaxRetryTimes 3 \
    --Remark test modify \
    --RetryPolicy.PolicyType EXPONENTIAL \
    --RetryPolicy.RetryInterval 180
```

Output: 
```
{
    "Response": {
        "RequestId": "6e2e65dd-bd8a-4685-8b17-5770686276f3"
    }
}
```

