**Example 1: 示例1**

修改实例密码复杂度策略

Input: 

```
tccli redis ModifyInstancePasswordPolicy --cli-unfold-argument  \
    --InstanceId crs-5x9h**** \
    --PasswordPolicy.Enabled True \
    --PasswordPolicy.MinLetterCount 2 \
    --PasswordPolicy.MinDigitCount 2 \
    --PasswordPolicy.MinSpecialCount 2 \
    --PasswordPolicy.MinLength 8
```

Output: 
```
{
    "Response": {
        "RequestId": "d44b2cfe-32e7-4aa1-9216-1ffdaee0089c"
    }
}
```

