**Example 1: 文件发起嵌入式合同组**



Input: 

```
tccli ess CreatePrepareFlowGroup --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --FlowGroupInfos.0.FileIds yDCWiUUckpv6iggyUyuqIrwyppQVS7TR \
    --FlowGroupInfos.0.FlowName 预发起合同 \
    --FlowGroupInfos.0.FlowType 嵌入式文件发起合同 \
    --FlowGroupInfos.0.FlowDescription 这是2025年购买食物的合同 \
    --FlowGroupInfos.0.Deadline 1757034793 \
    --FlowGroupInfos.0.Unordered False \
    --FlowGroupInfos.0.NeedSignReview False \
    --FlowGroupInfos.0.UserData  \
    --FlowGroupInfos.0.Approvers.0.ApproverType 1 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName  \
    --FlowGroupInfos.0.Approvers.0.ApproverName 典子签 \
    --FlowGroupInfos.0.Approvers.0.ApproverOption.CanEditApprover True \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 18700000000 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ChannelComponentId  \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ChannelComponentSource 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentDateFontSize 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentExtra  \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentId  \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentName  \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPage 3 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosX 160 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosY 360 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentRecipientId  \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentRequired False \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ForbidMoveAndDelete True \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.GenerateMode  \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.IsFormType False \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.KeywordOrder  \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.KeywordPage 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.LockComponentValue False \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.OffsetX 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.OffsetY 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.RelativeLocation  \
    --FlowGroupName group \
    --ResourceType 2
```

Output: 
```
{
    "Response": {
        "FlowGroupId": "yDttAUUckpxbcziqUySqdD5Eugn0LPHo",
        "RequestId": "s1747034803503801327",
        "PrepareUrl": "https://embed.test.qian.tencent.cn/contract-create?embed=1&expiredOn=1747035103&code=yDttAUUckpxbcHI&businessId=yDttAUUckpxbcziqUySqdD5o&channel=TENCENTCLOUD&operateSource=byFileGroup&themeId=saas_web_theme_yDhk9nE0qLixm"
    }
}
```

