**Example 1: 重新执行任务**

在某个节点上重新执行任务

Input: 

```
tccli tsf RedoTaskExecute --cli-unfold-argument  \
    --BatchId batch-12345678 \
    --ExecuteId execute-12345678 \
    --TaskId task-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "6281ddf9-1914-420b-afb8-93735ac3270a",
        "Result": "batch-1234456"
    }
}
```

