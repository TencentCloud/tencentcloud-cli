**Example 1: 发起解除协议（默认情况，使用原流程的签署人）**

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

**Example 2: 发起解除协议(使用本企业的签署人，替换用原流程中本企业的签署人)**

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

