**Example 1: 查询合规化审批单**



Input: 

```
tccli vpc DescribeCrossBorderCompliance --cli-unfold-argument  \
    --ServiceProvider UNICOM \
    --Company 腾讯科技（广州）有限公司 \
    --UniformSocialCreditCode 91440101327598294H \
    --LegalPerson 张颖 \
    --IssuingAuthority 广州市海珠区市场监督管理局 \
    --BusinessAddress 广州市海珠区新港中路397号自编72号(商业街F5-1) \
    --PostCode 510320 \
    --Manager 李四 \
    --ManagerId 360732199007108888 \
    --ManagerAddress 广州市海珠区新港中路8888号 \
    --ManagerTelephone 020-81167888 \
    --Email test@tencent.com \
    --ServiceStartDate 2020-07-29 \
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
                "Company": "腾讯科技（广州）有限公司",
                "UniformSocialCreditCode": "91440101327598294H",
                "LegalPerson": "张颖",
                "IssuingAuthority": "广州市海珠区市场监督管理局",
                "BusinessLicense": "************************************************************",
                "BusinessAddress": "广州市海珠区新港中路397号自编72号(商业街F5-1)",
                "PostCode": 510320,
                "Manager": "李四",
                "ManagerId": "360732199007108888",
                "ManagerIdCard": "************************************************************",
                "ManagerAddress": "广州市海珠区新港中路8888号",
                "ManagerTelephone": "020-81167888",
                "Email": "test@tencent.com",
                "ServiceHandlingForm": "************************************************************",
                "AuthorizationLetter": "************************************************************",
                "SafetyCommitment": "************************************************************",
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

