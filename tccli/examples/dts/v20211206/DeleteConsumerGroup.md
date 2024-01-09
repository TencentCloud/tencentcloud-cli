**Example 1: 删除消费组**

删除消费组

Input: 

```
tccli dts DeleteConsumerGroup --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw \
    --ConsumerGroupName account-subs-9jyki7hniw-test \
    --AccountName consumer-grp-subs-9jyki7hniw-test
```

Output: 
```
{
    "Response": {
        "RequestId": "bef6a6f0-f3b1-11ed-b987-7301347aa36f"
    }
}
```

