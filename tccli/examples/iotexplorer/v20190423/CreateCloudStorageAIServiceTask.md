**Example 1: 创建设备云存 AI 分析任务**



Input: 

```
tccli iotexplorer CreateCloudStorageAIServiceTask --cli-unfold-argument  \
    --ProductId TQBDY6RPI9 \
    --DeviceName cs_112114601_2 \
    --ServiceType Highlight \
    --StartTime 1710487888 \
    --EndTime 1710487898 \
    --ChannelId 0 \
    --Config {}
```

Output: 
```
{
    "Response": {
        "RequestId": "c497cdcb-8eaf-46b0-8850-311cfb278798",
        "TaskId": "fb066d7a-baac-4706-acda-058f56f82759"
    }
}
```

**Example 2: 使用外部数据源创建云存 AI 分析任务**



Input: 

```
tccli iotexplorer CreateCloudStorageAIServiceTask --cli-unfold-argument  \
    --ProductId TQBDY6RPI9 \
    --DeviceName cs_112114601_2 \
    --ServiceType Highlight \
    --StartTime 1710487888 \
    --EndTime 1710487898 \
    --ChannelId 0 \
    --Config {} \
    --VideoURLs https://example.com/video.mp4
```

Output: 
```
{
    "Response": {
        "RequestId": "c497cdcb-8eaf-46b0-8850-311cfb278798",
        "TaskId": "fb066d7a-baac-4706-acda-058f56f82759"
    }
}
```

