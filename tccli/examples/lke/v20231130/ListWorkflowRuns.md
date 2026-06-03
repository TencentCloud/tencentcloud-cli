**Example 1: 查询工作流异步运行实例的列表**

查询工作流异步运行实例的列表

Input: 

```
tccli lke ListWorkflowRuns --cli-unfold-argument  \
    --AppBizId 2029461666234922753 \
    --PageSize 20 \
    --Page 1 \
    --Query bnis908spzb4
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "WorkflowRuns": [
            {
                "AppBizId": "2029461666234922753",
                "CreateTime": "1772751757725",
                "EndTime": "1772751765933",
                "FailMessage": "",
                "Name": "异步工作流",
                "RunEnv": 0,
                "StartTime": "1772751758509",
                "State": 2,
                "TotalTokens": 436,
                "WorkflowId": "0e3510a6-1855-4dc2-9065-996a510a543c",
                "WorkflowRunId": "wfr-bnis908spzb4"
            }
        ],
        "RequestId": "109d44bc-937f-4ea5-9e99-b7480161efee"
    }
}
```

