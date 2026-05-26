**Example 1: 查看密码规则**



Input: 

```
tccli cam GetPasswordRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "UpdateTime": "2020-01-29 15:18:37",
        "Modifier": "20548499",
        "Rules": {
            "MinimumLength": 9,
            "MustContain": "A",
            "ForcePasswordChange": 1,
            "ReusePasswordLimit": 2,
            "RetryPasswordLimit": 0
        },
        "RequestId": "044c0502-6975-44c2-8342-8160eb666ab0"
    }
}
```

