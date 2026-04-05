**Example 1: 成功**

复制工作流成功

Input: 

```
tccli wedata CopyWorkflow --cli-unfold-argument  \
    --WorkspaceId 1346 \
    --OldWorkflowId 22b9891f-7f72-4e20-a746-d2b78f8c52e2 \
    --NewWorkflowName dcasdqwecopy
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkflowId": "12832f8b-618f-43ec-98d2-6820a413eff4"
        },
        "RequestId": "4db78735-a4f0-40e7-8c8c-0997b4a33b7e"
    }
}
```

