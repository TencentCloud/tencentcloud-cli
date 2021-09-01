**Example 1: 创建匿名访问Token**



Input: 

```
tccli iotvideo CreateAnonymousAccessToken --cli-unfold-argument  \
    --Tid 2345345 \
    --OldAccessToken 123 \
    --TtlMinutes 5
```

Output: 
```
{
    "Response": {
        "AccessId": "-4611686663866723169",
        "AccessToken": "02017525B4BCDXXXXXXXXXX305D97E0XXXXXXXX",
        "ExpireTime": 1602589211,
        "RequestId": "43348837-a756-4939-92b6-77c333c1b96e"
    }
}
```

