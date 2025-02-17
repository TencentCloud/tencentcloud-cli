**Example 1: 创建外部视频 AI 分析任务（执行成功）**



Input: 

```
tccli iotexplorer InvokeExternalSourceAIServiceTask --cli-unfold-argument  \
    --ProductId TQBDY6RPI9 \
    --ServiceType Highlight \
    --VideoURLs https://example.com/video.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "8b490930-d119-4ee2-963c-c58973a1ebe6",
        "Completed": true,
        "TaskId": "c31aa4f2-08c9-4088-9603-186d7311fdd8",
        "TaskInfo": {
            "ChannelId": 0,
            "CreateTime": 1714240802,
            "DeviceName": "dev001",
            "EndTime": 1714233600,
            "Files": [
                "output.mp4"
            ],
            "ProductId": "TSLFHRWDSD",
            "Result": "",
            "ServiceType": "Highlight",
            "StartTime": 1714147200,
            "Status": 3,
            "TaskId": "c31aa4f2-08c9-4088-9603-186d7311fdd8",
            "UpdateTime": 1714240802
        }
    }
}
```

**Example 2: 创建外部视频 AI 分析任务（超时未完成，转异步）**



Input: 

```
tccli iotexplorer InvokeExternalSourceAIServiceTask --cli-unfold-argument  \
    --ProductId TQBDY6RPI9 \
    --ServiceType Highlight \
    --VideoURLs https://example.com/video.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "8b490930-d119-4ee2-963c-c58973a1ebe6",
        "Completed": false,
        "TaskId": "c31aa4f2-08c9-4088-9603-186d7311fdd8",
        "TaskInfo": {
            "ChannelId": 0,
            "CreateTime": 1714240802,
            "DeviceName": "dev001",
            "EndTime": 1714233600,
            "Files": [],
            "ProductId": "TSLFHRWDSD",
            "Result": "",
            "ServiceType": "Highlight",
            "StartTime": 1714147200,
            "Status": 4,
            "TaskId": "c31aa4f2-08c9-4088-9603-186d7311fdd8",
            "UpdateTime": 1714240802
        }
    }
}
```

