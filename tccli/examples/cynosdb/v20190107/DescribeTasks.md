**Example 1: 查询任务列表**

查询任务列表

Input: 

```
tccli cynosdb DescribeTasks --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "TaskList": [
            {
                "ID": 1,
                "AppId": 23623651237,
                "ClusterId": "cynoadbmysql-ydtwlxig",
                "CreateTime": "2024-10-01 23:22:54",
                "DelayTime": "2024-10-12 17:52:19",
                "ErrMsg": "",
                "FlowId": 6521,
                "Input": "{\"AppId\":251232125,\"uin\":\"700000433509\",\"operateUin\":\"700000433509\",\"region\":1,\"zoneId\":100007,\"dealName\":\"20240627509001289127581\",\"bigDealId\":\"20240627509001289141381\",\"tranId\":\"20240627509001289127591\",\"productCode\":\"p_cynosdb\",\"subProductCode\":\"sp_cynosdb_mysql\",\"payMode\":0,\"projectId\":0,\"goodsDetail\":{\"requestId\":\"3d56fe0b-f839-42c6-b84e-1d5fbc874cba\",\"Action\":\"CreateMultiSpecClusters\",\"pid\":1001166,\"extparam\":{\"token\":\"\"},\"timeSpan\":3600,\"timeUnit\":\"s\",\"productCode\":\"p_cynosdb\",\"subProductCode\":\"sp_cynosdb_mysql\",\"goodsNum\":1,\"sv_cynosdb_cpu_mysql\":1,\"sv_cynosdb_memory_mysql\":1,\"sv_cynosdb_cpu_smallcommoncpu\":0,\"sv_cynosdb_memory_smallcommonmem\":0,\"sv_cynosdb_cpu_largecommoncpu\":0,\"sv_cynosdb_memory_largecommonmem\":0,\"sv_cynosdb_storage_mysql\":0,\"sv_cynosdb_ccu_mysql\":0,\"resourceTags\":[{\"tagKey\":\"mockTagKey\",\"tagValue\":\"mockTagValue\"}],\"productInfo\":[{\"name\":\"配置\",\"value\":\"1核,1GB内存\"},{\"name\":\"地域\",\"value\":\"ap-guangzhou\"},{\"name\":\"可用区\",\"value\":\"ap-guangzhou-7\"}],\"zone\":\"ap-guangzhou-7\",\"source\":\"API\",\"slaveZone\":\"\",\"businessType\":\"\",\"vpcId\":\"vpc-rhfuibtt\",\"subnetId\":\"subnet-87qviva4\",\"dbType\":\"MYSQL\",\"dbVersion\":\"5.7\",\"cynosVersion\":\"\",\"clusterName\":\"后付费集群\",\"adminPassword\":\"Abcde@123\",\"port\":3306,\"count\":1,\"haCount\":0,\"instanceCount\":1,\"storageTraceId\":\"\",\"storagePayMode\":0,\"rollbackStrategy\":\"noneRollback\",\"OrderSource\":\"go_test\",\"isLhdb\":\"no\",\"lhdbAppId\":0,\"isDisableConsole\":\"no\",\"sourcePlatform\":\"\",\"clusterParams\":[{\"ParamName\":\"character_set_server\",\"CurrentValue\":\"utf8\",\"OldValue\":\"\"},{\"ParamName\":\"collation_server\",\"CurrentValue\":\"utf8_general_ci\",\"OldValue\":\"\"}],\"ParamTemplateId\":0,\"instanceType\":\"rw\",\"clusterTraceId\":\"9642a74e-fa27-4f8f-b854-653b3083c4cb\",\"outside_invisible_is_skip_trade\":\"\",\"ClusterInstanceCount\":1}}",
                "InstanceGrpId": "cynosdbmysql-grp-ywnxpisy",
                "InstanceGroupId": "cynosdbmysql-grp-ywnxpisy",
                "InstanceId": "cynosdbmysql-qjuxpows",
                "ObjectId": "cynosdbmysql-grwlskip",
                "ObjectType": "taskCreateCluster",
                "Operator": "700000433509",
                "Output": "{\"Storage\":3000}",
                "Status": "success",
                "TaskType": "taskCreateCluster",
                "TriggerTaskId": 0,
                "UpdateTime": "2024-06-27 16:18:12",
                "StartTime": "2024-06-27 16:18:07",
                "EndTime": "2024-06-27 16:18:12",
                "ClusterName": "MyClusterName",
                "InstanceName": "MyInstanceName",
                "Process": 100,
                "ModifyParamsData": [
                    {
                        "Name": "sql_auto_is_null",
                        "OldValue": "OFF",
                        "CurValue": "ON"
                    }
                ],
                "CreateClustersData": {
                    "Cpu": 1,
                    "Memory": 2,
                    "StorageLimit": 200
                },
                "RollbackData": {
                    "Cpu": 1,
                    "Memory": 2,
                    "StorageLimit": 200,
                    "OriginalClusterId": "cynosdbmysql-tiwgxyts",
                    "OriginalClusterName": "MyOriginalClusterName",
                    "RollbackStrategy": "timeRollback",
                    "SnapshotTime": "2024-05-12 11:28:55",
                    "MinCpu": 2,
                    "MaxCpu": 8,
                    "SnapShotId": 5562,
                    "RollbackDatabases": [
                        {
                            "OldDatabase": "test_database",
                            "NewDatabase": "new_test_database"
                        }
                    ],
                    "RollbackTables": [
                        {
                            "Database": "test-database",
                            "Tables": [
                                {
                                    "OldTable": "test-table-1",
                                    "NewTable": "new-test-table-1"
                                }
                            ]
                        }
                    ],
                    "BackupFileName": "cynosdbmysql-oaj6te97_20240610111357"
                },
                "ModifyInstanceData": {
                    "Cpu": 2,
                    "Memory": 4,
                    "StorageLimit": 400,
                    "OldCpu": 1,
                    "OldMemory": 2,
                    "OldStorageLimit": 200,
                    "UpgradeType": "upgradeInMaintain"
                },
                "ManualBackupData": {
                    "BackupType": "snapshot",
                    "BackupMethod": "manual",
                    "SnapshotTime": "2023-11-03 15:27:22"
                },
                "ModifyDbVersionData": {
                    "OldVersion": "3.1.11",
                    "NewVersion": "3.1.13",
                    "UpgradeType": "upgradeInMaintain"
                },
                "ClusterSlaveData": {
                    "OldMasterZone": "ap-guangzhou-4",
                    "OldSlaveZone": [
                        "ap-guangzhou-7"
                    ],
                    "NewMasterZone": "ap-guangzhou-7",
                    "NewSlaveZone": [
                        "ap-guangzhou-4"
                    ],
                    "NewSlaveZoneAttr": [
                        {
                            "Zone": "ap-guangzhou-4",
                            "BinlogSyncWay": "sync"
                        }
                    ],
                    "OldSlaveZoneAttr": [
                        {
                            "Zone": "ap-guangzhou-7",
                            "BinlogSyncWay": "async"
                        }
                    ]
                },
                "SwitchClusterLogBin": {
                    "Status": "OFF"
                },
                "ModifyInstanceParamsData": {
                    "ClusterId": "cynosdbmysql-tiwgxyts",
                    "ClusterParamList": [
                        {
                            "ParamName": "innodb_backquery_history_limit",
                            "CurrentValue": "1100",
                            "OldValue": "1000"
                        }
                    ],
                    "ModifyInstanceParams": [
                        {
                            "InstanceId": "cynosdbmysql-ins-twpmnatl",
                            "ModifyInstanceParamList": [
                                {
                                    "ParamName": "innodb_secondary_evict_only_lru",
                                    "CurrentValue": "ON",
                                    "OldValue": "OFF"
                                }
                            ]
                        }
                    ]
                },
                "TaskMaintainInfo": {
                    "MaintainStartTime": 10800,
                    "MaintainDuration": 3600,
                    "MaintainWeekDays": [
                        "Mon",
                        "Tue",
                        "Wed",
                        "Thu",
                        "Fri"
                    ]
                }
            }
        ],
        "RequestId": "3d56fe0b-f839-42c6-b84e-1d5fbc874cba"
    }
}
```

