**Example 1: 创建发起合同签署链接-模板发起（固定一个参与方）**

1.这是一个B2C的合同模板， 创建发起合同签署链接，只指定一个子企业的参与方
2.FlowApproverList参数指定的参与方不能更改， 未指定的参与方可以修改
<img src="https://qcloudimg.tencent-cloud.cn/raw/f51c3d969db0093300094a22c6c01555.png" />


Input: 

```
tccli essbasic ChannelCreatePrepareFlow --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId zhansan \
    --ResourceId yDSL6UUckpo6ynynUx47m3cSKQavf88Q \
    --ResourceType 1 \
    --FlowInfo.FlowName 2024典子谦入职合同 \
    --FlowInfo.FlowType 入职合同 \
    --FlowInfo.FlowDescription 2024典子谦入职合同 \
    --FlowInfo.Deadline 1706335491 \
    --FlowInfo.Approvers.0.NotChannelOrganization False \
    --FlowInfo.Approvers.0.ApproverType 0 \
    --FlowInfo.Approvers.0.OrganizationOpenId org_dianziqian \
    --FlowInfo.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowInfo.Approvers.0.OpenId n9527 \
    --FlowInfo.Approvers.0.RecipientId yDSL6UUckpo6am9jUuRHYOWRfZbRAhm6
```

Output: 
```
{
    "Response": {
        "PrepareFlowUrl": "https://embed.beta.qian.tencent.cn/contract-create?code=yDCNBUUckpvlzt0sUypjGZRCTkEHyRh6",
        "PreviewFlowUrl": "",
        "FlowId": "yDC54UUckpyr7yh4UEfZcRRy3XMQvLvT",
        "RequestId": "296e3cfb-504e-494d-a86c-75101a87c09e"
    }
}
```

**Example 2: 创建B2C（本方企业对个人）发起合同链接-模板发起**

1.创建一份使用目模板的B2C合同发起链接,签署人分别是子客签署方典子谦示例企业员工和个人张三。
2.模板【yDSL6UUckpo6ynynUx47m3cSKQavf88Q】是B2C 模板,并且模板配置如下![img](https://qcloudimg.tencent-cloud.cn/raw/04ec6aadb113d87b65baccfadb9b7a36.png)
3.FlowApproverList参数指定的参与方数量和配置需要跟模板保持一致，包括下列几点。
3.1 签署人数量需要和模板保持一致。
3.2 本方子客签署人  OpenId、OrganizationName、OrganizationOpenId必传 ,ApproverType设置为0， RecipientId 需要跟模板中的保持一致。可从接口[DescribeTemplates](https://qian.tencent.com/developers/partnerApis/templates/DescribeTemplates)得到。
3.3 个人签署方  Name、Mobile必传, ApproverType设置为1 
效果如下图所示。
<img src="https://qcloudimg.tencent-cloud.cn/raw/935a3cebf2881b25c1d87e234a303a13.png" />


Input: 

```
tccli essbasic ChannelCreatePrepareFlow --cli-unfold-argument  \
    --ResourceId yDSL6UUckpo6ynynUx47m3cSKQavf88Q \
    --ResourceType 1 \
    --FlowInfo.FlowName 典子谦入职合同(17:53:30) \
    --FlowInfo.FlowType 入职合同 \
    --FlowInfo.FlowDescription 2024典子谦入职合同 \
    --FlowInfo.Deadline 1701679610 \
    --FlowInfo.Approvers.0.ApproverType 0 \
    --FlowInfo.Approvers.0.NotChannelOrganization False \
    --FlowInfo.Approvers.0.OrganizationOpenId org_dianziqian \
    --FlowInfo.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowInfo.Approvers.0.OpenId n131517 \
    --FlowInfo.Approvers.0.RecipientId yDSL6UUckpo6am9jUuRHYOWRfZbRAhm6 \
    --FlowInfo.Approvers.1.ApproverType 1 \
    --FlowInfo.Approvers.1.ApproverName 张三 \
    --FlowInfo.Approvers.1.ApproverMobile 1850000000 \
    --FlowInfo.Approvers.1.RecipientId yDSL6UUckpo6am9qUuRHYOWwmX5rZGCX \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId 110101200610116558
```

Output: 
```
{
    "Response": {
        "PrepareFlowUrl": "https://embed.beta.qian.tencent.cn/contract-create?embed=1&expiredOn=1700819911&code=yDSL6UUQEjIKK&businessId=yDSL6U3iY7&channel=PROXYCHANNEL&operateSource=byTemplate&themeId=channel_web_theme_yDwi3UAR2Yb",
        "PreviewFlowUrl": "",
        "FlowId": "yDC54UUckpyr7yh4UEfZcRRy3XMQvLvT",
        "RequestId": "c52aaa17-3f81-4640-be03-fca0a553d2e3"
    }
}
```

**Example 3: 文件发起-跳过文件上传**



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
    --FlowInfo.FlowDescription 合同 \
    --FlowInfo.Deadline 0 \
    --FlowInfo.Approvers.0.ApproverType 0 \
    --FlowInfo.Approvers.0.NotChannelOrganization False \
    --FlowInfo.Approvers.0.OrganizationOpenId org_dianziqian \
    --FlowInfo.Approvers.0.OrganizationName 典子谦示例企业 \
    --FlowInfo.Approvers.0.OpenId n131517 \
    --FlowInfo.Approvers.0.ApproverOption.CanEditApprover True \
    --FlowInfo.Approvers.0.IsFullText True \
    --FlowInfo.Approvers.0.PreReadTime 0 \
    --FlowInfo.Approvers.1.ApproverType 1 \
    --FlowInfo.Approvers.1.ApproverIdCardType  \
    --FlowInfo.Approvers.1.ApproverName 里斯 \
    --FlowInfo.Approvers.1.NotChannelOrganization False \
    --FlowInfo.Approvers.1.ApproverMobile 13312312312 \
    --FlowInfo.Approvers.1.IsFullText True \
    --FlowInfo.Approvers.1.PreReadTime 0 \
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
    --FlowOption.SkipUploadFile True \
    --FlowOption.CustomCreateFlowDescription 
```

Output: 
```
{
    "Response": {
        "PrepareFlowUrl": "https://embed.beta.qian.tencent.cn/contract-create?embed=1&expiredOn=1700819911&code=yDSL6UUQEjIKK&businessId=yDSL6U3iY7&channel=PROXYCHANNEL&operateSource=byTemplate&themeId=channel_web_theme_yDwi3UAR2Yb",
        "PreviewFlowUrl": "",
        "FlowId": "yDC54UUckpyr7yh4UEfZcRRy3XMQvLvT",
        "RequestId": "c52aaa17-3f81-4640-be03-fca0a553d2e3"
    }
}
```

