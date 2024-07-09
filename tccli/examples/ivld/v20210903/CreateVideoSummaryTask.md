**Example 1: 创建视频缩编任务**

创建视频缩编任务，并且生成视频回写到 cos。

Input: 

```
tccli ivld CreateVideoSummaryTask --cli-unfold-argument  \
    --SummaryType 1 \
    --VideoURL https://ai-media-1256936300.cos.ap-guangzhou.myqcloud.com/test_data/test-beijingninzao-6mins.mp4 \
    --WriteBackCosPath https://test-media-ai-251202827.cos.ap-guangzhou.myqcloud.com/ai-media/video-summary/ \
    --ActiveVideoGenerate True
```

Output: 
```
{
    "Response": {
        "RequestId": "5646aef2-9481-409b-ba6f-91c40f5f9de6",
        "TaskId": "task-5bMQVrmJyPJ"
    }
}
```

