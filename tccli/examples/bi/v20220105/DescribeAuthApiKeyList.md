**Example 1: 成功**



Input: 

```
tccli bi DescribeAuthApiKeyList --cli-unfold-argument  \
    --AllPage False \
    --PageNo 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "ApiKey": "5e1e693f6e13497691fece0373d3e88c",
                    "CorpId": "700000231283",
                    "CreatedAt": "2025-10-16 16:51:38",
                    "CreatedUser": "700000280185",
                    "DefaultUser": "700000231283",
                    "Id": 10001009,
                    "UpdatedAt": "2025-10-16 16:51:38",
                    "UpdatedUser": "700000280185"
                }
            ],
            "Total": 1,
            "TotalPages": 1
        },
        "Extra": "**",
        "Msg": "默认业务成功",
        "RequestId": "461fd326-b1f5-42b3-ac0b-a2a887f78bb1"
    }
}
```

