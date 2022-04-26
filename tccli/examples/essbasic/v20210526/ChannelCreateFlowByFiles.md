**Example 1: 使用文件创建流程**



Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --FlowName xx \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.AppId xx \
    --FlowApprovers.0.OpenId xx \
    --FlowApprovers.0.OrganizationName xx \
    --FlowApprovers.0.Name xx \
    --FlowApprovers.0.ApproverType xx \
    --FlowApprovers.0.Mobile xx \
    --FlowApprovers.0.OrganizationOpenId xx \
    --FlowApprovers.0.SignComponents.0.ComponentValue xx \
    --FlowApprovers.0.SignComponents.0.GenerateMode xx \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 0.0 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentName xx \
    --FlowApprovers.0.SignComponents.0.ComponentDateFontSize 0 \
    --FlowApprovers.0.SignComponents.0.ComponentExtra xx \
    --FlowApprovers.0.SignComponents.0.ComponentType xx \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentDescription xx \
    --FlowApprovers.0.SignComponents.0.ComponentRequired True \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 0.0 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 0.0 \
    --FlowApprovers.0.SignComponents.0.ComponentId xx \
    --FlowApprovers.0.SignComponents.0.DocumentId xx \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 0.0 \
    --Components.0.ComponentValue xx \
    --Components.0.GenerateMode xx \
    --Components.0.ComponentWidth 0.0 \
    --Components.0.FileIndex 0 \
    --Components.0.ComponentName xx \
    --Components.0.ComponentDateFontSize 0 \
    --Components.0.ComponentExtra xx \
    --Components.0.ComponentType xx \
    --Components.0.ComponentPage 0 \
    --Components.0.ComponentDescription xx \
    --Components.0.ComponentRequired True \
    --Components.0.ComponentPosX 0.0 \
    --Components.0.ComponentPosY 0.0 \
    --Components.0.ComponentId xx \
    --Components.0.DocumentId xx \
    --Components.0.ComponentHeight 0.0 \
    --CallbackUrl xx \
    --FileIds xx
```

Output: 
```
{
    "Response": {
        "FlowId": "xx",
        "RequestId": "xx"
    }
}
```

