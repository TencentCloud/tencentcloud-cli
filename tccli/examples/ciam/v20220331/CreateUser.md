**Example 1: 创建用户**

创建用户时使用

Input: 

```
tccli ciam CreateUser --cli-unfold-argument  \
    --UserStoreId d733b65803284091a998ab707d820726 \
    --PhoneNumber +86-19877755556 \
    --Email testuser006@test.com \
    --Password @ppServer123 \
    --UserName testuser006 \
    --UserOrg 8bee9039509c4c3c80b26fbb8cacedb9
```

Output: 
```
{
    "Response": {
        "User": {
            "Address": null,
            "AlipayUserId": null,
            "AlreadyFirstLogin": false,
            "Birthdate": null,
            "CreatedDate": 1776252106112,
            "CustomAttributes": [],
            "Description": null,
            "Email": "testuser006@test.com",
            "Gender": null,
            "IdentityVerificationMethod": null,
            "IdentityVerified": false,
            "IndexedAttribute1": null,
            "IndexedAttribute2": null,
            "IndexedAttribute3": null,
            "IndexedAttribute4": null,
            "IndexedAttribute5": null,
            "Job": null,
            "LastModifiedDate": 1776252106112,
            "LastSignOn": null,
            "Locale": null,
            "LockTime": null,
            "LockType": null,
            "Name": null,
            "Nationality": null,
            "Nickname": null,
            "PhoneNumber": "+86-19877755556",
            "Primary": true,
            "QqOpenId": null,
            "QqUnionId": null,
            "ResidentIdentityCard": null,
            "Status": "NOT_ENABLED",
            "TenantId": "100000090126",
            "UserDataSourceEnum": "管理员添加",
            "UserGroups": [],
            "UserId": "b8c22a1e34e94b7899626b1f5ed1a33b",
            "UserName": "testuser006",
            "UserOrgs": [
                "8bee9039509c4c3c80b26fbb8cacedb9"
            ],
            "UserStoreId": "d733b65803284091a998ab707d820726",
            "Version": null,
            "WeComUserId": null,
            "WechatOpenId": null,
            "WechatUnionId": null,
            "Zone": null
        },
        "RequestId": "59f481be-c906-4675-8f2e-7a8d49d49a9b"
    }
}
```

