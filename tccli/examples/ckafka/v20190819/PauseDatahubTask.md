**Example 1: 暂停连接器任务**

暂停连接器任务

Input: 

```
tccli ckafka PauseDatahubTask --cli-unfold-argument  \
    --TaskId task-qy9n446n
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "task-task-qy9n446n"
        },
        "RequestId": "e8042aea-b1b6-4d20-9626-9be4f3d9f69c"
    }
}
```

