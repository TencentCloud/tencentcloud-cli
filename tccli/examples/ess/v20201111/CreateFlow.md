**Example 1: 创建单C流程**

创建一个单C流程

Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --RelatedFlowId xxx \
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
    --Approvers.0.ApproverMobile 135****6345 \
    --Approvers.0.ApproverName 史国富 \
    --Approvers.0.PreReadTime 5 \
    --DeadLine 1652931170 \
    --ClientToken 字符串 \
    --Operator.UserId yDxMkUy*****E8VI2JmKxPkk \
    --Unordered true \
    --CallbackUrl 
```

Output: 
```
{
    "Response": {
        "FlowId": "yDR8YUUg****O4zjEuwxLMnR24",
        "RequestId": "2846e98d-xxxxx2632a7fceef"
    }
}
```

**Example 2: 创建签署流程**

创建一个B2C流程

Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowName 测试 \
    --Unordered False \
    --DeadLine 1604912664 \
    --CustomShowMap 合同名称:{合同名称} {发起方企业} {发起方姓名};国家:中国;发起方:{发起方企业};签署方1:  {签署方1企业};签署方2:  {签署方2企业}{签署方2姓名};签署方3:  {签署方3姓名} \
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

**Example 3: 创建含有动态签署人流程，签署方不指定具体的签署人**

创建一个B2C流程，两方签署方不指定具体的签署人
注：
`1.签署人相关信息为空，如：姓名、手机号码等`
`2.FillType需传值为1，表示为动态签署人（不确定具体的签署人），需后续进行补充。`

Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowName 测试 \
    --Unordered False \
    --DeadLine 1604912664 \
    --CustomShowMap 合同名称:{合同名称} {发起方企业} {发起方姓名};国家:中国;发起方:{发起方企业};签署方1:  {签署方1企业};签署方2:  {签署方2企业}{签署方2姓名};签署方3:  {签署方3姓名} \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.Required True \
    --Approvers.0.ApproverOption.FillType 1 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.Required True \
    --Approvers.1.ApproverOption.FillType 1
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

