**Example 1: 示例1**



Input: 

```
tccli wedata ListStreamTaskVersionDetail --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --PageNumber 1 \
    --PageSize 10 \
    --TaskId b367db28-52be-4b97-8ba0-bfd7bfa52125
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskInfoSet": [
                {
                    "AppId": null,
                    "BusinessLatency": null,
                    "Config": [],
                    "CreateTime": "1767592822725",
                    "CreateVersionTime": null,
                    "CreatorUin": "700002164618",
                    "CurrentSyncPosition": null,
                    "Description": null,
                    "ErrorMessage": null,
                    "ExecutorGroupName": null,
                    "ExecutorId": null,
                    "ExtConfig": [],
                    "Incharge": "653",
                    "InputDatasourceType": null,
                    "LastRunTime": null,
                    "Mappings": [],
                    "Nodes": [],
                    "NotExistsCheckPoint": null,
                    "NumRecordsIn": null,
                    "NumRecordsOut": null,
                    "NumRestarts": null,
                    "OperatorUin": "700002164618",
                    "OutputDatasourceType": null,
                    "OwnerUin": null,
                    "ReadPhase": null,
                    "ReaderDelay": null,
                    "SavePointId": null,
                    "SavePointPath": null,
                    "Status": null,
                    "StopTime": null,
                    "SyncType": 1,
                    "TaskId": "b367db28-52be-4b97-8ba0-bfd7bfa52125",
                    "TaskName": "MYSQL_20260105_140003",
                    "TaskSubType": null,
                    "TaskVersion": "4f0701c12e6a",
                    "UpdateTime": "1767592822725"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "92429378-9648-4e66-ba0f-7359d76770dc"
    }
}
```

