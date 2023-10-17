**Example 1: 创建交互式session并执行SQL任务**

本接口用于创建交互式session并执行SQL任务

Input: 

```
tccli dlc CreateNotebookSessionStatementSupportBatchSQL --cli-unfold-argument  \
    --SessionId d3018ad4-9a7e-4f64-a3f4-f38507c69742 \
    --Code select 1; \
    --Kind sql \
    --SaveResult True
```

Output: 
```
{
    "Response": {
        "NotebookSessionStatementBatches": {
            "NotebookSessionStatementBatch": [
                {
                    "Completed": 0,
                    "Started": 0,
                    "Progress": 0,
                    "StatementId": "ksiked7-ekd4-4e5e-993e-e5db64fa21c1",
                    "TaskId": "d301fsdd4-9a7e-4f64-a3dj-f38507c697dj",
                    "Code": "select 1",
                    "BatchId": "eiosldd7-ekd4-4e5e-993e-e5db64fa21c1",
                    "State": "available",
                    "OutPut": {
                        "ExecutionCount": 0,
                        "Data": [
                            {
                                "Key": "testKey",
                                "Value": "testValue"
                            }
                        ],
                        "Status": "available",
                        "ErrorName": "testErrorName",
                        "ErrorValue": "testErrorValue",
                        "ErrorMessage": [
                            "testErrorMessage"
                        ],
                        "SQLResult": "result"
                    }
                }
            ],
            "IsAvailable": true,
            "SessionId": "ksjeldd7-ekd4-4e5e-993e-e5db64fa21c1",
            "BatchId": "eiosldd7-ekd4-4e5e-993e-e5db64fa21c1"
        },
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

