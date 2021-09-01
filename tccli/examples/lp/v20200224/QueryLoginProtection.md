**Example 1: 登录保护接口示例**



Input: 

```
tccli lp QueryLoginProtection --cli-unfold-argument  \
    --AccountType 10004 \
    --Uid bfd81ee3ed27ad31c95ca75e21365973 \
    --LoginIp 101.231.62.66 \
    --LoginTime 1582029456
```

Output: 
```
{
    "Response": {
        "Level": 1,
        "LoginIp": "101.231.62.66",
        "LoginTime": "1582029456",
        "RiskType": [
            1,
            22
        ],
        "CodeDesc": "Success",
        "Uid": "bfd81ee3ed27ad31c95ca75e21365973"
    }
}
```

