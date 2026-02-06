**Example 1: 查看任务版本详情**

查看任务版本详情

Input: 

```
tccli wedata DescribeDsTaskVersionInfo --cli-unfold-argument  \
    --TaskId 20250506210555513 \
    --TaskVersion 12
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApproveName": null,
            "ApproveStatus": "无需审批",
            "ApproveTime": null,
            "CreateTime": "2025-05-06 21:07:35",
            "Creator": "qminliu",
            "LastSchedulerCommitTime": null,
            "TaskCycleLinkInfo": null,
            "TaskEventListener": null,
            "TaskEventPublisher": null,
            "TaskId": "20250506210555513",
            "TaskInfo": {
                "Alarm": null,
                "BrokerIp": "any",
                "ClusterId": null,
                "ConcurrentStrategy": null,
                "ContentType": null,
                "CreateTime": "2025-05-06 21:05:55",
                "Creater": "qminliu",
                "CrontabExpression": null,
                "CycleDependencyConfigList": null,
                "CycleStep": 5,
                "CycleType": "MINUTE_CYCLE",
                "DelayTime": 0,
                "DependencyConfigList": [],
                "DependencyRel": "and",
                "DependencyWorkflow": "no",
                "EndTime": "2025-05-06 23:59:59",
                "EventListenerConfig": null,
                "EventPublisherConfig": null,
                "ExecutionEndTime": "22:00",
                "ExecutionStartTime": "00:00",
                "ExecutionTTL": -1,
                "FolderId": "b43ef35b-90f1-11ed-8358-b8cef6281b20",
                "FolderName": "qminliu",
                "ImportErrMsg": null,
                "ImportResult": null,
                "InCharge": "qminliu",
                "InChargeId": "100028578885",
                "InstanceInitStrategy": "T_PLUS_0",
                "LastSchedulerCommitTime": null,
                "LastUpdate": "2025-05-06 21:07:11",
                "LeftCoordinate": 318,
                "LinkId": null,
                "MaxDateTime": null,
                "MaxRetryAttempts": 4,
                "MinDateTime": null,
                "NewOrUpdate": null,
                "NormalizedJobStartTime": "2025-05-06 00:00:00",
                "Notes": "",
                "OwnId": "100028448903",
                "ParamInList": null,
                "ParamOutList": null,
                "Params": null,
                "ProductName": "DATA_DEV",
                "ProjectId": "1474948357512937472",
                "ProjectIdent": "silicon_us_cloud",
                "ProjectName": "硅谷_调度_云_研发专用",
                "Properties": null,
                "RealWorkflowId": null,
                "RecoverFreezeStartTime": null,
                "RecycleTips": null,
                "RecycleUser": null,
                "ResourceGroup": "20240229221841125367",
                "ResourceGroupName": "wedata-auto-test-use(20240229221841125367)",
                "Retriable": 1,
                "RetryWait": 5,
                "RunPriority": 6,
                "ScheduleRunType": 0,
                "ScheduleTimeZone": "UTC+8",
                "SchedulerDesc": "",
                "ScriptChange": true,
                "SelfDepend": "serial",
                "SourceServer": null,
                "SourceServiceId": null,
                "SourceServiceName": null,
                "SourceServiceType": null,
                "StartTime": "2025-05-06 00:00:00",
                "StartupTime": 0,
                "Status": "Y",
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
                            "ParamKey": "calendar_open",
                            "ParamValue": "0"
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
                            "ParamValue": "wedata-na-sv-1257305158"
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
                            "ParamValue": "https://wedata-na-sv-1257305158.cos.accelerate.myqcloud.com//datastudio/project/1474948357512937472/qminliu/0506_wk/shell_0506_01_20250506210734798.sh"
                        },
                        {
                            "ParamKey": "tenantId",
                            "ParamValue": "1257305158"
                        },
                        {
                            "ParamKey": "region",
                            "ParamValue": "na-siliconvalley"
                        },
                        {
                            "ParamKey": "extraInfo",
                            "ParamValue": "{\"fromMapping\":false}"
                        }
                    ],
                    "TaskId": "20250506210555513"
                },
                "TaskFolderId": null,
                "TaskId": "20250506210555513",
                "TaskLinkInfo": null,
                "TaskName": "shell_0506_01",
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
                "TopCoordinate": 252,
                "TryLimit": 5,
                "UpdateTime": "2025-05-06 21:07:11",
                "UpdateUser": "qminliu",
                "UpdateUserId": "100028578885",
                "UserFileId": null,
                "UserId": "100028578885",
                "VersionDesc": "更新",
                "VirtualFlag": false,
                "VirtualTaskId": null,
                "VirtualTaskStatus": null,
                "WorkflowId": "8e7bf089-d43f-461f-9ed3-b10cf42b30ec",
                "WorkflowName": "0506_wk",
                "YarnQueue": null
            },
            "TaskInputParam": null,
            "TaskLinkInfo": null,
            "TaskOutputParam": null,
            "TaskParaInfo": null,
            "TaskRegisterOutputTable": null,
            "UpdateTime": "2025-05-06 21:07:35",
            "UsedVersion": 1,
            "VersionId": "20250506210555513_20250506210734913",
            "VersionNum": "V2",
            "VersionRemark": "1"
        },
        "RequestId": "22a065-73ab-47ba-9c4f-101cc1c2e04b"
    }
}
```

