**Example 1: 查询别称域名信息列表**



Input: 

```
tccli teo DescribeAliasDomains --cli-unfold-argument  \
    --ZoneId zone-28569s6od5na \
    --Limit 20 \
    --Filters.0.Values bbb.test.com \
    --Filters.0.Name alias-name \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "5ce6ee51-cda5-4e0d-a338-cff57a00bb3a",
        "AliasDomains": [
            {
                "Status": "pending",
                "ModifiedOn": "2020-09-22T00:00:00+00:00",
                "TargetName": "aaa.example.com",
                "CreatedOn": "2020-09-22T00:00:00+00:00",
                "ZoneId": "zone-28569s6od5na",
                "AliasName": "bbb.test.com",
                "ForbidMode": 0
            }
        ]
    }
}
```

