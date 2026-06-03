**Example 1: 成功**



Input: 

```
tccli bi DescribeAuthApiKeyInfo --cli-unfold-argument  \
    --ApiKey 5e1e693f6e13497691fece0373d3e88c
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApiKey": "5e1e693f6e13497691fece0373d3e88c",
            "CorpId": "700000231283",
            "CreatedAt": "2025-10-16 16:51:38",
            "CreatedUser": "700000280185",
            "DefaultUser": "700000231283",
            "Id": 10001009,
            "UpdatedAt": "2025-10-16 16:51:38",
            "UpdatedUser": "700000280185"
        },
        "Extra": "**",
        "Msg": "默认业务成功",
        "RequestId": "3fa241e0-be7e-457e-8220-142dfc20d2aa"
    }
}
```

