**Example 1: 创建数据流动任务示例**



Input: 

```
tccli goosefs CreateDataRepositoryTask --cli-unfold-argument  \
    --TaskType COS_TO_FS \
    --Bucket bucket-123456 \
    --FileSystemId x-c60-v321qq3 \
    --TaskPath test/ \
    --TaskName 预热任务 \
    --EnableDataFlowSubPath True \
    --DataFlowSubPath dst/
```

Output: 
```
{
    "Response": {
        "TaskId": "x_task_1769158823183",
        "RequestId": "7bc315dc-c3fa-4c23-b719-30e382d36afb"
    }
}
```

