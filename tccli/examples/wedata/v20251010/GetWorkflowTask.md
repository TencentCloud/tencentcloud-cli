**Example 1: 查询工作流任务信息**

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

**Example 2: 查询工作流任务信息（返回带CreateTime和UpdateTime）**

返回带CreateTime和UpdateTime

Input: 

```
tccli wedata GetWorkflowTask --cli-unfold-argument  \
    --WorkspaceId 17697667906247629 \
    --WorkflowId dc2a92f2-09e4-4f20-b46f-4bd5434e1e63 \
    --TaskId 2d6fcfbc-d2f8-4e06-bcc5-3d6018ab0517 \
    --ExtendReturnFieldList CreateTime
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "1773040030747",
            "DependOnList": [],
            "DependOnRunCondition": "ALL_SUCCESS",
            "Description": "",
            "LeftCoordinate": 50,
            "ParamList": [],
            "ResourceGroupId": "",
            "TaskId": "2d6fcfbc-d2f8-4e06-bcc5-3d6018ab0517",
            "TaskName": "rw_260309_150703",
            "TaskRetryStrategy": {
                "MaxRetryTime": 3,
                "RetryBetweenWaitTime": 5,
                "RetryBetweenWaitTimeUnit": "SECOND",
                "TaskRunFailureRetrySwitch": true,
                "TaskRunTimeoutRetrySwitch": false
            },
            "TaskType": {
                "TaskTypeName": "RUN_WORKFLOW",
                "TaskTypePropertyList": [
                    {
                        "PropertyKey": "WorkflowId",
                        "PropertyValue": "af977f79-1588-4747-828d-4b5cea82e9ea"
                    }
                ]
            },
            "TopCoordinate": 50,
            "UpdateTime": "1773040030747"
        },
        "RequestId": "763207a9-e168-48da-be3c-1e0525ecb1c3"
    }
}
```

