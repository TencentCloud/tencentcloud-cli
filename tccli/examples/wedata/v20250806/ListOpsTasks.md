**Example 1: 运维中心任务列表**



Input: 

```
tccli wedata ListOpsTasks --cli-unfold-argument  \
    --ProjectId 2428908825624145920
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "2025-04-28 15:17:35",
                    "CycleType": "MINUTE_CYCLE",
                    "ExecutorGroupId": "20231124174317834475",
                    "ExecutorGroupName": "u5e7fu5ddeu8c03u5ea6u8d44u6e90u7ec4-twrh68lc",
                    "FirstRunTime": "2025-04-28 00:00:00",
                    "FirstSubmitTime": "2025-04-28 15:20:16",
                    "FolderId": "db050617-2400-11f0-8c70-043f72d4907c",
                    "FolderName": "lina_test_0428",
                    "LastSchedulerCommitTime": "2025-04-28 15:20:16",
                    "LastUpdateTime": null,
                    "OwnerUin": "100028448903",
                    "ProjectId": "2428908825624145920",
                    "ProjectName": "project_wedata_1u62e8u6d4bu4e13u7528",
                    "ScheduleDesc": "u4ece2025u5e7404u670828u65e5 00:00:00u5f00u59cb,u6bcfu592900:00~23:59u5185uff0cu6bcfu95f4u96945u5206u949fu6267u884cu4e00u6b21(UTC+8)",
                    "Status": "Y",
                    "TaskId": "20250428151735671",
                    "TaskName": "lina_notebook_0428_1",
                    "TaskTypeDesc": "Notebooku63a2u7d22",
                    "TaskTypeId": 132,
                    "UpdateUserUin": "100029132669",
                    "WorkflowId": "e9685bc2-e122-4b2d-9b09-723962965b90",
                    "WorkflowName": "lina_gz_0428"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 891,
            "TotalPageNumber": 90
        },
        "RequestId": "8ff428af-77a3-4834-bbfd-73c3184d4888"
    }
}
```

