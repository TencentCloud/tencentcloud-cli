**Example 1: 查询密码规则**



Input: 

```
tccli tdmq DescribeRabbitMQTokenPwdRules --cli-unfold-argument  \
    --UserResourceId amqp-wdxk9k2q \
    --ResourceAccount test0318 \
    --InstanceType rabbitmq \
    --ResourceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequiredLength": 64,
        "Rules": [
            {
                "CharacterType": "specialcharacter",
                "Choices": "()`~!@#$%^&*_=|{}[]:;',.?/",
                "MinimumLength": 0,
                "MustStart": false
            }
        ],
        "RequestId": "067e81f1-a14d-4d1c-98c1-dafc62ac55ba"
    }
}
```

