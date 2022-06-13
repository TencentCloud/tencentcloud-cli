**Example 1: 查询用户画像规则**



Input: 

```
tccli teo DescribeSecurityPortraitRules --cli-unfold-argument  \
    --Entity xx \
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
                "RuleTypeName": "xx",
                "Description": "xx",
                "RuleId": 0
            }
        ],
        "Total": 0,
        "RequestId": "xx"
    }
}
```

