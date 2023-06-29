**Example 1: 根据ID查询用户信息**



Input: 

```
tccli ciam DescribeUserById --cli-unfold-argument  \
    --UserStoreId xx \
    --UserId xx
```

Output: 
```
{
    "Response": {
        "User": {
            "UserName": "xx",
            "Zone": "xx",
            "UserId": "xx",
            "ResidentIdentityCard": "xx",
            "TenantId": "xx",
            "CustomAttributes": [
                {
                    "Type": "xx",
                    "Name": "xx",
                    "Value": "xx"
                }
            ],
            "Version": 0,
            "WechatOpenId": "xx",
            "Email": "xx",
            "Status": "xx",
            "Description": "xx",
            "LastModifiedDate": 0,
            "AlreadyFirstLogin": true,
            "Job": "xx",
            "Address": "xx",
            "Nationality": "xx",
            "Nickname": "xx",
            "UserStoreId": "xx",
            "QqOpenId": "xx",
            "Name": "xx",
            "UserDataSourceEnum": "xx",
            "Gender": "xx",
            "IdentityVerificationMethod": "xx",
            "AlipayUserId": "xx",
            "LastSignOn": 0,
            "PhoneNumber": "xx",
            "Birthdate": 0,
            "QqUnionId": "xx",
            "UserGroups": [
                "xx"
            ],
            "Locale": "xx",
            "Primary": true,
            "IdentityVerified": true,
            "CreatedDate": 0,
            "LockTime": 0,
            "LockType": "xx",
            "WechatUnionId": "xx"
        },
        "RequestId": "xx"
    }
}
```

