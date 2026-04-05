**Example 1: 更新批量创建离线集成作业**



Input: 

```
tccli wedata UpdateIntegrationCreationBatchJob --cli-unfold-argument  \
    --WorkspaceId test_project_batch_002 \
    --BatchJobInfo.Id beb23b934-4c76-4c21-81aa-e9841236c38e \
    --BatchJobInfo.BatchJobName 测试批量作业-包含任务 \
    --BatchJobInfo.UserUinInCharge 700002164618
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true
        },
        "RequestId": "318e63a3-60dc-4f87-9d04-cc1ff64a6015"
    }
}
```

