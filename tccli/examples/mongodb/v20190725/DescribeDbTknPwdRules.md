**Example 1: 查看数据库密码规则**



Input: 

```
tccli mongodb DescribeDbTknPwdRules --cli-unfold-argument  \
    --UserResourceId cmgo-js2qrgp5 \
    --ResourceRegion ap-guangzhou \
    --InstanceType mongodb
```

Output: 
```
{
    "Response": {
        "RequestId": "9ab09c94-b2fc-4053-9115-ccc178e56000",
        "RequiredLength": 8,
        "Rules": [
            {
                "CharacterType": "uppercase",
                "Choices": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "MinimumLength": 4,
                "MustStart": false
            }
        ]
    }
}
```

