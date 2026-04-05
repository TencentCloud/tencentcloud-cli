**Example 1: 展示批量创建离线任务作业列表**



Input: 

```
tccli wedata ListIntegrationCreationBatchJobs --cli-unfold-argument  \
    --WorkspaceId test_project_batch_002 \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "BatchJobInfos": [
                {
                    "BatchJobName": "测试批量作业-包含任务",
                    "CreatorName": "",
                    "CreatorUin": "700002164618",
                    "Description": "",
                    "EndTime": "0",
                    "FailedCount": "0",
                    "Id": "beb23b934-4c76-4c21-81aa-e9841236c38e",
                    "SinkInstanceId": "",
                    "SinkType": "",
                    "SourceInstanceId": "",
                    "SourceType": "",
                    "StartTime": "0",
                    "Status": "0",
                    "SuccessCount": "0",
                    "TotalCount": "0",
                    "UserUinInCharge": ""
                }
            ],
            "CompleteCount": "0",
            "CreatingCount": "0",
            "TotalCount": "1"
        },
        "RequestId": "bfa3af4e-2930-4531-9a8a-ed61a4c674b3"
    }
}
```

