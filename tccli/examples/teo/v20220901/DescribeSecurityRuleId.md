**Example 1: bot规则**



Input: 

```
tccli teo DescribeSecurityRuleId --cli-unfold-argument  \
    --RuleType bot \
    --RuleIdList 1006 \
    --Entity runtimewu.eosecdev.xyz
```

Output: 
```
{
    "Response": {
        "WafGroupRules": [
            {
                "Status": "allow",
                "UpdateTime": "2022-09-01 00:00:00",
                "Description": "Site Monitor",
                "RuleId": 1006,
                "RuleTypeId": 0,
                "RuleLevelDesc": "Site Monitor",
                "RuleTypeName": "Site Monitor",
                "RuleTags": [
                    "site"
                ],
                "RuleTypeDesc": "Site Monitor"
            }
        ],
        "RequestId": "awj989f2j-afj9hf8-dj293d"
    }
}
```

