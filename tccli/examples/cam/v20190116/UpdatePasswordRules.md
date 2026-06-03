**Example 1: 更新密码规则**



Input: 

```
tccli cam UpdatePasswordRules --cli-unfold-argument  \
    --Rules.ReusePasswordLimit 0 \
    --Rules.RetryPasswordLimit 0 \
    --Rules.MustContain A \
    --Rules.ForcePasswordChange 0 \
    --Rules.MinimumLength 0
```

Output: 
```
{
    "Response": {
        "RequestId": "20ef9ac7-498c-40f8-814c-7ac71cf8b81f"
    }
}
```

