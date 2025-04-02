**Example 1: 同步消费组**



Input: 

```
tccli trocket SyncConsumerGroupInternal --cli-unfold-argument  \
    --InstanceId rocketmq-47x924vjavzz \
    --ConsumerGroup group-1 \
    --Namespace aega
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "46ef9a4b-a666-4b33-a8d1-3d378fa518aa"
    }
}
```

