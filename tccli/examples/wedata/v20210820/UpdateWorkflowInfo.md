**Example 1: 工作流更新整合接口**

更新工作流通用配置（基本信息 & 参数）

Input: 

```
tccli wedata UpdateWorkflowInfo --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --OperatorName kevinnie \
    --WorkflowId 3dfadfde-af87-11ee-8ec8-b8599f277de5 \
    --Owner zhanglin \
    --OwnerId 100028579801 \
    --WorkflowDesc fd \
    --WorkflowName bp_ext_clone_01
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "947beddf-ecac-472e-8727-fba35e8cb96e"
    }
}
```

