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

**Example 2: 真实案例**



Input: 

```
tccli wedata DescribeTaskInstances --cli-unfold-argument  \
    --PageSize 10 \
    --ProjectId 1 \
    --TaskNameList txyuwang_python2 \
    --DateFrom 2022-0601 \
    --TaskIdList 20220506192333449 \
    --PageNumber 1 \
    --WorkflowNameList txyuwang_wf1 \
    --DateTo 2022-0701 \
    --InstanceType 1 \
    --WorkflowIdList a183fd74-c243-11ec-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "RequestId": "c976f559-6a66-46d0-bcb9-43d0d318fb5e",
        "Data": {
            "TotalCount": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "Items": [
                {
                    "ProjectId": null,
                    "ProjectName": null,
                    "ProjectIdent": null,
                    "FolderId": "e989c626-9f70-11ec-8909-bc97e105ba60",
                    "FolderName": "txyuwang_test",
                    "WorkflowId": "a183fd74-c243-11ec-8909-bc97e105ba60",
                    "WorkflowName": "txyuwang_wf1",
                    "TaskId": "20220506192333449",
                    "TaskName": "txyuwang_python2",
                    "InCharge": "TBDS",
                    "CycleType": "D",
                    "TryLimit": 5,
                    "Tries": 0,
                    "State": 1,
                    "TaskTypeId": 30,
                    "TaskTypeDesc": "Python",
                    "StartTime": null,
                    "EndTime": null,
                    "CostTime": "00:00:00.000",
                    "SchedulerDateTime": "2022-07-01 00:00:00",
                    "SchedulerDesc": "每天00:00执行一次",
                    "InstanceType": 1
                }
            ]
        }
    }
}
```

