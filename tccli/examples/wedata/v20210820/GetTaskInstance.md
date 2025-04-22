**Example 1: 示例 一**

获取实例详情示例

Input: 

```
tccli wedata GetTaskInstance --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --InstanceKey 20250326150742906_2025-03-28 00:00:00 \
    --ScheduleTimeZone UTC+6
```

Output: 
```
{
    "Response": {
        "Data": {
            "CostTime": "00:00:12.000",
            "CurRunDate": "2025-03-28 00:00:00",
            "EndTime": "2025-03-27 22:18:55",
            "ExecutorGroupId": "20240222212719833743",
            "ExecutorGroupName": "qfh_test",
            "FolderId": "2493fc25-643d-11ef-8ec8-b8599f277de5",
            "FolderName": "dylandlwu",
            "InChargeList": [
                "dylandlwu"
            ],
            "InstanceKey": "20250326150742906_2025-03-28 00:00:00",
            "InstanceLifeCycleList": [
                {
                    "BrokerIp": "ins-6m365yvb",
                    "CodeFileName": null,
                    "CostTime": "-11",
                    "ExecutionJobId": "6820250328000318055",
                    "InstanceKey": "20250326150742906_2025-03-28 00:00:00",
                    "InstanceState": 2,
                    "LifeCycleDetailList": [
                        {
                            "DetailState": "COMPLETE",
                            "EndTime": null,
                            "StartTime": "2025-03-27 22:18:59",
                            "State": null
                        },
                        {
                            "DetailState": "RUNNING",
                            "EndTime": "2025-03-27 22:18:59",
                            "StartTime": "2025-03-27 22:18:43",
                            "State": null
                        },
                        {
                            "DetailState": "WAIT_RUN",
                            "EndTime": "2025-03-27 22:18:43",
                            "StartTime": "2025-03-27 22:02:58",
                            "State": null
                        },
                        {
                            "DetailState": "WAIT_UPSTREAM",
                            "EndTime": "2025-03-27 22:02:58",
                            "StartTime": "2025-03-27 22:02:44",
                            "State": null
                        }
                    ],
                    "LifeRoundNum": 0,
                    "LogType": null,
                    "OriginFileName": null,
                    "RunType": "PERIODIC",
                    "Tries": 0
                }
            ],
            "InstanceState": 2,
            "InstanceType": null,
            "LatestLog": {
                "BrokerIp": "ins-6m365yvb",
                "CodeFileSize": "1 KB",
                "CodeInfo": "echo this is log demo;",
                "EndTime": "2025-03-27 22:18:59",
                "ExtInfo": "45308",
                "InstanceKey": "20250326150742906_2025-03-28 00:00:00",
                "InstanceState": 2,
                "IsEnd": true,
                "LineCount": 331,
                "LogFileSize": "1 KB",
                "LogInfo": "2025-03-28 00:18:37 this is log demo",
                "ProjectId": "1460947878944567296",
                "RunType": "PERIODIC",
                "StartTime": "2025-03-27 22:18:43"
            },
            "NextCurDate": "2025-03-28 00:20:00",
            "ProjectId": "1460947878944567296",
            "SchedulerTime": "2025-03-27 22:00:00",
            "StartTime": "2025-03-27 22:18:43",
            "TaskCycleType": "I",
            "TaskId": "20250326150742906",
            "TaskName": "dq_test_dylan_shell_01",
            "TaskType": {
                "TypeDesc": "Shell",
                "TypeId": 35,
                "TypeSort": "数据计算"
            },
            "TotalRunNum": 1,
            "Tries": 1,
            "TryLimit": 5,
            "WorkflowId": "ec66594e-53a0-48cb-8044-a9eb3a58efe5",
            "WorkflowName": "dq_test_0326"
        },
        "RequestId": "e8393496-32f6-4273-8555-32b9a69d63cb"
    }
}
```

