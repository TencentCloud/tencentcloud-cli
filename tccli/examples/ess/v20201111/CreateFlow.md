**Example 1: 创建单C流程**

创建一个单C流程

Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --UserData 5a2X56ym5Liy \
    --FlowName 西红柿购买合同 \
    --FlowDescription 2024年西红柿购买合同 \
    --FlowType 采购合同 \
    --Approvers.0.ApproverType 1 \
    --Approvers.0.Required true \
    --Approvers.0.NotifyType SMS \
    --Approvers.0.ApproverMobile 113200000000 \
    --Approvers.0.ApproverName 典子谦 \
    --DeadLine 1652931170 \
    --Operator.UserId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --Unordered true
```

Output: 
```
{
    "Response": {
        "FlowId": "yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc",
        "RequestId": "2632a7fceef"
    }
}
```

**Example 2: 创建签署流程**

创建一个B2C流程

Input: 

```
tccli ess CreateFlow --cli-unfold-argument  \
    --Operator.UserId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --FlowName 西红柿采购合同 \
    --Unordered False \
    --DeadLine 1604912664 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName 典子谦示例企业 \
    --Approvers.0.Required True \
    --Approvers.0.ApproverName 典子谦 \
    --Approvers.0.ApproverMobile 13200000000 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.Required True \
    --Approvers.1.ApproverName 李四 \
    --Approvers.1.ApproverMobile 15100000000
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwfGUUckps86q8kUoTIbgRXTZbVk9I2",
        "RequestId": "001uSHUNDy"
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
    --Operator.UserId yDRS4UUgygqdcj51UuO4zjEyWTmzsIAR \
    --FlowName 西瓜购买合同 \
    --Unordered False \
    --DeadLine 1604912664 \
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
        "FlowId": "yDRS4UUgygqdcj5pUuO4zjEu602GFIe6",
        "RequestId": "4zjEBpXdcsHWX"
    }
}
```

