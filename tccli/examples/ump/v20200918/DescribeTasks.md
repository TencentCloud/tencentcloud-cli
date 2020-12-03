**Example 1: 查询任务列表**



Input: 

```
tccli ump DescribeTasks --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Tasks": [
            {
                "TaskType": 0,
                "TaskId": 1,
                "GroupCode": "code",
                "MallId": 1,
                "TaskContent": {
                    "CameraId": 1,
                    "RTSP": "rtsp://127.0.0.1/video0",
                    "Url": "cos put url"
                }
            }
        ]
    }
}
```

