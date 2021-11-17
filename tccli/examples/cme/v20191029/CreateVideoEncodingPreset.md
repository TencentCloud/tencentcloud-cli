**Example 1: 创建360p的视频编码配置**

创建360p的视频编码配置
详细功能：去除音频流，设置码率为500k bps

Input: 

```
tccli cme CreateVideoEncodingPreset --cli-unfold-argument  \
    --Platform test \
    --Name 自定义360p编码配置 \
    --RemoveAudio 1 \
    --VideoSetting.ShortEdge 360 \
    --VideoSetting.Bitrate 512000
```

Output: 
```
{
    "Response": {
        "Id": 100050,
        "RequestId": "e33fffc2-02c9-4074-9355-88443869e88b"
    }
}
```

**Example 2: 创建单声道音频编码配置**



Input: 

```
tccli cme CreateVideoEncodingPreset --cli-unfold-argument  \
    --Platform test \
    --Name 自定义单声道音频编码配置 \
    --AudioSetting.Channels 1
```

Output: 
```
{
    "Response": {
        "Id": 100049,
        "RequestId": "22392574-2d1d-4418-94bb-a71ee67fbc56"
    }
}
```

