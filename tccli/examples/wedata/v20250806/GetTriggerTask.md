**Example 1: 获取工作流调度任务详情信息**

获取工作流调度任务详情信息

Input: 

```
tccli wedata GetTriggerTask --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251124113217312
```

Output: 
```
{
    "Response": {
        "Data": {
            "TriggerTaskBaseAttribute": {
                "CreateTime": "2025-11-24 11:32:17",
                "CreateUserUin": "100028579801",
                "LastOpsTime": null,
                "LastOpsUserName": null,
                "LastUpdateTime": "2025-11-24 11:33:49",
                "LastUpdateUserName": "wenjieyao",
                "OwnerUin": "100028579801",
                "Status": "N",
                "Submit": false,
                "TaskDescription": null,
                "TaskId": "20251124113217312",
                "TaskLatestSubmitVersionNo": null,
                "TaskLatestVersionNo": null,
                "TaskName": "gallop_workflow_task_test_down",
                "TaskTypeId": 35,
                "UpdateUserUin": "100028579606",
                "WorkflowId": "d3e40dcc-bf42-4fb9-b081-b00408d478ec",
                "WorkflowName": "gallopcai_workflow"
            },
            "TriggerTaskConfiguration": {
                "BrokerIp": "any",
                "BundleId": null,
                "BundleInfo": null,
                "CodeContent": "IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMK",
                "DataCluster": null,
                "ResourceGroup": "20240222212719833743",
                "ResourceGroupName": null,
                "SourceServiceId": null,
                "SourceServiceName": null,
                "SourceServiceType": null,
                "TargetServiceId": null,
                "TargetServiceName": null,
                "TargetServiceType": null,
                "TaskExtConfigurationList": [
                    {
                        "ParamKey": "bucket",
                        "ParamValue": "wedata-fusion-dev-1257305158"
                    },
                    {
                        "ParamKey": "specLabelConfItems",
                        "ParamValue": "eyJzcGVjTGFiZWxDb25mSXRlbXMiOltdfQ=="
                    },
                    {
                        "ParamKey": "ftp.file.name",
                        "ParamValue": "/datastudio/project/1460947878944567296/默认文件夹/gallopcai_workflow/gallop_workflow_task_test_down.sh"
                    },
                    {
                        "ParamKey": "tenantId",
                        "ParamValue": "1257305158"
                    },
                    {
                        "ParamKey": "calendar_open",
                        "ParamValue": "0"
                    },
                    {
                        "ParamKey": "region",
                        "ParamValue": "ap-nanjing"
                    },
                    {
                        "ParamKey": "waitExecutionTotalTTL",
                        "ParamValue": "-1"
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
            "TriggerTaskSchedulerConfiguration": {
                "AllowRedoType": "ALL",
                "ExecutionTTLMinute": -1,
                "MaxRetryNumber": 4,
                "ParamTaskInList": null,
                "ParamTaskOutList": [
                    {
                        "ParamKey": "asadad",
                        "ParamValue": "1"
                    }
                ],
                "RetryWaitMinute": 5,
                "RunPriorityType": 6,
                "TaskOutputRegistryList": null,
                "UpstreamDependencyConfigList": [
                    {
                        "TaskId": "20251121163138956"
                    }
                ],
                "WaitExecutionTotalTTLMinute": -1
            }
        },
        "RequestId": "4bf84f37-45ab-495e-9a15-c52720209623"
    }
}
```

