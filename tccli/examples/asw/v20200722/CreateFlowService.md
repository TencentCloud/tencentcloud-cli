**Example 1: 生成状态机**

生成状态机服务

Input: 

```
tccli asw CreateFlowService --cli-unfold-argument  \
    --FlowServiceName flowservicetest \
    --Definition "{}" \
    --IsNewRole false \
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

