**Example 1: 务工卡-查询核身记录**



Input: 

```
tccli cpdp GetPayRollAuthList --cli-unfold-argument  \
    --WechatSubAppId wxa1111111 \
    --OpenId onqOjjmo8wmTOOtSKwXtGjg9Gb58 \
    --WechatAppId wxa1111111 \
    --AuthDate 2020-12-25 \
    --SubMerchantId 1111111 \
    --Limit 10 \
    --Offset 0 \
    --AuthStatus AUTHENTICATE_SUCCESS
```

Output: 
```
{
    "Response": {
        "Limit": 10,
        "Offset": 1,
        "RequestId": "req-164085656796",
        "Results": [
            {
                "AuthFailedReason": "",
                "AuthNumber": "mcdhehfgisdhfjghed39384564i83",
                "AuthScene": "FROM_MINI_APP",
                "AuthSource": "wdiooewl7587443649000",
                "AuthStatus": "FROM_MINI_APP",
                "AuthTime": "2015-05-20T13:29:35+08:00",
                "CompanyName": "某单位名称",
                "MerchantId": "1111111",
                "OpenId": "onqOjjmo8wmTOOtSKwXtGjg9Gb58",
                "ProjectName": "某项目",
                "SubMerchantId": "111111"
            }
        ],
        "Total": 9
    }
}
```

