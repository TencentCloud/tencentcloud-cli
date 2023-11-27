**Example 1: 创建发起合同签署链接**

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

