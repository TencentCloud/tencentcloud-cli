**Example 1: 合同组**

合同组示例

Input: 

```
tccli ess CreateFlowGroupByFiles --cli-unfold-argument  \
    --Operator.UserId **************** \
    --FlowGroupName 合同组 \
    --FlowGroupInfos.0.FileIds ************* \
    --FlowGroupInfos.0.FlowName B2B手动签署合同 \
    --FlowGroupInfos.0.FlowType 合同组 \
    --FlowGroupInfos.0.FlowDescription B2B手动签署合同 \
    --FlowGroupInfos.0.Deadline 0 \
    --FlowGroupInfos.0.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.0.OrganizationName 企业公司名称 \
    --FlowGroupInfos.0.Approvers.0.ApproverName 企业方签署人姓名 \
    --FlowGroupInfos.0.Approvers.0.ApproverMobile 企业方签署人手机号 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.0.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.0.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.0.Approvers.1.OrganizationName 企业公司名称 \
    --FlowGroupInfos.0.Approvers.1.ApproverName 企业方签署人姓名 \
    --FlowGroupInfos.0.Approvers.1.ApproverMobile 企业方签署人手机号 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.0.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.0.Approvers.1.NotifyType SMS \
    --FlowGroupInfos.0.CallbackUrl  \
    --FlowGroupInfos.1.FileIds ************ \
    --FlowGroupInfos.1.FlowName 公司自动签 \
    --FlowGroupInfos.1.FlowType 合同组 \
    --FlowGroupInfos.1.FlowDescription 公司自动签 \
    --FlowGroupInfos.1.Deadline 0 \
    --FlowGroupInfos.1.Approvers.0.ApproverType 3 \
    --FlowGroupInfos.1.Approvers.0.OrganizationName 发起方公司名称 \
    --FlowGroupInfos.1.Approvers.0.ApproverName 发起人姓名 \
    --FlowGroupInfos.1.Approvers.0.ApproverMobile 发起人手机号 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.1.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.1.Approvers.0.NotifyType SMS \
    --FlowGroupInfos.1.Approvers.1.ApproverType 0 \
    --FlowGroupInfos.1.Approvers.1.OrganizationName 企业公司名称 \
    --FlowGroupInfos.1.Approvers.1.ApproverName 企业签署人姓名 \
    --FlowGroupInfos.1.Approvers.1.ApproverMobile 企业签署人手机号 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.1.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.1.Approvers.1.NotifyType SMS \
    --FlowGroupInfos.1.CallbackUrl  \
    --FlowGroupInfos.2.FileIds ************** \
    --FlowGroupInfos.2.FlowName B2C发起 \
    --FlowGroupInfos.2.FlowType 合同组 \
    --FlowGroupInfos.2.FlowDescription B2C发起 \
    --FlowGroupInfos.2.Deadline 0 \
    --FlowGroupInfos.2.Approvers.0.ApproverType 0 \
    --FlowGroupInfos.2.Approvers.0.OrganizationName 企业签署方公司名称 \
    --FlowGroupInfos.2.Approvers.0.ApproverName 企业签署方姓名 \
    --FlowGroupInfos.2.Approvers.0.ApproverMobile 企业签署方手机号 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentPosY 100 \
    --FlowGroupInfos.2.Approvers.0.SignComponents.0.ComponentValue  \
    --FlowGroupInfos.2.Approvers.0.NotifyType SMS \
    --FlowGroupInfos.2.Approvers.1.ApproverType 1 \
    --FlowGroupInfos.2.Approvers.1.ApproverName 个人签署方姓名 \
    --FlowGroupInfos.2.Approvers.1.ApproverMobile 个人签署方手机号 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentRequired True \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.FileIndex 0 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentHeight 100 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentWidth 100 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPage 1 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPosX 100 \
    --FlowGroupInfos.2.Approvers.1.SignComponents.0.ComponentPosY 200 \
    --FlowGroupInfos.2.Approvers.1.NotifyType SMS \
    --FlowGroupInfos.2.CallbackUrl 
```

Output: 
```
{
    "Response": {
        "RequestId": "6ee9f545-96d8-4f3b-b382-917dc17089f4"
    }
}
```

