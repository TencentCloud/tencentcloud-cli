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
        "RequestId": "4b8c24c5-3576-40e0-82f9-60628c9c2d47",
        "Count": 1,
        "Total": 570,
        "WafGroupInfo": {
            "Switch": "on",
            "Act": "",
            "Mode": "block",
            "Level": "strict"
        }
    }
}
```

