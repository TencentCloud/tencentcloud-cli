**Example 1: 工作流更新整合接口**

更新工作流通用配置（基本信息 & 参数）

Input: 

```
tccli wedata UpdateWorkflowInfo --cli-unfold-argument  \
    --ProjectId abc \
    --OperatorName abc \
    --WorkflowId abc \
    --Owner abc \
    --OwnerId abc \
    --WorkflowDesc abc \
    --WorkflowName abc \
    --FolderId abc \
    --UserGroupId abc \
    --UserGroupName abc \
    --WorkflowParams.0.ParamKey abc \
    --WorkflowParams.0.ParamValue abc \
    --GeneralTaskParams.0.Type abc \
    --GeneralTaskParams.0.Value abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

