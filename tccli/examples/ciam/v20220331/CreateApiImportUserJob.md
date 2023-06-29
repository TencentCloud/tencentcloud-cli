**Example 1: 新建接口导入用户任务**



Input: 

```
tccli ciam CreateApiImportUserJob --cli-unfold-argument  \
    --UserStoreId xx \
    --DataFlowUserCreateList.0.UserName xx \
    --DataFlowUserCreateList.0.Zone xx \
    --DataFlowUserCreateList.0.ResidentIdentityCard xx \
    --DataFlowUserCreateList.0.WechatOpenId xx \
    --DataFlowUserCreateList.0.Email xx \
    --DataFlowUserCreateList.0.CustomizationAttributes.0.Type xx \
    --DataFlowUserCreateList.0.CustomizationAttributes.0.Name xx \
    --DataFlowUserCreateList.0.CustomizationAttributes.0.Value xx \
    --DataFlowUserCreateList.0.Description xx \
    --DataFlowUserCreateList.0.Job xx \
    --DataFlowUserCreateList.0.Address xx \
    --DataFlowUserCreateList.0.Nationality xx \
    --DataFlowUserCreateList.0.Password xx \
    --DataFlowUserCreateList.0.Nickname xx \
    --DataFlowUserCreateList.0.QqOpenId xx \
    --DataFlowUserCreateList.0.Name xx \
    --DataFlowUserCreateList.0.Gender xx \
    --DataFlowUserCreateList.0.IdentityVerificationMethod xx \
    --DataFlowUserCreateList.0.AlipayUserId xx \
    --DataFlowUserCreateList.0.Birthdate 2020-09-22 \
    --DataFlowUserCreateList.0.PhoneNumber xx \
    --DataFlowUserCreateList.0.UserGroup xx \
    --DataFlowUserCreateList.0.PasswordEncryptTypeEnum xx \
    --DataFlowUserCreateList.0.Salt.SaltLocation.SaltLocationRule.Regex xx \
    --DataFlowUserCreateList.0.Salt.SaltLocation.SaltLocationTypeEnum xx \
    --DataFlowUserCreateList.0.Salt.SaltValue xx \
    --DataFlowUserCreateList.0.QqUnionId xx \
    --DataFlowUserCreateList.0.Locale xx \
    --DataFlowUserCreateList.0.IdentityVerified True \
    --DataFlowUserCreateList.0.WechatUnionId xx
```

Output: 
```
{
    "Response": {
        "Job": {
            "Status": "xx",
            "Format": "xx",
            "ErrorDetails": [
                {
                    "UserId": "xx",
                    "Error": "xx"
                }
            ],
            "Location": "xx",
            "CreatedDate": 0,
            "FailedUsers": [
                {
                    "FailedUserIdentification": "xx",
                    "FailedReason": "xx"
                }
            ],
            "Type": "xx",
            "Id": "xx"
        },
        "RequestId": "xx"
    }
}
```

