**Example 1: 创建电子签流程**



Input: 

```
tccli ess CreateFlowByFiles --cli-unfold-argument  \
    --Operator.UserId 11910aa00cdded2eb389595ed05f5a7b \
    --Operator.ClientIp  \
    --Operator.Channel  \
    --Operator.OpenId  \
    --Operator.ProxyIp  \
    --FlowName 测试 \
    --FlowDescription 测试流程的描述信息 \
    --Unordered False \
    --FlowType 合同 \
    --Deadline 1604912664 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 腾讯云计算（西安）有限责任公司 \
    --Approvers.0.ApproverName  \
    --Approvers.0.ApproverMobile  \
    --Approvers.0.SignComponents.0.ComponentValue SealId \
    --Approvers.0.SignComponents.0.ComponentPosY 100.0 \
    --Approvers.0.SignComponents.0.ComponentWidth 100.0 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPage 1 \
    --Approvers.0.SignComponents.0.ComponentPosX 100.0 \
    --Approvers.0.SignComponents.0.ComponentHeight 100.0 \
    --Approvers.0.SignComponents.1.ComponentValue  \
    --Approvers.0.SignComponents.1.ComponentPosY 120.0 \
    --Approvers.0.SignComponents.1.ComponentWidth 120.0 \
    --Approvers.0.SignComponents.1.FileIndex 0 \
    --Approvers.0.SignComponents.1.ComponentType SIGN_DATE \
    --Approvers.0.SignComponents.1.ComponentPage 1 \
    --Approvers.0.SignComponents.1.ComponentPosX 120.0 \
    --Approvers.0.SignComponents.1.ComponentHeight 120.0 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.OrganizationName  \
    --Approvers.1.ApproverName 呱呱叫 \
    --Approvers.1.ApproverMobile 185111111111 \
    --Approvers.1.SignComponents.0.ComponentValue  \
    --Approvers.1.SignComponents.0.ComponentPosY 100.0 \
    --Approvers.1.SignComponents.0.ComponentWidth 100.0 \
    --Approvers.1.SignComponents.0.FileIndex 0 \
    --Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.1.SignComponents.0.ComponentPage 1 \
    --Approvers.1.SignComponents.0.ComponentPosX 100.0 \
    --Approvers.1.SignComponents.0.ComponentHeight 100.0 \
    --Approvers.1.SignComponents.1.ComponentValue  \
    --Approvers.1.SignComponents.1.ComponentPosY 120.0 \
    --Approvers.1.SignComponents.1.ComponentWidth 120.0 \
    --Approvers.1.SignComponents.1.FileIndex 0 \
    --Approvers.1.SignComponents.1.ComponentType SIGN_DATE \
    --Approvers.1.SignComponents.1.ComponentPage 1 \
    --Approvers.1.SignComponents.1.ComponentPosX 120.0 \
    --Approvers.1.SignComponents.1.ComponentHeight 120.0 \
    --FileIds ResourceId1 ResourceId2 \
    --Components.0.ComponentValue 自定义单行文本内容 \
    --Components.0.ComponentPosY 100.0 \
    --Components.0.ComponentWidth 100.0 \
    --Components.0.FileIndex 0 \
    --Components.0.ComponentType TEXT \
    --Components.0.ComponentPage 1 \
    --Components.0.ComponentPosX 100.0 \
    --Components.0.ComponentHeight 100.0 \
    --Components.0.ComponentExtra {"FontSize":20} \
    --Components.1.ComponentValue 自定义多行文本内容 \
    --Components.1.ComponentPosY 100.0 \
    --Components.1.ComponentWidth 100.0 \
    --Components.1.FileIndex 0 \
    --Components.1.ComponentType MULTI_LINE_TEXT \
    --Components.1.ComponentPage 1 \
    --Components.1.ComponentPosX 100.0 \
    --Components.1.ComponentHeight 100.0 \
    --Components.1.ComponentExtra {"FontSize":20}
```

Output: 
```
{
    "Response": {
        "FlowId": "429b82b40900a9f870a90d45c715bad7",
        "RequestId": "be3e7fcc21f2714926d2caca4ca5d02c"
    }
}
```

