**Example 1: 修改消费组属性**

修改消费组属性

Input: 

```
tccli trocket ModifyConsumerGroup --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --ConsumerGroup group \
    --ConsumeEnable True \
    --ConsumeMessageOrderly True \
    --MaxRetryTimes 16 \
    --Remark test
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "239a3769-8dc6-41e9-bc01-67be452db5a3"
    }
}
```

