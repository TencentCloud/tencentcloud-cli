**Example 1: 停止任务运行**

成功停止任务运行

Input: 

```
tccli wedata KillTaskExecution --cli-unfold-argument  \
    --WorkspaceId 1 \
    --TaskExecutionIdList t_exec_1001_1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ActionResults": [
                {
                    "ErrorMessage": "",
                    "ExecutionActionId": "",
                    "ItemId": "t_exec_1001_1",
                    "ItemName": "",
                    "OpStatus": true
                }
            ]
        },
        "RequestId": "f8e89fe7-9d22-414c-8298-2fe8b58b3b08"
    }
}
```

