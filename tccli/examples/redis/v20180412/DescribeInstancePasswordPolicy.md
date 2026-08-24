**Example 1: 查询实例密码复杂度策略**



Input: 

```
tccli redis DescribeInstancePasswordPolicy --cli-unfold-argument  \
    --InstanceId crs-5x9h****
```

Output: 
```
{
    "Response": {
        "PasswordPolicy": {
            "Enabled": true,
            "MinDigitCount": 2,
            "MinLength": 8,
            "MinLetterCount": 2,
            "MinSpecialCount": 2
        },
        "RequestId": "8b5dce2d-3bce-468f-bead-d9c91f52fbe1"
    }
}
```

