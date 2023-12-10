**Example 1: 查询渠道子客企业信息**

查询渠道子客企业信息

Input: 

```
tccli essbasic DescribeChannelOrganizations --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "ChannelOrganizationInfos": [
            {
                "AdminMobile": "186****0000",
                "AdminName": "张三",
                "AdminOpenId": "zhangsan",
                "AuthorizationStatus": "VERIFYING",
                "AuthorizationType": "AuthorizationLegalPerson",
                "LegalName": "李四",
                "LegalOpenId": "lisi",
                "OrganizationId": "yDwFqUUckpxxxxxxxxxxxxRvShTIZ3e",
                "OrganizationName": "渠道测试企业",
                "OrganizationOpenId": "dianziqian_orgopenid",
                "UnifiedSocialCreditCode": "913xxxxxxxxxxxxxx5W"
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s1701931761617688110",
        "Total": 1
    }
}
```

