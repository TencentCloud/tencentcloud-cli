**Example 1: 停止任务执行**

停止正在某个节点上执行的任务

Input: 

```
tccli tsf StopTaskExecute --cli-unfold-argument  \
    --BatchId batch-12345677 \
    --ExecuteId execute-12345678 \
    --TaskId task-12345667
```

Output: 
```
{
    "Response": {
        "RequestId": "6281ddf9-1914-420b-afb8-93735ac3270a",
        "Result": true
    }
}
```

