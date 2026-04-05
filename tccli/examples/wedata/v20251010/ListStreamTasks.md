**Example 1: 实例1**



Input: 

```
tccli wedata ListStreamTasks --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --PageNumber 1 \
    --PageSize 10 \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskInfoSet": [
                {
                    "AppId": "251436191",
                    "BusinessLatency": null,
                    "Config": [
                        {
                            "Name": "ValidateIsCheck",
                            "Value": "false"
                        }
                    ],
                    "CreateTime": "1768114367596",
                    "CreateVersionTime": null,
                    "CreatorUin": "700002164618",
                    "CurrentSyncPosition": null,
                    "Description": null,
                    "ErrorMessage": null,
                    "ExecutorGroupName": null,
                    "ExecutorId": null,
                    "ExtConfig": [
                        {
                            "Name": "ValidateIsCheck",
                            "Value": "false"
                        }
                    ],
                    "GroupId": null,
                    "HasException": null,
                    "HasUpdateConfig": null,
                    "Incharge": "700002164618",
                    "InputDatasourceType": "MYSQL",
                    "LastRunTime": null,
                    "Mappings": [
                        {
                            "ExtConfig": [],
                            "SchemaMappings": [],
                            "SchemaNameMappings": [],
                            "SinkId": "2",
                            "SourceId": "1",
                            "SourceSchema": []
                        }
                    ],
                    "Nodes": [
                        {
                            "AppId": null,
                            "Config": [
                                {
                                    "Name": "SourceRule",
                                    "Value": "regexMatch"
                                }
                            ],
                            "ConnectionId": "0108ec75-eafb-4294-95ce-78b55a1d2b61",
                            "ConnectionType": "MYSQL",
                            "CreateTime": null,
                            "CreatorUin": null,
                            "Description": null,
                            "ExtConfig": null,
                            "Id": null,
                            "Name": null,
                            "NodeMapping": null,
                            "NodeType": "INPUT",
                            "OperatorUin": null,
                            "OwnerUin": null,
                            "Schema": null,
                            "TaskId": null,
                            "UpdateTime": null
                        }
                    ],
                    "NotExistsCheckPoint": null,
                    "NumRecordsIn": null,
                    "NumRecordsOut": null,
                    "NumRestarts": null,
                    "OperatorUin": "700002164618",
                    "OutputDatasourceType": null,
                    "OwnerUin": "700002164618",
                    "ReadPhase": null,
                    "ReaderDelay": null,
                    "SavePointId": null,
                    "SavePointPath": null,
                    "Status": 1,
                    "StopTime": null,
                    "SyncType": 1,
                    "TaskId": "ta-e72e601f",
                    "TaskName": "MYSQL_20260111_145247",
                    "TaskSubType": null,
                    "TaskVersion": null,
                    "UpdateTime": "1768114422250"
                }
            ],
            "TotalCount": 19
        },
        "RequestId": "dc47102f-128e-4e2f-b6b8-4f5bb13c8bd2"
    }
}
```

