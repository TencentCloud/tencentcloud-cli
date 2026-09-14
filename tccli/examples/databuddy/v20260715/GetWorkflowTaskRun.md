**Example 1: 查询任务运行详情**



Input: 

```
tccli databuddy GetWorkflowTaskRun --cli-unfold-argument  \
    --WorkspaceId 17697410068842890 \
    --WorkflowTaskRunId f2d5ffc0-af32-4584-a315-b106637f1bfe_1786115878097_1
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "1786115878247",
            "CreateUserUin": "700002164618",
            "DependOnList": [],
            "DependenceFinishedTime": "0",
            "ErrorCodeString": "",
            "IsLatestRun": true,
            "JobId": "",
            "LeftCoordinate": 0,
            "RerunTimes": 0,
            "ResourceGroupId": "",
            "ResourceGroupInfoList": [],
            "RetryTimes": 0,
            "RunCostTime": "0",
            "RunParams": "",
            "RunResult": "",
            "RunState": "CREATE",
            "RunUserName": "weda***0*d*v*********c**",
            "RunUserUin": "700002164618",
            "TaskId": "f2d5ffc0-af32-4584-a315-b106637f1bfe",
            "TaskName": "py_0807",
            "TaskTypeExtensions": "{\"TaskTypeName\":\"PYTHON\",\"Notebook\":null,\"TaskTypePropertyList\":[{\"PropertyKey\":\"Source\",\"PropertyValue\":\"5\"},{\"PropertyKey\":\"SourcePath\",\"PropertyValue\":\"/Workspace/test.py\"}],\"RuntimePropertyList\":[{\"PropertyKey\":\"ConfigType\",\"PropertyValue\":\"DEFAULT\"},{\"PropertyKey\":\"DriverCU\",\"PropertyValue\":\"large\"},{\"PropertyKey\":\"DriverGPU\",\"PropertyValue\":\"\"},{\"PropertyKey\":\"ExecutorAllocation\",\"PropertyValue\":\"DYNAMIC\"},{\"PropertyKey\":\"ExecutorCU\",\"PropertyValue\":\"large\"},{\"PropertyKey\":\"ExecutorFixedNum\",\"PropertyValue\":\"1\"},{\"PropertyKey\":\"ExecutorGPU\",\"PropertyValue\":\"\"},{\"PropertyKey\":\"ExecutorMaxNum\",\"PropertyValue\":\"15\"},{\"PropertyKey\":\"ExecutorMinNum\",\"PropertyValue\":\"1\"},{\"PropertyKey\":\"ResourceMode\",\"PropertyValue\":\"1\"},{\"PropertyKey\":\"Style\",\"PropertyValue\":\"UI\"}]}",
            "TaskTypeName": "PYTHON",
            "TaskVersionId": "2cf47642-f9b8-4b93-a6fa-31a03810c423",
            "TimeZone": "",
            "TopCoordinate": 0,
            "TriggerType": "",
            "UpdateTime": "1786115878236",
            "WaitTime": "1645528",
            "WorkflowId": "8e0e3485-2736-4530-92ed-932e019898f1",
            "WorkflowName": "new_workflow_20260807_190451",
            "WorkflowRunId": "8e0e3485-2736-4530-92ed-932e019898f1_1786115878097",
            "WorkflowTaskRunId": "f2d5ffc0-af32-4584-a315-b106637f1bfe_1786115878097_1",
            "WorkspaceId": "17697410068842890"
        },
        "RequestId": "f3a6c04b-fe86-48b3-bdb5-8bd4523a7698"
    }
}
```

