**Example 1: 查询单个企业的企业信息**

查询单个企业的企业信息

Input: 

```
tccli essbasic DescribeChannelOrganizations --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --OrganizationOpenId org_dianziqian \
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
                "AdminName": "典子谦",
                "AdminOpenId": "n9527",
                "AuthorizationStatus": "VERIFYING",
                "AuthorizationType": "AuthorizationLegalPerson",
                "LegalName": "典子谦",
                "LegalOpenId": "n9527",
                "OrganizationId": "yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF",
                "OrganizationName": "典子谦示例企业",
                "OrganizationOpenId": "org_dianziqian",
                "UnifiedSocialCreditCode": "X1440101304662708B"
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s1701931761617688110",
        "Total": 1
    }
}
```

**Example 2: 批量查询应用下的所有企业信息**

批量查询应用下的所有企业信息

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
                "AdminName": "典子谦",
                "AdminOpenId": "n9527",
                "AuthorizationStatus": "VERIFYING",
                "AuthorizationType": "AuthorizationLegalPerson",
                "LegalName": "典子谦",
                "LegalOpenId": "n9527",
                "OrganizationId": "yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF",
                "OrganizationName": "典子谦示例企业",
                "OrganizationOpenId": "org_dianziqian",
                "UnifiedSocialCreditCode": "X1440101304662708B"
            },
            {
                "AdminMobile": "151****0000",
                "AdminName": "李四",
                "AdminOpenId": "org_lisi",
                "AuthorizationStatus": "VERIFYING",
                "AuthorizationType": "AuthorizationLegalPerson",
                "LegalName": "张三",
                "LegalOpenId": "n02468",
                "OrganizationId": "yDwFqUUckpxxxxxxxxxxxxRvShTIZ3e",
                "OrganizationName": "张三示例企业",
                "OrganizationOpenId": "org_zhansan",
                "UnifiedSocialCreditCode": "X1440106MA59B1269X"
            }
        ],
        "Limit": 20,
        "Offset": 0,
        "RequestId": "s1701931761617688110",
        "Total": 2
    }
}
```

