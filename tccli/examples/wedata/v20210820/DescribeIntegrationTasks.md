**Example 1: 查询集成任务列表**

查询集成任务列表

Input: 

```
tccli wedata DescribeIntegrationTasks --cli-unfold-argument  \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --PageSize 0 \
    --ProjectId xx \
    --OrderFields.0.Direction xx \
    --OrderFields.0.Name xx \
    --PageNumber 0 \
    --StartTime xx \
    --EndTime xx
```

Output: 
```
{
    "Response": {
        "TaskInfoSet": [
            {
                "TaskGroupId": "xx",
                "Status": 0,
                "WorkflowId": "xx",
                "Description": "xx",
                "CreatorUin": "xx",
                "SyncType": 0,
                "ProjectId": "xx",
                "OwnerUin": "xx",
                "ExecuteContext": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "ScheduleTaskId": "xx",
                "TaskType": 0,
                "AppId": "xx",
                "ExecutorId": "xx",
                "TaskId": "xx",
                "OperatorUin": "xx",
                "Nodes": [
                    {
                        "NodeType": "xx",
                        "Description": "xx",
                        "CreatorUin": "xx",
                        "DataSourceType": "xx",
                        "ProjectId": "xx",
                        "OwnerUin": "xx",
                        "ExtConfig": [
                            {
                                "Name": "xx",
                                "Value": "xx"
                            }
                        ],
                        "DatasourceId": "xx",
                        "NodeMapping": {
                            "SourceId": "xx",
                            "SchemaMappings": [
                                {
                                    "SinkSchemaId": "xx",
                                    "SourceSchemaId": "xx"
                                }
                            ],
                            "SinkId": "xx",
                            "SourceSchema": [
                                {
                                    "Type": "xx",
                                    "Id": "xx",
                                    "Value": "xx",
                                    "Name": "xx"
                                }
                            ]
                        },
                        "TaskId": "xx",
                        "AppId": "xx",
                        "Schema": [
                            {
                                "Type": "xx",
                                "Id": "xx",
                                "Value": "xx",
                                "Name": "xx"
                            }
                        ],
                        "Config": [
                            {
                                "Name": "xx",
                                "Value": "xx"
                            }
                        ],
                        "Id": "xx",
                        "OperatorUin": "xx",
                        "Name": "xx"
                    }
                ],
                "ExtConfig": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "Config": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "TaskName": "xx",
                "Mappings": [
                    {
                        "SourceId": "xx",
                        "SchemaMappings": [
                            {
                                "SinkSchemaId": "xx",
                                "SourceSchemaId": "xx"
                            }
                        ],
                        "SinkId": "xx",
                        "SourceSchema": [
                            {
                                "Type": "xx",
                                "Id": "xx",
                                "Value": "xx",
                                "Name": "xx"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

