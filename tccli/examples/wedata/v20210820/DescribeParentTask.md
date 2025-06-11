**Example 1: 成功示例**



Input: 

```
tccli wedata DescribeParentTask --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --TaskId 20250606112506283
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DependencyStrategy": {
                    "PollingNullStrategy": "EXECUTING"
                },
                "MainCyclicConfig": "RANGE_DAY",
                "Offset": "-1,0",
                "ParentTask": {
                    "Alarm": null,
                    "BrokerIp": "any",
                    "ClusterId": null,
                    "ConcurrentStrategy": null,
                    "ContentType": null,
                    "CreateTime": "2025-06-06 11:26:04",
                    "Creater": "peanutzhu",
                    "CrontabExpression": "0 0 22 30 * ?",
                    "CycleDependencyConfigList": null,
                    "CycleStep": 1,
                    "CycleType": "DAY_CYCLE",
                    "DelayTime": 0,
                    "DependencyConfigList": null,
                    "DependencyRel": "and",
                    "DependencyWorkflow": "no",
                    "EndTime": "2099-12-31 23:59:59",
                    "EventListenerConfig": null,
                    "EventPublisherConfig": null,
                    "ExecutionEndTime": "23:59",
                    "ExecutionStartTime": "00:00",
                    "ExecutionTTL": -1,
                    "FolderId": null,
                    "FolderName": null,
                    "ImportErrMsg": null,
                    "ImportResult": null,
                    "InCharge": "peanutzhu",
                    "InChargeId": "100028578753",
                    "InstanceInitStrategy": "T_PLUS_0",
                    "LastSchedulerCommitTime": null,
                    "LastUpdate": "2025-06-06 16:37:58",
                    "LeftCoordinate": 325,
                    "LinkId": "19029a7b-4286-11f0-8ec8-b8599f277de5",
                    "MaxDateTime": null,
                    "MaxRetryAttempts": null,
                    "MinDateTime": null,
                    "NewOrUpdate": null,
                    "NormalizedJobStartTime": null,
                    "Notes": "",
                    "OwnId": "100028448903",
                    "ParamInList": null,
                    "ParamOutList": null,
                    "Params": null,
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1464962169590902784",
                    "ProjectIdent": null,
                    "ProjectName": "wedata数据开发",
                    "Properties": null,
                    "RealWorkflowId": null,
                    "RecoverFreezeStartTime": null,
                    "RecycleTips": null,
                    "RecycleUser": null,
                    "ResourceGroup": "20240703113703331017",
                    "ResourceGroupName": null,
                    "Retriable": 1,
                    "RetryWait": null,
                    "RunPriority": 6,
                    "ScheduleRunType": 0,
                    "ScheduleTimeZone": "UTC+8",
                    "SchedulerDesc": null,
                    "ScriptChange": false,
                    "SelfDepend": "serial",
                    "SourceServer": null,
                    "SourceServiceId": null,
                    "SourceServiceName": null,
                    "SourceServiceType": null,
                    "StartTime": "2025-06-06 00:00:00",
                    "StartupTime": 0,
                    "Status": "N",
                    "Submit": false,
                    "TargetServer": null,
                    "TargetServiceId": null,
                    "TargetServiceType": null,
                    "TaskAction": "",
                    "TaskAutoSubmit": null,
                    "TaskExt": {
                        "DryRunExtAttributes": null,
                        "DryRunParameter": null,
                        "Properties": [
                            {
                                "ParamKey": "calendar_id",
                                "ParamValue": ""
                            },
                            {
                                "ParamKey": "python_type",
                                "ParamValue": "python3"
                            },
                            {
                                "ParamKey": "data_cluster",
                                "ParamValue": ""
                            },
                            {
                                "ParamKey": "calendar_open",
                                "ParamValue": "0"
                            },
                            {
                                "ParamKey": "ExecutionTTLStrategy",
                                "ParamValue": "kill"
                            },
                            {
                                "ParamKey": "calendar_name",
                                "ParamValue": ""
                            },
                            {
                                "ParamKey": "waitExecutionTotalTTL",
                                "ParamValue": "-1"
                            },
                            {
                                "ParamKey": "bucket",
                                "ParamValue": "wedata-fusion-dev-1257305158"
                            },
                            {
                                "ParamKey": "specLabelConfItems",
                                "ParamValue": "eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ=="
                            },
                            {
                                "ParamKey": "python_sub_version",
                                "ParamValue": "python3"
                            },
                            {
                                "ParamKey": "ftp.file.name",
                                "ParamValue": "https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com/datastudio/project/1464962169590902784/0_00克隆测试/test_ceshi/test_0606_1.sh"
                            },
                            {
                                "ParamKey": "tenantId",
                                "ParamValue": "1257305158"
                            },
                            {
                                "ParamKey": "region",
                                "ParamValue": "ap-nanjing"
                            },
                            {
                                "ParamKey": "enableKerberosLogin",
                                "ParamValue": "false"
                            },
                            {
                                "ParamKey": "extraInfo",
                                "ParamValue": "{\"fromMapping\":false}"
                            }
                        ],
                        "TaskId": "20250606112604725"
                    },
                    "TaskFolderId": null,
                    "TaskId": "20250606112604725",
                    "TaskLinkInfo": null,
                    "TaskName": "test_0606_1",
                    "TaskRegisterOutputTable": null,
                    "TaskType": {
                        "BrokerParallelism": 10,
                        "CreateTime": "2022-02-12 11:13:41",
                        "DefaultAliveWait": 720,
                        "DoRedoParallelism": 10000,
                        "DowngradePriorityTries": 2,
                        "ExcludeCommonLib": false,
                        "FileType": null,
                        "InCharge": "admin",
                        "KillAble": 0,
                        "ParamList": "<parameters><parameter><name>hdpClient</name><value>/usr/hdp/current/hadoop-client</value></parameter><parameter><name>hiveClient</name><value>/usr/hdp/current/hive-client</value></parameter></parameters>",
                        "PollingSeconds": 5,
                        "PostHooks": null,
                        "RetryLimit": 5,
                        "RetryWait": 5,
                        "RunJarName": "IdexShell.jar",
                        "SelectFilePath": null,
                        "SourceServerType": null,
                        "TargetServerType": null,
                        "TaskParallelism": 10,
                        "TaskTypeExtension": null,
                        "TypeDesc": "Shell",
                        "TypeId": 35,
                        "TypeSort": "数据计算"
                    },
                    "Tasks": null,
                    "TemplateId": null,
                    "TenantId": "1315051789",
                    "TopCoordinate": 204,
                    "TryLimit": 5,
                    "UpdateTime": "2025-06-06 16:37:58",
                    "UpdateUser": "peanutzhu",
                    "UpdateUserId": "100028578753",
                    "UserFileId": null,
                    "UserId": "100028578753",
                    "VersionDesc": null,
                    "VirtualFlag": false,
                    "VirtualTaskId": null,
                    "VirtualTaskStatus": null,
                    "WorkflowId": "ab43623e-2473-413a-8c80-59e875167c96",
                    "WorkflowName": "test_ceshi",
                    "YarnQueue": null
                },
                "SonTask": null,
                "SubordinateCyclicConfig": null
            }
        ],
        "RequestId": "dd39dc67-049f-4028-b93c-78e776b01647"
    }
}
```

