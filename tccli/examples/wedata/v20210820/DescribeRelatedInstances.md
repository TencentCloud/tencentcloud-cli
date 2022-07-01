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

