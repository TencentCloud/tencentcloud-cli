**Example 1: 发起解除协议（默认情况，使用原流程的签署人）**

1. 使用原流程的签署人
2. 包含了详细的解除内容

Input: 

```
tccli essbasic ChannelCreateReleaseFlow --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId d7c13a8***********0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc***********3aff766cac \
    --Agent.AppId 65f***********aa382cc5ed0e \
    --NeedRelievedFlowId 待解除的流程编号xx \
    --ReliveInfo.Reason 解除理由xx \
    --ReliveInfo.RemainInForceItem 保留条款xx \
    --ReliveInfo.OriginalExpenseSettlement 原合同费用结算xx \
    --ReliveInfo.OriginalOtherSettlement 原合同其他约定xx \
    --ReliveInfo.OtherDeals 其他约定xx
```

Output: 
```
{
    "Response": {
        "FlowId": "yDRsF*****************cbBRXBW6Rd",
        "RequestId": "s1669186754600597655"
    }
}
```

**Example 2: 发起解除协议（使用本企业的签署人，替换用原流程中本企业的签署人）**

1. 使用本企业的签署人
2. 包含了详细的解除内容
3. 替换原流程中本企业的签署人
4. 被替换的原流程中的签署人ApproverNumber=1（即第二个签署人，在原流程签署人列表中的第二位）

扩展信息：
针对ApproverNumber举个例子，
例如在原流程中共有三个签署人（a, b, c），
那么a是第一位(ApproverNumber=0)，b是第二位(ApproverNumber=1)，c是第三位(ApproverNumber=2)，
注意这里的顺序不是签署顺序，仅仅是签署人列表中的自然顺序，签署人列表的获取可以参考DescribeFlowDetailInfo接口。

Input: 

```
tccli essbasic ChannelCreateReleaseFlow --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId d7c13a8***********0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc***********3aff766cac \
    --Agent.AppId 65f***********aa382cc5ed0e \
    --NeedRelievedFlowId 待解除的流程编号test \
    --ReleasedApprovers.0.ApproverNumber 1 \
    --ReleasedApprovers.0.Name 张三 \
    --ReleasedApprovers.0.Mobile 13******** \
    --ReleasedApprovers.0.ApproverType ORGANIZATION \
    --ReleasedApprovers.0.OrganizationName test \
    --ReliveInfo.Reason 解除理由test \
    --ReliveInfo.RemainInForceItem 保留条款test \
    --ReliveInfo.OriginalExpenseSettlement 原合同费用结算test \
    --ReliveInfo.OriginalOtherSettlement 原合同其他约定test \
    --ReliveInfo.OtherDeals 其他约定test
```

Output: 
```
{
    "Response": {
        "FlowId": "yDRsF*****************cbBRXBW6Rd",
        "RequestId": "s16692xxx82203341"
    }
}
```

