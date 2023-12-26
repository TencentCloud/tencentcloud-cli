**Example 1: 查询某个迁移任务详情**

查询某个迁移任务详情

Input: 

```
tccli dts DescribeMigrationDetail --cli-unfold-argument  \
    --JobId dts-amm1jw5q
```

Output: 
```
{
    "Response": {
        "Action": {
            "AllAction": [
                "view",
                "modify",
                "check",
                "start",
                "configure",
                "stop",
                "complete",
                "resume",
                "createCmpTask",
                "isolate",
                "offline",
                "resize",
                "recover"
            ],
            "AllowedAction": [
                "view",
                "stop",
                "complete",
                "createCmpTask",
                "view",
                "isolate",
                "resize"
            ]
        },
        "CheckStepInfo": {
            "EndAt": "2022-07-11 17:19:25",
            "Progress": {
                "Message": "success",
                "Percent": 100,
                "Status": "success",
                "StepAll": 12,
                "Steps": [
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "ConnectDBCheck",
                        "StepMessage": "",
                        "StepName": "连接DB检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "VersionCheck",
                        "StepMessage": "",
                        "StepName": "版本检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "SrcPrivilegeCheck",
                        "StepMessage": "",
                        "StepName": "源实例权限检查",
                        "StepNo": 0,
                        "Warnings": [
                            {
                                "HelpDoc": "",
                                "Message": "您的授权情况：GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, PROCESS, REFERENCES, INDEX, ALTER, SHOW DATABASES, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE ON *.* TO 'root'@'%' WITH GRANT OPTION。 源端账号权限范围大于要求的账号权限范围，腾讯云DTS不会使用超过必要的权限，请按照最小化原则给与授权: https://cloud.tencent.com/document/product/571/58700",
                                "Solution": ""
                            }
                        ]
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "SimpleParamCheck",
                        "StepMessage": "",
                        "StepName": "部分实例参数检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "DstPrivilegeCheck",
                        "StepMessage": "",
                        "StepName": "目标实例权限检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "DstEmptyCheck",
                        "StepMessage": "",
                        "StepName": "目标实例内容冲突检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "DstSpaceCheck",
                        "StepMessage": "",
                        "StepName": "目标实例空间检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "BinlogParamCheck",
                        "StepMessage": "",
                        "StepName": "binlog参数检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "ConstraintCheck",
                        "StepMessage": "",
                        "StepName": "外键依赖检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "ConstraintRefCheck",
                        "StepMessage": "",
                        "StepName": "外键部分库表依赖检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "ViewCheck",
                        "StepMessage": "",
                        "StepName": "视图检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 100,
                        "StartTime": "",
                        "Status": "finished",
                        "StepId": "WarningParamCheck",
                        "StepMessage": "",
                        "StepName": "警告项检查",
                        "StepNo": 0,
                        "Warnings": []
                    },
                    {
                        "Errors": [],
                        "Percent": 0,
                        "StartTime": "",
                        "Status": "skipped",
                        "StepId": "OptimizeCheck",
                        "StepMessage": "",
                        "StepName": "周边检查",
                        "StepNo": 0,
                        "Warnings": [
                            {
                                "HelpDoc": "",
                                "Message": "skipped",
                                "Solution": ""
                            }
                        ]
                    }
                ],
                "StepNow": 12
            },
            "StartAt": "2022-07-11 17:18:57"
        },
        "CompareTask": {
            "CompareTaskId": "dts-amm1jw5q-cmp-bmuum7jk",
            "Status": "consistent"
        },
        "CreateTime": "2022-07-11 16:20:49",
        "DstInfo": {
            "AccessType": "cdb",
            "DatabaseType": "mysql",
            "ExtraAttr": [],
            "Info": [
                {
                    "Account": "",
                    "AccountMode": "",
                    "AccountRole": "",
                    "CcnGwId": "",
                    "CvmInstanceId": "",
                    "DbKernel": "",
                    "EngineVersion": "",
                    "Host": "",
                    "InstanceId": "cdb-o7uph0cj",
                    "Password": "xxx",
                    "Port": 0,
                    "Role": "",
                    "SubnetId": "",
                    "TmpSecretId": "",
                    "TmpSecretKey": "",
                    "TmpToken": "",
                    "UniqDcgId": "",
                    "UniqVpnGwId": "",
                    "User": "root",
                    "VpcId": ""
                }
            ],
            "NodeType": "simple",
            "Region": "ap-guangzhou",
            "Supplier": ""
        },
        "EndTime": "0000-00-00 00:00:00",
        "ErrorInfo": [],
        "ExpectRunTime": "2022-07-11 17:16:50",
        "JobId": "dts-amm1jw5q",
        "JobName": "test_config_api",
        "BriefMsg": "",
        "MigrateOption": {
            "Consistency": {
                "Mode": "full"
            },
            "DatabaseTable": {
                "Databases": [
                    {
                        "DBMode": "partial",
                        "DbName": "big100",
                        "EventMode": "",
                        "FunctionMode": "",
                        "NewDbName": "",
                        "NewSchemaName": "",
                        "ProcedureMode": "",
                        "RoleMode": "",
                        "Roles": [],
                        "SchemaMode": "",
                        "SchemaName": "",
                        "TableMode": "partial",
                        "Tables": [
                            {
                                "NewTableName": "",
                                "TableEditMode": "",
                                "TableName": "sbtest1",
                                "TmpTables": []
                            },
                            {
                                "NewTableName": "new_sbtest10",
                                "TableEditMode": "rename",
                                "TableName": "sbtest10",
                                "TmpTables": []
                            },
                            {
                                "NewTableName": "",
                                "TableEditMode": "",
                                "TableName": "sbtest100",
                                "TmpTables": []
                            }
                        ],
                        "TriggerMode": "",
                        "ViewMode": "none",
                        "Views": []
                    },
                    {
                        "DBMode": "all",
                        "DbName": "db1",
                        "EventMode": "",
                        "FunctionMode": "",
                        "NewDbName": "",
                        "NewSchemaName": "",
                        "ProcedureMode": "",
                        "RoleMode": "",
                        "Roles": [],
                        "SchemaMode": "",
                        "SchemaName": "",
                        "TableMode": "",
                        "Tables": [],
                        "TriggerMode": "",
                        "ViewMode": "",
                        "Views": []
                    }
                ],
                "AdvancedObjects": [
                    "function"
                ],
                "ObjectMode": "partial"
            },
            "ExtraAttr": [],
            "IsMigrateAccount": false,
            "IsDstReadOnly": false,
            "IsOverrideRoot": false,
            "MigrateType": "fullAndIncrement"
        },
        "RequestId": "ac300ff0-00f2-11ed-b005-4930e69d89c2",
        "RunMode": "immediate",
        "SrcInfo": {
            "AccessType": "intranet",
            "DatabaseType": "mysql",
            "ExtraAttr": [],
            "Info": [
                {
                    "Account": "",
                    "AccountMode": "",
                    "AccountRole": "",
                    "CcnGwId": "",
                    "CvmInstanceId": "",
                    "DbKernel": "",
                    "EngineVersion": "5.7",
                    "Host": "9.123.456.789",
                    "InstanceId": "",
                    "Password": "xxx",
                    "Port": 31035,
                    "Role": "",
                    "SubnetId": "",
                    "TmpSecretId": "",
                    "TmpSecretKey": "",
                    "TmpToken": "",
                    "UniqDcgId": "",
                    "UniqVpnGwId": "",
                    "User": "root",
                    "VpcId": ""
                }
            ],
            "NodeType": "simple",
            "Region": "ap-guangzhou",
            "Supplier": ""
        },
        "StartTime": "2022-07-11 17:20:56",
        "Status": "readyComplete",
        "StepInfo": {
            "MasterSlaveDistance": 0,
            "SecondsBehindMaster": 0,
            "StepAll": 3,
            "StepInfo": [
                {
                    "StepMessage": "",
                    "Percent": 100,
                    "Errors": [],
                    "StartTime": "2022-07-11 17:21:59",
                    "Status": "finished",
                    "StepId": "dumper",
                    "StepName": "源库导出",
                    "StepNo": 1,
                    "Warnings": []
                },
                {
                    "StepMessage": "",
                    "Percent": 100,
                    "Errors": [],
                    "StartTime": "2022-07-11 17:22:43",
                    "Status": "finished",
                    "StepId": "loader",
                    "StepName": "数据导入",
                    "StepNo": 2,
                    "Warnings": []
                },
                {
                    "StepMessage": "",
                    "Percent": 100,
                    "Errors": [],
                    "StartTime": "2022-07-11 17:23:26",
                    "Status": "running",
                    "StepId": "sinker",
                    "StepName": "同步增量",
                    "StepNo": 3,
                    "Warnings": []
                }
            ],
            "StepNow": 3
        },
        "Tags": [],
        "TradeInfo": {
            "BillingType": "billing",
            "DealName": "20220711715001047929481",
            "ExpireTime": "0000-00-00 00:00:00",
            "InstanceClass": "xlarge",
            "IsolateReason": "",
            "LastDealName": "",
            "OfflineReason": "",
            "PayType": "postpay",
            "TradeStatus": "normal",
            "OfflineTime": "",
            "IsolateTime": ""
        },
        "UpdateTime": "2022-07-11 19:53:03",
        "DumperResumeCtrl": "no"
    }
}
```

