**Example 1: 查询集成任务列表**

查询集成任务列表

Input: 

```
tccli wedata DescribeIntegrationTasks --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --ProjectId abc \
    --OrderFields.0.Name abc \
    --OrderFields.0.Direction abc \
    --StartTime abc \
    --EndTime abc \
    --PageNumber 0 \
    --PageSize 0 \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "TaskInfoSet": [
            {
                "TaskGroupId": "abc",
                "Status": 0,
                "WorkflowId": "abc",
                "Description": "abc",
                "CreatorUin": "abc",
                "SyncType": 0,
                "ProjectId": "abc",
                "OwnerUin": "abc",
                "ExecuteContext": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "ScheduleTaskId": "abc",
                "TaskType": 0,
                "AppId": "abc",
                "ExecutorId": "abc",
                "TaskId": "abc",
                "OperatorUin": "abc",
                "Nodes": [
                    {
                        "NodeType": "abc",
                        "Description": "abc",
                        "CreatorUin": "abc",
                        "DataSourceType": "abc",
                        "ProjectId": "abc",
                        "OwnerUin": "abc",
                        "ExtConfig": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "DatasourceId": "abc",
                        "NodeMapping": {
                            "SourceId": "abc",
                            "SchemaMappings": [
                                {
                                    "SinkSchemaId": "abc",
                                    "SourceSchemaId": "abc"
                                }
                            ],
                            "SinkId": "abc",
                            "SourceSchema": [
                                {
                                    "Type": "abc",
                                    "Id": "abc",
                                    "Value": "abc",
                                    "Name": "abc"
                                }
                            ]
                        },
                        "TaskId": "abc",
                        "AppId": "abc",
                        "Schema": [
                            {
                                "Type": "abc",
                                "Id": "abc",
                                "Value": "abc",
                                "Name": "abc"
                            }
                        ],
                        "Config": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "Id": "abc",
                        "OperatorUin": "abc",
                        "Name": "abc"
                    }
                ],
                "ExtConfig": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "Config": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "TaskName": "abc",
                "Mappings": [
                    {
                        "SourceId": "abc",
                        "SchemaMappings": [
                            {
                                "SinkSchemaId": "abc",
                                "SourceSchemaId": "abc"
                            }
                        ],
                        "SinkId": "abc",
                        "SourceSchema": [
                            {
                                "Type": "abc",
                                "Id": "abc",
                                "Value": "abc",
                                "Name": "abc"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: DescribeIntegrationTasks**

DescribeIntegrationTasks

Input: 

```
tccli wedata DescribeIntegrationTasks --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --ProjectId abc \
    --OrderFields.0.Name abc \
    --OrderFields.0.Direction abc \
    --StartTime abc \
    --EndTime abc \
    --PageNumber 0 \
    --PageSize 0 \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "TaskInfoSet": [
            {
                "TaskName": "abc",
                "Description": "abc",
                "SyncType": 0,
                "TaskType": 0,
                "WorkflowId": "abc",
                "TaskId": "abc",
                "ScheduleTaskId": "abc",
                "TaskGroupId": "abc",
                "ProjectId": "abc",
                "CreatorUin": "abc",
                "OperatorUin": "abc",
                "OwnerUin": "abc",
                "AppId": "abc",
                "Status": 0,
                "Nodes": [
                    {
                        "Id": "abc",
                        "TaskId": "abc",
                        "Name": "abc",
                        "NodeType": "abc",
                        "DataSourceType": "abc",
                        "Description": "abc",
                        "DatasourceId": "abc",
                        "Config": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "ExtConfig": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "Schema": [
                            {
                                "Id": "abc",
                                "Name": "abc",
                                "Value": "abc",
                                "Type": "abc",
                                "Properties": [
                                    {
                                        "Name": "abc",
                                        "Value": "abc"
                                    }
                                ],
                                "Alias": "abc"
                            }
                        ],
                        "NodeMapping": {
                            "SourceId": "abc",
                            "SinkId": "abc",
                            "SourceSchema": [
                                {
                                    "Id": "abc",
                                    "Name": "abc",
                                    "Value": "abc",
                                    "Type": "abc",
                                    "Alias": "abc"
                                }
                            ],
                            "SchemaMappings": [
                                {
                                    "SourceSchemaId": "abc",
                                    "SinkSchemaId": "abc"
                                }
                            ]
                        },
                        "AppId": "abc",
                        "ProjectId": "abc",
                        "CreatorUin": "abc",
                        "OperatorUin": "abc",
                        "OwnerUin": "abc",
                        "CreateTime": "abc",
                        "UpdateTime": "abc"
                    }
                ],
                "ExecutorId": "abc",
                "Mappings": [
                    {
                        "SourceId": "abc",
                        "SinkId": "abc",
                        "SourceSchema": [
                            {
                                "Id": "abc",
                                "Name": "abc",
                                "Value": "abc",
                                "Type": "abc",
                                "Alias": "abc"
                            }
                        ],
                        "SchemaMappings": [
                            {
                                "SourceSchemaId": "abc",
                                "SinkSchemaId": "abc"
                            }
                        ]
                    }
                ],
                "TaskMode": "abc",
                "Incharge": "abc",
                "OfflineTaskAddEntity": {
                    "WorkflowName": "abc",
                    "DependencyWorkflow": "abc",
                    "StartTime": "abc",
                    "EndTime": "abc",
                    "CycleType": 1,
                    "CycleStep": 1,
                    "DelayTime": 1,
                    "CrontabExpression": "abc",
                    "RetryWait": 1,
                    "Retriable": 1,
                    "TryLimit": 1,
                    "RunPriority": 1,
                    "ProductName": "abc",
                    "SelfDepend": 1,
                    "TaskAction": "abc",
                    "ExecutionEndTime": "abc",
                    "ExecutionStartTime": "abc"
                },
                "ExecutorGroupName": "abc",
                "InLongManagerUrl": "abc",
                "InLongStreamId": "abc",
                "InLongManagerVersion": "abc",
                "DataProxyUrl": [
                    "abc"
                ],
                "Submit": true,
                "InputDatasourceType": "abc",
                "OutputDatasourceType": "abc",
                "NumRecordsIn": 0,
                "NumRecordsOut": 0,
                "ReaderDelay": 0,
                "NumRestarts": 0,
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "LastRunTime": "abc",
                "StopTime": "abc",
                "HasVersion": true,
                "Locked": true,
                "Locker": "abc",
                "RunningCu": 0,
                "TaskAlarmRegularList": [
                    "abc"
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

