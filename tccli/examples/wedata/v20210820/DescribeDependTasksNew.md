**Example 1: 根据层级查找上-下游任务节点**



Input: 

```
tccli wedata DescribeDependTasksNew --cli-unfold-argument  \
    --Deep 1 \
    --TaskId 123123 \
    --Up 2 \
    --ProjectId 1 \
    --WorkflowId 338a6229-72d6-11ec-854b-525400f55a20
```

Output: 
```
{
    "Response": {
        "Data": {
            "TasksList": [
                {
                    "TaskId": "20220107114644842",
                    "TaskName": "hive_sql",
                    "WorkflowId": "be741023-6d44-11ec-a07d-525400f55a20",
                    "WorkflowName": "mywf1",
                    "ProjectName": "zch",
                    "ProjectIdent": "zch",
                    "Status": "F",
                    "TaskTypeId": 34,
                    "TaskTypeDesc": "Hive SQL",
                    "ProjectId": "8",
                    "FolderName": "mytest",
                    "FolderId": "b9f64ab3-6d44-11ec-a07d-525400f55a20",
                    "FirstSubmitTime": "2022-02-19 19:33:07",
                    "FirstRunTime": null,
                    "ScheduleDesc": null,
                    "CycleUnit": "D",
                    "InCharge": ";wangling;xue;",
                    "TaskAction": "",
                    "DelayTime": 0,
                    "LeftCoordinate": 755.17,
                    "TopCoordinate": 459.5,
                    "VirtualFlag": true
                },
                {
                    "TaskId": "20220107142238149",
                    "TaskName": "asdfasfaasdf",
                    "WorkflowId": "be741023-6d44-11ec-a07d-525400f55a20",
                    "WorkflowName": "mywf1",
                    "ProjectName": "zch",
                    "ProjectIdent": "zch",
                    "Status": "Y",
                    "TaskTypeId": 30,
                    "TaskTypeDesc": "Python",
                    "ProjectId": "8",
                    "FolderName": "mytest",
                    "FolderId": "b9f64ab3-6d44-11ec-a07d-525400f55a20",
                    "FirstSubmitTime": "2022-01-12 21:32:47",
                    "FirstRunTime": null,
                    "ScheduleDesc": null,
                    "CycleUnit": "D",
                    "InCharge": ";admin;",
                    "TaskAction": "",
                    "DelayTime": 0,
                    "LeftCoordinate": 206.0,
                    "TopCoordinate": 254.0,
                    "VirtualFlag": false
                },
                {
                    "TaskId": "20220111200138961",
                    "TaskName": "shell_01",
                    "WorkflowId": "338a6229-72d6-11ec-854b-525400f55a20",
                    "WorkflowName": "ceshi",
                    "ProjectName": "zch",
                    "ProjectIdent": "zch",
                    "Status": "Y",
                    "TaskTypeId": 38,
                    "TaskTypeDesc": "SHELL",
                    "ProjectId": "8",
                    "FolderName": "hhhuilli",
                    "FolderId": "a7704640-72c0-11ec-854b-525400f55a20",
                    "FirstSubmitTime": "2022-01-18 17:30:45",
                    "FirstRunTime": "2022-01-12 00:00:00",
                    "ScheduleDesc": "从2022-01-12 00:00:00开始，每间隔1天执行一次",
                    "CycleUnit": "D",
                    "InCharge": ";hui;",
                    "TaskAction": "",
                    "DelayTime": 0,
                    "LeftCoordinate": 1691.0,
                    "TopCoordinate": 234.0,
                    "VirtualFlag": false
                }
            ],
            "LinksList": [
                {
                    "TaskTo": "20220111200138961",
                    "TaskFrom": "20220107114644842",
                    "LinkType": "virtual_real",
                    "LinkId": "c89d3dd2-ad84-11ec-9431-e997374ddc6b"
                },
                {
                    "TaskTo": "20220107142238149",
                    "TaskFrom": "20220111200138961",
                    "LinkType": "virtual_real",
                    "LinkId": "b8504d7e-ad85-11ec-9431-e997374ddc6b"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

