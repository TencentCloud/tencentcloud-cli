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

**Example 2: 创建含有动态签署人流程，签署方不指定具体的签署人**

创建一个B2C流程，两方签署方不指定具体的签署人
注： 
`1.签署人相关信息为空，如：姓名、手机号码等` 
`2.FillType需传值为1，表示为动态签署人（不确定具体的签署人），需后续进行补充。` 
`3.需保留对应的角色编号，即RecipientId，后续补充具体的签署人时需指定对应的RecipientId`

Input: 

```
tccli essbasic ChannelCreateFlowByFiles --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId zhangsan \
    --Agent.ProxyOrganizationOpenId ess_open_organization_1 \
    --Agent.AppId yDwFoUUckps**********yhWGhIR2RkhOjw2 \
    --Unordered True \
    --FlowName 发起动态签署人合同示例 \
    --FlowApprovers.0.Name  \
    --FlowApprovers.0.Mobile  \
    --FlowApprovers.0.ApproverType PERSON \
    --FlowApprovers.0.ApproverRoleName 个人签署方 \
    --FlowApprovers.0.ApproverOption.FillType 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.0.SignComponents.0.ComponentWidth 100 \
    --FlowApprovers.0.SignComponents.0.FileIndex 0 \
    --FlowApprovers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --FlowApprovers.0.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.0.SignComponents.0.ComponentPosX 260 \
    --FlowApprovers.0.SignComponents.0.ComponentHeight 100 \
    --FlowApprovers.1.ApproverType ORGANIZATION \
    --FlowApprovers.1.ApproverRoleName 企业签署方 \
    --FlowApprovers.1.ApproverOption.FillType 1 \
    --FlowApprovers.1.SignComponents.0.ComponentPosY 260 \
    --FlowApprovers.1.SignComponents.0.ComponentWidth 100 \
    --FlowApprovers.1.SignComponents.0.FileIndex 0 \
    --FlowApprovers.1.SignComponents.0.ComponentType SIGN_SEAL \
    --FlowApprovers.1.SignComponents.0.ComponentPage 1 \
    --FlowApprovers.1.SignComponents.0.ComponentPosX 260 \
    --FlowApprovers.1.SignComponents.0.ComponentHeight 100 \
    --FileIds yDwFhUUckpsxas68UuZf2EREDkOykmDp
```

Output: 
```
{
    "Response": {
        "FlowId": "2fb48c3945****65aaedf6",
        "Approvers": [
            {
                "SignId": "yDw7hUUckpkm57vuUxeFIKavjSsJtcaN",
                "RecipientId": "yDw7hUUckpkm57v4UxeFIKaS5kF2iWh8",
                "ApproverRoleName": "个人签署方"
            },
            {
                "SignId": "yDw7hUUckpkm57v7UxeFIKa8kitjb9XB",
                "RecipientId": "yDw7hUUckpkm57vxUxeFIKaCJX9krcZN",
                "ApproverRoleName": "企业签署方"
            }
        ],
        "RequestId": "s1234345677xxxx"
    }
}
```

