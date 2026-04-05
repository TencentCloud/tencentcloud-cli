**Example 1: 重新启动批量创建离线集成作业任务**



Input: 

```
tccli wedata RestartIntegrationCreationBatchJobTasks --cli-unfold-argument  \
    --WorkspaceId test_project_batch_002 \
    --BatchJobId beb23b934-4c76-4c21-81aa-e9841236c38e \
    --BatchJobTaskIds ffa96d94-339e-4fdf-a981-bbbacdb17b31
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true
        },
        "RequestId": "f0c9aa67-8e8b-4d8c-aa04-ae1198c4bbf0"
    }
}
```

