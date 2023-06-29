**Example 1: 创建签署流程**

通过页面创建签署流程

Input: 

```
tccli ess CreatePrepareFlow --cli-unfold-argument  \
    --Operator.UserId 1956103********520fde6a \
    --FlowName 测试 \
    --Unordered False \
    --IntelligentStatus OPEN \
    --UserFlowTypeId test \
    --ResourceId test \
    --Deadline 1604912664 \
    --Approvers.0.ApproverType 0 \
    --Approvers.0.OrganizationName ***有限公司 \
    --Approvers.0.Required True \
    --Approvers.0.ApproverName 张三 \
    --Approvers.0.ApproverMobile 185****11111 \
    --Approvers.1.ApproverType 1 \
    --Approvers.1.Required True \
    --Approvers.1.ApproverName 李四 \
    --Approvers.1.ApproverMobile 185****2222
```

Output: 
```
{
    "Response": {
        "Url": "",
        "RequestId": "s1234345677xxxx"
    }
}
```

