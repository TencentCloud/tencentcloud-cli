**Example 1: 查看实例账号的密码规则**



Input: 

```
tccli postgres DescribeDbTknPwdRules --cli-unfold-argument  \
    --UserResourceId postgres-bd0t2ayr \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount cam_test_2 \
    --InstanceType postgres
```

Output: 
```
{
    "Response": {
        "RequestId": "ee2e9808-2a44-47b5-8cde-659c5502bee8",
        "RequiredLength": 32,
        "Rules": [
            {
                "CharacterType": "uppercase",
                "Choices": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "MinimumLength": 1,
                "MustStart": true
            },
            {
                "CharacterType": "lowercase",
                "Choices": "abcdefghijklmnopqrstuvwxyz",
                "MinimumLength": 1,
                "MustStart": false
            },
            {
                "CharacterType": "numbers",
                "Choices": "1234567890",
                "MinimumLength": 1,
                "MustStart": false
            },
            {
                "CharacterType": "specialcharacter",
                "Choices": "()`~!@#$%^&*-+=_|{}[]:<>,.?",
                "MinimumLength": 1,
                "MustStart": false
            }
        ]
    }
}
```

