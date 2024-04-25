**Example 1: 查询 Dbtkn 数据库实例的密码规则**

查询 Dbtkn 数据库实例的密码规则

Input: 

```
tccli cynosdb DescribeDbTknPwdRules --cli-unfold-argument  \
    --UserResourceId cynosdbysql-on5xw0ni \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount test \
    --InstanceType cynosdb
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "CharacterType": "uppercase",
                "Choices": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "MinimumLength": 4,
                "MustStart": true
            },
            {
                "CharacterType": "lowercase",
                "Choices": "abcdefghijklmnopqrstuvwxyz",
                "MinimumLength": 4,
                "MustStart": false
            },
            {
                "CharacterType": "numbers",
                "Choices": "1234567890",
                "MinimumLength": 4,
                "MustStart": false
            },
            {
                "CharacterType": "specialcharacter",
                "Choices": "!@#$%()",
                "MinimumLength": 4,
                "MustStart": false
            }
        ],
        "RequiredLength": 32,
        "RequestId": "b8e6b67f-3ca7-4341-b4fa-a372bdf4e11c"
    }
}
```

