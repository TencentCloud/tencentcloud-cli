**Example 1: 批量取消Session 中执行的任务**

本接口用于批量取消Session 中执行的任务

Input: 

```
tccli dlc CancelNotebookSessionStatementBatch --cli-unfold-argument  \
    --SessionId d3018ad4-9a7e-4f64-a3f4-f38507c69742 \
    --BatchId kdsesad4-9a7e-4f64-a3dj-f38507c697dj
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

