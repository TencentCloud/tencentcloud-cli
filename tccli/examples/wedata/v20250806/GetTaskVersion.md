**Example 1: 成功示例**



Input: 

```
tccli wedata GetTaskVersion --cli-unfold-argument  \
    --TaskId 20250723102549746 \
    --ProjectId 1464962169590902784 \
    --VersionId 20250723102549746_20250826152851866
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApproveStatus": null,
            "ApproveTime": null,
            "ApproveUserUin": null,
            "CreateTime": "2025-08-26 15:28:52",
            "CreateUserUin": "100028578753",
            "Task": {
                "TaskBaseAttribute": {
                    "CreateTime": "2025-07-23 10:25:49",
                    "CreateUserUin": "100028578753",
                    "LastOpsTime": null,
                    "LastOpsUserName": null,
                    "LastUpdateTime": "2025-08-26 15:28:27",
                    "LastUpdateUserName": "peanutzhu",
                    "OwnerUin": "100028578753",
                    "Status": "N",
                    "Submit": false,
                    "TaskDescription": "",
                    "TaskId": "20250723102549746",
                    "TaskLatestSubmitVersionNo": null,
                    "TaskLatestVersionNo": null,
                    "TaskName": "test_shell_0723",
                    "TaskTypeId": 35,
                    "UpdateUserUin": "100028578753",
                    "WorkflowId": "6754d9ac-caf9-4278-a339-0d0f0d2e9dbd",
                    "WorkflowName": "test_0799"
                },
                "TaskConfiguration": {
                    "BrokerIp": "any",
                    "BundleId": null,
                    "BundleInfo": null,
                    "CodeContent": "IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHBlYW51dHpodQojI2NyZWF0ZSB0aW1lOiAyMDI1LTA3LTIzIDEwOjI1OjQ1CiMqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiojCiAgIHEgICAgICAg",
                    "DataCluster": "",
                    "ResourceGroup": "20240703113703331017",
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
                            "ParamValue": "https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com//datastudio/project/1464962169590902784/0_clone_cases/test_0799/test_shell_0723_20250826152851064.sh"
                        },
                        {
                            "ParamKey": "pre_dependence_config",
                            "ParamValue": "{\"configList\":[{\"taskId\":\"20250724155107573\",\"value\":\"CD\",\"pollingNullStrategy\":\"WAITING\",\"mainCyclicConfig\":\"DAY\"},{\"taskId\":\"20250723102628422\",\"value\":\"CD\",\"pollingNullStrategy\":\"WAITING\",\"mainCyclicConfig\":\"DAY\"}]}"
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
                    "TaskSchedulingParameterList": [
                        {
                            "ParamKey": "q",
                            "ParamValue": "11"
                        }
                    ],
                    "YarnQueue": null
                },
                "TaskSchedulerConfiguration": {
                    "AllowRedoType": "ALL",
                    "CalendarId": "",
                    "CalendarName": "",
                    "CalendarOpen": "0",
                    "CrontabExpression": "",
                    "CycleType": "CRONTAB_CYCLE",
                    "DownStreamDependencyConfigList": [],
                    "EndTime": "2100-01-01 23:59:59",
                    "EventListenerList": null,
                    "ExecutionEndTime": "03:59",
                    "ExecutionStartTime": "04:00",
                    "ExecutionTTL": -1,
                    "InitStrategy": "T_PLUS_0",
                    "MaxRetryAttempts": null,
                    "ParamTaskInList": null,
                    "ParamTaskOutList": null,
                    "RetryWait": 5,
                    "RunPriority": 6,
                    "ScheduleRunType": 0,
                    "ScheduleTimeZone": "UTC+4",
                    "SelfDepend": "serial",
                    "StartTime": "2025-07-25 00:00:00",
                    "TaskOutputRegistryList": null,
                    "UpstreamDependencyConfigList": [],
                    "WaitExecutionTotalTTL": "-1"
                }
            },
            "VersionId": "20250723102549746_20250826152851866",
            "VersionNum": "V30",
            "VersionRemark": "11"
        },
        "RequestId": "f0824314-eac9-4a87-bb8e-a97f07685984"
    }
}
```

