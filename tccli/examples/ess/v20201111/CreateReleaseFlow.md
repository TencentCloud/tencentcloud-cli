**Example 1: 发起解除协议（默认情况，使用原流程的签署人）**

1.使用原流程的签署人
2.包含了详细的解除内容

Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId xxxOUUgydjfxgnzUuO4zjEWA0dddl \
    --NeedRelievedFlowId xxxnGUUgygkgi7fdUx6JlVOE0wzdddd \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方人民币10000元以作赔偿 \
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
        "RequestId": "s187767536345780"
    }
}
```

**Example 2: 发起解除协议（使用本企业的签署人，替换用原流程中本企业的签署人）**

发起解除协议（使用本企业的签署人，替换用原流程中本企业的签署人）


Input: 

```
tccli ess CreateReleaseFlow --cli-unfold-argument  \
    --Operator.UserId yDxjOUUgydjfxgnzUuO4zjEWA07rC2xl \
    --NeedRelievedFlowId yDwnGUUgygkgi7fdUx6JlVOE0wxxxxx \
    --ReleasedApprovers.0.Mobile 1870000000 \
    --ReleasedApprovers.0.Name 典子谦 \
    --ReleasedApprovers.0.RelievedApproverReceiptId yDRscUUgyg1zr7vjUyJ8QKxxxxxxx \
    --ReliveInfo.OriginalExpenseSettlement 甲方需付给乙方人民币10000元以作赔偿 \
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

