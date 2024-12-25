**Example 1: 修改消费组密码**

修改消费组密码

Input: 

```
tccli dts ModifyConsumerGroupPassword --cli-unfold-argument  \
    --SubscribeId subs-9jyki7hniw \
    --AccountName account-subs-9jyki7hniw-group-1 \
    --ConsumerGroupName consumer-grp-subs-9jyki7hniw-jason \
    --OldPassword qJ3e1Wd~ \
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

