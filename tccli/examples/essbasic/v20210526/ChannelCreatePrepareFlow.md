**Example 1: 文件发起-跳过文件上传**



Input: 

```
tccli essbasic ChannelCreatePrepareFlow --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId 5d18c1c4c8926cd11 \
    --Agent.ProxyOrganizationOpenId 572c69xxxxxx245e4 \
    --Agent.AppId yDRsbUUgxxxx7ZfBvipOMJ \
    --ResourceId yDwqFUUckp3em41rUwWPgIBjsYgG5bba \
    --ResourceType 2 \
    --FlowInfo.FlowName 第三方预发起合同-跳过文件上传 \
    --FlowInfo.FlowType 第三方嵌入式文件发起合同 \
    --FlowInfo.FlowDescription  \
    --FlowInfo.Deadline 0 \
    --FlowInfo.Unordered False \
    --FlowInfo.IntelligentStatus CLOSE \
    --FlowInfo.NeedCreateReview False \
    --FlowInfo.NeedSignReview False \
    --FlowInfo.UserData  \
    --FlowOption.CanEditFlow True \
    --FlowOption.HideShowFlowName False \
    --FlowOption.HideShowFlowType False \
    --FlowOption.HideShowDeadline False \
    --FlowOption.ForbidEditFillComponent False \
    --FlowOption.CustomCreateFlowDescription  \
    --FlowApproverList.0.ApproverType 0 \
    --FlowApproverList.0.NotChannelOrganization False \
    --FlowApproverList.0.OrganizationOpenId org_dianziqian \
    --FlowApproverList.0.OrganizationName 典子谦示例企业 \
    --FlowApproverList.0.OpenId n131517 \
    --FlowApproverList.0.ApproverOption.CanEditApprover True \
    --FlowApproverList.0.IsFullText True \
    --FlowApproverList.0.PreReadTime 0 \
    --FlowApproverList.1.ApproverType 1 \
    --FlowApproverList.1.ApproverIdCardType  \
    --FlowApproverList.1.ApproverName 里斯 \
    --FlowApproverList.1.NotChannelOrganization False \
    --FlowApproverList.1.ApproverMobile 13312312312 \
    --FlowApproverList.1.IsFullText True \
    --FlowApproverList.1.PreReadTime 0
```

Output: 
```
{
    "Response": {
        "PrepareFlowUrl": "https://embed.beta.qian.tencent.cn/contract-create?embed=1&expiredOn=1700819911&code=yDSL6UUQEjIKK&businessId=yDSL6U3iY7&channel=PROXYCHANNEL&operateSource=byTemplate&themeId=channel_web_theme_yDwi3UAR2Yb",
        "PreviewFlowUrl": "",
        "RequestId": "c52aaa17-3f81-4640-be03-fca0a553d2e3"
    }
}
```

**Example 2: 创建发起合同签署链接-模板发起**

创建发起合同签署链接， 提前定义两个签署人， 分别是 B端渠道子客企业的员工和C端为张三这个自然人

Input: 

```
tccli essbasic ChannelCreatePrepareFlow --cli-unfold-argument  \
    --ResourceId yDSL6UUckpo6ynynUx47m3cSKQavf88Q \
    --ResourceType 1 \
    --FlowInfo.FlowName 典子谦入职合同(17:53:30) \
    --FlowInfo.FlowType 入职合同 \
    --FlowInfo.FlowDescription 2024典子谦入职合同 \
    --FlowInfo.Deadline 1701679610 \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId 110101200610116558 \
    --FlowApproverList.0.NotChannelOrganization False \
    --FlowApproverList.0.OrganizationOpenId org_dianziqian \
    --FlowApproverList.0.OrganizationName 典子谦示例企业 \
    --FlowApproverList.0.OpenId n131517 \
    --FlowApproverList.0.RecipientId yDSL6UUckpo6am9jUuRHYOWRfZbRAhm6 \
    --FlowApproverList.1.ApproverType 1 \
    --FlowApproverList.1.NotChannelOrganization False \
    --FlowApproverList.1.ApproverName 张三 \
    --FlowApproverList.1.ApproverMobile 1850000000 \
    --FlowApproverList.1.RecipientId yDSL6UUckpo6am9qUuRHYOWwmX5rZGCX
```

Output: 
```
{
    "Response": {
        "PrepareFlowUrl": "https://embed.beta.qian.tencent.cn/contract-create?embed=1&expiredOn=1700819911&code=yDSL6UUQEjIKK&businessId=yDSL6U3iY7&channel=PROXYCHANNEL&operateSource=byTemplate&themeId=channel_web_theme_yDwi3UAR2Yb",
        "PreviewFlowUrl": "",
        "RequestId": "c52aaa17-3f81-4640-be03-fca0a553d2e3"
    }
}
```

