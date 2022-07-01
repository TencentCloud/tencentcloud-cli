**Example 1: 示例**



Input: 

```
tccli wedata DescribeTaskInstances --cli-unfold-argument  \
    --TaskCycleUnitList xx \
    --InChargeList xx \
    --PageSize 0 \
    --ProjectId xx \
    --TaskNameList xx \
    --OrderFields.0.Direction xx \
    --OrderFields.0.Name xx \
    --StateList xx \
    --TaskTypeIdList 0 \
    --TaskIdList 0 \
    --DateFrom xx \
    --PageNumber 0 \
    --WorkflowIdList xx \
    --DateTo xx \
    --InstanceType 0 \
    --WorkflowNameList xx
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

