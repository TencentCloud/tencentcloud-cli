**Example 1: 更新工作流信息范例**

更新工作流信息

Input: 

```
tccli wedata ModifyWorkflowInfo --cli-unfold-argument  \
    --WorkflowId 34e51bc4-0cd9-11ed-8909-bc97e105ba60 \
    --WorkflowName 测试工作流 \
    --UserGroupName  \
    --WorkflowParams.0.ParamValue 11 \
    --WorkflowParams.0.ParamKey ff \
    --GeneralTaskParams.0.Type SPARK_SQL \
    --GeneralTaskParams.0.Value cc \
    --ProjectId 1 \
    --WorkflowDesc ccc \
    --UserGroupId 1 \
    --Owner jack \
    --OwnerId 104293423 \
    --FolderId sdf-ddsef-oge923
```

Output: 
```
{
    "Response": {
        "RequestId": "f13c9348-c817-4ff0-b747-1c7581862281",
        "Data": true
    }
}
```

