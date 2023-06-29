**Example 1: 运行时异常进程策略列表**



Input: 

```
tccli tcss DescribeAbnormalProcessRules --cli-unfold-argument  \
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

