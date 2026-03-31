**Example 1: 查询工作流运行详情**

成功查询工作流运行详情

Input: 

```
tccli wedata GetWorkflowExecution --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --WorkflowExecutionId 17b556ed-2afc-4b26-b4d1-fe4d5251a7d6 \
    --PageSize 1 \
    --PageNumber 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "BizStateEnumInfos": [
                {
                    "Count": 1,
                    "LabelKey": "FAILED",
                    "LabelValue": "失败"
                }
            ],
            "TaskExecutions": [
                {
                    "CreateTime": "1767943933731",
                    "CreateUin": "700002164618",
                    "DependOnList": [],
                    "DependenceFinishedTime": "1767943934432",
                    "ErrorCodeStr": "TaskExecuteFailed",
                    "ExecuteUserName": "wedata30-dev@tencent.com",
                    "ExecuteUserUin": "700002164618",
                    "ExecutionEndTime": "1767944060000",
                    "ExecutionId": "5ab46ddb-beb4-465a-88d5-7100c9c22dc3",
                    "ExecutionResult": "",
                    "ExecutionStartTime": "1767943983000",
                    "ExecutionState": "FAILED",
                    "ExecutionTime": "77000",
                    "IsLatestExecution": true,
                    "IssueTime": "1767943934967",
                    "JobId": "6820260109153214007",
                    "RerunTimes": 0,
                    "ResourceGroupId": "res-fa1fbcf4",
                    "ResourceGroupInfoList": [
                        {
                            "ResourceGroupId": "res-fa1fbcf4",
                            "ResourceGroupName": "dev_test_260107_104759",
                            "ResourceGroupStatus": "3"
                        }
                    ],
                    "RetryTimes": 0,
                    "RunParams": "{\"c_t\": \"b\"}",
                    "TaskId": "ffa770e9-e1c1-45fa-bc70-07d1ac0ec6d9",
                    "TaskName": "26-01-09-15-32-divewang_test_0109_10-84b0dd9a19ee414eacdda62c8e2c9a37-task",
                    "TaskTypeExtensions": "{\"TaskTypeName\":\"NOTEBOOK\",\"Notebook\":null,\"TaskTypePropertyList\":[{\"PropertyKey\":\"Source\",\"PropertyValue\":\"3\"},{\"PropertyKey\":\"NotebookPath\",\"PropertyValue\":\"/Workspace/Users/wedata30-dev@tencent.com@700002164618/automl/26-01-09-15-32-divewang_test_0109_10-84b0dd9a19ee414eacdda62c8e2c9a37/26-01-09-15-32-divewang_test_0109_10-84b0dd9a19ee414eacdda62c8e2c9a37-code.ipynb\"},{\"PropertyKey\":\"CodeFileId\",\"PropertyValue\":\"797487896134057984\"},{\"PropertyKey\":\"PreCodeCosPath\",\"PropertyValue\":\"https://bucket-30-251436191.cos.ap-guangzhou.myqcloud.com/sci/17663856806379896/personal/700002164618/797487896134057984/notebook_preload_script.py\"}]}",
                    "TaskTypeName": "NOTEBOOK",
                    "TaskVersionId": "c2b51691-55d7-4cf7-9722-aab4e2ef90f2",
                    "TimeZone": "",
                    "TriggerType": "Manual",
                    "UpdateTime": "1767944064196",
                    "WaitTime": "49269",
                    "WorkflowExecutionId": "17b556ed-2afc-4b26-b4d1-fe4d5251a7d6",
                    "WorkflowId": "0ee6af26-f378-43c0-bd86-16ba79d5583e",
                    "WorkflowName": "26-01-09-15-32-divewang_test_0109_10-84b0dd9a19ee414eacdda62c8e2c9a37-workflow",
                    "WorkspaceId": "17663856806379896"
                }
            ],
            "WorkflowExecution": {
                "AppId": "251436191",
                "CreateTime": "1767943933508",
                "EndTime": "1767944066429",
                "ErrorCodeStr": "ExecutionFailed",
                "ExecuteUserName": "wedata30-dev@tencent.com",
                "ExecuteUserUin": "700002164618",
                "ExecutionCostTime": "83",
                "ExecutionEndTime": "1767944066429",
                "ExecutionId": "17b556ed-2afc-4b26-b4d1-fe4d5251a7d6",
                "ExecutionStartTime": "1767943983000",
                "ExecutionState": "FAILED",
                "LabelList": [],
                "ParentTaskExecutionId": "",
                "ParentTaskExecutionName": "",
                "ParentWorkflowExecutionId": "",
                "PendingCostTime": "48",
                "PendingStartTime": "1767943934096",
                "Permission": "",
                "QueueCostTime": "0",
                "QueueStartTime": "1767943933815",
                "RerunTimes": 0,
                "ResourceGroupIds": [
                    "res-fa1fbcf4"
                ],
                "ResourceGroupInfoList": [
                    {
                        "ResourceGroupId": "res-fa1fbcf4",
                        "ResourceGroupName": "dev_test_260107_104759",
                        "ResourceGroupStatus": "3"
                    }
                ],
                "SelectedTaskIds": [
                    "ffa770e9-e1c1-45fa-bc70-07d1ac0ec6d9"
                ],
                "SupportRerun": true,
                "TriggerType": "Manual",
                "WorkflowId": "0ee6af26-f378-43c0-bd86-16ba79d5583e",
                "WorkflowName": "26-01-09-15-32-divewang_test_0109_10-84b0dd9a19ee414eacdda62c8e2c9a37-workflow",
                "WorkflowParams": "{\"c_t\": \"a\"}",
                "WorkflowVersionId": "92a0c33e-0db2-48d1-9eb2-cc5f152d9ef4",
                "WorkspaceId": "17663856806379896"
            }
        },
        "RequestId": "8596beea-811a-47f8-ab28-1b36e8512da6"
    }
}
```

