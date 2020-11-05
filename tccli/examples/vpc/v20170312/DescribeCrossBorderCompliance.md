**Example 1: Querying a compliance review form**



Input: 

```
tccli vpc DescribeCrossBorderCompliance --cli-unfold-argument  \
    --ServiceProvider UNICOM\
    --Company 'Guangzhou Tencent Technology Co., Ltd'\
    --UniformSocialCreditCode 91440101327598294H\
    --LegalPerson 'Zhang Ying'\
    --IssuingAuthority 'Guangzhou Haizhu District Administration for Market Regulation'\
    --BusinessAddress 'Commercial Street F5-1, No. 397-72, Middle Xingang Road, Haizhu District, Guangzhou City, China'\
    --PostCode 510320\
    --Manager Tom\
    --ManagerId 360732199007108888\
    --ManagerAddress 'No. 8888, Middle Xingang Road, Haizhu District, Guangzhou City, China'\
    --ManagerTelephone 020-81167888\
    --Email test@tencent.com\
    --ServiceStartDate 2020-07-29\
    --ServiceEndDate 2021-07-29
```

Output: 
```
{
    "Response": {
        "CrossBorderComplianceSet": [
            {
                "ComplianceId": 10013,
                "ServiceProvider": "UNICOM",
                "Company": "Guangzhou Tencent Technology Co., Ltd",
                "UniformSocialCreditCode": "91440101327598294H",
                "LegalPerson": "Zhang Ying",
                "IssuingAuthority": "Guangzhou Haizhu District Administration for Market Regulation",
                "BusinessLicense": "https://cross-border-connection-1258344699.cos.ap-guangzhou.myqcloud.com/BusinessLicense.png?q-sign-algorithm=sha1&q-ak=AKIDLYWGm2QAuUZP1NqFm6OaEcjaCYkVuMRF&q-sign-time=1596446068%3B1596449728&q-key-time=1596446068%3B1596449728&q-header-list=&q-url-param-list=&q-signature=d6f3d34ec6cdb4e7a84b29d96ebab0ceb649e441",
                "BusinessAddress": "Commercial Street F5-1, No. 397-72, Middle Xingang Road, Haizhu District, Guangzhou City, China",
                "PostCode": 510320,
                "Manager": "Tom",
                "ManagerId": "360732199007108888",
                "ManagerIdCard": "https://cross-border-connection-1258344699.cos.ap-guangzhou.myqcloud.com/ManagerIdCard.png?q-sign-algorithm=sha1&q-ak=AKIDLYWGm2QAuUZP1NqFm6OaEcjaCYkVuMRF&q-sign-time=1596446068%3B1596449728&q-key-time=1596446068%3B1596449728&q-header-list=&q-url-param-list=&q-signature=0eef108d574b332046de78b260c84844159b1fc1",
                "ManagerAddress": "No. 8888, Middle Xingang Road, Haizhu District, Guangzhou City, China",
                "ManagerTelephone": "020-81167888",
                "Email": "test@tencent.com",
                "ServiceHandlingForm": "https://cross-border-connection-1258344699.cos.ap-guangzhou.myqcloud.com/ServiceHandlingForm.png?q-sign-algorithm=sha1&q-ak=AKIDLYWGm2QAuUZP1NqFm6OaEcjaCYkVuMRF&q-sign-time=1596446068%3B1596449728&q-key-time=1596446068%3B1596449728&q-header-list=&q-url-param-list=&q-signature=8083e838f07cbc5db0d8604962c2148067604311",
                "AuthorizationLetter": "https://cross-border-connection-1258344699.cos.ap-guangzhou.myqcloud.com/AuthorizationLetter.png?q-sign-algorithm=sha1&q-ak=AKIDLYWGm2QAuUZP1NqFm6OaEcjaCYkVuMRF&q-sign-time=1596446068%3B1596449728&q-key-time=1596446068%3B1596449728&q-header-list=&q-url-param-list=&q-signature=e66ea70810c159dcd2c4fe576194e87ea4e11fbb",
                "SafetyCommitment": "https://cross-border-connection-1258344699.cos.ap-guangzhou.myqcloud.com/SafetyCommitment.png?q-sign-algorithm=sha1&q-ak=AKIDLYWGm2QAuUZP1NqFm6OaEcjaCYkVuMRF&q-sign-time=1596446068%3B1596449728&q-key-time=1596446068%3B1596449728&q-header-list=&q-url-param-list=&q-signature=991615e1b56f1ab107f6840dd7bfe20230825f55",
                "ServiceStartDate": "2020-07-29",
                "ServiceEndDate": "2021-07-29",
                "State": "PENDING",
                "CreatedTime": "2020-08-03 16:59:45"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c3e0aa8b-5dce-467d-a63f-242126b3eabf"
    }
}
```

