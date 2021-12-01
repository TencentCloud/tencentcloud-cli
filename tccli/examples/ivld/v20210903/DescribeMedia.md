**Example 1: 导入中(正在进行转码)，此时返回的视频元信息没有意义**



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
                "BitRate": 0,
                "Duration": 0,
                "FPS": 0,
                "FileSize": 0,
                "Height": 0,
                "MD5": "",
                "NumFrames": 0,
                "Width": 0
            },
            "Name": "demo-video.mp4",
            "Progress": 0,
            "Status": 5
        },
        "RequestId": "7f415981-cba6-426d-92df-331f29f3bb16"
    }
}
```

**Example 2: 导入完成，返回媒资视频元信息**



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
            "Status": 8
        },
        "RequestId": "d4c8bf8e-43ba-482a-a257-b6ac7a6296ec"
    }
}
```

