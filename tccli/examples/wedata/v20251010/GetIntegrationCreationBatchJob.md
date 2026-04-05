**Example 1: 查询批量创建任务**



Input: 

```
tccli wedata GetIntegrationCreationBatchJob --cli-unfold-argument  \
    --WorkspaceId test_project_batch_002 \
    --Id c3ff20f3d-28e7-4e8f-96bd-0797f3798b4d
```

Output: 
```
{
    "Response": {
        "Data": {
            "BatchJobInfo": {
                "BatchJobName": "测试批量作业-包含任务",
                "Config": [],
                "Description": "批量创建任务-包含2个同步任务",
                "Id": "c3ff20f3d-28e7-4e8f-96bd-0797f3798b4d",
                "SinkConfig": [],
                "SinkInstanceId": "sink_instance_002",
                "SinkType": "TCLake",
                "SourceConfig": [],
                "SourceInstanceId": "source_instance_002",
                "SourceType": "MYSQL",
                "Status": "0",
                "TaskInfos": []
            }
        },
        "RequestId": "482d0976-9da4-4401-bb64-67eb3d398f5c"
    }
}
```

