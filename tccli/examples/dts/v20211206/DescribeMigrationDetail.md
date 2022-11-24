**Example 1: 查询某个迁移任务详情**



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
                "ObjectMode": "partial"
            },
            "ExtraAttr": [],
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
                    "Errors": [],
                    "StartTime": "2022-07-11 17:21:59",
                    "Status": "finished",
                    "StepId": "dumper",
                    "StepName": "源库导出",
                    "StepNo": 1,
                    "Warnings": []
                },
                {
                    "Errors": [],
                    "StartTime": "2022-07-11 17:22:43",
                    "Status": "finished",
                    "StepId": "loader",
                    "StepName": "数据导入",
                    "StepNo": 2,
                    "Warnings": []
                },
                {
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
            "TradeStatus": "normal"
        },
        "UpdateTime": "2022-07-11 19:53:03"
    }
}
```

