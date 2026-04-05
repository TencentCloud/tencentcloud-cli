**Example 1: 失败**

取消收藏工作流失败

Input: 

```
tccli wedata CancelMarkWorkflow --cli-unfold-argument  \
    --WorkspaceId 1346 \
    --WorkflowId 22b9891f-7f72-4e20-a746-d2b78f8c52e2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": false
        },
        "RequestId": "53a94687-c733-46d2-8ec5-d27191d1d7f1"
    }
}
```

