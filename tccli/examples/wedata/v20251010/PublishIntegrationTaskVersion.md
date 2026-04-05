**Example 1: 发布集成任务版本**



Input: 

```
tccli wedata PublishIntegrationTaskVersion --cli-unfold-argument  \
    --WorkspaceId test-project-001 \
    --TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --TaskVersion 20251219171210
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true
        },
        "RequestId": "5a31e7f5-4e1e-407e-9f83-7bf7ed1c79fd"
    }
}
```

