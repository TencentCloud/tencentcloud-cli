**Example 1: 根据层级查找上-下游任务节点示例**

任务运维-根据层级查找上-下游任务节点

Input: 

```
tccli wedata DescribeDependOpsTasks --cli-unfold-argument  \
    --TaskId your taskId \
    --Deep 1 \
    --Up 1 \
    --ProjectId your projectId \
    --WorkflowId c66ddxa3ee-aa0b-11ee-8d13-aaaa20f8272
```

Output: 
```
{
    "Response": {
        "Data": {
            "LinksList": [],
            "TasksList": [
                {
                    "CycleUnit": "D",
                    "DelayTime": 0,
                    "FirstRunTime": "2024-01-03 00:00:00",
                    "FirstSubmitTime": "2024-01-03 16:36:35",
                    "FolderId": "b1f2ff1-aa0b-11ee-8d13-ae120f8272",
                    "FolderName": "0_axb",
                    "InCharge": ";jack;",
                    "Layer": null,
                    "LeftCoordinate": 3615,
                    "ProjectId": "your projectId",
                    "ProjectIdent": "project_wedata",
                    "ProjectName": "project_wedata",
                    "ScheduleDesc": "每天00:00执行一次",
                    "Status": "Y",
                    "TaskAction": "",
                    "TaskId": "your taskId",
                    "TaskName": "mysql2hive_test",
                    "TaskTypeDesc": "离线同步",
                    "TaskTypeId": 26,
                    "TopCoordinate": 1612,
                    "VirtualFlag": false,
                    "WorkflowId": "c66ddxa3ee-aa0b-11ee-8d13-aaaa20f8272",
                    "WorkflowName": "test11",
                    "TargetServiceId": "123",
                    "CreateTime": "2024-01-03 00:00:00",
                    "ExecutionStartTime": "2024-01-03 00:00:00",
                    "ExecutionEndTime": "2024-01-04 00:00:00",
                    "SourceServiceId": "321",
                    "SourceServiceType": "hive",
                    "TargetServiceType": "hive",
                    "AlarmType": "1"
                }
            ]
        },
        "RequestId": "5c961bb7-d22a-4a3e-bfa6-9a4a64084632"
    }
}
```

