**Example 1: 查询用户画像规则**



Input: 

```
tccli teo DescribeSecurityPortraitRules --cli-unfold-argument  \
    --Entity a.eotest.com \
    --ZoneId zone-285thql0vdhi
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "PortraitManagedRuleDetails": [
            {
                "ClassificationId": 0,
                "Description": "AttackerIP1",
                "RuleId": 1,
                "RuleTypeName": "botdb",
                "Status": "block"
            }
        ],
        "Total": 1,
        "RequestId": "2f292f3rff-23ra3ra-a34fgag"
    }
}
```

