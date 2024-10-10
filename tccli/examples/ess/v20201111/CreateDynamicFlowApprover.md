**Example 1: 补充企业自动签签署人**

补充企业自动签签署人

Input: 

```
tccli ess CreateDynamicFlowApprover --cli-unfold-argument  \
    --Operator.UserId 操作人id \
    --FlowId 合同id \
    --AutoSignScene  \
    --Approvers.0.ApproverType 3 \
    --Approvers.0.OrganizationName 发起方企业 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.SignComponents.0.ComponentPosX 160 \
    --Approvers.0.SignComponents.0.ComponentPosY 160 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentValue yDCHZUUckpa9v4i1UuSIlP8KougrzLuQ \
    --Approvers.0.SignComponents.0.ComponentPage 1
```

Output: 
```
{
    "Response": {
        "DynamicFlowApproverList": [
            {
                "ApproverStatus": 1,
                "RecipientId": "yDCjFUUckp48f6hcUyh7ukYyfaIqHqnR",
                "SignId": "yDCjFUUckp48f6hiUyh7ukYBjxSiGXzB"
            }
        ],
        "FlowId": "yDCjFUUckp48f680Uyh7ukYy5JFb80ux",
        "RequestId": "s1728544317709049372"
    }
}
```

**Example 2: 二要素形式补充企业签署人**

二要素形式补充签署人

Input: 

```
tccli ess CreateDynamicFlowApprover --cli-unfold-argument  \
    --Operator.UserId 操作人id \
    --FlowId 合同id \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 企业名称 \
    --Approvers.0.ApproverName 签署人姓名 \
    --Approvers.0.ApproverMobile 签署人手机号 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.SignComponents.0.ComponentPosX 260 \
    --Approvers.0.SignComponents.0.ComponentPosY 260 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPage 1
```

Output: 
```
{
    "Response": {
        "DynamicFlowApproverList": [
            {
                "ApproverStatus": 1,
                "RecipientId": "yDCjFUUckp48f6hcUyh7ukYyfaIqHqnR",
                "SignId": "yDCjFUUckp48f6hiUyh7ukYBjxSiGXzB"
            }
        ],
        "FlowId": "yDCjFUUckp48f680Uyh7ukYy5JFb80ux",
        "RequestId": "s1728544317709049372"
    }
}
```

**Example 3: 二要素补充个人签署人**

二要素补充个人签署人

Input: 

```
tccli ess CreateDynamicFlowApprover --cli-unfold-argument  \
    --Operator.UserId 操作人id \
    --FlowId 合同id \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.ApproverName 签署人姓名 \
    --Approvers.0.ApproverMobile 签署人手机号 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.SignComponents.0.ComponentPosX 260 \
    --Approvers.0.SignComponents.0.ComponentPosY 260 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPage 1
```

Output: 
```
{
    "Response": {
        "DynamicFlowApproverList": [
            {
                "ApproverStatus": 1,
                "RecipientId": "yDCjFUUckp48f6hcUyh7ukYyfaIqHqnR",
                "SignId": "yDCjFUUckp48f6hiUyh7ukYBjxSiGXzB"
            }
        ],
        "FlowId": "合同id",
        "RequestId": "s1728544317709049372"
    }
}
```

**Example 4: 补充个人自动签签署人**

补充个人自动签签署人

Input: 

```
tccli ess CreateDynamicFlowApprover --cli-unfold-argument  \
    --Operator.UserId 操作人id \
    --FlowId 合同id \
    --AutoSignScene E_PRESCRIPTION_AUTO_SIGN \
    --Approvers.0.ApproverType 7 \
    --Approvers.0.ApproverName 签署人姓名 \
    --Approvers.0.ApproverMobile 签署人手机号 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.SignComponents.0.ComponentPosX 360 \
    --Approvers.0.SignComponents.0.ComponentPosY 360 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SIGNATURE \
    --Approvers.0.SignComponents.0.ComponentPage 1
```

Output: 
```
{
    "Response": {
        "DynamicFlowApproverList": [
            {
                "ApproverStatus": 1,
                "RecipientId": "yDCjFUUckp48f6hcUyh7ukYyfaIqHqnR",
                "SignId": "yDCjFUUckp48f6hiUyh7ukYBjxSiGXzB"
            }
        ],
        "FlowId": "合同id",
        "RequestId": "s1728544317709049372"
    }
}
```

**Example 5: 补充或签签署人**

补充或签签署人

Input: 

```
tccli ess CreateDynamicFlowApprover --cli-unfold-argument  \
    --Operator.UserId 操作人id \
    --FlowId 合同id \
    --AutoSignScene  \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 企业名称 \
    --Approvers.0.CustomApproverTag 唯一标志 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.SignComponents.0.ComponentPosX 333 \
    --Approvers.0.SignComponents.0.ComponentPosY 333 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPage 1
```

Output: 
```
{
    "Response": {
        "DynamicFlowApproverList": [
            {
                "ApproverStatus": 1,
                "RecipientId": "yDCjFUUckp48f6hcUyh7ukYyfaIqHqnR",
                "SignId": "yDCjFUUckp48f6hiUyh7ukYBjxSiGXzB"
            }
        ],
        "FlowId": "合同id",
        "RequestId": "s1728544317709049372"
    }
}
```

**Example 6: 补充动态签署人**

补充动态签署人

Input: 

```
tccli ess CreateDynamicFlowApprover --cli-unfold-argument  \
    --Operator.UserId 操作人id \
    --FlowId 合同id \
    --AutoSignScene  \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.ApproverOption.FillType 1 \
    --Approvers.0.PreReadTime 3 \
    --Approvers.0.SignComponents.0.ComponentPosX 60 \
    --Approvers.0.SignComponents.0.ComponentPosY 360 \
    --Approvers.0.SignComponents.0.ComponentWidth 100 \
    --Approvers.0.SignComponents.0.ComponentHeight 100 \
    --Approvers.0.SignComponents.0.FileIndex 0 \
    --Approvers.0.SignComponents.0.ComponentType SIGN_SEAL \
    --Approvers.0.SignComponents.0.ComponentPage 1
```

Output: 
```
{
    "Response": {
        "DynamicFlowApproverList": [
            {
                "ApproverStatus": 1,
                "RecipientId": "yDCjFUUckp48f6hcUyh7ukYyfaIqHqnR",
                "SignId": "yDCjFUUckp48f6hiUyh7ukYBjxSiGXzB"
            }
        ],
        "FlowId": "合同id",
        "RequestId": "s1728544317709049372"
    }
}
```

