**Example 1: 创建设备云存 AI 分析任务（执行成功）**



Input: 

```
tccli iotexplorer InvokeCloudStorageAIServiceTask --cli-unfold-argument  \
    --ProductId TSLFHRWDSD \
    --DeviceName dev002 \
    --ServiceType VideoToText \
    --StartTime 1732780832 \
    --EndTime 1732780835 \
    --VideoURLs https://example.com/video.mp4
```

Output: 
```
{
    "Response": {
        "Completed": true,
        "RequestId": "5acdfd09-5634-4ae3-8ebd-1d4c33bb7dd7",
        "TaskId": "019371d2-da8b-7171-a6de-fc077173b205",
        "TaskInfo": {
            "ChannelId": 0,
            "CreateTime": 1732781464,
            "DeviceName": "dev002",
            "EndTime": 1732780835,
            "Files": [],
            "ProductId": "TSLFHRWDSD",
            "Result": "{\"DetectedClassifications\": [\"person\"], \"Summary\": \"白衣人走在湿漉漉的路面上\"}",
            "ServiceType": "VideoToText",
            "StartTime": 1732780832,
            "Status": 3,
            "TaskId": "019371d2-da8b-7171-a6de-fc077173b205",
            "UpdateTime": 1732781466
        }
    }
}
```

**Example 2: 创建设备云存 AI 分析任务（超时未完成，转异步）**



Input: 

```
tccli iotexplorer InvokeCloudStorageAIServiceTask --cli-unfold-argument  \
    --ProductId TSLFHRWDSD \
    --DeviceName dev002 \
    --ServiceType VideoToText \
    --StartTime 1732780832 \
    --EndTime 1732780835 \
    --VideoURLs https://example.com/video.mp4
```

Output: 
```
{
    "Response": {
        "Completed": false,
        "RequestId": "5acdfd09-5634-4ae3-8ebd-1d4c33bb7dd7",
        "TaskId": "019371d2-da8b-7171-a6de-fc077173b205",
        "TaskInfo": {
            "ChannelId": 0,
            "CreateTime": 1732781464,
            "DeviceName": "dev002",
            "EndTime": 1732780835,
            "Files": [],
            "ProductId": "TSLFHRWDSD",
            "Result": "",
            "ServiceType": "VideoToText",
            "StartTime": 1732780832,
            "Status": 4,
            "TaskId": "019371d2-da8b-7171-a6de-fc077173b205",
            "UpdateTime": 1732781464
        }
    }
}
```

