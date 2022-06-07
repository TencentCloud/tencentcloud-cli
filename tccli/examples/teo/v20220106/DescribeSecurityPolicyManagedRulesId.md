**Example 1: test**



Input: 

```
tccli teo DescribeSecurityPolicyManagedRulesId --cli-unfold-argument  \
    --RuleId 16
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "Status": "xx",
                "UpdateTime": "xx",
                "Description": "xx",
                "RuleId": 16,
                "RuleTypeId": 0,
                "RuleLevelDesc": "xx",
                "RuleTypeName": "xx",
                "RuleTags": [
                    "xx"
                ],
                "RuleTypeDesc": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

**Example 2: 规则id查询门神规则**



Input: 

```
tccli teo DescribeSecurityPolicyManagedRulesId --cli-unfold-argument  \
    --RuleId 16
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "Status": "xx",
                "UpdateTime": "xx",
                "Description": "xx",
                "RuleId": 0,
                "RuleLevelDesc": "xx",
                "RuleTypeName": "xx"
            }
        ],
        "Total": 0,
        "RequestId": "xx"
    }
}
```

