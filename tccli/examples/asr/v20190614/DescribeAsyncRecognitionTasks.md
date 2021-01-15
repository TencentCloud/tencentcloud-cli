**Example 1: 查询运行中的任务列表**



Input: 

```
tccli asr DescribeAsyncRecognitionTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "8824366f-0e8f-4bd4-8924-af5e84127caa",
        "Data": {
            "Tasks": [
                {
                    "TaskId": 9266418,
                    "Url": ""
                }
            ]
        }
    }
}
```

