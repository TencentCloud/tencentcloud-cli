**Example 1: 创建离线任务**

创建离线任务

Input: 

```
tccli wedata CreateOfflineTask --cli-unfold-argument  \
    --ProjectId abc \
    --CycleStep 0 \
    --DelayTime 0 \
    --EndTime abc \
    --Notes abc \
    --StartTime abc \
    --TaskName abc \
    --TypeId 0 \
    --TaskAction abc \
    --TaskMode abc
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "Data": "abc",
        "RequestId": "abc"
    }
}
```

