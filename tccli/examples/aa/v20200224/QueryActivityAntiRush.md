**Example 1: 活动防刷接口示范**



Input: 

```
tccli aa QueryActivityAntiRush --cli-unfold-argument  \
    --AccountType 10004 \
    --Uid bfd81ee3ed27ad31c95ca75e21365973 \
    --UserIp 101.231.62.66 \
    --PostTime 1582029456
```

Output: 
```
{
    "Response": {
        "Level": 1,
        "PostTime": "1582029456",
        "RequestId": "fafjdlsajfldsj",
        "RiskType": [
            1,
            2
        ],
        "UserIp": "101.231.62.66",
        "CodeDesc": "Success",
        "Uid": "bfd81ee3ed27ad31c95ca75e21365973",
        "RootId": "xx",
        "AssociateAccount": "xx"
    }
}
```

