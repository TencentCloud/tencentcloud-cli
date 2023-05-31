**Example 1: DescribeOperateTasks**

任务运维-查询任务列表

Input: 

```
tccli wedata DescribeOperateTasks --cli-unfold-argument  \
    --StatusList xx \
    --InChargeList xx \
    --SortType xx \
    --PageSize xx \
    --ProjectId xx \
    --TaskNameList xx \
    --FolderIdList xx \
    --TaskTypeIdList xx \
    --TaskIdList xx \
    --PageNumber xx \
    --WorkFlowIdList xx \
    --SortItem xx \
    --WorkFlowNameList xx \
    --TaskCycleUnitList xx \
    --ProductNameList xxx
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Status": "xx",
                    "CycleUnit": "xx",
                    "WorkflowId": "xx",
                    "LeftCoordinate": 0.0,
                    "TaskTypeDesc": "xx",
                    "TaskId": "xx",
                    "TopCoordinate": 0.0,
                    "ProjectName": "xx",
                    "InCharge": "xx",
                    "FolderName": "xx",
                    "TaskTypeId": 1,
                    "ScheduleDesc": "xx",
                    "WorkflowName": "xx",
                    "ProjectId": "xx",
                    "FirstSubmitTime": "xx",
                    "TaskName": "xx",
                    "FolderId": "xx",
                    "FirstRunTime": "xx",
                    "ProjectIdent": "xx"
                },
                {
                    "Status": "xx",
                    "CycleUnit": "xx",
                    "WorkflowId": "xx",
                    "LeftCoordinate": 0.0,
                    "TaskTypeDesc": "xx",
                    "TaskTypeId": 1,
                    "WorkflowName": "xx",
                    "ProjectName": "xx",
                    "InCharge": "xx",
                    "FolderName": "xx",
                    "TopCoordinate": 0.0,
                    "ScheduleDesc": "xx",
                    "TaskId": "xx",
                    "ProjectId": "xx",
                    "FirstSubmitTime": "xx",
                    "TaskName": "xx",
                    "FolderId": "xx",
                    "FirstRunTime": "xx",
                    "ProjectIdent": "xx"
                },
                {
                    "Status": "xx",
                    "CycleUnit": "xx",
                    "WorkflowId": "xx",
                    "LeftCoordinate": 0.0,
                    "TaskTypeDesc": "xx",
                    "TaskTypeId": 1,
                    "WorkflowName": "xx",
                    "ProjectName": "xx",
                    "InCharge": "xx",
                    "FolderName": "xx",
                    "TopCoordinate": 0.0,
                    "ScheduleDesc": "xx",
                    "TaskId": "xx",
                    "ProjectId": "xx",
                    "FirstSubmitTime": "xx",
                    "TaskName": "xx",
                    "FolderId": "xx",
                    "FirstRunTime": "xx",
                    "ProjectIdent": "xx"
                }
            ],
            "TotalPage": 1,
            "PageNumber": 1,
            "PageSize": 1
        },
        "RequestId": "xx"
    }
}
```

