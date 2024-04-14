**Example 1: 创建离线任务**

创建离线任务

Input: 

```
tccli wedata CreateOfflineTask --cli-unfold-argument  \
    --ProjectId 1486446569620893696 \
    --CycleStep 1 \
    --DelayTime 0 \
    --EndTime 2099-12-31 00:00:00 \
    --Notes  \
    --StartTime 2022-04-11 00:00:00 \
    --TaskName task test name \
    --TypeId 27 \
    --TaskAction  \
    --TaskMode 1
```

Output: 
```
{
    "Response": {
        "TaskId": "20220411181355382",
        "Data": "true",
        "RequestId": "7508483f-5202-44b3-a846-8c6efb42acb0"
    }
}
```

