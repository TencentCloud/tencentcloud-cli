**Example 1: 获取任务状态**

获取任务状态

Input: 

```
tccli cr DescribeTaskStatus --cli-unfold-argument  \
    --Module Task \
    --Operation DescribeTaskStatus \
    --TaskId tad-i9yf5g5f0d
```

Output: 
```
{
    "Response": {
        "RequestId": "cea58738-396c-49fa-915e-f32280bc1ac2",
        "TaskResult": "File Uploading Task Success.",
        "TaskType": "002"
    }
}
```

