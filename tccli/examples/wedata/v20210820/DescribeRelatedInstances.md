**Example 1: 示例**



Input: 

```
tccli wedata DescribeRelatedInstances --cli-unfold-argument  \
    --PageSize 0 \
    --CurRunDate xx \
    --ProjectId xx \
    --Depth 0 \
    --PageNumber 0 \
    --TaskId 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "FolderName": "xx",
                    "State": 0,
                    "WorkflowName": "xx",
                    "EndTime": "xx",
                    "TaskTypeDesc": "xx",
                    "SchedulerDesc": "xx",
                    "Tries": 0,
                    "InstanceType": 0,
                    "TaskId": "xx",
                    "ProjectId": "xx",
                    "CostTime": "xx",
                    "TaskName": "xx",
                    "WorkflowId": "xx",
                    "ProjectIdent": "xx",
                    "ProjectName": "xx",
                    "InCharge": "xx",
                    "TryLimit": 0,
                    "TaskTypeId": 1,
                    "CycleType": "xx",
                    "StartTime": "xx",
                    "SchedulerDateTime": "xx",
                    "FolderId": "xx"
                }
            ],
            "PageNumber": 0,
            "PageSize": 0,
            "TotalCount": 0
        },
        "RequestId": "xx"
    }
}
```

**Example 2: 真实案例**



Input: 

```
tccli wedata DescribeRelatedInstances --cli-unfold-argument  \
    --PageSize 10 \
    --CurRunDate 2022-06-30 00:00:00 \
    --ProjectId 1 \
    --Depth 1 \
    --PageNumber 1 \
    --TaskId 20220506192333449
```

Output: 
```
{
    "Response": {
        "RequestId": "12ada6cc-83c2-45f1-b5dc-0887e4fb751d",
        "Data": {
            "TotalCount": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "Items": [
                {
                    "ProjectId": "1",
                    "ProjectName": null,
                    "ProjectIdent": null,
                    "FolderId": "e989c626-9f70-11ec-8909-bc97e105ba60",
                    "FolderName": "txyuwang_test",
                    "WorkflowId": "a183fd74-c243-11ec-8909-bc97e105ba60",
                    "WorkflowName": "txyuwang_wf1",
                    "TaskId": "20220506192401374",
                    "TaskName": "txyuwang_shell2",
                    "InCharge": "TBDS",
                    "CycleType": "D",
                    "TryLimit": 5,
                    "Tries": 0,
                    "State": 1,
                    "TaskTypeId": 35,
                    "TaskTypeDesc": "Shell",
                    "StartTime": null,
                    "EndTime": null,
                    "CostTime": "00:00:00.000",
                    "SchedulerDateTime": "2022-06-30 00:00:00",
                    "SchedulerDesc": "每天00:00执行一次",
                    "InstanceType": 1
                }
            ]
        }
    }
}
```

