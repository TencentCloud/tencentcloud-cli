**Example 1: 成功**

查询工作流信息成功

Input: 

```
tccli wedata DrawWorkflow --cli-unfold-argument  \
    --WorkspaceId 1346 \
    --WorkflowId 22b9891f-7f72-4e20-a746-d2b78f8c52e2
```

Output: 
```
{
    "Response": {
        "Data": {
            "AdvanceConfig": {
                "MaxConcurrentNum": 1,
                "QueuingMode": "OFF"
            },
            "BaseInfo": {
                "CreateUserName": "",
                "CreateUserUin": "600000561778",
                "Description": "",
                "ExecuteUserName": "",
                "ExecuteUserUin": "",
                "WorkflowId": "22b9891f-7f72-4e20-a746-d2b78f8c52e2",
                "WorkflowName": "dasewqe232323"
            },
            "BundleId": "",
            "BundleInfo": "",
            "LabelList": [],
            "MyFavorite": false,
            "ParamList": [],
            "TaskList": [],
            "Trigger": [],
            "WorkspaceId": "1346"
        },
        "RequestId": "83f8394f-b128-4ab4-a008-cf5618b1447b"
    }
}
```

