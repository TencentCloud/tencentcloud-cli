**Example 1: ListUpstreamOpsTasks（异常）**

异常示例（注意：此接口仅用于 任务调度 项目，其他类型项目使用此接口，可能会出现如下报错）

Input: 

```
tccli wedata ListUpstreamOpsTasks --cli-unfold-argument  \
    --TaskId 20250725174033396 \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound",
            "Message": "WeData通用内部异常:资源未找到"
        },
        "RequestId": "07faa9b8-f855-48bd-903b-88f35e180f22"
    }
}
```

**Example 2: ListUpstreamOpsTasks（正常）**

正常示例（注意：此接口仅用于 任务调度 项目）

Input: 

```
tccli wedata ListUpstreamOpsTasks --cli-unfold-argument  \
    --ProjectId 2917455276892352512 \
    --TaskId 20250917185450618
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CycleType": "DAY_CYCLE",
                    "ExecutionEndTime": null,
                    "ExecutionStartTime": null,
                    "FirstRunTime": null,
                    "FirstSubmitTime": "2025-09-17 19:15:04",
                    "FolderId": "e37d78f2-8d2e-11f0-a985-98039b019e92",
                    "FolderName": "bbk",
                    "OwnerUin": null,
                    "ProjectId": "2917455276892352512",
                    "ProjectName": "ZD_APItest",
                    "ScheduleDesc": "u6bcfu592919:18u6267u884cu4e00u6b21",
                    "Status": "Y",
                    "TaskId": "20250909114238680",
                    "TaskName": "bbk_py",
                    "TaskTypeDesc": "Python",
                    "TaskTypeId": 30,
                    "WorkflowId": "d5de2330-a41d-4dca-8095-0e9562795987",
                    "WorkflowName": "bbk_wf"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "cf558d27-2ca9-4f58-b97f-17b3a2e67de7"
    }
}
```

