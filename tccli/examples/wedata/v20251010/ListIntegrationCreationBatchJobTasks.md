**Example 1: 展示批量创建离线集成作业下的任务**



Input: 

```
tccli wedata ListIntegrationCreationBatchJobTasks --cli-unfold-argument  \
    --WorkspaceId test_project_batch_002 \
    --Id t11845635-955a-43fb-b0be-d304e37692eb \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskInfos": [],
            "TotalCount": "0"
        },
        "RequestId": "07af6139-6c2e-4b0f-8249-df2c1c3e8c6c"
    }
}
```

