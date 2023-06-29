**Example 1: 查询自动化规则**

查询自动化规则

Input: 

```
tccli hasim DescribeRules --cli-unfold-argument  \
    --RuleID 10010
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 0,
            "List": [
                {
                    "Distance": 0,
                    "Notice": 0,
                    "Email": "xx",
                    "Name": "xx",
                    "District": 0,
                    "SignalStrength": 0,
                    "Url": "xx",
                    "DataThreshold": 0,
                    "IsActive": true,
                    "UpdatedAt": "xx",
                    "DeletedAt": "xx",
                    "Type": 0,
                    "ID": 0,
                    "CreatedAt": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

