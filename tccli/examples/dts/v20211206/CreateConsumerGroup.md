**Example 1: 创建消费组**

创建消费组

Input: 

```
tccli dts CreateConsumerGroup --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw \
    --ConsumerGroupName group-1 \
    --AccountName jason \
    --Password qJ3e1Wd~ \
    --Description this is a test account
```

Output: 
```
{
    "Response": {
        "RequestId": "20461920-b18e-11ec-ae1a-cfe224f4f21f"
    }
}
```

