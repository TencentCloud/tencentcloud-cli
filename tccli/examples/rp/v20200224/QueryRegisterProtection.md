**Example 1: 注册保护接口示范**



Input: 

```
tccli rp QueryRegisterProtection --cli-unfold-argument  \
    --AccountType 10004 \
    --Uid bfd81ee3ed27ad31c95ca75e21365973 \
    --RegisterIp 101.231.62.66 \
    --RegisterTime 1582029456
```

Output: 
```
{
    "Response": {
        "Level": 1,
        "RegisterIp": "101.231.62.66",
        "RegisterTime": "1582029456",
        "RiskType": [
            1,
            22
        ],
        "CodeDesc": "Success",
        "Uid": "bfd81ee3ed27ad31c95ca75e21365973"
    }
}
```

