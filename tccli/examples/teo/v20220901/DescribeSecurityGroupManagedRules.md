**Example 1: 查询托管规则组**



Input: 

```
tccli teo DescribeSecurityGroupManagedRules --cli-unfold-argument  \
    --Offset 2 \
    --Entity a.eotest.xyz \
    --Limit 1 \
    --ZoneId zone-285thql0vdhi
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "Total": 570,
        "RequestId": "xx",
        "WafGroupInfo": {
            "Switch": "xx",
            "Act": "xx",
            "WafGroupDetails": [
                {
                    "Level": "xx",
                    "RuleTypeId": 0,
                    "RuleTypeName": "xx",
                    "WafGroupRules": [
                        {
                            "Status": "xx",
                            "UpdateTime": "xx",
                            "Description": "xx",
                            "RuleId": 0,
                            "RuleTypeId": 0,
                            "RuleLevelDesc": "xx",
                            "RuleTypeName": "xx",
                            "RuleTags": [
                                "xx"
                            ],
                            "RuleTypeDesc": "xx"
                        }
                    ],
                    "Action": "xx",
                    "RuleTypeDesc": "xx"
                }
            ],
            "Mode": "xx",
            "Level": "xx"
        }
    }
}
```

