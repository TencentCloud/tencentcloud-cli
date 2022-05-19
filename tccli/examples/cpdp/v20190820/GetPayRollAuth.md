**Example 1: 务工卡-查询授权关系**



Input: 

```
tccli cpdp GetPayRollAuth --cli-unfold-argument  \
    --WechatSubAppId wxa1111111 \
    --OpenId onqOjjmo8wmTOOtSKwXtGjg9Gb58 \
    --WechatAppId wxa1111111 \
    --SubMerchantId 1111111
```

Output: 
```
{
    "Response": {
        "AuthStatus": "UNAUTHORIZED",
        "AuthTime": "2015-05-20T13:29:35.120+08:00",
        "CancelAuthTime": "2015-05-20T13:29:35.120+08:00",
        "MerchantId": "1111111",
        "OpenId": "9x111111",
        "RequestId": "req-164085490080",
        "SubMerchantId": "1111111"
    }
}
```

