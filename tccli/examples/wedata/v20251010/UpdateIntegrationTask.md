**Example 1: 更新集成任务**



Input: 

```
tccli wedata UpdateIntegrationTask --cli-unfold-argument  \
    --TaskInfo.TaskName test job name \
    --TaskInfo.TaskMode 1 \
    --TaskInfo.SyncType 0 \
    --TaskInfo.Description test job description \
    --TaskInfo.TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --WorkspaceId test-project-001
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed",
            "TaskVersion": "20251219171210"
        },
        "RequestId": "e059ed67-7c2a-41f2-96be-400c1bb529e8"
    }
}
```

