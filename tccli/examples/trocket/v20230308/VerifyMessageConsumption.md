**Example 1: 消息验证成功**



Input: 

```
tccli trocket VerifyMessageConsumption --cli-unfold-argument  \
    --InstanceId abc \
    --Topic abc \
    --ConsumerGroup abc \
    --ClientId abc \
    --MsgId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

