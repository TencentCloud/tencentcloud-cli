**Example 1: 手动任务触发运行**

手动任务触发运行

Input: 

```
tccli wedata TriggerManualTasks --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --TriggerName test_name \
    --TriggerScope ENTIRE_WORKFLOW \
    --DataTimeList '2025-01-14 00:00:00' '2025-01-14 01:00:00' \
    --WorkflowId d4d7e9a7-0649-4410-a2ae-89818043c58a \
    --Remark  \
    --SchedulerResourceGroup 20240703113703331017 \
    --IntegrationResourceGroup  \
    --ExecOrder RAND \
    --CustomParams.0.K param1 \
    --CustomParams.0.V 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "2025-01-14T17:42:37.069",
            "DatetimeList": [
                "2025-01-14 00:00:00",
                "2025-01-14 01:00:00"
            ],
            "FinishedInstanceCnt": null,
            "InstanceCnt": null,
            "OwnerUin": "100028448903",
            "ProjectId": "1464962169590902784",
            "Remark": "",
            "Status": "INIT",
            "SuccessInstanceCnt": null,
            "TaskCnt": null,
            "TenantId": "1315051789",
            "TriggerId": "9a350a12-40bd-4610-9d9e-445ee8730d6e",
            "TriggerName": "test_name",
            "TriggerParams": "{\"ProjectId\":\"1464962169590902784\",\"TriggerName\":\"test_name\",\"Remark\":\"\",\"TriggerScope\":\"ENTIRE_WORKFLOW\",\"WorkflowId\":\"d4d7e9a7-0649-4410-a2ae-89818043c58a\",\"TaskIds\":[\"20241223224113778\",\"20241224171752455\",\"20241223224056125\"],\"DataTimeList\":[\"2025-01-14 00:00:00\",\"2025-01-14 01:00:00\"],\"SchedulerResourceGroup\":\"20240703113703331017\",\"IntegrationResourceGroup\":\"\",\"ExecOrder\":\"RAND\",\"CustomParams\":[{\"K\":\"param1\",\"V\":\"10\"}],\"ExtraParams\":null}",
            "UserName": "wenjieyao",
            "UserUin": "100028579606"
        },
        "RequestId": "da12b6d9-fd32-4b3e-8716-5085722e06e5"
    }
}
```

