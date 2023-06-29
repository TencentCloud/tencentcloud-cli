**Example 1: 获取数据流通任务实时状态**

创建数据流通任务后, 获取任务的状态

Input: 

```
tccli goosefs DescribeDataRepositoryTaskStatus --cli-unfold-argument  \
    --FileSystemId x_c60_r3c4fa1f \
    --TaskId x_task_xxf4
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "FinishedFileNumber": 1,
        "FinishedCapacity": 1,
        "TaskId": "x_task_xxf4",
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

