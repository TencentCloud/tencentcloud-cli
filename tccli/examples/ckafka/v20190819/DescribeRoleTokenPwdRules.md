**Example 1: 查询密码复杂度规则**



Input: 

```
tccli ckafka DescribeRoleTokenPwdRules --cli-unfold-argument  \
    --InstanceType ckafka \
    --UserResourceId ckafka-*****xx \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount ckafka#****User
```

Output: 
```
{
    "Response": {
        "RequiredLength": 32,
        "Rules": [
            {
                "CharacterType": "numbers",
                "Choices": "1234567890",
                "MinimumLength": 4,
                "MustStart": false
            }
        ],
        "RequestId": "dde117e6-29d2-4147-89e3-4d9633b4195f"
    }
}
```

