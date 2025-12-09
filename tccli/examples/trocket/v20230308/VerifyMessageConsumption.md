**Example 1: 消息验证成功**



Input: 

```
tccli trocket VerifyMessageConsumption --cli-unfold-argument  \
    --InstanceId rmq-72mo3a9o \
    --Topic test_topic \
    --ConsumerGroup test_group \
    --ClientId 10.185.22.31@7#782332544 \
    --MsgId 1464F14500017DAF6ECC79CA6CAA0288
```

Output: 
```
{
    "Response": {
        "RequestId": "960dfb7a-44af-49f4-8172-22896c57a8be"
    }
}
```

