**Example 1: 在session中执行代码片段**

本接口用于在session中执行代码片段

Input: 

```
tccli dlc CreateNotebookSessionStatement --cli-unfold-argument  \
    --SessionId d3018ad4-9a7e-4f64-a3f4-f38507c69742 \
    --Code select 1 \
    --Kind sql
```

Output: 
```
{
    "Response": {
        "NotebookSessionStatement": {
            "Started": 1662635695652,
            "Completed": 1662635695652,
            "State": "running",
            "StatementId": "d3018ad4-9a7e-4f64-a3dj-f38507c697dj",
            "TaskId": "d301fsdd4-9a7e-4f64-a3dj-f38507c697dj",
            "Progress": 100,
            "OutPut": {
                "ExecutionCount": 1,
                "Data": [
                    {
                        "Value": "value",
                        "Key": "key"
                    }
                ],
                "Status": "ok",
                "ErrorName": "testErr",
                "ErrorValue": "Error",
                "ErrorMessage": [
                    "Error"
                ],
                "SQLResult": "result"
            }
        },
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

