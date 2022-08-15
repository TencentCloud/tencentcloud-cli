**Example 1: 提交企业签署流程审批结果**



Input: 

```
tccli essbasic ChannelCreateFlowSignReview --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId 622201199508023314 \
    --Agent.ProxyOrganizationOpenId sharpezhang-testorg-pay \
    --Agent.AppId 15edb41f2ee412f5ff533ac0185ebb0b \
    --FlowId xxxx \
    --ReviewType PASS \
    --ReviewMessage 企业内部审核通过，允许签署
```

Output: 
```
{
    "Response": {
        "RequestId": "s16221xxxx12775546"
    }
}
```

