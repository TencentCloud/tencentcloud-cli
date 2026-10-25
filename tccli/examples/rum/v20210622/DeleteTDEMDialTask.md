**Example 1: 删除拨测任务**

把任务标记为已删除。已上报的探测记录仍保留。

Input: 

```
tccli rum DeleteTDEMDialTask --cli-unfold-argument  \
    --AppId 5 \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "TaskId": "1",
        "RequestId": "a21efbfa-e8d8-489e-b238-224a78d0721b"
    }
}
```

