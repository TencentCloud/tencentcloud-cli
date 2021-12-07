**Example 1: 运行时访问控制策略列表**



Input: 

```
tccli tcss DescribeAccessControlRules --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RuleSet": [
            {
                "UpdateTime": "xx",
                "IsEnable": true,
                "RuleId": "xx",
                "EffectImageCount": 1,
                "EditUserName": "xx",
                "RuleName": "xx",
                "IsDefault": true
            }
        ],
        "RequestId": "xx"
    }
}
```

