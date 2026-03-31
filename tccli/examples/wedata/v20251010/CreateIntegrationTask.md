**Example 1: 创建集成任务**



Input: 

```
tccli wedata CreateIntegrationTask --cli-unfold-argument  \
    --TaskInfo.TaskName test job name \
    --TaskInfo.TaskMode 1 \
    --TaskInfo.SyncType 0 \
    --TaskInfo.Description test job description \
    --WorkspaceId test-project-001
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed"
        },
        "RequestId": "a92d85b1-7860-4176-b1e0-35000181c4eb"
    }
}
```

