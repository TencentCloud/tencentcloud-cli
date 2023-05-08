**Example 1: 范例**



Input: 

```
tccli wedata ModifyWorkflowInfo --cli-unfold-argument  \
    --WorkflowId 34e51bc4-0cd9-11ed-8909-bc97e105ba60 \
    --WorkflowName  \
    --UserGroupName  \
    --WorkflowParams.0.ParamValue 11 \
    --WorkflowParams.0.ParamKey ff \
    --GeneralTaskParams.0.Type SPARK_SQL \
    --GeneralTaskParams.0.Value cc \
    --ProjectId 1 \
    --WorkflowDesc ccc \
    --UserGroupId  \
    --Owner  \
    --OwnerId  \
    --FolderId 
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

