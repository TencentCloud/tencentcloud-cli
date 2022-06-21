**Example 1: 创建电子签流程。**



Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowName 测试 \
    --Unordered False \
    --DeadLine 1604912664 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName ***有限公司 \
    --Approvers.0.Required True \
    --Approvers.0.ApproverName 张三 \
    --Approvers.0.ApproverMobile 185****11111 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.Required True \
    --Approvers.1.ApproverName 李四 \
    --Approvers.1.ApproverMobile 185****2222
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

**Example 2: 测试**



Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --UserData 字符串 \
    --FlowName 字符串 \
    --FlowDescription 字符串 \
    --FlowType 字符串 \
    --Approvers.0.OrganizationName 字符串 \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.IsFullText false \
    --Approvers.0.VerifyChannel WEIXIN \
    --Approvers.0.Required true \
    --Approvers.0.UserId  \
    --Approvers.0.RecipientId  \
    --Approvers.0.NotifyType SMS \
    --Approvers.0.ApproverMobile 13554456345 \
    --Approvers.0.ApproverName 史国富 \
    --Approvers.0.PreReadTime 5 \
    --DeadLine 1652931170 \
    --ClientToken 字符串 \
    --Operator.ProxyIp 字符串 \
    --Operator.ClientIp 字符串 \
    --Operator.UserId yDxMkUyKQDWLhGUuO4zjE8VI2JmKxPkk \
    --Operator.Channel YUFU \
    --Operator.OpenId us-6c4f28eda1994ec6bafe176c2b1cb86a \
    --Unordered true \
    --CallbackUrl 
```

Output: 
```
{
    "Response": {
        "FlowId": "yDR8YUUgygqpxi8zUuO4zjEuwxLMnR24",
        "RequestId": "2846e98d-53bd-4d1f-807f-d2632a7fceef"
    }
}
```

