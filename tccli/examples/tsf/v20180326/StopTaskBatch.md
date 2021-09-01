**Example 1: 停止执行中的任务批次**

停止执行中的任务批次

Input: 

```
tccli tsf StopTaskBatch --cli-unfold-argument  \
    --BatchId batch-12345678
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

