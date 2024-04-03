**Example 1: 通过姓名+证件类型+证件号通过某个个人签署人的签署阻断**

1.签署审核通过企业签署人（ApproverType 设置为PERSON）
2.使用 姓名 + 手机号 定位合同组内所有子合同的该签署人
3.拒绝（阻断）该签署人的签署操作 （ReviewType 设置为REJECT）

Input: 

```
tccli essbasic CreateFlowGroupSignReview --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowGroupId yDSxIUUckpt1ea9hUx5oXYkSgVNJaxOE \
    --ReviewType REJECT \
    --ReviewMessage 不能签署 \
    --ApproverInfo.ApproverName 典子谦 \
    --ApproverInfo.ApproverIdCardNumber 620000198802020000 \
    --ApproverInfo.ApproverIdCardType ID_CARD \
    --ApproverInfo.ApproverType PERSON
```

Output: 
```
{
    "Response": {
        "RequestId": "s1703576009516564065"
    }
}
```

**Example 2: 示例1 通过企业名称+姓名+手机号通过某个企业签署人的签署阻断**

1.签署审核通过企业签署人（ApproverType 设置为ORGANIZATION）
2.使用企业名称 + 姓名 + 手机号 定位合同组内所有子合同的该签署人
3.通过该签署人的签署审核（该签署人可以进行签署操作）（ReviewType 设置为PASS）

Input: 

```
tccli essbasic CreateFlowGroupSignReview --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --FlowGroupId yDSxIUUckpt1ea9hUx5oXYkSgVNJaxOE \
    --ReviewType PASS \
    --ReviewMessage 可以签署 \
    --ApproverInfo.ApproverType ORGANIZATION \
    --ApproverInfo.ApproverName 典子签 \
    --ApproverInfo.OrganizationName 典子签示例企业 \
    --ApproverInfo.ApproverMobile 18200000000
```

Output: 
```
{
    "Response": {
        "RequestId": "s1703576009516564064"
    }
}
```

