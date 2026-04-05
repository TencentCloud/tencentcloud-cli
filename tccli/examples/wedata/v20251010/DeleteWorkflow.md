**Example 1: 删除工作流成功**

删除工作流成功

Input: 

```
tccli wedata DeleteWorkflow --cli-unfold-argument  \
    --WorkspaceId 1346 \
    --WorkflowIdList 22b9891f-7f72-4e20-a746-d2b78f8c52e2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "89e10d97-33d5-4e83-9d79-5e40c64a788e"
    }
}
```

