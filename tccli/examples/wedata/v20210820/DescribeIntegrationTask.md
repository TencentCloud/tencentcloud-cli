**Example 1: 查询集成任务**

查询集成任务

Input: 

```
tccli wedata DescribeIntegrationTask --cli-unfold-argument  \
    --TaskId r8f71567c-90eb-4452-98ee-432b7d516053 \
    --ProjectId 2804706451775033344
```

Output: 
```
{
    "Response": {
        "AgentStatus": null,
        "TaskInfo": {
            "AppId": "1300298608",
            "ArrangeSpaceTaskId": null,
            "BusinessLatency": null,
            "Config": [
                {
                    "Name": "TableType",
                    "Value": "in"
                }
            ],
            "CreateTime": "2026-07-27 16:18:27",
            "CreatorUin": "700001601851",
            "CurrentSyncPosition": null,
            "DataProxyUrl": null,
            "Description": "",
            "ErrorMessage": null,
            "ExecuteContext": [],
            "ExecutorGroupName": null,
            "ExecutorId": "20260604232305097989",
            "ExtConfig": null,
            "HasVersion": true,
            "InLongManagerUrl": null,
            "InLongManagerVersion": null,
            "InLongStreamId": "",
            "Incharge": "700001815122",
            "InputDatasourceType": "MYSQL",
            "InstanceVersion": 3,
            "LastOperateInfo": {
                "CreatedTime": "2026-08-17 19:27:54",
                "ErrorMsg": null,
                "OperateId": "df73c92c-052c-4024-b7d6-dfe2a7095f1a",
                "TaskEvent": "STOP",
                "UpdatedTime": "2026-08-17 19:28:09"
            },
            "LastRunTime": null,
            "Locked": true,
            "Locker": "700001601851",
            "Mappings": null,
            "Nodes": [
                {
                    "AppId": "1300298608",
                    "Config": [
                        {
                            "Name": "StartupMode",
                            "Value": "INIT"
                        }
                    ],
                    "CreateTime": null,
                    "CreatorUin": null,
                    "DataSourceType": "MYSQL",
                    "DatasourceId": "65614",
                    "Description": null,
                    "ExtConfig": null,
                    "Id": "1",
                    "Name": "mysql_menghuiyu",
                    "NodeMapping": null,
                    "NodeType": "INPUT",
                    "OperatorUin": null,
                    "OwnerUin": "700001601851",
                    "ProjectId": "2804706451775033344",
                    "Schema": null,
                    "TaskId": "r8f71567c-90eb-4452-98ee-432b7d516053",
                    "UpdateTime": null
                }
            ],
            "NotExistsCheckPoint": null,
            "NumRecordsIn": -1,
            "NumRecordsOut": -1,
            "NumRestarts": -1,
            "OfflineTaskAddEntity": null,
            "OfflineTaskStatus": 1,
            "OperatorUin": "700001601851",
            "OutputDatasourceType": "DLC",
            "OwnerUin": "700001601851",
            "ProjectId": "2804706451775033344",
            "ReadPhase": null,
            "ReaderDelay": -1,
            "RunningCu": 0,
            "SavePointId": null,
            "SavePointPath": null,
            "ScheduleTaskId": "",
            "Status": 6,
            "StopTime": null,
            "Submit": null,
            "SwitchResource": null,
            "SyncType": 1,
            "TagList": null,
            "TaskAlarmRegularList": null,
            "TaskGroupId": "-1",
            "TaskId": "r8f71567c-90eb-4452-98ee-432b7d516053",
            "TaskImportInfo": null,
            "TaskMode": "",
            "TaskName": "test_cheneiwang2",
            "TaskType": 201,
            "UpdateTime": "2026-08-17 19:28:10",
            "WorkflowId": "-1"
        },
        "TaskVersion": null,
        "TaskVersionList": [
            {
                "InstanceDate": "2026-08-13 17:11:35",
                "RunningOrderId": 1
            }
        ],
        "RequestId": "6cbbf4d0-1b01-410d-8860-84c5d3c1be7b"
    }
}
```

