**Example 1: 查询集成任务指标列表**



Input: 

```
tccli wedata ListIntegrationTaskMetrics --cli-unfold-argument  \
    --WorkspaceId test-project-001 \
    --TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ExecJobStatus": "RUNNING",
                    "JobId": "1",
                    "ReadSucceedRecords": "1200",
                    "RecordSpeed": "300",
                    "RunEndTime": "1700000000001",
                    "RunStartTime": "1700000000000",
                    "RunUserName": "zhangsan",
                    "RunUserUin": "100000002",
                    "TaskExecutionId": "exec-xyz",
                    "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed",
                    "TaskName": "testName",
                    "TotalErrorRecords": "0",
                    "WorkspaceId": "test-project-001",
                    "WriteSucceedRecords": "1000"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "2ef7f7e0-47c2-417d-8458-581be495d6bb"
    }
}
```

