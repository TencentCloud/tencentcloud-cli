**Example 1: 查询恶意外连白名单**



Input: 

```
tccli tcss DescribeMaliciousConnectionWhiteList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "RuleID": 1,
                "CreatedTime": "xx",
                "RuleType": "xx",
                "UpdateTime": "xx",
                "Remark": "xx",
                "Address": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

