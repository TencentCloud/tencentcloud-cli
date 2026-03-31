**Example 1: 成功**

获取工作流下任务信息成功

Input: 

```
tccli wedata GetWorkflowTask --cli-unfold-argument  \
    --WorkspaceId 1 \
    --WorkflowId 4b8763136afd71984ff044233c7ff2a4 \
    --TaskId 0029fecd-6ec9-4168-910b-216b7d33a4c4
```

Output: 
```
{
    "Response": {
        "Data": {
            "DependOnList": [],
            "DependOnRunCondition": "ALL_SUCCESS",
            "Description": "",
            "LeftCoordinate": 0,
            "ParamList": [],
            "ResourceGroupId": "1",
            "TaskId": "0029fecd-6ec9-4168-910b-216b7d33a4c4",
            "TaskName": "task_ss_01",
            "TaskRetryStrategy": {
                "MaxRetryTime": 0,
                "RetryBetweenWaitTime": 0,
                "RetryBetweenWaitTimeUnit": "MINUTE",
                "TaskRunFailureRetrySwitch": false,
                "TaskRunTimeoutRetrySwitch": false
            },
            "TaskType": {
                "Notebook": {
                    "DisplayPath": "/workspace/notebook/test.ipynb",
                    "NotebookAbsolutePath": "",
                    "NotebookPath": "/workspace/notebook/test.ipynb",
                    "Source": "SCRIPT_SOURCE_CFS"
                },
                "TaskTypeName": "NOTEBOOK"
            },
            "TopCoordinate": 0
        },
        "RequestId": "33f34664-699f-4598-94ce-c21e55f4b8ef"
    }
}
```

