**Example 1: 查询session 中执行任务的详情**

本接口用于查询session 中执行任务的详情

Input: 

```
tccli dlc DescribeNotebookSessionStatement --cli-unfold-argument  \
    --SessionId d3018ad4-9a7e-4f64-a3f4-f38507c69742 \
    --StatementId d3018ad4-9a7e-4f64-a3dj-f38507c697dj
```

Output: 
```
{
    "Response": {
        "NotebookSessionStatement": {
            "Completed": 1662635695652,
            "Started": 1662635695652,
            "Progress": 100,
            "StatementId": "d3018ad4-9a7e-4f64-a3dj-f38507c697dj",
            "TaskId": "d301fsdd4-9a7e-4f64-a3dj-f38507c697dj",
            "State": "running",
            "OutPut": {
                "ExecutionCount": 1,
                "Data": [
                    {
                        "Key": "key",
                        "Value": "value"
                    }
                ],
                "Status": "ok",
                "ErrorName": "testErr",
                "ErrorValue": "Error",
                "ErrorMessage": [
                    "Error"
                ],
                "SQLResult": "result"
            },
            "BatchId": "bdsad7dd7-ekd4-4e5e-993e-e5db64fa21c1",
            "Code": "selelct 1;"
        },
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

