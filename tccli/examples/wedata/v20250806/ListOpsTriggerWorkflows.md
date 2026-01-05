**Example 1: 查询工作流列表信息**



Input: 

```
tccli wedata ListOpsTriggerWorkflows --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
                    "FolderName": "默认文件夹",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 0,
                    "UserNameInCharge": "shianwang",
                    "UserUinInCharge": "100044424942",
                    "WorkflowId": "0e780658-d93b-48a6-8388-d5081e27fe79",
                    "WorkflowName": "1shianceshi",
                    "WorkflowTriggerConfig": null
                },
                {
                    "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
                    "FolderName": "默认文件夹",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 0,
                    "UserNameInCharge": "delphichen",
                    "UserUinInCharge": "100043191163",
                    "WorkflowId": "4f5ba381-9243-44e3-a3e2-298121ae0e45",
                    "WorkflowName": "aaaaaa111",
                    "WorkflowTriggerConfig": null
                },
                {
                    "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
                    "FolderName": "默认文件夹",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 0,
                    "UserNameInCharge": "delphichen",
                    "UserUinInCharge": "100043191163",
                    "WorkflowId": "ee2e298f-2d3a-48fc-aa37-e7953a8bbb77",
                    "WorkflowName": "testddsd",
                    "WorkflowTriggerConfig": null
                },
                {
                    "FolderId": "27683508-bee2-11f0-9366-7c8c09fca71c",
                    "FolderName": "bonneyyu",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 1,
                    "UserNameInCharge": "bonneyyu",
                    "UserUinInCharge": "100044422442",
                    "WorkflowId": "da6b9817-923d-4c04-8e4d-59b961e50a5f",
                    "WorkflowName": "bonneyyu_test",
                    "WorkflowTriggerConfig": null
                },
                {
                    "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
                    "FolderName": "默认文件夹",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 0,
                    "UserNameInCharge": "erinhong",
                    "UserUinInCharge": "100044422498",
                    "WorkflowId": "5353e5ba-b2e7-4855-b14d-a8a26d7fdc04",
                    "WorkflowName": "3444",
                    "WorkflowTriggerConfig": null
                },
                {
                    "FolderId": "f4afe0e4-4b5a-11f0-8ec8-b8599f277de5",
                    "FolderName": "0001",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 1,
                    "UserNameInCharge": "jaydenjhu",
                    "UserUinInCharge": "100028578851",
                    "WorkflowId": "acb9a8b2-b138-4b82-b76f-4ea459e53173",
                    "WorkflowName": "jayden_sub_workflow",
                    "WorkflowTriggerConfig": null
                },
                {
                    "FolderId": "a1eb11e9-6f1a-11ed-8909-bc97e105ba60",
                    "FolderName": "默认文件夹",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 0,
                    "UserNameInCharge": null,
                    "UserUinInCharge": "100039182306",
                    "WorkflowId": "6da17a9d-a7fb-494d-83d9-68ab2a723452",
                    "WorkflowName": "时区优化测试",
                    "WorkflowTriggerConfig": {
                        "ConfigMode": "COMMON",
                        "CrontabExpression": "0 0 0 * * ? *",
                        "CycleType": "DAY_CYCLE",
                        "EndTime": "4102329600000",
                        "ExtraInfo": null,
                        "ScheduleTimeZone": "Asia/Shanghai",
                        "StartTime": "1764172800000",
                        "TriggerId": "c6fe2e76-60be-4090-820f-8eab6df67b76",
                        "TriggerMode": "TIME_TRIGGER"
                    }
                },
                {
                    "FolderId": "f4afe0e4-4b5a-11f0-8ec8-b8599f277de5",
                    "FolderName": "0001",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 3,
                    "UserNameInCharge": "jaydenjhu",
                    "UserUinInCharge": "100028578851",
                    "WorkflowId": "6fd5819f-70ec-4d8c-9ddb-7a43bd5d23c6",
                    "WorkflowName": "jayden_parameter_passing",
                    "WorkflowTriggerConfig": null
                },
                {
                    "FolderId": "28d5fadc-cb6d-11f0-9366-7c8c09fca71c",
                    "FolderName": "ives测试工作流调度专用",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 1,
                    "UserNameInCharge": "ivesjcjiang",
                    "UserUinInCharge": "100028578781",
                    "WorkflowId": "f9e7b3a0-6188-48e9-a887-95ab205ce8b7",
                    "WorkflowName": "A",
                    "WorkflowTriggerConfig": null
                },
                {
                    "FolderId": "f38220ec-6bb3-11f0-9366-7c8c09fca71c",
                    "FolderName": "0_yulingfan",
                    "ProjectId": "1460947878944567296",
                    "TaskCount": 2,
                    "UserNameInCharge": "wenjieyao",
                    "UserUinInCharge": "100028579606",
                    "WorkflowId": "fbf8d2a4-6f2f-4a61-9542-04e231fb3d22",
                    "WorkflowName": "yulingfan_workflow_trigger",
                    "WorkflowTriggerConfig": {
                        "ConfigMode": "COMMON",
                        "CrontabExpression": "0 0/30 0-23 * * ? *",
                        "CycleType": "MINUTE_CYCLE",
                        "EndTime": "1764432000000",
                        "ExtraInfo": null,
                        "ScheduleTimeZone": "Asia/Shanghai",
                        "StartTime": "1764172800000",
                        "TriggerId": "a4912088-9b43-472b-85f1-2e3b3a3c5151",
                        "TriggerMode": "TIME_TRIGGER"
                    }
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 64,
            "TotalPageNumber": 7
        },
        "RequestId": "a235fe32-1e15-4d78-b1bc-832e6bade136"
    }
}
```

