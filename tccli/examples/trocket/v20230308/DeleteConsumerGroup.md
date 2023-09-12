**Example 1: 删除消费组**

删除消费组

Input: 

```
tccli trocket DeleteConsumerGroup --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --ConsumerGroup group
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "8221cd04-dafc-438d-bc1f-816fd87df24e"
    }
}
```

