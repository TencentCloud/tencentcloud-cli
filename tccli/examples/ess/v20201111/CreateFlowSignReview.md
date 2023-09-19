**Example 1: 提交企业签署流程审批结果通过**

提交企业签署流程审批结果通过

Input: 

```
tccli ess CreateFlowSignReview --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
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

**Example 2: 提交企业签署流程审批结果，结果为拒绝。**

提交企业签署流程审批结果，结果为拒绝。

Input: 

```
tccli ess CreateFlowSignReview --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --ReviewType REJECT \
    --ReviewMessage 合同内容姓名填写错误，不允许进行签署
```

Output: 
```
{
    "Response": {
        "RequestId": "s1234345677xxxx"
    }
}
```

**Example 3: 错误示例，提交企业签署流程审批结果，没有填写原因**

错误示例，提交企业签署流程审批结果，没有填写原因

Input: 

```
tccli ess CreateFlowSignReview --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --FlowId yDwFmUUckpstqfvzUE1h3jo1f3cqjkGm \
    --ReviewType REJECT
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "审核操作原因(ReviewMessage)在取消时不能为空，请确认后重试"
        },
        "RequestId": "s1694848471031289687"
    }
}
```

