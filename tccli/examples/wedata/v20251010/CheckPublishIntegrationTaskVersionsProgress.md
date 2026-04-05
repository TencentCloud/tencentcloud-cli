**Example 1: 	检查批量发布任务版本进度**



Input: 

```
tccli wedata CheckPublishIntegrationTaskVersionsProgress --cli-unfold-argument  \
    --Id eef1867bb-fbab-4b5e-be5b-2d4c140d1ee1 \
    --WorkspaceId test-project-001
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskInfos": [
                {
                    "BatchJobId": "eef1867bb-fbab-4b5e-be5b-2d4c140d1ee1",
                    "BatchJobTaskId": "",
                    "ColumnMappingType": "0",
                    "ExecutorGroupId": "",
                    "FailedMessage": "Publish failed: 错误代码:[1201104], 错误描述:[无效参数：AppId，cannot be null。请检查后重试。]",
                    "SchemaMappings": [],
                    "SinkColumn": [],
                    "SinkConfig": [],
                    "SinkDatabase": "",
                    "SinkFileName": "",
                    "SinkPath": "",
                    "SinkSchema": "",
                    "SinkTableName": "",
                    "SourceColumn": [],
                    "SourceConfig": [],
                    "SourceDatabase": "",
                    "SourcePath": "",
                    "SourceSchema": "",
                    "SourceTableName": "",
                    "Status": "1",
                    "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed",
                    "TaskName": ""
                }
            ]
        },
        "RequestId": "34f37600-f8ad-43e7-a7aa-983405c69585"
    }
}
```

