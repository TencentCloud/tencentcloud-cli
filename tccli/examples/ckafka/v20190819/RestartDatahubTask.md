**Example 1: 重启连接器任务**

重启连接器任务

Input: 

```
tccli ckafka RestartDatahubTask --cli-unfold-argument  \
    --TaskId task-qy9e9b6n
```

Output: 
```
{
    "Response": {
        "Result": {
            "TaskId": "task-qy9e9b6n"
        },
        "RequestId": "e8042aea-b1b6-4d20-9626-9be4f3d9f69c"
    }
}
```

