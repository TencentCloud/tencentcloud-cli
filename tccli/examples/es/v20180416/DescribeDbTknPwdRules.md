**Example 1: 查询 Dbtkn 数据库实例的密码规则**

查询 Dbtkn 数据库实例的密码规则

Input: 

```
tccli es DescribeDbTknPwdRules --cli-unfold-argument  \
    --UserResourceId es-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "dfee0a60-ab2f-11f0-a752-5254001f3b6b",
        "Rules": [
            {
                "CharacterType": "lowercase",
                "Choices": "abcdefghijklmnopqrstuvwxyz",
                "MinimumLength": 4,
                "MustStart": true
            },
            {
                "CharacterType": "uppercase",
                "Choices": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "MinimumLength": 2,
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
                "Choices": "!@#$%()",
                "MinimumLength": 1,
                "MustStart": false
            }
        ],
        "RequiredLength": 12
    }
}
```

