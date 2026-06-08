**Example 1: 恢复连接器任务**

恢复连接器任务

Input: 

```
tccli ckafka ResumeDatahubTask --cli-unfold-argument  \
    --TaskId task-qy9z246n
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "task-qy9z246n"
        },
        "RequestId": "e8042aea-b1b6-4d20-9626-9be4f3d9f69c"
    }
}
```

