**Example 1: 查询用户列表**



Input: 

```
tccli ciam ListUserByProperty --cli-unfold-argument  \
    --UserStoreId 2c3aca3b****************a7efe88e \
    --PropertyCode phoneNumber \
    --PropertyValue 130****0000 \
    --Original True
```

Output: 
```
{
    "Response": {
        "Users": [
            {
                "UserId": "53e25c3****************e4eb5bd1",
                "UserName": "zhangsan",
                "PhoneNumber": "132****0000",
                "Email": "132****@qq.com",
                "LastSignOn": 1711002933442,
                "CreatedDate": 1718332940956,
                "Status": "NORMAL",
                "UserDataSourceEnum": "管理员添加",
                "Nickname": "昵称1",
                "Address": "北京市海淀区",
                "Birthdate": 1706682491339,
                "UserGroups": [
                    "6cd22e51****************f6f7cb81"
                ],
                "LastModifiedDate": 1722420973329,
                "CustomAttributes": [
                    {
                        "Name": "k",
                        "Value": "v",
                        "Type": "STRING"
                    }
                ],
                "ResidentIdentityCard": "123456789012345678",
                "QqOpenId": "qqopenid",
                "QqUnionId": "qqunionid",
                "WechatOpenId": "wechatopenid",
                "WechatUnionId": "wechatunionid",
                "AlipayUserId": "alipayuserid",
                "WeComUserId": "wecomuserid",
                "Description": "用户1",
                "Name": "姓名",
                "Locale": "地理位置",
                "Gender": "男",
                "IdentityVerificationMethod": "nameAndIdCard",
                "IdentityVerified": true,
                "Job": "员工",
                "Nationality": "汉族",
                "Primary": true,
                "Zone": "时区",
                "AlreadyFirstLogin": true,
                "TenantId": "tenantId",
                "UserStoreId": "2c3aca3b****************a7efe88e",
                "Version": 0,
                "LockType": "failureLock",
                "LockTime": 0,
                "IndexedAttribute1": "value1",
                "IndexedAttribute2": "value2",
                "IndexedAttribute3": "value3",
                "IndexedAttribute4": "value4",
                "IndexedAttribute5": "value5"
            }
        ],
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

