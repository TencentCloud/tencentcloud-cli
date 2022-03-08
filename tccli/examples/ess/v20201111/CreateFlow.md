**Example 1: 创建电子签流程。**



Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.Channel  \
    --Operator.OpenId  \
    --Operator.ProxyIp  \
    --FlowName 测试 \
    --FlowDescription 测试流程的描述信息 \
    --Unordered False \
    --FlowType 合同 \
    --DeadLine 1604912664 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName ***有限公司 \
    --Approvers.0.Required True \
    --Approvers.0.ApproverName 呱呱叫 \
    --Approvers.0.ApproverMobile 185****11111 \
    --Approvers.0.ApproverIdCardType ID_CARD \
    --Approvers.0.ApproverIdCardNumber 4***********5 \
    --Approvers.0.RecipientId 195610*******0fde6a \
    --Approvers.0.UserId  \
    --Approvers.0.IsFullText True \
    --Approvers.0.PreReadTime 10 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.OrganizationName  \
    --Approvers.1.Required True \
    --Approvers.1.ApproverName  \
    --Approvers.1.ApproverMobile mobile \
    --Approvers.1.ApproverIdCardType ID_CARD \
    --Approvers.1.ApproverIdCardNumber 3********8 \
    --Approvers.1.RecipientId yDxM6*******AMwutB \
    --Approvers.1.UserId 195610*******fde6a \
    --Approvers.1.IsFullText False \
    --Approvers.1.PreReadTime 10 \
    --Approvers.2.ApproverType 1 \
    --Approvers.2.OrganizationName  \
    --Approvers.2.Required False \
    --Approvers.2.ApproverName  \
    --Approvers.2.ApproverMobile  \
    --Approvers.2.ApproverIdCardType  \
    --Approvers.2.ApproverIdCardNumber  \
    --Approvers.2.RecipientId yDxM6U******utBsRy \
    --Approvers.2.UserId 9d726******49e055 \
    --Approvers.2.IsFullText True \
    --Approvers.2.PreReadTime 0 \
    --Approvers.3.ApproverType 1 \
    --Approvers.3.OrganizationName  \
    --Approvers.3.Required True \
    --Approvers.3.ApproverName  \
    --Approvers.3.ApproverMobile  \
    --Approvers.3.ApproverIdCardType  \
    --Approvers.3.ApproverIdCardNumber  \
    --Approvers.3.RecipientId yDxM******wutBsRy \
    --Approvers.3.UserId dc3df0d00******37507f8323 \
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
        "FlowId": "2fb48c3945****65aaedf6",
        "RequestId": "s1234345677xxxx"
    }
}
```

