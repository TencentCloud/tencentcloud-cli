**Example 1: 使用文件创建签署流程**

使用文件创建签署流程

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --FlowName name \
    --Agent.ProxyOrganizationOpenId id \
    --Agent.ProxyOperator.OpenId id \
    --Agent.AppId id \
    --CustomShowMap 合同名称:{合同名称} {发起方企业} {发起方姓名};国家:中国;发起方:{发起方企业};签署方1:  {签署方1企业};签署方2:  {签署方2企业}{签署方2姓名};签署方3:  {签署方3姓名} \
    --FlowApprovers.0.OpenId id \
    --FlowApprovers.0.OrganizationName name \
    --FlowApprovers.0.Name name \
    --FlowApprovers.0.ApproverType type \
    --FlowApprovers.0.Mobile mobile \
    --FlowApprovers.0.OrganizationOpenId id \
    --FlowApprovers.0.SignComponents.0.ComponentRecipientId id \
    --FlowApprovers.0.SignComponents.0.ComponentValue test \
    --FlowApprovers.0.SignComponents.0.GenerateMode test \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 0.0 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentName test \
    --FlowApprovers.0.SignComponents.0.ComponentDateFontSize 0 \
    --FlowApprovers.0.SignComponents.0.ComponentExtra test \
    --FlowApprovers.0.SignComponents.0.ComponentType test \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentDescription test \
    --FlowApprovers.0.SignComponents.0.ComponentRequired True \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 0.0 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 0.0 \
    --FlowApprovers.0.SignComponents.0.ComponentId test \
    --FlowApprovers.0.SignComponents.0.DocumentId test \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 0.0 \
    --Components.0.ComponentRecipientId test \
    --Components.0.ComponentValue test \
    --Components.0.GenerateMode test \
    --Components.0.ComponentWidth 0.0 \
    --Components.0.FileIndex 0 \
    --Components.0.ComponentName test \
    --Components.0.ComponentDateFontSize 0 \
    --Components.0.ComponentExtra test \
    --Components.0.ComponentType test \
    --Components.0.ComponentPage 0 \
    --Components.0.ComponentDescription test \
    --Components.0.ComponentRequired True \
    --Components.0.ComponentPosX 0.0 \
    --Components.0.ComponentPosY 0.0 \
    --Components.0.ComponentId test \
    --Components.0.DocumentId test \
    --Components.0.ComponentHeight 0.0 \
    --CallbackUrl test \
    --ApproverVerifyType VerifyCheck \
    --FileIds test
```

Output: 
```
{
    "Response": {
        "FlowId": "id",
        "RequestId": "id"
    }
}
```

