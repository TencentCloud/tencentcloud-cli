**Example 1: 创建外部视频 AI 分析任务**



Input: 

```
tccli iotexplorer CreateExternalSourceAIServiceTask --cli-unfold-argument  \
    --ProductId TQBDY6RPI9 \
    --ServiceType Highlight \
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

