**Example 1: 实例1**



Input: 

```
tccli wedata GetStreamTask --cli-unfold-argument  \
    --TaskId ta-ad218e6d \
    --WorkspaceId 17663856806379896 \
    --TaskVersion tv-c54d0523
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskInfo": {
                "AppId": "251436191",
                "Config": [
                    {
                        "Name": "ValidateIsCheck",
                        "Value": "false"
                    }
                ],
                "CreateTime": "1769675327964",
                "CreatorName": "",
                "CreatorUin": "700002164618",
                "Description": "",
                "ExecutorId": "res-794330dd",
                "ExtConfig": [
                    {
                        "Name": "ValidateIsCheck",
                        "Value": "false"
                    }
                ],
                "Incharge": "700002164618",
                "InputConnectionId": "fac52c67-86f7-4a78-b7b5-eb9042e2d01b",
                "InputConnectionIds": [
                    "fac52c67-86f7-4a78-b7b5-eb9042e2d01b"
                ],
                "InputConnectionName": "kafka",
                "InputConnectionNames": [
                    "kafka"
                ],
                "InputConnectionType": "KAFKA",
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
                        "AppId": "",
                        "Config": [
                            {
                                "Name": "SchemaMatchRule",
                                "Value": "fromSource"
                            }
                        ],
                        "ConnectionId": "c4",
                        "ConnectionType": "TCLake",
                        "CreateTime": "8874",
                        "CreatorUin": "",
                        "Description": "",
                        "ExtConfig": [],
                        "Id": "",
                        "Name": "",
                        "NodeMapping": {
                            "ExtConfig": [],
                            "SchemaMappings": [
                                {
                                    "SinkSchemaId": "354",
                                    "SourceSchemaId": "354"
                                }
                            ],
                            "SchemaNameMappings": [
                                {
                                    "SinkSchemaName": "354",
                                    "SourceSchemaName": "354"
                                }
                            ],
                            "SinkId": "354",
                            "SourceId": "354",
                            "SourceSchema": [
                                {
                                    "Alias": "354",
                                    "Category": "354",
                                    "Comment": "354",
                                    "Id": "354",
                                    "Name": "354",
                                    "Properties": [],
                                    "Type": "354",
                                    "Value": "354"
                                }
                            ]
                        },
                        "NodeType": "OUTPUT",
                        "OperatorUin": "",
                        "OwnerUin": "",
                        "Schema": [],
                        "TaskId": "",
                        "UpdateTime": "8874",
                        "WorkspaceId": "8874"
                    }
                ],
                "OperatorUin": "700002164618",
                "OutputConnectionType": "TCLake",
                "OwnerUin": "700002164618",
                "Status": 1,
                "SyncType": 1,
                "TaskId": "ta-ad218e6d",
                "TaskName": "KAFKA_20260129_162647",
                "TaskVersion": "tv-c54d0523",
                "UpdateTime": "1769675327964",
                "UpdaterName": ""
            }
        },
        "RequestId": "7e9ead51-6d8e-4a91-b193-e49572c59b9d"
    }
}
```

