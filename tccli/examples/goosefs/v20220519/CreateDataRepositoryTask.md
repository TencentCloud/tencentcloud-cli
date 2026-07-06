**Example 1: 创建接口调用示例**



Input: 

```
tccli goosefs CreateDataRepositoryTask --cli-unfold-argument  \
    --TaskType FS_TO_COS \
    --Bucket goosefsx-bj-df-test02-1252246555 \
    --FileSystemId x-c60-3980hscb \
    --TaskPath ace_test/ \
    --TaskName ace测试
```

Output: 
```
{
    "Response": {
        "TaskId": "x_task_1782965149652",
        "RequestId": "64ba388d-d33e-4194-8006-81b1cc2d1a00"
    }
}
```

