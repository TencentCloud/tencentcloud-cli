**Example 1: 发起解除协议（主代子场景）**

1. 解除某个签署完成的合同
2. 主企业代子企业操作(通过指定Agent中的ProxyOrganizationId)

Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Agent.ProxyOrganizationId yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP \
    --NeedRelievedFlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --ReleasedApprovers.0.Mobile 13200000000 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.RelievedApproverReceiptId yDRSRUUgygj6rqouUuO4zjESlnSFPcIE \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方xxxx以作赔偿 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无 \
    --ReliveInfo.Reason 因为业务调整, 结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwJBUUc***uxAppfh2XR",
        "RequestId": "s1693969234439636483"
    }
}
```

**Example 2: 发起解除协议（默认情况，使用原流程的签署人）**

1.使用原流程的签署人
2.包含了详细的解除内容

Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId xxxOUUgyxxxxEWA0dddl \
    --NeedRelievedFlowId xxxnGUUgygkgi7fdUx6JlVOE0wzdddd \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方xxxxxx以作赔偿 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无 \
    --ReliveInfo.Reason 因为业务调整,结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwnGUUgygkgi7fdUx6JlVOE0wzmtxxx",
        "RequestId": "s18776xxx345780"
    }
}
```

**Example 3: 错误示例-解除协议中更换原合同个人类型的参与人**

1. 解除某个包含个人类型签署人的合同
2. 更换其他个人类型签署人作为解除协议的参与人

Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --NeedRelievedFlowId yDR1AUUgygjazuesUuO4zjESPW4PkfNi \
    --ReleasedApprovers.0.Mobile 15100000000 \
    --ReleasedApprovers.0.Name 李四 \
    --ReleasedApprovers.0.RelievedApproverReceiptId yDwFdUUckpsvi8mpUEn0aFR1tWzReoTk \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方xxxx以作赔偿 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无 \
    --ReliveInfo.Reason 因为业务调整, 结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "不能更换非企业签署人身份信息"
        },
        "RequestId": "s16939xxx23898"
    }
}
```

**Example 4: 发起解除协议（记录下原合同与解除协议的映射关系）**

1. 更换原合同中的企业参与人(通过指定ReleasedApprovers中的RelievedApproverReceiptId)
2. 在解除协议中记录下原合同ID(通过设置UserData字段)

Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --UserData {"OriginalFlowId":"yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm"} \
    --NeedRelievedFlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --ReleasedApprovers.0.Mobile 13200000000 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.RelievedApproverReceiptId yDRSRUUgygj6rqouUuO4zjESlnSFPcIE \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方xxxx以作赔偿 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无 \
    --ReliveInfo.Reason 因为业务调整, 结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwJBUUc***uxAppfh2XR",
        "RequestId": "s1693969233639636483"
    }
}
```

**Example 5: 发起解除协议（替换原流程中本企业的参与人并指定其为自动签署）**

1. 更换原合同中本方企业的参与人
2. 给该企业参与人指定未自动签署(ApproverType 设置为 ENTERPRISESERVER)

Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --NeedRelievedFlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --ReleasedApprovers.0.Mobile 13200000000 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.RelievedApproverReceiptId yDRSRUUgygj6rqouUuO4zjESlnSFPcIE \
    --ReleasedApprovers.0.ApproverType ENTERPRISESERVER \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方以作赔偿 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无 \
    --ReliveInfo.Reason 因为业务调整, 结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm",
        "RequestId": "s312334445587989"
    }
}
```

**Example 6: 发起解除协议（使用本企业的签署人，替换用原流程中本企业的签署人）**

发起解除协议（使用本企业的签署人，替换用原流程中本企业的签署人）


Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId yDxjOUUgydjxxxxxjEWA07rC2xl \
    --NeedRelievedFlowId yDwnGUUgygkgi7fdUx6JlVOE0wxxxxx \
    --ReleasedApprovers.0.Mobile 1870000000 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.RelievedApproverReceiptId yDRscUUgyg1zr7vjUyJ8QKxxxxxxx \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方xxxx以作赔偿 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无 \
    --ReliveInfo.Reason 因为业务调整,结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。
```

Output: 
```
{
    "Response": {
        "FlowId": "yDRscAABDg1zr7vjUyJ8QKxxxxxxx",
        "RequestId": "s1989876373464"
    }
}
```

**Example 7: 发起解除协议（替换原流程中本企业的参与人并指定签署人角色、签署控件）**

1. 更换原合同中本方企业的参与人
2. 给该企业参与人指定自定义的角色名称(通过设置ApproverSignRole)
3. 给该企业参与人指定签署控件类型为手写签名(通过设置ApproverSignComponentType)

Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --NeedRelievedFlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --ReleasedApprovers.0.Mobile 13200000000 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.RelievedApproverReceiptId yDRSRUUgygj6rqouUuO4zjESlnSFPcIE \
    --ReleasedApprovers.0.ApproverSignRole 自定义的签署方角色(供应商) \
    --ReleasedApprovers.0.ApproverSignComponentType SIGN_SIGNATURE \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方以作赔偿 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无 \
    --ReliveInfo.Reason 因为业务调整, 结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwgkUU7y***********zWBfv",
        "RequestId": "s1688099393764508839"
    }
}
```

