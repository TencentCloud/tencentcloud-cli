**Example 1: 创建视频语义异步搜索任务**



Input: 

```
tccli iotexplorer CreateAISearchTaskAsync --cli-unfold-argument  \
    --ProductId MVTYMD8YCD \
    --DeviceName dev001 \
    --Query What happened on April 1st
```

Output: 
```
{
    "Response": {
        "RequestId": "a9a9d232-01c0-494a-baa3-57c384463c3f",
        "TaskId": "task_0001"
    }
}
```

