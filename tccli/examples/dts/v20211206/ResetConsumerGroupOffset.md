**Example 1: 重置消费组offset**

将一个订阅任务的kafka offset重置到2023-05-16 00:00:00附近的checkpoint

Input: 

```
tccli dts ResetConsumerGroupOffset --cli-unfold-argument  \
    --ConsumerGroupName consumer-grp-subs-635ns8r71g-1 \
    --PartitionNos 0 1 2 3 \
    --ResetMode datetime \
    --ResetDatetime 2023-05-16 00:00:00 \
    --SubscribeId subs-635ns8r71g \
    --TopicName account-subs-635ns8r71g-1
```

Output: 
```
{
    "Response": {
        "RequestId": "20461920-b18e-11ec-ae1a-cfe224f4f21f"
    }
}
```

