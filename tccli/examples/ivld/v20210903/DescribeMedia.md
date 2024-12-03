**Example 1: 导入完成，返回媒资视频元信息**



Input: 

```
tccli ivld DescribeMedia --cli-unfold-argument  \
    --MediaId media-ly5qgk6j
```

Output: 
```
{
    "Response": {
        "MediaInfo": {
            "DownLoadURL": "https://ai-media-1256936300.cos.ap-guangzhou.myqcloud.com/ai-media/test/test-beijingninzao-6mins.mp4",
            "FailedReason": "",
            "MediaId": "media-ly5qgk6j",
            "Metadata": {
                "BitRate": 1420,
                "Duration": 356.024,
                "FPS": 25,
                "FileSize": 63195585,
                "Height": 720,
                "MD5": "b67489b0f5ca7822c94f4b6102ac7d13",
                "NumFrames": 8900,
                "Width": 1280
            },
            "Name": "demo-video-0",
            "Progress": 0,
            "Label": "",
            "Status": 8,
            "CallbackURL": "http://example.com/api/callback",
            "MediaType": 1,
            "AudioMetadata": null,
            "ImageMetadata": null,
            "TextMetadata": null
        },
        "RequestId": "d4c8bf8e-43ba-482a-a257-b6ac7a6296ec"
    }
}
```

**Example 2: 导入中(正在进行转码)，此时返回的视频元信息没有意义**



Input: 

```
tccli ivld DescribeMedia --cli-unfold-argument  \
    --MediaId media-ly5qgk6j
```

Output: 
```
{
    "Response": {
        "MediaInfo": {
            "DownLoadURL": "https://ai-media-1256936300.cos.ap-guangzhou.myqcloud.com/ai-media/test/test-beijingninzao-6mins.mp4",
            "FailedReason": "",
            "MediaId": "media-ly5qgk6j",
            "Metadata": {
                "BitRate": 1420,
                "Duration": 356.024,
                "FPS": 25,
                "FileSize": 63195585,
                "Height": 720,
                "MD5": "b67489b0f5ca7822c94f4b6102ac7d13",
                "NumFrames": 8900,
                "Width": 1280
            },
            "Name": "demo-video-0",
            "Progress": 0,
            "Label": "",
            "Status": 8,
            "CallbackURL": "http://example.com/api/callback",
            "MediaType": 1,
            "AudioMetadata": null,
            "ImageMetadata": null,
            "TextMetadata": null
        },
        "RequestId": "d4c8bf8e-43ba-482a-a257-b6ac7a6296ec"
    }
}
```

