**Example 1: 嵌入式文件发起合同组**



Input: 

```
tccli essbasic ChannelCreatePrepareFlowGroup --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId kevinlcheng_open_organization_1 \
    --Agent.ProxyOperator.OpenId kevinlcheng_1 \
    --FlowGroupName group \
    --ResourceType 2 \
    --BaseFlowInfos.0.FlowName 第三方预发起合同 \
    --BaseFlowInfos.0.FlowType 第三方嵌入式文件发起合同 \
    --BaseFlowInfos.0.FileIds yDCWiUUckpv6iggyUyuqIrwyppQVS7TR \
    --BaseFlowInfos.0.FlowDescription 描述 \
    --BaseFlowInfos.0.Deadline 1757034793 \
    --BaseFlowInfos.0.Unordered False \
    --BaseFlowInfos.0.IntelligentStatus CLOSE \
    --BaseFlowInfos.0.NeedCreateReview False \
    --BaseFlowInfos.0.NeedSignReview False \
    --BaseFlowInfos.0.UserData  \
    --BaseFlowInfos.0.Approvers.0.ApproverType 1 \
    --BaseFlowInfos.0.Approvers.0.OrganizationName  \
    --BaseFlowInfos.0.Approvers.0.NotChannelOrganization False \
    --BaseFlowInfos.0.Approvers.0.ApproverName 张轩 \
    --BaseFlowInfos.0.Approvers.0.ApproverOption.CanEditApprover True \
    --BaseFlowInfos.0.Approvers.0.IsFullText True \
    --BaseFlowInfos.0.Approvers.0.ApproverMobile 18729585347 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ChannelComponentId  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentDateFontSize 0 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentDescription  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentExtra  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentId  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentName  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentPage 3 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentPosX 160 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentPosY 360 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentRecipientId  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentRequired False \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentValue  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.DocumentId  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.FileIndex 0 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.ForbidMoveAndDelete True \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.GenerateMode  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.KeywordOrder  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.KeywordPage 0 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.LockComponentValue False \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.OffsetX 0 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.OffsetY 0 \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.Placeholder  \
    --BaseFlowInfos.0.Approvers.0.SignComponents.0.RelativeLocation 
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDttAUUckpxbcz9uUySqdD58t8bwneLp",
        "PrepareUrl": "https://embed.test.qian.tencent.cn/contract-create?embed=1&expiredOn=1747036582&code=yDttAUUckpxbcz9vUySqdD5u3jnsKVT6&businessId=yDttAUUckpxbcz9uUySqdD58t8bwneLp&channel=PROXYCHANNEL&operateSource=byFileGroup&themeId=channel_web_theme_yDSLbUUckpo3e14eUEK7ajSyPX7g3kIc",
        "RequestId": "s1747036282702037847"
    }
}
```

