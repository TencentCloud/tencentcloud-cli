**Example 1: 调用**



Input: 

```
tccli goosefs CreateDataRepositoryTask --cli-unfold-argument  \
    --TaskType COS_TO_FS \
    --Bucket ace-bj-donot-del-xxxxx \
    --FileSystemId x-c60-xxxx \
    --TaskPath dup/ \
    --TaskName 预热测试_1 \
    --EnableCustomDestPath False \
    --OutputBucket ace-bj-donot-del-xxxxx \
    --OutputPrefix data-repository-task-results/
```

Output: 
```
{
    "Response": {
        "TaskId": "x_task_1787660399825",
        "RequestId": "17015b3c-9d94-4c0a-8e00-5d53cc86fca5"
    }
}
```

