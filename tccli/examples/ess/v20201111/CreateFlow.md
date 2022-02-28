**Example 1: 创建电子签流程。**



Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --Operator.UserId 11910aa00cdded2eb389595ed05f5a7b \
    --Operator.ClientIp  \
    --Operator.Channel  \
    --Operator.OpenId  \
    --Operator.ProxyIp  \
    --FlowName 测试 \
    --FlowDescription 测试流程的描述信息 \
    --Unordered False \
    --FlowType 合同 \
    --DeadLine 1604912664 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 腾讯云计算（西安）有限责任公司 \
    --Approvers.0.Required True \
    --Approvers.0.ApproverName 呱呱叫 \
    --Approvers.0.ApproverMobile 185111111111 \
    --Approvers.0.ApproverIdCardType ID_CARD \
    --Approvers.0.ApproverIdCardNumber 370724200002042233 \
    --Approvers.0.RecipientId a10712ca1e6a4c3f042ec1dbe0c3a7ed \
    --Approvers.0.UserId  \
    --Approvers.0.IsFullText True \
    --Approvers.0.PreReadTime 10 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.OrganizationName  \
    --Approvers.1.Required True \
    --Approvers.1.ApproverName  \
    --Approvers.1.ApproverMobile  \
    --Approvers.1.ApproverIdCardType  \
    --Approvers.1.ApproverIdCardNumber  \
    --Approvers.1.RecipientId 6dd5f6936019a3b84086f570280a6441 \
    --Approvers.1.UserId 274335800500d186a317872dd05d3853 \
    --Approvers.1.IsFullText False \
    --Approvers.1.PreReadTime 10 \
    --Approvers.2.ApproverType 1 \
    --Approvers.2.OrganizationName  \
    --Approvers.2.Required False \
    --Approvers.2.ApproverName  \
    --Approvers.2.ApproverMobile  \
    --Approvers.2.ApproverIdCardType  \
    --Approvers.2.ApproverIdCardNumber  \
    --Approvers.2.RecipientId 1f8ef4eff8e5b03d801a1ff6617852e2 \
    --Approvers.2.UserId 57e2cd3775fce1cd68e57e584f00fb16 \
    --Approvers.2.IsFullText True \
    --Approvers.2.PreReadTime 0 \
    --Approvers.3.ApproverType 1 \
    --Approvers.3.OrganizationName  \
    --Approvers.3.Required True \
    --Approvers.3.ApproverName  \
    --Approvers.3.ApproverMobile  \
    --Approvers.3.ApproverIdCardType  \
    --Approvers.3.ApproverIdCardNumber  \
    --Approvers.3.RecipientId ba7f7356e6031feaeca06892c3fa526a \
    --Approvers.3.UserId be3e7fcc21f2714926d2caca4ca5d02c \
    --Approvers.3.IsFullText False \
    --Approvers.3.PreReadTime 0 \
    --CallbackUrl http://www.qq.com \
    --UserData 用户自定义信息 \
    --ClientToken 我是Token
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

