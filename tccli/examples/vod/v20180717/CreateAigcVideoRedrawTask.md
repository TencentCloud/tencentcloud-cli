**Example 1: 创建创建视频转绘任务**



Input: 

```
tccli vod CreateAigcVideoRedrawTask --cli-unfold-argument  \
    --SubAppId 221073 \
    --FileInfo.Type Url \
    --FileInfo.Url https://cg-sdk-1258344699.cos.ap-nanjing.myqcloud.com/BackendBeauty/testcase/input.mp4
```

Output: 
```
{
    "Response": {
        "TaskId": "221073-AigcVideoRedrawTask-2242390fb******************e33b0t",
        "RequestId": "6b3ebd10-f36c-4286-9389-f91b17e7042b"
    }
}
```

