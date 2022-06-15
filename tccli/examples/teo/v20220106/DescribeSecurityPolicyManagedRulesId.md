**Example 1: 规则id查询门神规则**



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
        "Count": 0,
        "RequestId": "xx"
    }
}
```

