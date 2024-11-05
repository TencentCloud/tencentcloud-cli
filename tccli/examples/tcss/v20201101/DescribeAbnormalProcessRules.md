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
                "UpdateTime": "2022-01-01 00:00:00",
                "IsEnable": true,
                "RuleId": "10001",
                "EffectImageCount": 1,
                "EditUserName": "admin",
                "RuleName": "rule_name",
                "IsDefault": true
            }
        ],
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

