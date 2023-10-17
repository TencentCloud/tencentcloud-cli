**Example 1: 查询集成任务**

查询集成任务

Input: 

```
tccli wedata DescribeIntegrationTask --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId abc \
    --TaskType 1 \
    --InstanceVersion 0
```

Output: 
```
{
    "Response": {
        "TaskInfo": {
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
                            "Alias": "abc",
                            "Comment": "abc"
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
                                "Alias": "abc",
                                "Comment": "abc",
                                "Properties": [
                                    {
                                        "Name": "abc",
                                        "Value": "abc"
                                    }
                                ]
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
                            "Alias": "abc",
                            "Comment": "abc",
                            "Properties": [
                                {
                                    "Name": "abc",
                                    "Value": "abc"
                                }
                            ]
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
                "ExecutionStartTime": "abc",
                "TaskAutoSubmit": true,
                "InstanceInitStrategy": "abc"
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
            ],
            "SwitchResource": 0,
            "ReadPhase": 0,
            "InstanceVersion": 0,
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
            "ExecuteContext": [
                {
                    "Name": "abc",
                    "Value": "abc"
                }
            ]
        },
        "AgentStatus": {
            "Running": 0,
            "Abnormal": 0,
            "InOperation": 0
        },
        "TaskVersion": {
            "InstanceVersion": 0,
            "VersionDesc": "abc",
            "ChangeType": 0,
            "SubmitterUin": "abc",
            "InstanceDate": "abc",
            "InstanceStatus": 0
        },
        "RequestId": "abc"
    }
}
```

