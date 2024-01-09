**Example 1: 修改消费组密码**

修改消费组密码

Input: 

```
tccli dts ModifyConsumerGroupPassword --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw \
    --AccountName account-subs-9jyki7hniw-1 \
    --ConsumerGroupName consumer-grp-subs-9jyki7hniw-1 \
    --OldPassword 123 \
    --NewPassword asdiouy09
```

Output: 
```
{
    "Response": {
        "RequestId": "bef6a6f0-f3b1-11ed-b987-7301347aa36f"
    }
}
```

