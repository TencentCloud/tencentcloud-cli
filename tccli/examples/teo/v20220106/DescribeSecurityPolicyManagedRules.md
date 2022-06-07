**Example 1: 查询门神规则**



Input: 

```
tccli teo DescribeSecurityPolicyManagedRules --cli-unfold-argument  \
    --PerPage 0 \
    --Entity xx \
    --Page 0 \
    --ZoneId xx
```

Output: 
```
{
    "Response": {
        "Count": 0,
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

