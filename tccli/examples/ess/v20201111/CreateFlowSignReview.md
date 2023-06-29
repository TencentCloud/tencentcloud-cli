**Example 1: 提交企业签署流程审批结果**

提交企业签署流程审批结果

Input: 

```
tccli ess CreateFlowSignReview --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowId xxxx \
    --ReviewType PASS \
    --ReviewMessage 企业内部审核通过，允许签署
```

Output: 
```
{
    "Response": {
        "RequestId": "s1234345677xxxx"
    }
}
```

