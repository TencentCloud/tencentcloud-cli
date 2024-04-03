**Example 1: 导入图片**



Input: 

```
tccli ivld ImportMedia --cli-unfold-argument  \
    --URL https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/phye-debug/male.png \
    --Name male.png \
    --MediaType 1
```

Output: 
```
{
    "Response": {
        "MediaId": "media-9DfyyCOZ",
        "RequestId": "a642b499-9ebd-4601-a57e-a8cf5c2bee49"
    }
}
```

**Example 2: 发起导入任务成功**



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

