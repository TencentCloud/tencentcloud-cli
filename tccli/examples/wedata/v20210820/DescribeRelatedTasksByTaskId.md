**Example 1: 成功示例**



Input: 

```
tccli wedata DescribeRelatedTasksByTaskId --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --TaskId 20250606112506283 \
    --PageNumber 1 \
    --PageSize 10 \
    --DependencyDirection UP \
    --Environment DEV \
    --TaskName 
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 10,
            "RelatedTaskList": [
                {
                    "CycleType": "D",
                    "DependencyDirection": "UP",
                    "OwnerName": "peanutzhu",
                    "ProjectDisplayName": "wedata数据开发",
                    "ProjectId": "1464962169590902784",
                    "Status": "N",
                    "TaskId": "20250606112604725",
                    "TaskName": "test_0606_1",
                    "TaskTypeId": 35,
                    "WorkflowId": "ab43623e-2473-413a-8c80-59e875167c96",
                    "WorkflowName": "test_ceshi"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "49c7dfc2-c145-4937-830d-96ab1608a430"
    }
}
```

