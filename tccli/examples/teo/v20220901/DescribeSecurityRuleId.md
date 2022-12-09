**Example 1: bot规则**



Input: 

```
tccli teo DescribeSecurityRuleId --cli-unfold-argument  \
    --RuleType bot \
    --RuleIdList 1006 \
    --Entity runtimewu.eosecdev.xyz \
    --Domains runtimewu1.eosecdev.xyz runtimewu2.eosecdev.xyz
```

Output: 
```
{
    "Response": {
        "WafGroupRules": [],
        "SecurityRules": [
            {
                "Status": "allow",
                "Description": "Site Monitor",
                "RuleId": 1006,
                "RuleTypeId": 0,
                "RuleLevelDesc": "Site Monitor",
                "RuleTypeName": "Site Monitor",
                "RuleTags": [
                    "site"
                ],
                "RuleTypeDesc": "Site Monitor",
                "Entity": "runtimewu.eosecdev.xyz"
            }
        ],
        "RequestId": "awj989f2j-afj9hf8-dj293d"
    }
}
```

