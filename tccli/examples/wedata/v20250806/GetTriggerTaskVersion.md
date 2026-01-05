**Example 1: 查询工作流调度任务指定提交版本**

查询工作流调度任务指定提交版本

Input: 

```
tccli wedata GetTriggerTaskVersion --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251121163138956 \
    --VersionId 20251121163138956_20251124175701621
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApproveStatus": null,
            "ApproveTime": null,
            "ApproveUserUin": null,
            "CreateTime": "2025-11-24 17:57:02",
            "CreateUserUin": "100028579606",
            "Task": {
                "TriggerTaskBaseAttribute": {
                    "CreateTime": "2025-11-21 16:31:39",
                    "CreateUserUin": "100028579606",
                    "LastOpsTime": null,
                    "LastOpsUserName": null,
                    "LastUpdateTime": "2025-11-24 17:52:47",
                    "LastUpdateUserName": "gallopcai",
                    "OwnerUin": "100028579606",
                    "Status": "Y",
                    "Submit": true,
                    "TaskDescription": "",
                    "TaskId": "20251121163138956",
                    "TaskLatestSubmitVersionNo": null,
                    "TaskLatestVersionNo": null,
                    "TaskName": "gallop_workflow_task_test",
                    "TaskTypeId": 35,
                    "UpdateUserUin": "100028660434",
                    "WorkflowId": "d3e40dcc-bf42-4fb9-b081-b00408d478ec",
                    "WorkflowName": "gallopcai_workflow"
                },
                "TriggerTaskConfiguration": {
                    "BrokerIp": "any",
                    "BundleId": null,
                    "BundleInfo": null,
                    "CodeContent": "IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMK",
                    "DataCluster": "",
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
                            "ParamValue": ""
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
                            "ParamValue": "python3.11"
                        },
                        {
                            "ParamKey": "ftp.file.name",
                            "ParamValue": "https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com//datastudio/project/1460947878944567296/默认文件夹/gallopcai_workflow/gallop_workflow_task_test_20251124175700990.sh"
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
                "TriggerTaskSchedulerConfiguration": {
                    "AllowRedoType": "ALL",
                    "ParamTaskInList": null,
                    "ParamTaskOutList": [
                        {
                            "ParamKey": "asadad",
                            "ParamValue": "1"
                        }
                    ],
                    "TaskOutputRegistryList": null,
                    "UpstreamDependencyConfigList": []
                }
            },
            "VersionId": "20251121163138956_20251124175701621",
            "VersionNum": "V3",
            "VersionRemark": "submit_test_2"
        },
        "RequestId": "57965292-32c2-4480-8fe9-10a01fc0d9fa"
    }
}
```

**Example 2: 查询工作流调度任务最新的提交版本**

查询工作流调度任务最新的提交版本

Input: 

```
tccli wedata GetTriggerTaskVersion --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251121163138956
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApproveStatus": null,
            "ApproveTime": null,
            "ApproveUserUin": null,
            "CreateTime": "2025-11-24 18:05:47",
            "CreateUserUin": "100028579606",
            "Task": {
                "TriggerTaskBaseAttribute": {
                    "CreateTime": "2025-11-21 16:31:39",
                    "CreateUserUin": "100028579606",
                    "LastOpsTime": null,
                    "LastOpsUserName": null,
                    "LastUpdateTime": "2025-11-24 17:52:47",
                    "LastUpdateUserName": "gallopcai",
                    "OwnerUin": "100028579606",
                    "Status": "Y",
                    "Submit": true,
                    "TaskDescription": "",
                    "TaskId": "20251121163138956",
                    "TaskLatestSubmitVersionNo": null,
                    "TaskLatestVersionNo": null,
                    "TaskName": "gallop_workflow_task_test",
                    "TaskTypeId": 35,
                    "UpdateUserUin": "100028660434",
                    "WorkflowId": "d3e40dcc-bf42-4fb9-b081-b00408d478ec",
                    "WorkflowName": "gallopcai_workflow"
                },
                "TriggerTaskConfiguration": {
                    "BrokerIp": "any",
                    "BundleId": null,
                    "BundleInfo": null,
                    "CodeContent": "IyEvYmluL2Jhc2gKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMKIyNhdXRob3I6IHpoYW5nbGluCiMjY3JlYXRlIHRpbWU6IDIwMjQtMTItMDQgMTE6MTI6NDkKIyoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiMK",
                    "DataCluster": "",
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
                            "ParamValue": ""
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
                            "ParamValue": "python3.11"
                        },
                        {
                            "ParamKey": "ftp.file.name",
                            "ParamValue": "https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com//datastudio/project/1460947878944567296/默认文件夹/gallopcai_workflow/gallop_workflow_task_test_20251124180545470.sh"
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
                "TriggerTaskSchedulerConfiguration": {
                    "AllowRedoType": "ALL",
                    "ParamTaskInList": null,
                    "ParamTaskOutList": [
                        {
                            "ParamKey": "asadad",
                            "ParamValue": "1"
                        }
                    ],
                    "TaskOutputRegistryList": null,
                    "UpstreamDependencyConfigList": []
                }
            },
            "VersionId": "20251121163138956_20251124180546791",
            "VersionNum": "V4",
            "VersionRemark": "submit_test_2"
        },
        "RequestId": "a4f219cb-5404-43b4-9a98-50c750a657ad"
    }
}
```

