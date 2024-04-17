**Example 1: 查询集成任务**

查询集成任务

Input: 

```
tccli wedata DescribeIntegrationTask --cli-unfold-argument  \
    --TaskId c6f6968-97c0-4e40-b25b-8258c0170f4 \
    --ProjectId 1486446569620893696 \
    --TaskType 201 \
    --InstanceVersion 12
```

Output: 
```
{
    "Response": {
        "TaskInfo": {
            "TaskName": "testtaskname",
            "Description": "testdesc",
            "SyncType": 2,
            "TaskType": 202,
            "WorkflowId": "",
            "TaskId": "n11a6d01c-0ec6-4efc-bd14-97a921d01d3f",
            "ScheduleTaskId": "cql-hjlx38yl",
            "TaskGroupId": "a5d814828-452c-46f6-b128-19c1a3249bf0",
            "ProjectId": "1486446569620893696",
            "CreatorUin": "100022187073",
            "OperatorUin": "100022187073",
            "OwnerUin": "100022187073",
            "AppId": "1257305888",
            "Status": 3,
            "Nodes": [
                {
                    "Id": "130973",
                    "TaskId": "n11a6d01c-0ec6-4efc-bd14-97a921d01d3f",
                    "Name": "nodeTestName",
                    "NodeType": "INPUT",
                    "DataSourceType": "MYSQL",
                    "Description": "testdesc",
                    "DatasourceId": "914840",
                    "Config": [
                        {
                            "Name": "Type",
                            "Value": "MYSQL"
                        },
                        {
                            "Name": "splitPk",
                            "Value": "id"
                        },
                        {
                            "Name": "Database",
                            "Value": "databasetestname"
                        },
                        {
                            "Name": "TableNames",
                            "Value": "tabletestname"
                        },
                        {
                            "Name": "PrimaryKey",
                            "Value": "id"
                        },
                        {
                            "Name": "isNew",
                            "Value": "true"
                        },
                        {
                            "Name": "PrimaryKey_INPUT_SYMBOL",
                            "Value": "input"
                        },
                        {
                            "Name": "splitPk_INPUT_SYMBOL",
                            "Value": "input"
                        },
                        {
                            "Name": "isClean",
                            "Value": "0"
                        },
                        {
                            "Name": "encoding",
                            "Value": "utf-8"
                        }
                    ],
                    "ExtConfig": [
                        {
                            "Name": "x",
                            "Value": "300"
                        },
                        {
                            "Name": "y",
                            "Value": "260"
                        },
                        {
                            "Name": "iconPosition",
                            "Value": "left"
                        },
                        {
                            "Name": "size",
                            "Value": "m"
                        }
                    ],
                    "Schema": [
                        {
                            "Type": "String",
                            "Alias": "name",
                            "Comment": "名字",
                            "Id": "616042880",
                            "Name": "name",
                            "Value": "nihao",
                            "Properties": [
                                {
                                    "Name": "exttestname",
                                    "Value": "exttestvalue"
                                }
                            ]
                        }
                    ],
                    "NodeMapping": {
                        "SourceId": "130973",
                        "SinkId": "130972",
                        "SourceSchema": [
                            {
                                "Id": "597853056",
                                "Name": "name",
                                "Value": "test",
                                "Type": "String",
                                "Alias": "name",
                                "Comment": "名称",
                                "Properties": [
                                    {
                                        "Name": "exttestname",
                                        "Value": "exttestvalue"
                                    }
                                ]
                            }
                        ],
                        "SchemaMappings": [
                            {
                                "SourceSchemaId": "597853056",
                                "SinkSchemaId": "616042880"
                            }
                        ],
                        "ExtConfig": [
                            {
                                "Name": "Type",
                                "Value": "MYSQL"
                            }
                        ]
                    },
                    "AppId": "1315051999",
                    "ProjectId": "1486446569620893696",
                    "CreatorUin": "100028644005",
                    "OperatorUin": "100028644005",
                    "OwnerUin": "100028644005",
                    "CreateTime": "2022-05-07 10:13:21",
                    "UpdateTime": "2022-05-07 10:13:21"
                }
            ],
            "ExecutorId": "20220331190555092303",
            "Mappings": [
                {
                    "SourceId": "130973",
                    "SinkId": "130972",
                    "SourceSchema": [
                        {
                            "Id": "597853056",
                            "Name": "name",
                            "Value": "test",
                            "Type": "String",
                            "Alias": "name",
                            "Comment": "名称",
                            "Properties": [
                                {
                                    "Name": "exttestname",
                                    "Value": "exttestvalue"
                                }
                            ]
                        }
                    ],
                    "SchemaMappings": [
                        {
                            "SourceSchemaId": "597853056",
                            "SinkSchemaId": "616042880"
                        }
                    ],
                    "ExtConfig": [
                        {
                            "Name": "Type",
                            "Value": "MYSQL"
                        }
                    ]
                }
            ],
            "TaskMode": "1",
            "Incharge": "100028625403",
            "OfflineTaskAddEntity": {
                "WorkflowName": "",
                "DependencyWorkflow": "",
                "StartTime": "2024-04-10 00:00:00",
                "EndTime": "2099-12-31 00:00:00",
                "CycleType": 1,
                "CycleStep": 5,
                "DelayTime": 0,
                "CrontabExpression": "",
                "RetryWait": 3,
                "Retriable": 1,
                "TryLimit": 3,
                "RunPriority": 6,
                "ProductName": "DATA_INTEGRATION",
                "SelfDepend": 3,
                "TaskAction": "",
                "ExecutionEndTime": "23:59",
                "ExecutionStartTime": "00:00",
                "TaskAutoSubmit": true,
                "InstanceInitStrategy": "T+0"
            },
            "ExecutorGroupName": "资源组01",
            "InLongManagerUrl": "172.16.64.68:8083",
            "InLongStreamId": "f8317843e-68f9-4373-914f-241d7200a9a4",
            "InLongManagerVersion": "v17",
            "DataProxyUrl": [
                "172.16.64.68:8086"
            ],
            "Submit": true,
            "InputDatasourceType": "MYSQL",
            "OutputDatasourceType": "DLC",
            "NumRecordsIn": 1000,
            "NumRecordsOut": 1000,
            "ReaderDelay": 5,
            "NumRestarts": 2,
            "CreateTime": "2022-05-07 10:13:21",
            "UpdateTime": "2022-05-07 10:13:21",
            "LastRunTime": "2022-05-07 10:13:21",
            "StopTime": "2022-05-07 10:13:21",
            "HasVersion": true,
            "Locked": true,
            "Locker": "100022187073",
            "RunningCu": 2,
            "TaskAlarmRegularList": [
                "1769,1768"
            ],
            "SwitchResource": 1,
            "ReadPhase": 0,
            "InstanceVersion": 12,
            "ArrangeSpaceTaskId": "20230112170349643",
            "OfflineTaskStatus": 1,
            "Config": [
                {
                    "Name": "Type",
                    "Value": "MYSQL"
                }
            ],
            "ExtConfig": [
                {
                    "Name": "Type",
                    "Value": "MYSQL"
                }
            ],
            "ExecuteContext": [
                {
                    "Name": "Type",
                    "Value": "MYSQL"
                }
            ]
        },
        "AgentStatus": {
            "Running": 0,
            "Abnormal": 0,
            "InOperation": 0
        },
        "TaskVersion": {
            "InstanceVersion": 12,
            "VersionDesc": "版本描述",
            "ChangeType": 0,
            "SubmitterUin": "100006908545",
            "InstanceDate": "2022-09-29 16:40:38",
            "InstanceStatus": 0
        },
        "RequestId": "4ec1ea77-7729-47bc-b541-e73412fc5fd7"
    }
}
```

