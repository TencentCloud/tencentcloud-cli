**Example 1: 务工卡-获取核身结果**



Input: 

```
tccli cpdp GetPayRollAuthResult --cli-unfold-argument  \
    --AuthNumber mcdhehfgisdhfjghed39384564i83 \
    --SubMerchantId 1111111
```

Output: 
```
{
    "Response": {
        "RequestId": "req-164085621426",
        "Result": {
            "AuthFailedReason": "人脸验证未通过",
            "AuthNumber": "mcdhehfgisdhfjghed39384564i83",
            "AuthScene": "FROM_MINI_APP",
            "AuthSource": "wdiooewl7587443649000",
            "AuthStatus": "AUTHENTICATE_SUCCESS",
            "AuthTime": "2015-05-20T13:29:35+08:00",
            "CompanyName": "某单位名称",
            "MerchantId": "1111111",
            "OpenId": "onqOjjmo8wmTOOtSKwXtGjg9Gb58",
            "ProjectName": "某项目",
            "SubMerchantId": "111111"
        }
    }
}
```

