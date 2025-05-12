**Example 1: 分页查询引用模板的任务的列表**



Input: 

```
tccli wedata DescribeTasksForCodeTemplate --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --PageNumber 1 \
    --PageSize 10 \
    --TemplateId 20250311141017356
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "InCharge": "peterpksong",
                    "OwnId": "100028448903",
                    "TaskId": "20250312151216033",
                    "TaskName": "asdasdasdas",
                    "TaskTypeId": 30,
                    "TenantId": "1315051789",
                    "UserId": "100028694266",
                    "WorkflowId": "4b4b885b-cf56-49f7-ae52-05d679b21411",
                    "WorkflowName": "上下游依赖问题"
                },
                {
                    "InCharge": "candouwang",
                    "OwnId": "100028448903",
                    "TaskId": "20250312175744154",
                    "TaskName": "fadfadfad",
                    "TaskTypeId": 30,
                    "TenantId": "1315051789",
                    "UserId": "100028649379",
                    "WorkflowId": "eb3ab1cb-464f-4009-b0d0-b3eee4744c24",
                    "WorkflowName": "abel_test"
                },
                {
                    "InCharge": "peterpksong;wenjieyao",
                    "OwnId": "100028448903",
                    "TaskId": "20250312111133801",
                    "TaskName": "peter",
                    "TaskTypeId": 30,
                    "TenantId": "1315051789",
                    "UserId": "100028694266",
                    "WorkflowId": "4b4b885b-cf56-49f7-ae52-05d679b21411",
                    "WorkflowName": "上下游依赖问题"
                },
                {
                    "InCharge": "peterpksong",
                    "OwnId": "100028448903",
                    "TaskId": "20250312225619856",
                    "TaskName": "peterTest",
                    "TaskTypeId": 30,
                    "TenantId": "1315051789",
                    "UserId": "100028694266",
                    "WorkflowId": "8966c7a5-15b0-400e-8062-9502967e8e34",
                    "WorkflowName": "aiops_delete"
                },
                {
                    "InCharge": "wenjieyao",
                    "OwnId": "100028448903",
                    "TaskId": "20250312161138565",
                    "TaskName": "petertest1",
                    "TaskTypeId": 30,
                    "TenantId": "1315051789",
                    "UserId": "100028579606",
                    "WorkflowId": "4b4b885b-cf56-49f7-ae52-05d679b21411",
                    "WorkflowName": "上下游依赖问题"
                },
                {
                    "InCharge": "peanutzhu",
                    "OwnId": "100028448903",
                    "TaskId": "20250311145732181",
                    "TaskName": "test_0999",
                    "TaskTypeId": 30,
                    "TenantId": "1315051789",
                    "UserId": "100028578753",
                    "WorkflowId": "8966c7a5-15b0-400e-8062-9502967e8e34",
                    "WorkflowName": "aiops_delete"
                },
                {
                    "InCharge": "peanutzhu",
                    "OwnId": "100028448903",
                    "TaskId": "20250311145611244",
                    "TaskName": "test_peanut_11",
                    "TaskTypeId": 30,
                    "TenantId": "1315051789",
                    "UserId": "100028578753",
                    "WorkflowId": "8966c7a5-15b0-400e-8062-9502967e8e34",
                    "WorkflowName": "aiops_delete"
                }
            ],
            "PageCount": 1,
            "TotalCount": 7
        },
        "RequestId": "8ecf6437-d3e0-47b1-acce-525c952907fc"
    }
}
```

