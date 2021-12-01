**Example 1: 发起导入任务成功**



Input: 

```
tccli ivld ImportMedia --cli-unfold-argument  \
    --URL https://ai-media-1256936300.cos.ap-guangzhou.myqcloud.com/ai-media/test/test-news-6mins.mp4 \
    --Name demo-video-0
```

Output: 
```
{
    "Response": {
        "MediaId": "media-a1b2c3d4",
        "RequestId": "50f3df82-beae-4f5f-9b47-23e8302f62ae"
    }
}
```

