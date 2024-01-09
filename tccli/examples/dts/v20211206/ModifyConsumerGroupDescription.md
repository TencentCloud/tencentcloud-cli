**Example 1: 修改消费组备注**

修改消费组备注

Input: 

```
tccli dts ModifyConsumerGroupDescription --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw \
    --AccountName account-subs-9jyki7hniw-1 \
    --ConsumerGroupName consumer-grp-subs-9jyki7hniw-1 \
    --Description this is a test group
```

Output: 
```
{
    "Response": {
        "RequestId": "bef6a6f0-f3b1-11ed-b987-7301347aa36f"
    }
}
```

