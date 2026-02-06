**Example 1: 成功示例**



Input: 

```
tccli wedata DescribeRelatedTasksByTaskId --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --TaskId 20250731175055049 \
    --PageNumber 1 \
    --PageSize 10 \
    --DependencyDirection DOWN \
    --Environment DEV
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
                    "DependencyDirection": "DOWN",
                    "OwnerName": "jasonzcwang",
                    "ProjectDisplayName": "wedata数据开发_新",
                    "ProjectId": "1470547050521227264",
                    "Status": "N",
                    "TaskId": "20250805162149172",
                    "TaskName": "test_ds",
                    "TaskTypeId": 46,
                    "WorkflowId": "a6557acf-1dc4-4251-84c2-c1210d5a6390",
                    "WorkflowName": "wf2"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "02b7c343-0225-4685-99d4-59a5e468793d"
    }
}
```

