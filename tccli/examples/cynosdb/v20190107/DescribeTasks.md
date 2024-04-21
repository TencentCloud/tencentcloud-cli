**Example 1: 查询任务列表**

查询任务列表

Input: 

```
tccli cynosdb DescribeTasks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "TaskList": [
            {
                "ID": 0,
                "AppId": 0,
                "ClusterId": "abc",
                "CreateTime": "abc",
                "DelayTime": "abc",
                "ErrMsg": "abc",
                "FlowId": 0,
                "Input": "abc",
                "InstanceGrpId": "abc",
                "InstanceGroupId": "abc",
                "InstanceId": "abc",
                "ObjectId": "abc",
                "ObjectType": "abc",
                "Operator": "abc",
                "Output": "abc",
                "Status": "abc",
                "TaskType": "abc",
                "TriggerTaskId": 0,
                "UpdateTime": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "ClusterName": "abc",
                "InstanceName": "abc",
                "Process": 0,
                "ModifyParamsData": [
                    {
                        "Name": "abc",
                        "OldValue": "abc",
                        "CurValue": "abc"
                    }
                ],
                "CreateClustersData": {
                    "Cpu": 0,
                    "Memory": 0,
                    "StorageLimit": 0
                },
                "RollbackData": {
                    "Cpu": 0,
                    "Memory": 0,
                    "StorageLimit": 0,
                    "OriginalClusterId": "abc",
                    "OriginalClusterName": "abc",
                    "RollbackStrategy": "abc",
                    "SnapshotTime": "abc",
                    "MinCpu": 0,
                    "MaxCpu": 0,
                    "SnapShotId": 1,
                    "RollbackDatabases": [
                        {
                            "OldDatabase": "abc",
                            "NewDatabase": "abc"
                        }
                    ],
                    "RollbackTables": [
                        {
                            "Database": "abc",
                            "Tables": [
                                {
                                    "OldTable": "abc",
                                    "NewTable": "abc"
                                }
                            ]
                        }
                    ],
                    "BackupFileName": "abc"
                },
                "ModifyInstanceData": {
                    "Cpu": 0,
                    "Memory": 0,
                    "StorageLimit": 0,
                    "OldCpu": 0,
                    "OldMemory": 0,
                    "OldStorageLimit": 0,
                    "UpgradeType": "abc"
                },
                "ManualBackupData": {
                    "BackupType": "abc",
                    "BackupMethod": "abc",
                    "SnapshotTime": "abc"
                },
                "ModifyDbVersionData": {
                    "OldVersion": "abc",
                    "NewVersion": "abc",
                    "UpgradeType": "abc"
                },
                "ClusterSlaveData": {
                    "OldMasterZone": "abc",
                    "OldSlaveZone": [
                        "abc"
                    ],
                    "NewMasterZone": "abc",
                    "NewSlaveZone": [
                        "abc"
                    ],
                    "NewSlaveZoneAttr": [
                        {
                            "Zone": "ap-guangzhou-4",
                            "BinlogSyncWay": "sync"
                        }
                    ],
                    "OldSlaveZoneAttr": [
                        {
                            "Zone": "ap-guangzhou-5",
                            "BinlogSyncWay": "async"
                        }
                    ]
                },
                "SwitchClusterLogBin": {
                    "Status": "abc"
                },
                "ModifyInstanceParamsData": {
                    "ClusterId": "abc",
                    "ClusterParamList": [
                        {
                            "ParamName": "abc",
                            "CurrentValue": "abc",
                            "OldValue": "abc"
                        }
                    ],
                    "ModifyInstanceParams": [
                        {
                            "InstanceId": "abc",
                            "ModifyInstanceParamList": [
                                {
                                    "ParamName": "abc",
                                    "CurrentValue": "abc",
                                    "OldValue": "abc"
                                }
                            ]
                        }
                    ]
                },
                "TaskMaintainInfo": {
                    "MaintainStartTime": 0,
                    "MaintainDuration": 0,
                    "MaintainWeekDays": [
                        "abc"
                    ]
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

