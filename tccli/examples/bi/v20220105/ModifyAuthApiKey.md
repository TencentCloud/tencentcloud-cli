**Example 1: 成功**



Input: 

```
tccli bi ModifyAuthApiKey --cli-unfold-argument  \
    --ApiKey a46a65f2d17444c4800e57ed2a9f0206 \
    --DefaultUser 700000280185
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApiKey": "a46a65f2d17444c4800e57ed2a9f0206",
            "CorpId": "700000231283",
            "CreatedAt": "2026-04-15 19:47:14",
            "CreatedUser": "700000280185",
            "DefaultUser": "700000280185",
            "Id": 10001010,
            "UpdatedAt": "2026-04-15 19:47:14",
            "UpdatedUser": "700000280185"
        },
        "Extra": "**",
        "Msg": "默认业务成功",
        "RequestId": "9df975b5-1b9a-4dfc-bc2d-da2dbd2de18d"
    }
}
```

