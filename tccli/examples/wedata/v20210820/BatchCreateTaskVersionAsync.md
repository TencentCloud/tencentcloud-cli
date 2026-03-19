**Example 1: 批量提交任务**

批量提交任务

Input: 

```
tccli wedata BatchCreateTaskVersionAsync --cli-unfold-argument  \
    --Tasks.0.TaskId 20260120104606329 \
    --ProjectId 1464962169590902784
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": 2528
        },
        "RequestId": "e1362eb3-40b7-456d-b801-c8f1e319fc63"
    }
}
```

