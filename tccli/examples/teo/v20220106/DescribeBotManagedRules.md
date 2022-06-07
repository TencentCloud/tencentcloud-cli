**Example 1: 查询门神规则**



Input: 

```
tccli teo DescribeBotManagedRules --cli-unfold-argument  \
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

