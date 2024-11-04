**Example 1: 新建接口导入用户任务**

批量导入用户时使用

Input: 

```
tccli ciam CreateApiImportUserJob --cli-unfold-argument  \
    --UserStoreId abc \
    --DataFlowUserCreateList.0.UserName zhangsan \
    --DataFlowUserCreateList.0.PhoneNumber 132****0000 \
    --DataFlowUserCreateList.0.Email 132****@qq.com \
    --DataFlowUserCreateList.0.ResidentIdentityCard 123456789012345678 \
    --DataFlowUserCreateList.0.Nickname 昵称1 \
    --DataFlowUserCreateList.0.Address 北京市海淀区 \
    --DataFlowUserCreateList.0.UserGroup 6cd22e51****************f6f7cb81 \
    --DataFlowUserCreateList.0.QqOpenId qqopenid \
    --DataFlowUserCreateList.0.QqUnionId qqunionid \
    --DataFlowUserCreateList.0.WechatOpenId wechatopenid \
    --DataFlowUserCreateList.0.WechatUnionId wechatunionid \
    --DataFlowUserCreateList.0.AlipayUserId alipayuserid \
    --DataFlowUserCreateList.0.WeComUserId wecomuserid \
    --DataFlowUserCreateList.0.Description 用户1 \
    --DataFlowUserCreateList.0.Birthdate 2022-10-20 \
    --DataFlowUserCreateList.0.Name 姓名 \
    --DataFlowUserCreateList.0.Locale 地理位置 \
    --DataFlowUserCreateList.0.Gender 男 \
    --DataFlowUserCreateList.0.IdentityVerificationMethod 无 \
    --DataFlowUserCreateList.0.IdentityVerified True \
    --DataFlowUserCreateList.0.Job 员工 \
    --DataFlowUserCreateList.0.Nationality 汉族 \
    --DataFlowUserCreateList.0.Zone 时区 \
    --DataFlowUserCreateList.0.Password password \
    --DataFlowUserCreateList.0.CustomizationAttributes.0.Name nickname \
    --DataFlowUserCreateList.0.CustomizationAttributes.0.Value 昵称 \
    --DataFlowUserCreateList.0.CustomizationAttributes.0.Type STRING \
    --DataFlowUserCreateList.0.Salt.SaltValue salt*** \
    --DataFlowUserCreateList.0.Salt.SaltLocation.SaltLocationTypeEnum HEAD \
    --DataFlowUserCreateList.0.Salt.SaltLocation.SaltLocationRule.Regex passwordabc123 \
    --DataFlowUserCreateList.0.PasswordEncryptTypeEnum SHA1 \
    --DataFlowUserCreateList.0.IndexedAttribute1 value1 \
    --DataFlowUserCreateList.0.IndexedAttribute2 value2 \
    --DataFlowUserCreateList.0.IndexedAttribute3 value3 \
    --DataFlowUserCreateList.0.IndexedAttribute4 value4 \
    --DataFlowUserCreateList.0.IndexedAttribute5 value5
```

Output: 
```
{
    "Response": {
        "Job": {
            "Id": "c29f2c0f****************405ec698",
            "Status": "PENDING",
            "Type": "IMPORT_USER",
            "CreatedDate": 1715156770024,
            "Format": "NDJSON",
            "Location": "http://aa.com/bb.csv",
            "ErrorDetails": [
                {
                    "UserId": "53e25c3****************e4eb5bd1",
                    "Error": "error message"
                }
            ],
            "FailedUsers": [
                {
                    "FailedUserIdentification": "53e25c3****************e4eb5bd1",
                    "FailedReason": "error reason"
                }
            ]
        },
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

