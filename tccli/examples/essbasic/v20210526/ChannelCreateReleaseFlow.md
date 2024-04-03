**Example 1: 发起解除协议(默认情况，使用原流程的签署人)**

1. 使用原流程的签署人
2. 包含了详细的解除内容

Input: 

```
tccli essbasic ChannelCreateReleaseFlow --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDRSRUUgygj6rqi6UuO4zjEBDACwAjgT \
    --NeedRelievedFlowId yDwFmUUckpst10i3UubBSat8PWOt2iQF \
    --ReliveInfo.Reason 因为业务调整, 结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。 \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方xxxx以作赔偿。 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwFdUUckps******xAhL7zuaIwkMth",
        "RequestId": "s1669**2203341"
    }
}
```

**Example 2: 错误示例-解除协议中更换原合同个人类型的参与人**

1. 解除某个包含个人类型签署人的合同
2. 更换其他个人类型签署人作为解除协议的参与人

Input: 

```
tccli essbasic ChannelCreateReleaseFlow --cli-unfold-argument  \
    --Agent.AppId yDRSRUUgygj6rqi6UuO4zjEBDACwAjgT \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --NeedRelievedFlowId yDR1AUUgygjazuesUuO4zjESPW4PkfNi \
    --ReleasedApprovers.0.ApproverNumber 2 \
    --ReleasedApprovers.0.ApproverType PERSON \
    --ReleasedApprovers.0.Mobile 15100000000 \
    --ReleasedApprovers.0.Name 李四 \
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
        "RequestId": "s16939***23898"
    }
}
```

**Example 3: 发起解除协议（替换原流程中本企业的参与人并指定其为自动签署）**

1. 更换原合同中本方企业的参与人
2. 该企业参与人指定为自动签署(ApproverType 设置为 ENTERPRISESERVER)

Input: 

```
tccli essbasic ChannelCreateReleaseFlow --cli-unfold-argument  \
    --Agent.AppId yDRSRUUgygj6rqi6UuO4zjEBDACwAjgT \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --NeedRelievedFlowId yDR1AUUgygjazuesUuO4zjESPW4PkfNi \
    --ReleasedApprovers.0.Mobile 13200000000 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.ApproverNumber 2 \
    --ReleasedApprovers.0.ApproverType ENTERPRISESERVER \
    --ReleasedApprovers.0.OrganizationName 典子谦示例企业 \
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

**Example 4: 发起解除协议(使用本企业的签署人，替换用原流程中本企业的签署人)**

1. 使用本企业的签署人
2. 包含了详细的解除内容
3. 替换原流程中本企业的签署人
4. 被替换的原流程中的签署人ApproverNumber=1(即第二个签署人，在原流程签署人列表中的第二位)

扩展信息：
针对ApproverNumber举个例子，
例如在原流程中共有三个签署人(a, b, c)，
那么a是第一位(ApproverNumber=0)，b是第二位(ApproverNumber=1)，c是第三位(ApproverNumber=2)，
注意这里的顺序不是签署顺序，仅仅是签署人列表中的自然顺序，签署人列表的获取可以参考DescribeFlowDetailInfo接口。

Input: 

```
tccli essbasic ChannelCreateReleaseFlow --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDRSRUUgygj6rqi6UuO4zjEBDACwAjgT \
    --NeedRelievedFlowId yDwFmUUckpst10i3UubBSat8PWOt2iQF \
    --ReleasedApprovers.0.ApproverNumber 1 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.Mobile 13200000000 \
    --ReleasedApprovers.0.ApproverType ORGANIZATION \
    --ReleasedApprovers.0.OrganizationName 典子谦示例企业 \
    --ReliveInfo.Reason 因为业务调整, 结束合作。 \
    --ReliveInfo.RemainInForceItem 在业务结束前已产生的订单依旧有效。 \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方xxxx以作赔偿。 \
    --ReliveInfo.OriginalOtherSettlement 无 \
    --ReliveInfo.OtherDeals 无
```

Output: 
```
{
    "Response": {
        "FlowId": "yDwFdUUckps******xAhL7zuaIwkMth4",
        "RequestId": "s1669**2203341"
    }
}
```

**Example 5: 发起解除协议(替换原流程中本企业的参与人并指定签署人角色、签署控件)**

1. 更换原合同中本方企业的参与人
2. 给该企业参与人指定自定义的角色名称(通过设置ApproverSignRole)
3. 给该企业参与人指定签署控件类型为手写签名(通过设置ApproverSignComponentType)

Input: 

```
tccli essbasic ChannelCreateReleaseFlow --cli-unfold-argument  \
    --Agent.AppId yDRSRUUgygj6rqi6UuO4zjEBDACwAjgT \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --NeedRelievedFlowId yDwFmUUckpst10i3UubBSat8PWOt2iQF \
    --ReleasedApprovers.0.ApproverNumber 1 \
    --ReleasedApprovers.0.ApproverSignComponentType SIGN_SIGNATURE \
    --ReleasedApprovers.0.ApproverSignRole 自定义的签署方角色(供应商) \
    --ReleasedApprovers.0.ApproverType ORGANIZATION \
    --ReleasedApprovers.0.Mobile 13200000000 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.OrganizationName 典子谦示例企业 \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方xxxx以作赔偿。 \
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
        "RequestId": "s168809**839"
    }
}
```

