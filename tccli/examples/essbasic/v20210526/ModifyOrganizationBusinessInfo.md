**Example 1: 变更企业信息，共有 87 份 saas 和 第三方子客未完结的合同，拦截**



Input: 

```
tccli essbasic ModifyOrganizationBusinessInfo --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId ess_open_organization_1 \
    --Agent.ProxyOperator.OpenId yuan \
    --BizLicenseResourceId yDCNIUUckpv809ikUuxOPaXRjLuPnGvS \
    --OrganizationName 东莞万御安防科技服务有限公司 \
    --NewLegalMobile 132****0000
```

Output: 
```
{
    "Response": {
        "ChannelFlowIds": [
            "yD3JcUUckpep6qq5U1UyDrfDm8l6NzKw"
        ],
        "ErrorCode": 1,
        "ErrorMessage": "存在 87 份未完结的合同，请先撤销或者完成合同",
        "FlowIds": [
            "yD3JaUUckperbj2gU1UxOsoPKSdAroVT"
        ],
        "UnfinishedCount": 87,
        "RequestId": "f0572876-6ef1-4616-a77e-c2f28dee3c1f"
    }
}
```

**Example 2: 变更企业信息，有 4 份 第三方子客未完结的合同，拦截**



Input: 

```
tccli essbasic ModifyOrganizationBusinessInfo --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId huo_la_dun_ping_yuan \
    --Agent.ProxyOperator.OpenId kyle_huo_xian \
    --BizLicenseResourceId yD3JaUUckperpm7qUxaAsRsEvrnOVuVD \
    --OrganizationName 黑****测试 \
    --Address  \
    --LegalName  \
    --NewLegalMobile 
```

Output: 
```
{
    "Response": {
        "ChannelFlowIds": [
            "yD3JaUUckperl3wcU1UVOahuSNCPtvmn"
        ],
        "ErrorCode": 1,
        "ErrorMessage": "存在 4 份未完结的合同，请先撤销或者完成合同",
        "FlowIds": [],
        "UnfinishedCount": 4,
        "RequestId": "dbe937ef-2ee0-4130-9a14-731425ffd627"
    }
}
```

**Example 3: 变更企业信息成功，修改企业名称以及法人**



Input: 

```
tccli essbasic ModifyOrganizationBusinessInfo --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId huo_la_dun_ping_yuan \
    --Agent.ProxyOperator.OpenId kyle_huo_xian \
    --BizLicenseResourceId yD3JaUUckperpm7qUxaAsRsEvrnOVuVD \
    --OrganizationName 黄****测试 \
    --Address  \
    --LegalName 东**淑 \
    --NewLegalMobile 19*******27
```

Output: 
```
{
    "Response": {
        "ChannelFlowIds": [],
        "ErrorCode": 0,
        "ErrorMessage": "",
        "FlowIds": [],
        "UnfinishedCount": 0,
        "RequestId": "43b5b52f-0c57-48c3-a36d-e314b1498b26"
    }
}
```

