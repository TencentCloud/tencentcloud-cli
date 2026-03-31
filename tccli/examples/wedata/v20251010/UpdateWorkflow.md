**Example 1: 成功**

更新工作流成功

Input: 

```
tccli wedata UpdateWorkflow --cli-unfold-argument  \
    --WorkspaceId 1346 \
    --WorkflowId 22b9891f-7f72-4e20-a746-d2b78f8c52e2 \
    --NewSetting.BaseInfo.WorkflowName 213213dsadsad
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "9dc50caa-0eac-4e6d-acd9-c8b5161412a9"
    }
}
```

