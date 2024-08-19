**Example 1: 快速剪辑视频**



Input: 

```
tccli vod FastEditMedia --cli-unfold-argument  \
    --FileInfos.0.EndTimeOffset 0.0 \
    --FileInfos.0.StartTimeOffset 30.0 \
    --FileInfos.0.AudioVideoType Original \
    --FileInfos.0.TranscodeDefinition 100210 \
    --FileInfos.0.FileId 5285890784246869930
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "FileId": "152854854879852xxxxx",
        "Url": "https://xxx.vod2.myqcloud.com/xxx/xxx.m3u8"
    }
}
```

