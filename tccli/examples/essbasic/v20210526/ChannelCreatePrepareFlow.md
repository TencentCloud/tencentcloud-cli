**Example 1: 创建预发起合同链接**

创建预发起合同链接-BBC

Input: 

```
tccli essbasic ChannelCreatePrepareFlow --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId test-open_org_id \
    --Agent.AppId test-channel_app_id \
    --ResourceId test_resource_id \
    --ResourceType 1 \
    --FlowInfo.FlowName 无序BBC发起填写全部无法编辑 \
    --FlowInfo.NeedSignReview True \
    --FlowInfo.FlowType 快速生成创建合同链接 \
    --FlowInfo.FlowDescription 无序BBC发起填写全部无法编辑 \
    --FlowInfo.Deadline 1708497660 \
    --FlowInfo.FormFields.0.ComponentId ComponentId_16 \
    --FlowInfo.FormFields.0.ComponentName 单行文本 \
    --FlowInfo.FormFields.0.ComponentValue 单行文本 \
    --FlowOption.CanEditFlow False \
    --FlowApproverList.0.ApproverType 0 \
    --FlowApproverList.0.OrganizationId  \
    --FlowApproverList.0.OrganizationOpenId test-open_org_id \
    --FlowApproverList.0.OrganizationName test百货-子公司 \
    --FlowApproverList.0.UserId  \
    --FlowApproverList.0.OpenId testOpenId \
    --FlowApproverList.0.ApproverName  \
    --FlowApproverList.0.ApproverMobile  \
    --FlowApproverList.0.RecipientId yDw9XUUgyg3ervqtUrQhCRCfEBQfKtBx \
    --FlowApproverList.0.PreReadTime 300 \
    --FlowApproverList.0.IsFullText True \
    --FlowApproverList.0.NotifyType  \
    --FlowApproverList.0.ApproverOption.CanEditApprover False \
    --FlowApproverList.0.NotChannelOrganization False \
    --FlowApproverList.1.ApproverType 0 \
    --FlowApproverList.1.OrganizationId  \
    --FlowApproverList.1.OrganizationOpenId  \
    --FlowApproverList.1.OrganizationName 测试SAAS企业 \
    --FlowApproverList.1.UserId  \
    --FlowApproverList.1.OpenId  \
    --FlowApproverList.1.ApproverName 张三 \
    --FlowApproverList.1.ApproverMobile 18888888888 \
    --FlowApproverList.1.RecipientId yDw9XUUgyg3ervqkUrQhCRur6kMcOYn0 \
    --FlowApproverList.1.PreReadTime 10 \
    --FlowApproverList.1.IsFullText True \
    --FlowApproverList.1.NotifyType  \
    --FlowApproverList.1.ApproverOption.CanEditApprover False \
    --FlowApproverList.1.NotChannelOrganization True \
    --FlowApproverList.2.ApproverType 1 \
    --FlowApproverList.2.OrganizationId  \
    --FlowApproverList.2.OrganizationOpenId  \
    --FlowApproverList.2.OrganizationName  \
    --FlowApproverList.2.UserId  \
    --FlowApproverList.2.OpenId  \
    --FlowApproverList.2.ApproverName 李四 \
    --FlowApproverList.2.ApproverMobile 15555555555 \
    --FlowApproverList.2.RecipientId yDw9XUUgyg3ervq1UrQhCRyWnKMeua1Z \
    --FlowApproverList.2.PreReadTime 10 \
    --FlowApproverList.2.IsFullText True \
    --FlowApproverList.2.NotifyType  \
    --FlowApproverList.2.ApproverOption.CanEditApprover False \
    --FlowApproverList.2.NotChannelOrganization True
```

Output: 
```
{
    "Response": {
        "PrepareFlowUrl": "https://test.ess.tencent.cn/new-contract-create/template/channel?embed=1&expiredOn=1678073737&code=yDwn2UUgygkpxtidUy5ozz8jhVMwzQNQ&businessId=yDwn2UUgygkpxtigUy5ozzEd7YgDtJTZ&byTemplate=template&channel=PROXYCHANNEL&themeId=channel_web_theme_d69192f65cf1e0da4fcd8024ea34afa5",
        "PreviewFlowUrl": "",
        "RequestId": "s1678073437432767156"
    }
}
```

