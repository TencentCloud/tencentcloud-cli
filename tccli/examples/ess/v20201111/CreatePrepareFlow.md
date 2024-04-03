**Example 1: 创建签署流程**

通过文件发起，无序，b2c，开启智能填写区

Input: 

```
tccli ess CreatePrepareFlow --cli-unfold-argument  \
    --Operator.UserId yDRSsUxxxxxxxxxxxxxxxxxLdSu \
    --Unordered True \
    --IntelligentStatus OPEN \
    --FlowName 文件发起-嵌入式合同 \
    --Deadline 1791859333 \
    --ResourceId yDR0xxxxxxxxxxxxxxxxxxxEYm \
    --ResourceType 2 \
    --UserFlowTypeId  \
    --FlowType 嵌入式文件发起合同 \
    --UserData  \
    --FlowId  \
    --InitiatorComponents.0.ComponentPosX 160 \
    --InitiatorComponents.0.ComponentPosY 760 \
    --InitiatorComponents.0.ComponentHeight 30 \
    --InitiatorComponents.0.ComponentWidth 300 \
    --InitiatorComponents.0.FileIndex 0 \
    --InitiatorComponents.0.ComponentType TEXT \
    --InitiatorComponents.0.ComponentValue 这是发起填写控件{{ @now }} \
    --InitiatorComponents.0.LockComponentValue True \
    --InitiatorComponents.0.ForbidMoveAndDelete True \
    --InitiatorComponents.0.ComponentRequired True \
    --InitiatorComponents.0.ComponentPage 1 \
    --FlowOption.CanEditFlow False \
    --FlowOption.CanEditFormField True \
    --FlowOption.HideShowFlowName True \
    --FlowOption.HideShowFlowType True \
    --FlowOption.HideShowDeadline True \
    --FlowOption.CanSkipAddApprover True \
    --FlowOption.SkipUploadFile True \
    --FlowOption.ForbidEditFillComponent True \
    --FlowOption.CustomCreateFlowDescription  \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.Required True \
    --Approvers.0.ApproverOption.NoRefuse True \
    --Approvers.0.ApproverOption.NoTransfer True \
    --Approvers.0.ApproverOption.CanEditApprover True \
    --Approvers.0.ApproverVerifyTypes 1 2 \
    --Approvers.0.ApproverSignTypes 1 2 \
    --Approvers.0.Components.0.ComponentPosX 160 \
    --Approvers.0.Components.0.ComponentPosY 560 \
    --Approvers.0.Components.0.ComponentHeight 30 \
    --Approvers.0.Components.0.ComponentWidth 300 \
    --Approvers.0.Components.0.FileIndex 0 \
    --Approvers.0.Components.0.ComponentType TEXT \
    --Approvers.0.Components.0.ComponentValue 这是第一个签署人的填写控件{{ @now }} \
    --Approvers.0.Components.0.LockComponentValue True \
    --Approvers.0.Components.0.ForbidMoveAndDelete True \
    --Approvers.0.Components.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 160 \
    --Approvers.0.SignComponents.0.ComponentPosY 360 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.0.SignComponents.0.ForbidMoveAndDelete True \
    --Approvers.0.SignComponents.0.ComponentValue  \
    --Approvers.0.SignComponents.0.LockComponentValue True \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.IsFullText True \
    --Approvers.1.ApproverType 0 \
    --Approvers.1.OrganizationName 典子谦示例企业 \
    --Approvers.1.ApproverName 典子谦 \
    --Approvers.1.ApproverMobile 13200000001 \
    --Approvers.1.PreReadTime 3 \
    --Approvers.1.Required True \
    --Approvers.1.Components.0.ComponentPosX 160 \
    --Approvers.1.Components.0.ComponentPosY 660 \
    --Approvers.1.Components.0.ComponentHeight 30 \
    --Approvers.1.Components.0.ComponentWidth 300 \
    --Approvers.1.Components.0.FileIndex 0 \
    --Approvers.1.Components.0.ComponentType TEXT \
    --Approvers.1.Components.0.ComponentValue 这是第二个签署人的填写控件 \
    --Approvers.1.Components.0.LockComponentValue True \
    --Approvers.1.Components.0.ForbidMoveAndDelete True \
    --Approvers.1.Components.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 160 \
    --Approvers.1.SignComponents.0.ComponentPosY 260 \
    --Approvers.1.SignComponents.0.ComponentWidth 100 \
    --Approvers.1.SignComponents.0.ComponentHeight 100 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.1.SignComponents.0.ForbidMoveAndDelete True \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.IsFullText True
```

Output: 
```
{
    "Response": {
        "RequestId": "s1692004929990936987",
        "Url": "https://embed.beta.qian.tencent.cn/contract-create?embed=1&expiredOn=1692005230&code=yDwqmxxxxxxxxxxxxxKaLJfQEGm&businessId=yDwqmUUxxxxxxxxxDAgN4fKi&channel=TENCENTCLOUD&operateSource=byFile&themeId=saas_web_theme_732aaefa78c439d726f541b89c49e022"
    }
}
```

**Example 2: 通过模板发起嵌入式url**

模板发起，b2c

Input: 

```
tccli ess CreatePrepareFlow --cli-unfold-argument  \
    --Operator.UserId yDRSsUxxxxxxxxxxxxxxxxxLdSu \
    --Unordered True \
    --IntelligentStatus open \
    --FlowName 模板发起-嵌入式合同 \
    --Deadline 1991859333 \
    --ResourceId yDwXXUUckxxxxxxxxxx4S7NM8r \
    --ResourceType 1 \
    --UserFlowTypeId  \
    --FlowType  \
    --UserData  \
    --FlowOption.CanEditFlow False \
    --FlowOption.CanEditFormField True \
    --FlowOption.HideShowFlowName True \
    --FlowOption.HideShowFlowType True \
    --FlowOption.HideShowDeadline True \
    --FlowOption.CanSkipAddApprover True \
    --FlowOption.SkipUploadFile True \
    --FlowOption.ForbidEditFillComponent True \
    --FlowOption.CustomCreateFlowDescription  \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.Required True \
    --Approvers.0.RecipientId yDwXXxxxxxxxxxxxxxxOZbdgN6 \
    --Approvers.0.ApproverOption.NoRefuse True \
    --Approvers.0.ApproverOption.NoTransfer True \
    --Approvers.0.ApproverOption.CanEditApprover True \
    --Approvers.0.ApproverVerifyTypes 1 2 \
    --Approvers.0.ApproverSignTypes 1 2 \
    --Approvers.0.IsFullText True \
    --Approvers.1.ApproverType 0 \
    --Approvers.1.OrganizationName 典子谦示例企业 \
    --Approvers.1.ApproverName 典子谦 \
    --Approvers.1.ApproverMobile 13200000001 \
    --Approvers.1.PreReadTime 3 \
    --Approvers.1.Required True \
    --Approvers.1.RecipientId yDwXXUUxxxxxxxxxxxxxxO1XEwdCTnI \
    --Approvers.1.IsFullText True
```

Output: 
```
{
    "Response": {
        "RequestId": "s1692004929990936987",
        "Url": "https://embed.beta.qian.tencent.cn/contract-create?embed=1&expiredOn=1692005230&code=yDwqmxxxxxxxxxxxxxKaLJfQEGm&businessId=yDwqmUUxxxxxxxxxDAgN4fKi&channel=TENCENTCLOUD&operateSource=byFile&themeId=saas_web_theme_732aaefa78c439d726f541b89c49e022"
    }
}
```

**Example 3: 通过模板发起待签署审核**



Input: 

```
tccli ess CreatePrepareFlow --cli-unfold-argument  \
    --Operator.UserId yDRSsUxxxxxxxxxxxxxxxxxLdSu \
    --Unordered True \
    --IntelligentStatus open \
    --FlowName 模板发起-嵌入式合同 \
    --Deadline 1991859333 \
    --ResourceId yDwXXUUckxxxxxxxxxx4S7NM8r \
    --ResourceType 1 \
    --NeedCreateReview True \
    --FlowType  \
    --UserData  \
    --FlowOption.CanEditFlow False \
    --FlowOption.CanEditFormField True \
    --FlowOption.HideShowFlowName True \
    --FlowOption.HideShowFlowType True \
    --FlowOption.HideShowDeadline True \
    --FlowOption.CanSkipAddApprover True \
    --FlowOption.SkipUploadFile True \
    --FlowOption.ForbidEditFillComponent True \
    --FlowOption.CustomCreateFlowDescription  \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.Required True \
    --Approvers.0.RecipientId yDwXXxxxxxxxxxxxxxxOZbdgN6 \
    --Approvers.0.ApproverOption.NoRefuse True \
    --Approvers.0.ApproverOption.NoTransfer True \
    --Approvers.0.ApproverOption.CanEditApprover True \
    --Approvers.0.ApproverVerifyTypes 1 2 \
    --Approvers.0.ApproverSignTypes 1 2 \
    --Approvers.0.IsFullText True \
    --Approvers.1.ApproverType 0 \
    --Approvers.1.OrganizationName 典子谦示例企业 \
    --Approvers.1.ApproverName 典子谦 \
    --Approvers.1.ApproverMobile 13200000001 \
    --Approvers.1.PreReadTime 3 \
    --Approvers.1.Required True \
    --Approvers.1.RecipientId yDwXXUUxxxxxxxxxxxxxxO1XEwdCTnI \
    --Approvers.1.IsFullText True
```

Output: 
```
{
    "Response": {
        "RequestId": "s1692004929990936987",
        "Url": "https://embed.beta.qian.tencent.cn/contract-create?embed=1&expiredOn=1692005230&code=yDwqmxxxxxxxxxxxxxKaLJfQEGm&businessId=yDwqmUUxxxxxxxxxDAgN4fKi&channel=TENCENTCLOUD&operateSource=byFile&themeId=saas_web_theme_732aaefa78c439d726f541b89c49e022"
    }
}
```

**Example 4: 文件发起，设置跳过上传文件，必须要传资源id**



Input: 

```
tccli ess CreatePrepareFlow --cli-unfold-argument  \
    --Operator.UserId yDRSsUxxxxxxxxxxxxxxxxxLdSu \
    --Unordered True \
    --IntelligentStatus OPEN \
    --FlowName 文件发起-嵌入式合同 \
    --Deadline 1791859333 \
    --ResourceId  \
    --ResourceType 2 \
    --UserFlowTypeId  \
    --FlowType 嵌入式文件发起合同 \
    --UserData  \
    --FlowId  \
    --FlowOption.CanEditFlow False \
    --FlowOption.CanEditFormField True \
    --FlowOption.HideShowFlowName True \
    --FlowOption.HideShowFlowType True \
    --FlowOption.HideShowDeadline True \
    --FlowOption.CanSkipAddApprover True \
    --FlowOption.SkipUploadFile True \
    --FlowOption.ForbidEditFillComponent True \
    --FlowOption.CustomCreateFlowDescription  \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.Required True \
    --Approvers.0.ApproverOption.NoRefuse True \
    --Approvers.0.ApproverOption.NoTransfer True \
    --Approvers.0.ApproverOption.CanEditApprover True \
    --Approvers.0.ApproverVerifyTypes 1 2 \
    --Approvers.0.ApproverSignTypes 1 2 \
    --Approvers.0.Components.0.ComponentPosX 160 \
    --Approvers.0.Components.0.ComponentPosY 560 \
    --Approvers.0.Components.0.ComponentHeight 30 \
    --Approvers.0.Components.0.ComponentWidth 300 \
    --Approvers.0.Components.0.FileIndex 0 \
    --Approvers.0.Components.0.ComponentType TEXT \
    --Approvers.0.Components.0.ComponentValue 这是第一个签署人的填写控件{{ @now }} \
    --Approvers.0.Components.0.LockComponentValue True \
    --Approvers.0.Components.0.ForbidMoveAndDelete True \
    --Approvers.0.Components.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 160 \
    --Approvers.0.SignComponents.0.ComponentPosY 360 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.0.SignComponents.0.ForbidMoveAndDelete True \
    --Approvers.0.SignComponents.0.ComponentValue  \
    --Approvers.0.SignComponents.0.LockComponentValue True \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.IsFullText True \
    --Approvers.1.ApproverType 0 \
    --Approvers.1.OrganizationName 典子谦示例企业 \
    --Approvers.1.ApproverName 典子谦 \
    --Approvers.1.ApproverMobile 13200000001 \
    --Approvers.1.PreReadTime 3 \
    --Approvers.1.Required True \
    --Approvers.1.Components.0.ComponentPosX 160 \
    --Approvers.1.Components.0.ComponentPosY 660 \
    --Approvers.1.Components.0.ComponentHeight 30 \
    --Approvers.1.Components.0.ComponentWidth 300 \
    --Approvers.1.Components.0.FileIndex 0 \
    --Approvers.1.Components.0.ComponentType TEXT \
    --Approvers.1.Components.0.ComponentValue 这是第二个签署人的填写控件 \
    --Approvers.1.Components.0.LockComponentValue True \
    --Approvers.1.Components.0.ForbidMoveAndDelete True \
    --Approvers.1.Components.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 160 \
    --Approvers.1.SignComponents.0.ComponentPosY 260 \
    --Approvers.1.SignComponents.0.ComponentWidth 100 \
    --Approvers.1.SignComponents.0.ComponentHeight 100 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.1.SignComponents.0.ForbidMoveAndDelete True \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.IsFullText True
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue",
            "Message": "请指定文件类型的资源id"
        },
        "RequestId": "s1694764534616690016"
    }
}
```

