**Example 1: 查询自动化规则**

查询自动化规则

Input: 

```
tccli hasim DescribeRule --cli-unfold-argument  \
    --RuleID 10010
```

Output: 
```
{
    "Response": {
        "Data": {
            "Distance": 0,
            "Notice": 0,
            "DataThreshold": 0,
            "Name": "xx",
            "District": 0,
            "SignalStrength": 0,
            "Url": "xx",
            "LostDay": 0,
            "IsActive": true,
            "SalePlan": "xx",
            "Email": "xx",
            "UpdatedAt": "xx",
            "TagIDs": [
                0
            ],
            "DeletedAt": "xx",
            "Type": 0,
            "ID": 0,
            "CreatedAt": "xx"
        },
        "RequestId": "xx"
    }
}
```

