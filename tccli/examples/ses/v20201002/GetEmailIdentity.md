**Example 1: 获取域名配置详情**



Input: 

```
tccli ses GetEmailIdentity --cli-unfold-argument  \
    --EmailIdentity test007.cloudses.com
```

Output: 
```
{
    "Response": {
        "Attributes": [
            {
                "CurrentValue": "v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA58lMBFjalue8JSUKjNHaSN1vzIXtAiKGupG0k/xDfXTKhurbGtVp/J2CZwhd7e9WXXSkdLn3ex1dTlPFQClDHHS2DcCfnuZXSgPgwAlaLsgomI4uCQ1x9aP+ACmidJFlvRhbF/Om3UlkYyYoeD0n7OHj7kMw6PjzzfS8PCtzXlJDsBOolmnYd9vL9DwTvi8h3pLrr/aniojXXxvj7hQ3SbTBD9TKpOSVBLtNe/5f5znETDfvzuta8QjLO+xoM23GI8+nrqSaAQMqxPHODQwpMdM2pVmi7gp7lNuvuzZKDfBcRJqrvA4r1+JE5bIlVD5/cQqGM8STSVsICRzHyhlUMQIDAQAB",
                "ExpectedValue": "v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA58lMBFjalue8JSUKjNHaSN1vzIXtAiKGupG0k/xDfXTKhurbGtVp/J2CZwhd7e9WXXSkdLn3ex1dTlPFQClDHHS2DcCfnuZXSgPgwAlaLsgomI4uCQ1x9aP+ACmidJFlvRhbF/Om3UlkYyYoeD0n7OHj7kMw6PjzzfS8PCtzXlJDsBOolmnYd9vL9DwTvi8h3pLrr/aniojXXxvj7hQ3SbTBD9TKpOSVBLtNe/5f5znETDfvzuta8QjLO+xoM23GI8+nrqSaAQMqxPHODQwpMdM2pVmi7gp7lNuvuzZKDfBcRJqrvA4r1+JE5bIlVD5/cQqGM8STSVsICRzHyhlUMQIDAQAB",
                "SendDomain": "qcloud._domainkey.test007.cloudses.com",
                "Status": true,
                "Type": "TXT"
            }
        ],
        "DKIMOption": 1,
        "IdentityType": "DOMAIN",
        "TagList": [
            {
                "TagKey": "部门",
                "TagValue": "邮件测试产研部门"
            }
        ],
        "VerifiedForSendingStatus": true,
        "RequestId": "417c19bc-c15b-4b8d-ae16-45ebff6fb854"
    }
}
```

