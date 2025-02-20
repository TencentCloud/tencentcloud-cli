**Example 1: 查询最新1条任务记录**

查询最新1条任务记录

Input: 

```
tccli postgres DescribeTasks --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --OrderBy StartTime \
    --OrderByType desc
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": 1202345,
                "TaskType": "RestoreDatabase",
                "DBInstanceId": "postgres-q6fj84vb",
                "StartTime": "2024-09-27 13:14:11",
                "EndTime": "2024-09-27 13:18:11",
                "Status": "Success",
                "Progress": 100,
                "TaskDetail": {}
            }
        ],
        "RequestId": "3f164712-8746-464f-a490-3084a470000e",
        "TotalCount": 20
    }
}
```

**Example 2: 查询指定任务ID的任务**

查询指定任务ID的任务

Input: 

```
tccli postgres DescribeTasks --cli-unfold-argument  \
    --TaskId 120321 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7460a34c-2cf8-4d5c-9346-6977830da6e1",
        "TaskSet": [
            {
                "DBInstanceId": "postgres-0e3hth5b",
                "EndTime": "",
                "Progress": 0,
                "StartTime": "2024-09-27 16:06:02",
                "Status": "Running",
                "TaskDetail": {
                    "AllSteps": "",
                    "Input": "",
                    "Output": ""
                },
                "TaskId": 120321,
                "TaskType": "DestroyInstance"
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 3: 查询指定实例的任务**

分页查询指定实例的所有任务

Input: 

```
tccli postgres DescribeTasks --cli-unfold-argument  \
    --DBInstanceId postgres-q6fj84vb \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "53872de1-b750-4aa4-b660-5a3627a44d34",
        "TaskSet": [
            {
                "DBInstanceId": "postgres-q6fj84vb",
                "EndTime": "2024-09-27 13:18:11",
                "Progress": 100,
                "StartTime": "2024-09-27 13:14:11",
                "Status": "Success",
                "TaskDetail": {
                    "AllSteps": "[{\"StepId\":1,\"StepName\":\"Pre-check\"},{\"StepId\":2,\"StepName\":\"Download Base Backup\",\"StepProcess\":100,\"StepMessage\":\"download cos file success, cost time:12 s\"},{\"StepId\":3,\"StepName\":\"Download WAL Logs and Redo\",\"StepProcess\":100,\"StepMessage\":\"specifyBackupSet type ,skip download wal log and redo step\"},{\"StepId\":4,\"StepName\":\"Execute Recovery\"},{\"StepId\":5,\"StepName\":\"Task Complete\"}]",
                    "CurrentStep": "Task Complete",
                    "Input": "{\"RestoreObjects\":[\"postgres\"],\"RestoreType\":\"specifyBackupSet\",\"BackupSetTime\":\"2024-09-26 19:11:45\"}",
                    "Output": "{\"BeforeRestoreObjects\":[\"postgres\"],\"AfterRestoreObjects\":[\"postgres_bak_1727414053\"],\"RestoreType\":\"specifyBackupSet\",\"BackupSetTime\":\"2024-09-26 19:11:45\",\"Message\":\"success\"}"
                },
                "TaskId": 120006,
                "TaskType": "RestoreDatabase"
            },
            {
                "DBInstanceId": "postgres-q6fj84vb",
                "EndTime": "2024-09-27 13:13:31",
                "Progress": 100,
                "StartTime": "2024-09-27 13:09:15",
                "Status": "Success",
                "TaskDetail": {
                    "AllSteps": "[{\"StepId\":1,\"StepName\":\"Pre-check\"},{\"StepId\":2,\"StepName\":\"Download Base Backup\",\"StepProcess\":100,\"StepMessage\":\"download cos file success, cost time:11 s\"},{\"StepId\":3,\"StepName\":\"Download WAL Logs and Redo\",\"StepProcess\":100,\"StepMessage\":\"specifyBackupSet type ,skip download wal log and redo step\"},{\"StepId\":4,\"StepName\":\"Execute Recovery\"},{\"StepId\":5,\"StepName\":\"Task Complete\"}]",
                    "CurrentStep": "Task Complete",
                    "Input": "{\"RestoreObjects\":[\"postgres\"],\"RestoreType\":\"specifyBackupSet\",\"BackupSetTime\":\"2024-09-26T19:11:45+08:00\"}",
                    "Output": "{\"BeforeRestoreObjects\":[\"postgres\"],\"AfterRestoreObjects\":[\"postgres_bak_1727413757\"],\"RestoreType\":\"specifyBackupSet\",\"BackupSetTime\":\"2024-09-26T19:11:45+08:00\",\"Message\":\"success\"}"
                },
                "TaskId": 120005,
                "TaskType": "RestoreDatabase"
            },
            {
                "DBInstanceId": "postgres-q6fj84vb",
                "EndTime": "2024-09-27 12:35:58",
                "Progress": 100,
                "StartTime": "2024-09-27 12:31:50",
                "Status": "Success",
                "TaskDetail": {
                    "AllSteps": "[{\"StepId\":1,\"StepName\":\"Pre-check\"},{\"StepId\":2,\"StepName\":\"Download Base Backup\",\"StepProcess\":100,\"StepMessage\":\"download cos file success, cost time:1 s\"},{\"StepId\":3,\"StepName\":\"Download WAL Logs and Redo\",\"StepProcess\":100,\"StepMessage\":\"specifyBackupSet type ,skip download wal log and redo step\"},{\"StepId\":4,\"StepName\":\"Execute Recovery\"},{\"StepId\":5,\"StepName\":\"Task Complete\"}]",
                    "CurrentStep": "Task Complete",
                    "Input": "{\"RestoreObjects\":[\"postgres\"],\"RestoreType\":\"specifyBackupSet\"}",
                    "Output": "{\"BeforeRestoreObjects\":[\"postgres\"],\"AfterRestoreObjects\":[\"postgres_bak_1727411512\"],\"RestoreType\":\"specifyBackupSet\",\"Message\":\"success\"}"
                },
                "TaskId": 120004,
                "TaskType": "RestoreDatabase"
            },
            {
                "DBInstanceId": "postgres-q6fj84vb",
                "EndTime": "2024-09-27 12:31:28",
                "Progress": 100,
                "StartTime": "2024-09-27 12:30:06",
                "Status": "Success",
                "TaskDetail": {
                    "AllSteps": "[{\"StepId\":1,\"StepName\":\"Pre-check\"},{\"StepId\":2,\"StepName\":\"Download Base Backup\"},{\"StepId\":3,\"StepName\":\"Download WAL Logs and Redo\"},{\"StepId\":4,\"StepName\":\"Execute Recovery\"},{\"StepId\":5,\"StepName\":\"Task Complete\"}]",
                    "CurrentStep": "Task Complete",
                    "Input": "{\"RestoreObjects\":[\"postgres\"],\"RestoreType\":\"timestamp\",\"RestoreTargetTime\":\"2024-09-26 15:20:14\"}",
                    "Output": "{\"BeforeRestoreObjects\":[\"postgres\"],\"AfterRestoreObjects\":[\"postgres_bak_1727411408\"],\"RestoreType\":\"timestamp\",\"RestoreTargetTime\":\"2024-09-26 15:20:14\",\"Message\":\"success\"}"
                },
                "TaskId": 120003,
                "TaskType": "RestoreDatabase"
            },
            {
                "DBInstanceId": "postgres-q6fj84vb",
                "EndTime": "2024-09-27 12:29:04",
                "Progress": 100,
                "StartTime": "2024-09-27 12:24:29",
                "Status": "Success",
                "TaskDetail": {
                    "AllSteps": "[{\"StepId\":1,\"StepName\":\"Pre-check\"},{\"StepId\":2,\"StepName\":\"Download Base Backup\"},{\"StepId\":3,\"StepName\":\"Download WAL Logs and Redo\"},{\"StepId\":4,\"StepName\":\"Execute Recovery\"},{\"StepId\":5,\"StepName\":\"Task Complete\"}]",
                    "CurrentStep": "Task Complete",
                    "Input": "{\"RestoreObjects\":[\"postgres\"],\"RestoreType\":\"timestamp\",\"RestoreTargetTime\":\"2024-09-26 15:20:14\"}",
                    "Output": "{\"BeforeRestoreObjects\":[\"postgres\"],\"AfterRestoreObjects\":[\"postgres_bak_1727411071\"],\"RestoreType\":\"timestamp\",\"RestoreTargetTime\":\"2024-09-26 15:20:14\",\"Message\":\"success\"}"
                },
                "TaskId": 120002,
                "TaskType": "RestoreDatabase"
            },
            {
                "DBInstanceId": "postgres-q6fj84vb",
                "EndTime": "2024-09-27 11:32:50",
                "Progress": 100,
                "StartTime": "2024-09-27 11:29:03",
                "Status": "Success",
                "TaskDetail": {
                    "AllSteps": "[{\"StepId\":1,\"StepName\":\"Pre-check\"},{\"StepId\":2,\"StepName\":\"Download Base Backup\",\"StepProcess\":100,\"StepMessage\":\"download cos file success, cost time:1 s\"},{\"StepId\":3,\"StepName\":\"Download WAL Logs and Redo\",\"StepProcess\":100,\"StepMessage\":\"specifyBackupSet type ,skip download wal log and redo step\"},{\"StepId\":4,\"StepName\":\"Execute Recovery\"},{\"StepId\":5,\"StepName\":\"Task Complete\"}]",
                    "CurrentStep": "Task Complete",
                    "Input": "{\"RestoreObjects\":[\"postgres\"],\"RestoreType\":\"specifyBackupSet\",\"BackupSetId\":\"17083520-3ce6-5b50-9c25-73ff3d4d80b7\"}",
                    "Output": "{\"RestoreObjects\":[\"postgres\"],\"RestoreType\":\"specifyBackupSet\",\"BackupSetId\":\"17083520-3ce6-5b50-9c25-73ff3d4d80b7\",\"RestoreTargetTime\":\"1970-01-01 08:00:00\",\"Message\":\"success\"}"
                },
                "TaskId": 120001,
                "TaskType": "RestoreDatabase"
            }
        ],
        "TotalCount": 6
    }
}
```

