**Example 1: 查询同步任务列表**

查询同步任务列表

Input: 

```
tccli dts DescribeSyncJobs --cli-unfold-argument  \
    --JobId sync-bkm3mppi
```

Output: 
```
{
    "Response": {
        "JobList": [
            {
                "Actions": [
                    "pause",
                    "stop",
                    "limitRate",
                    "view",
                    "resize",
                    "isolate",
                    "postPay2prePay",
                    "configureOptObj"
                ],
                "AllActions": [
                    "view",
                    "configure",
                    "check",
                    "start",
                    "stop",
                    "resume",
                    "pause",
                    "continue",
                    "limitRate",
                    "resize",
                    "isolate",
                    "offline",
                    "recover",
                    "postPay2prePay",
                    "configureOptObj",
                    "checkOptObj",
                    "startOptObj",
                    "createCmpTask"
                ],
                "AutoRenew": 0,
                "AutoRetryTimeRangeMinutes": 0,
                "CreateTime": "2023-12-18 20:55:27",
                "Detail": {
                    "CauseOfCompareDisable": "当前任务开启了DML过滤()。",
                    "CurrentStepProgress": 0,
                    "ErrInfo": {
                        "Message": "",
                        "Reason": "",
                        "Solution": ""
                    },
                    "MasterSlaveDistance": 0,
                    "Message": "",
                    "Progress": -1,
                    "SecondsBehindMaster": 0,
                    "StepAll": 4,
                    "StepInfos": [
                        {
                            "Errors": null,
                            "Progress": -1,
                            "StartTime": "2023-12-20 17:03:39",
                            "Status": "finished",
                            "StepId": "schema-init",
                            "StepName": "增量库表初始化",
                            "StepNo": 1,
                            "Warnings": []
                        },
                        {
                            "Errors": null,
                            "Progress": -1,
                            "StartTime": "2023-12-20 17:03:49",
                            "Status": "finished",
                            "StepId": "dumper",
                            "StepName": "全量导出",
                            "StepNo": 2,
                            "Warnings": []
                        },
                        {
                            "Errors": null,
                            "Progress": -1,
                            "StartTime": "2023-12-20 17:07:50",
                            "Status": "finished",
                            "StepId": "loader",
                            "StepName": "全量导入",
                            "StepNo": 3,
                            "Warnings": []
                        },
                        {
                            "Errors": null,
                            "Progress": -1,
                            "StartTime": "2023-12-20 17:16:49",
                            "Status": "running",
                            "StepId": "sinker",
                            "StepName": "同步增量",
                            "StepNo": 4,
                            "Warnings": []
                        }
                    ],
                    "StepNow": 4
                },
                "DstAccessType": "noProxy",
                "DstDatabaseType": "mysql",
                "DstInfo": {
                    "Account": "",
                    "AccountMode": "",
                    "AccountRole": "",
                    "CcnId": "",
                    "CcnOwnerUin": "",
                    "CvmInstanceId": "",
                    "DatabaseNetEnv": "",
                    "DbKernel": "",
                    "DbName": "",
                    "EncryptConn": "",
                    "EngineVersion": "",
                    "InstanceId": "",
                    "Ip": "11.141.232.156",
                    "Password": "",
                    "Port": 3306,
                    "Region": "ap-guangzhou",
                    "Role": "",
                    "RoleExternalId": "",
                    "SubnetId": "",
                    "Supplier": "",
                    "TmpSecretId": "",
                    "TmpSecretKey": "",
                    "TmpToken": "",
                    "UniqDcgId": "",
                    "UniqVpnGwId": "",
                    "User": "root",
                    "VpcId": ""
                },
                "DstInfos": {
                    "AccessType": "",
                    "DatabaseType": "",
                    "Info": null,
                    "Region": ""
                },
                "DstNodeType": "single",
                "DstRegion": "ap-qingyuan",
                "DumperResumeCtrl": "yes",
                "EndTime": "0000-00-00 00:00:00",
                "ExpectRunTime": "0000-00-00 00:00:00",
                "ExpireTime": "0000-00-00 00:00:00",
                "InstanceClass": "medium",
                "JobId": "sync-09vy1os1",
                "JobName": "roger_test",
                "Objects": {
                    "Databases": [
                        {
                            "DbMode": "All",
                            "DbName": "db_big",
                            "EventMode": "",
                            "FunctionMode": "",
                            "NewDbName": "",
                            "NewSchemaName": "",
                            "ProcedureMode": "",
                            "SchemaName": "",
                            "TableMode": "All",
                            "TriggerMode": "",
                            "ViewMode": "All"
                        }
                    ],
                    "Mode": "Partial",
                    "OnlineDDL": {
                        "Status": ""
                    }
                },
                "OfflineTime": "0000-00-00 00:00:00",
                "Options": {
                    "AddAdditionalColumn": false,
                    "AutoRetryTimeRangeMinutes": 0,
                    "ConflictHandleOption": {
                        "ConditionColumn": "",
                        "ConditionOperator": "",
                        "ConditionOrderInSrcAndDst": ""
                    },
                    "ConflictHandleType": "Cover",
                    "DdlOptions": null,
                    "DealOfExistSameTable": "ExecuteAfterIgnore",
                    "FilterBeginCommit": false,
                    "FilterCheckpoint": false,
                    "InitType": "Full",
                    "KafkaOption": {
                        "DDLTopicName": "",
                        "DataType": "",
                        "TopicRules": [],
                        "TopicType": ""
                    },
                    "OpTypes": null,
                    "RateLimitOption": {
                        "CurrentDumpRps": 0,
                        "CurrentDumpThread": 8,
                        "CurrentLoadRps": 0,
                        "CurrentLoadThread": 8,
                        "CurrentSinkerThread": 32,
                        "DefaultDumpRps": 0,
                        "DefaultDumpThread": 8,
                        "DefaultLoadRps": 0,
                        "DefaultLoadThread": 8,
                        "DefaultSinkerThread": 32,
                        "HasUserSetRateLimit": "no"
                    }
                },
                "PayMode": "PostPay",
                "RunMode": "Immediate",
                "Specification": "",
                "SrcAccessType": "noProxy",
                "SrcDatabaseType": "mysql",
                "SrcInfo": {
                    "Account": "",
                    "AccountMode": "",
                    "AccountRole": "",
                    "CcnId": "",
                    "CcnOwnerUin": "",
                    "CvmInstanceId": "",
                    "DatabaseNetEnv": "",
                    "DbKernel": "",
                    "DbName": "",
                    "EncryptConn": "",
                    "EngineVersion": "",
                    "InstanceId": "",
                    "Ip": "11.141.232.195",
                    "Password": "",
                    "Port": 3306,
                    "Region": "ap-guangzhou",
                    "Role": "",
                    "RoleExternalId": "",
                    "SubnetId": "",
                    "Supplier": "",
                    "TmpSecretId": "",
                    "TmpSecretKey": "",
                    "TmpToken": "",
                    "UniqDcgId": "",
                    "UniqVpnGwId": "",
                    "User": "root",
                    "VpcId": ""
                },
                "SrcInfos": {
                    "AccessType": "",
                    "DatabaseType": "",
                    "Info": null,
                    "Region": ""
                },
                "SrcNodeType": "single",
                "SrcRegion": "ap-qingyuan",
                "StartTime": "2023-12-19 15:54:18",
                "Status": "Running",
                "Tags": [],
                "TradeStatus": "Normal"
            }
        ],
        "RequestId": "268b0711-a3b2-4692-8c91-88d743bc8b9f",
        "TotalCount": 1
    }
}
```

