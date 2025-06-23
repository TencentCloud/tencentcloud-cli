**Example 1: 查询手动任务触发记录**

查询手动任务触发记录

Input: 

```
tccli wedata DescribeManualTriggerRecordPage --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
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
                    "CreateTime": "2025-01-13T21:58:50",
                    "DatetimeList": [
                        "2025-01-13 00:00:00"
                    ],
                    "FinishedInstanceCnt": 1,
                    "InstanceCnt": 3,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "",
                    "Status": "RUNNING",
                    "SuccessInstanceCnt": 0,
                    "TaskCnt": 3,
                    "TenantId": "1315051789",
                    "TriggerId": "02ed938c-754b-4b0d-82e8-a814779d3b53",
                    "TriggerName": "patch_20250113215838_4213",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20250113215838_4213\",\"Remark\":\"\",\"TriggerScope\":\"SPECIFIED_TASK\",\"WorkflowId\":\"802d9fb8-78a2-4e81-aff8-ed9e30d96649\",\"TaskIds\":[\"20241228224855990\",\"20241228224931798\",\"20241228224911377\"],\"DataTimeList\":[\"2025-01-13 00:00:00\"],\"SchedulerResourceGroup\":\"\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"RAND\",\"CustomParams\":[],\"ExtraParams\":null}",
                    "UserName": "gshengshi",
                    "UserUin": "100028649389"
                },
                {
                    "CreateTime": "2025-01-13T21:15:51",
                    "DatetimeList": [
                        "2025-01-14 00:00:00",
                        "2025-01-15 00:00:00"
                    ],
                    "FinishedInstanceCnt": 2,
                    "InstanceCnt": 2,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "",
                    "Status": "FINISHED",
                    "SuccessInstanceCnt": 0,
                    "TaskCnt": 1,
                    "TenantId": "1315051789",
                    "TriggerId": "4edcf5fe-dae3-44d6-a887-d6329782815f",
                    "TriggerName": "patch_20250113211536_3265",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20250113211536_3265\",\"Remark\":\"\",\"TriggerScope\":\"ENTIRE_WORKFLOW\",\"WorkflowId\":\"644b7b81-ba38-4712-a1fe-c4fd2ca94b62\",\"TaskIds\":[\"20250113211401610\",\"20250113211347878\"],\"DataTimeList\":[\"2025-01-14 00:00:00\",\"2025-01-15 00:00:00\"],\"SchedulerResourceGroup\":\"\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"RAND\",\"CustomParams\":[],\"ExtraParams\":null}",
                    "UserName": "gshengshi",
                    "UserUin": "100028649389"
                },
                {
                    "CreateTime": "2024-12-28T22:22:59",
                    "DatetimeList": [
                        "2024-06-02 00:00:00",
                        "2024-06-01 00:00:00"
                    ],
                    "FinishedInstanceCnt": 2,
                    "InstanceCnt": 6,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "",
                    "Status": "RUNNING",
                    "SuccessInstanceCnt": 2,
                    "TaskCnt": 3,
                    "TenantId": "1315051789",
                    "TriggerId": "f93a56ee-b4a9-4bde-87e7-104a0cc75409",
                    "TriggerName": "patch_20241228221214_4461",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20241228221214_4461\",\"Remark\":\"\",\"TriggerScope\":\"ENTIRE_WORKFLOW\",\"WorkflowId\":\"02c48958-df99-48fc-85c3-1801ef153737\",\"TaskIds\":[\"20241228165127816\",\"20241228145406028\",\"20241228145947741\"],\"DataTimeList\":[\"2024-06-02 00:00:00\",\"2024-06-01 00:00:00\"],\"SchedulerResourceGroup\":\"\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"ASC\",\"CustomParams\":[],\"ExtraParams\":null}",
                    "UserName": "hongdianlin",
                    "UserUin": "100039182306"
                },
                {
                    "CreateTime": "2024-12-28T22:19:22",
                    "DatetimeList": [
                        "2024-12-28 00:00:00",
                        "2024-12-24 00:00:00"
                    ],
                    "FinishedInstanceCnt": 0,
                    "InstanceCnt": 6,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "dsdf",
                    "Status": "INIT",
                    "SuccessInstanceCnt": 0,
                    "TaskCnt": 3,
                    "TenantId": "1315051789",
                    "TriggerId": "8c5cca9f-b908-490c-9b9c-3c2bf48a597f",
                    "TriggerName": "david2342",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"david2342\",\"Remark\":\"dsdf\",\"TriggerScope\":\"SPECIFIED_TASK\",\"WorkflowId\":\"02c48958-df99-48fc-85c3-1801ef153737\",\"TaskIds\":[\"20241228165127816\",\"20241228145406028\",\"20241228145947741\"],\"DataTimeList\":[\"2024-12-28 00:00:00\",\"2024-12-24 00:00:00\"],\"SchedulerResourceGroup\":\"20240703113703331017\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"DESC\",\"CustomParams\":[{\"K\":\"33\",\"V\":\"44\"},{\"K\":\"3332\",\"V\":\"\"}],\"ExtraParams\":null}",
                    "UserName": "davidfjiang",
                    "UserUin": "100028602619"
                },
                {
                    "CreateTime": "2024-12-28T22:13:25",
                    "DatetimeList": [
                        "2024-08-01 00:00:01",
                        "2024-08-02 00:00:00"
                    ],
                    "FinishedInstanceCnt": 4,
                    "InstanceCnt": 4,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "",
                    "Status": "FINISHED",
                    "SuccessInstanceCnt": 4,
                    "TaskCnt": 2,
                    "TenantId": "1315051789",
                    "TriggerId": "817fbc11-10f3-4089-b05f-94b9920e6155",
                    "TriggerName": "patch_20241228221214_4460",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20241228221214_4460\",\"Remark\":\"\",\"TriggerScope\":\"SPECIFIED_TASK\",\"WorkflowId\":\"02c48958-df99-48fc-85c3-1801ef153737\",\"TaskIds\":[\"20241228165127816\",\"20241228145947741\"],\"DataTimeList\":[\"2024-08-01 00:00:01\",\"2024-08-02 00:00:00\"],\"SchedulerResourceGroup\":\"\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"ASC\",\"CustomParams\":[],\"ExtraParams\":null}",
                    "UserName": "hongdianlin",
                    "UserUin": "100039182306"
                },
                {
                    "CreateTime": "2024-12-28T21:57:58",
                    "DatetimeList": [
                        "2024-09-21 00:00:02",
                        "2024-12-16 00:00:06"
                    ],
                    "FinishedInstanceCnt": 1,
                    "InstanceCnt": 6,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "",
                    "Status": "RUNNING",
                    "SuccessInstanceCnt": 1,
                    "TaskCnt": 3,
                    "TenantId": "1315051789",
                    "TriggerId": "463852ea-41a8-48e6-a283-0e3b5b631478",
                    "TriggerName": "patch_20241228215639_1107",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20241228215639_1107\",\"Remark\":\"\",\"TriggerScope\":\"ENTIRE_WORKFLOW\",\"WorkflowId\":\"02c48958-df99-48fc-85c3-1801ef153737\",\"TaskIds\":[\"20241228165127816\",\"20241228145406028\",\"20241228145947741\"],\"DataTimeList\":[\"2024-09-21 00:00:02\",\"2024-12-16 00:00:06\"],\"SchedulerResourceGroup\":\"\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"ASC\",\"CustomParams\":[],\"ExtraParams\":null}",
                    "UserName": "hongdianlin",
                    "UserUin": "100039182306"
                },
                {
                    "CreateTime": "2024-12-28T20:06:55",
                    "DatetimeList": [
                        "2024-09-01 00:00:00",
                        "2024-08-28 00:00:00"
                    ],
                    "FinishedInstanceCnt": 4,
                    "InstanceCnt": 4,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "",
                    "Status": "FINISHED",
                    "SuccessInstanceCnt": 4,
                    "TaskCnt": 2,
                    "TenantId": "1315051789",
                    "TriggerId": "7712a54d-7cc8-4976-8530-7d108295ca3b",
                    "TriggerName": "patch_20241228200212_3228",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20241228200212_3228\",\"Remark\":\"\",\"TriggerScope\":\"SPECIFIED_TASK\",\"WorkflowId\":\"02c48958-df99-48fc-85c3-1801ef153737\",\"TaskIds\":[\"20241228165127816\",\"20241228145947741\"],\"DataTimeList\":[\"2024-09-01 00:00:00\",\"2024-08-28 00:00:00\"],\"SchedulerResourceGroup\":\"\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"ASC\",\"CustomParams\":[],\"ExtraParams\":null}",
                    "UserName": "hongdianlin",
                    "UserUin": "100039182306"
                },
                {
                    "CreateTime": "2024-12-28T19:57:09",
                    "DatetimeList": [
                        "2024-11-05 00:00:01",
                        "2024-10-28 00:00:00"
                    ],
                    "FinishedInstanceCnt": 2,
                    "InstanceCnt": 4,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "",
                    "Status": "RUNNING",
                    "SuccessInstanceCnt": 2,
                    "TaskCnt": 2,
                    "TenantId": "1315051789",
                    "TriggerId": "f4b8c65e-f234-48ab-bf24-f172dfb87f6a",
                    "TriggerName": "patch_20241228192323_9475",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20241228192323_9475\",\"Remark\":\"\",\"TriggerScope\":\"SPECIFIED_TASK\",\"WorkflowId\":\"02c48958-df99-48fc-85c3-1801ef153737\",\"TaskIds\":[\"20241228165127816\",\"20241228145947741\"],\"DataTimeList\":[\"2024-11-05 00:00:01\",\"2024-10-28 00:00:00\"],\"SchedulerResourceGroup\":\"\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"ASC\",\"CustomParams\":[],\"ExtraParams\":null}",
                    "UserName": "hongdianlin",
                    "UserUin": "100039182306"
                },
                {
                    "CreateTime": "2024-12-28T19:13:18",
                    "DatetimeList": [
                        "2024-01-01 00:00:09",
                        "2024-01-01 00:00:10"
                    ],
                    "FinishedInstanceCnt": 2,
                    "InstanceCnt": 2,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": null,
                    "Status": "FINISHED",
                    "SuccessInstanceCnt": 2,
                    "TaskCnt": 1,
                    "TenantId": "1315051789",
                    "TriggerId": "d6188f93-67f2-4a1d-b64f-c211b66695f5",
                    "TriggerName": "patch_20241228185813_6676",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20241228185813_6676\",\"Remark\":null,\"TriggerScope\":\"SPECIFIED_TASK\",\"WorkflowId\":\"02c48958-df99-48fc-85c3-1801ef153737\",\"TaskIds\":[\"20241228165127816\"],\"DataTimeList\":[\"2024-01-01 00:00:09\",\"2024-01-01 00:00:10\"],\"SchedulerResourceGroup\":\"20221201071126354503\",\"IntegrationResourceGroup\":\"20221201071126354503\",\"ExecOrder\":\"ASC\",\"CustomParams\":null,\"ExtraParams\":null}",
                    "UserName": "wenjieyao",
                    "UserUin": "100028579606"
                },
                {
                    "CreateTime": "2024-12-28T19:07:58",
                    "DatetimeList": [
                        "2024-12-01 00:00:56"
                    ],
                    "FinishedInstanceCnt": 3,
                    "InstanceCnt": 3,
                    "OwnerUin": "100028448903",
                    "ProjectId": "1464962169590902784",
                    "Remark": "",
                    "Status": "FINISHED",
                    "SuccessInstanceCnt": 3,
                    "TaskCnt": 3,
                    "TenantId": "1315051789",
                    "TriggerId": "9efce5e5-dbdf-4e70-8824-b16fd55c7c23",
                    "TriggerName": "patch_20241228185813_6675",
                    "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"patch_20241228185813_6675\",\"Remark\":\"\",\"TriggerScope\":\"ENTIRE_WORKFLOW\",\"WorkflowId\":\"02c48958-df99-48fc-85c3-1801ef153737\",\"TaskIds\":[\"20241228165127816\",\"20241228145406028\",\"20241228145947741\"],\"DataTimeList\":[\"2024-12-01 00:00:56\"],\"SchedulerResourceGroup\":\"\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"ASC\",\"CustomParams\":[{\"K\":\"task3\",\"V\":\"1321451421\"}],\"ExtraParams\":null}",
                    "UserName": "hongdianlin",
                    "UserUin": "100039182306"
                }
            ],
            "PageCount": 10,
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 49,
            "TotalPage": 5
        },
        "RequestId": "e2a22345-9143-4b3e-9bc4-8846e9ab0efc"
    }
}
```

