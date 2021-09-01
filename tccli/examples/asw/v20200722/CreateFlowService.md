**Example 1: 生成状态机**

生成状态机服务

Input: 

```
tccli asw CreateFlowService --cli-unfold-argument  \
    --FlowServiceName FlowServiceTest \
    --Definition "{}" \
    --IsNewRole false \
    --RoleResource qcs%3A%3Acam%3A%3Auin%2F20103392%3AroleName%2FSomeRoleForYourStateMachine \
    --Type EXPRESS
```

Output: 
```
{
    "Response": {
        "FlowServiceResource": "flowservicetest",
        "CreateDate": "1595227100",
        "RequestId": "ab1b30fc-3503-4b27-96dc-94c14d2fd43w"
    }
}
```

