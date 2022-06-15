**Example 1: 查询用户列表**



Input: 

```
tccli ciam ListUser --cli-unfold-argument  \
    --UserStoreId xx \
    --Pageable.PageNumber 0 \
    --Pageable.PageSize 0 \
    --Filters.0.Values xx \
    --Filters.0.Key xx \
    --Filters.0.Logic True
```

Output: 
```
{
    "Response": {
        "Content": [
            {
                "UserName": "xx",
                "Zone": "xx",
                "ResidentIdentityCard": "xx",
                "TenantId": "xx",
                "WechatOpenId": "xx",
                "Email": "xx",
                "Status": "xx",
                "Description": "xx",
                "UserId": "xx",
                "Job": "xx",
                "Address": "xx",
                "Nationality": "xx",
                "Nickname": "xx",
                "UserStoreId": "xx",
                "QqOpenId": "xx",
                "Name": "xx",
                "Gender": "xx",
                "IdentityVerificationMethod": "xx",
                "AlipayUserId": "xx",
                "LastSignOn": "xx",
                "PhoneNumber": "xx",
                "QqUnionId": "xx",
                "Locale": "xx",
                "Primary": true,
                "IdentityVerified": true,
                "WechatUnionId": "xx"
            }
        ],
        "Total": 0,
        "Pageable": {
            "PageNumber": 0,
            "PageSize": 0
        },
        "RequestId": "xx"
    }
}
```

