**Example 1: B2C签署，批量补充两方动态签署人信息，子客企业签署人未实名**

在B2C签署中，双方签署方未指定具体签署人时，需要进行补充。 
注:
`补充动态签署人时FillApproverType传值为1 `
`子客企业签署人OpenId未实名的情况下，需要传入签署人姓名和手机号码（ApproverName和ApproverMobile）`

Input: 

```
tccli essbasic ChannelCreateFlowApprovers --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.CustomUserId  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --FlowId 111111***22222 \
    --FillApproverType 1 \
    --Approvers.0.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.OpenId zhangsan \
    --Approvers.0.OrganizationName ***有限公司 \
    --Approvers.0.OrganizationOpenId org_diziqian \
    --Approvers.1.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888
```

Output: 
```
{
    "Response": {
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e"
    }
}
```

**Example 2: B2C签署，补充合同组两方动态签署人信息**

在B2C签署中，双方签署方未指定具体签署人时，需要进行补充。 
注:`补充动态签署人时FillApproverType传值为1 `

Input: 

```
tccli essbasic ChannelCreateFlowApprovers --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.CustomUserId  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --FlowGroupId 111111***22222 \
    --FillApproverType 1 \
    --Approvers.0.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.OrganizationName ***有限公司 \
    --Approvers.0.FlowId yDCVMUUckpwytrk2UE1RW1FSR2BqdoGS \
    --Approvers.1.RecipientId yDCVMUUckpwytrksUE1RW1FRR08t7Lxf \
    --Approvers.1.ApproverName 典子谦 \
    --Approvers.1.ApproverMobile 13200000000 \
    --Approvers.1.OrganizationName ***有限公司 \
    --Approvers.1.FlowId yDC5BUUckpypucutUETpDyAwpDJckfDR
```

Output: 
```
{
    "Response": {
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e"
    }
}
```

**Example 3: B2C签署，批量补充两方动态签署人信息时重复补充报错**

在B2C签署中，双方签署方未指定具体签署人时，需要进行补充。当重复补充同一个签署节点时，会进行部分补充报错。 
注:`补充动态签署人时FillApproverType传值为1 `

Input: 

```
tccli essbasic ChannelCreateFlowApprovers --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.CustomUserId  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --FlowId 111111***22222 \
    --FillApproverType 1 \
    --Approvers.0.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.0.OrganizationName ***有限公司 \
    --Approvers.1.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888
```

Output: 
```
{
    "Response": {
        "FillError": [
            {
                "ErrMessage": "个人信息已补充，请勿重复补充",
                "RecipientId": "yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc"
            }
        ],
        "RequestId": "s1696921563375938822"
    }
}
```

**Example 4: B2C签署，通过姓名和证件类型、证件号码补充已实名个人用户**

通过姓名和证件类型、证件号码补充已实名个人用户

Input: 

```
tccli essbasic ChannelCreateFlowApprovers --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.CustomUserId  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --FlowId 111111***22222 \
    --FillApproverType 1 \
    --Approvers.0.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.0.ApproverName 张三 \
    --Approvers.0.ApproverIdCardType ID_CARD \
    --Approvers.0.ApproverIdCardNumber 620000198802020000
```

Output: 
```
{
    "Response": {
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e"
    }
}
```

**Example 5: B2C签署，批量补充两方动态签署人信息，子客企业签署人已实名**

在B2C签署中，双方签署方未指定具体签署人时，需要进行补充。 
注:
`补充动态签署人时FillApproverType传值为1 `

Input: 

```
tccli essbasic ChannelCreateFlowApprovers --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.CustomUserId  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --FlowId 111111***22222 \
    --FillApproverType 1 \
    --Approvers.0.RecipientId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --Approvers.0.OpenId zhangsan \
    --Approvers.0.OrganizationName ***有限公司 \
    --Approvers.0.OrganizationOpenId org_diziqian \
    --Approvers.1.RecipientId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --Approvers.1.ApproverName 张三 \
    --Approvers.1.ApproverMobile 18888888888
```

Output: 
```
{
    "Response": {
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e"
    }
}
```

