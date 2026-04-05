**Example 1: 停止批量创建离线集成作业**



Input: 

```
tccli wedata StopIntegrationCreationBatchJob --cli-unfold-argument  \
    --WorkspaceId test_project_batch_002 \
    --Id beb23b934-4c76-4c21-81aa-e9841236c38e
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true
        },
        "RequestId": "a89fa034-ab43-4abf-b687-256a14d1795b"
    }
}
```

