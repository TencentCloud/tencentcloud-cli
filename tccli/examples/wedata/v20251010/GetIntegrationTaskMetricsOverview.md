**Example 1: 集成任务指标概览信息**



Input: 

```
tccli wedata GetIntegrationTaskMetricsOverview --cli-unfold-argument  \
    --WorkspaceId test-project-001 \
    --TaskId 314a06b9-19ea-459c-b613-871ab5b606ed \
    --StartTime 1704067200000 \
    --EndTime 1704067200001
```

Output: 
```
{
    "Response": {
        "Data": {
            "EndTime": "1704067200001",
            "Histograms": [
                {
                    "EndTime": "1704153600",
                    "ReadSucceedRecords": "1000",
                    "StartTime": "1704067200",
                    "TotalErrorRecords": "0",
                    "WriteSucceedRecords": "1000"
                }
            ],
            "ReadSucceedBytes": "1231245",
            "ReadSucceedRecords": "1000",
            "StartTime": "1704067200000",
            "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed",
            "TotalErrorRecords": "0",
            "WorkspaceId": "test-project-001",
            "WriteSucceedBytes": "1231245",
            "WriteSucceedRecords": "1000"
        },
        "RequestId": "d6c91e09-ba35-4dc8-bdfd-9d837b6160a2"
    }
}
```

