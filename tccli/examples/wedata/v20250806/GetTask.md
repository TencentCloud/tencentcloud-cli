**Example 1: 获取任务详情**

获取任务详情

Input: 

```
tccli wedata GetTask --cli-unfold-argument  \
    --ProjectId 2417334454903762944 \
    --TaskId 20250908225847483
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskBaseAttribute": {
                "CreateTime": "2025-09-08 22:58:47",
                "CreateUserUin": "100028579801",
                "LastOpsTime": null,
                "LastOpsUserName": null,
                "LastUpdateTime": "2025-09-10 16:29:22",
                "LastUpdateUserName": "zhanglin",
                "OwnerUin": "100028579801",
                "Status": "N",
                "Submit": false,
                "TaskDescription": "",
                "TaskId": "20250908225847483",
                "TaskLatestSubmitVersionNo": null,
                "TaskLatestVersionNo": "V22",
                "TaskName": "sh_241204_111248_copy",
                "TaskTypeId": 35,
                "UpdateUserUin": "100028579801",
                "WorkflowId": "a5acf635-a297-458d-a311-14745662dcae",
                "WorkflowName": "wf_ssh_test_01"
            },
            "TaskConfiguration": {
                "BrokerIp": "any",
                "BundleId": null,
                "BundleInfo": null,
                "CodeContent": "IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMK",
                "DataCluster": "",
                "ResourceGroup": "20240416215649571819",
                "ResourceGroupName": null,
                "SourceServiceId": null,
                "SourceServiceName": null,
                "SourceServiceType": null,
                "TargetServiceId": null,
                "TargetServiceName": null,
                "TargetServiceType": null,
                "TaskExtConfigurationList": [
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
                        "ParamKey": "calendar_name",
                        "ParamValue": ""
                    },
                    {
                        "ParamKey": "waitExecutionTotalTTL",
                        "ParamValue": "-1"
                    },
                    {
                        "ParamKey": "executionTTLStrategy",
                        "ParamValue": "fail"
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
                        "ParamKey": "waitExecutionTotalTTLStrategy",
                        "ParamValue": "fail"
                    },
                    {
                        "ParamKey": "python_sub_version",
                        "ParamValue": "python3"
                    },
                    {
                        "ParamKey": "ftp.file.name",
                        "ParamValue": "https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com/datastudio/project/2417334454903762944/case_ssh/wf_ssh_test_01/sh_241204_111248_20250908225847483.sh"
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
                "TaskSchedulingParameterList": [],
                "YarnQueue": null
            },
            "TaskSchedulerConfiguration": {
                "AllowRedoType": "ALL",
                "CalendarId": "",
                "CalendarName": "",
                "CalendarOpen": "0",
                "CrontabExpression": "0 0 0 * * ? *",
                "CycleType": "DAY_CYCLE",
                "DownStreamDependencyConfigList": [],
                "EndTime": "2099-12-31 23:59:59",
                "EventListenerList": [
                    {
                        "EventBroadcastType": "BROADCAST",
                        "EventName": "event_241030",
                        "EventSubType": "DAY",
                        "PropertiesList": null
                    }
                ],
                "ExecutionEndTime": "23:59",
                "ExecutionStartTime": "00:00",
                "ExecutionTTL": -1,
                "InitStrategy": "T_PLUS_0",
                "MaxRetryAttempts": 4,
                "ParamTaskInList": [
                    {
                        "FromParamKey": "taskout_v1",
                        "FromTaskId": "20241204111252781",
                        "ParamDesc": "DATA_DEV_SIM_PROJ_01.sh_241204_111248.taskout_v1",
                        "ParamKey": "intask_v"
                    }
                ],
                "ParamTaskOutList": [
                    {
                        "ParamKey": "asadad",
                        "ParamValue": "1"
                    }
                ],
                "RetryWait": 5,
                "RunPriority": 6,
                "ScheduleRunType": 0,
                "ScheduleTimeZone": "UTC+8",
                "SelfDepend": "serial",
                "StartTime": "2024-12-04 00:00:00",
                "TaskOutputRegistryList": null,
                "UpstreamDependencyConfigList": [
                    {
                        "DependencyStrategy": {
                            "PollingNullStrategy": "WAITING",
                            "TaskDependencyExecutingStrategies": null,
                            "TaskDependencyExecutingTimeoutValue": null
                        },
                        "MainCyclicConfig": "DAY",
                        "Offset": null,
                        "SubordinateCyclicConfig": "CURRENT_DAY",
                        "TaskId": "20241204111252781"
                    }
                ],
                "WaitExecutionTotalTTL": "-1"
            }
        },
        "RequestId": "b195b143-3336-403c-9cfb-dd1db04fedc3"
    }
}
```

