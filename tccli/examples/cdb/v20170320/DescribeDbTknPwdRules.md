**Example 1: 查询轮转密码规则**



Input: 

```
tccli cdb DescribeDbTknPwdRules --cli-unfold-argument  \
    --UserResourceId testUserResourceId \
    --ResourceRegion testResourceRegion \
    --ResourceAccount testResourceAccount \
    --InstanceType testInstanceType
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "CharacterType": "abc",
                "Choices": "abc",
                "MinimumLength": 0,
                "MustStart": true
            }
        ],
        "RequiredLength": 0,
        "RequestId": "abc"
    }
}
```

