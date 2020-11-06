**Example 1: 重新执行批次**

重新执行批次

Input: 

```
tccli tsf RedoTaskBatch --cli-unfold-argument  \
    --TaskId task-qov7j8ky \
    --BatchId batch-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "6281ddf9-1914-420b-afb8-93735ac3270a",
        "Result": "batch-123456"
    }
}
```

