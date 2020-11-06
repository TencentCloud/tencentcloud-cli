**Example 1: 裁剪 HLS 视频（时间偏移量均为正数）**

裁剪视频第 2 秒到 第 10 秒

Input: 

```
tccli vod SimpleHlsClip --cli-unfold-argument  \
    --Url http://xxxxx.vod2.myqcloud.com/xxxxx/aaaaaa/hhh.m3u8 \
    --StartTimeOffset 2 \
    --EndTimeOffset 10
```

Output: 
```
{
    "Response": {
        "Url": "http://xxxxx.vod2.myqcloud.com/xxxxx/aaaaaa/10_50.m3u8",
        "MetaData": {
            "Size": 0,
            "Container": "hls",
            "Bitrate": 622014,
            "Height": 480,
            "Width": 640,
            "Duration": 48,
            "Rotate": 0,
            "VideoStreamSet": [
                {
                    "Bitrate": 592385,
                    "Height": 480,
                    "Width": 640,
                    "Codec": "h264",
                    "Fps": 25
                }
            ],
            "AudioStreamSet": [
                {
                    "Bitrate": 29629,
                    "SamplingRate": 44100,
                    "Codec": "aac"
                }
            ],
            "VideoDuration": 0,
            "AudioDuration": 0
        },
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: 裁剪 HLS 视频（时间偏移量为负数）**

裁剪第 2 秒开始到倒数第 10 秒

Input: 

```
tccli vod SimpleHlsClip --cli-unfold-argument  \
    --Url http://xxxxx.vod2.myqcloud.com/xxxxx/aaaaaa/hhhh.m3u8 \
    --StartTimeOffset 2 \
    --EndTimeOffset -10
```

Output: 
```
{
    "Response": {
        "Url": "http://xxxxx.vod2.myqcloud.com/xxxxx/aaaaaa/10_50.m3u8",
        "MetaData": {
            "Size": 0,
            "Container": "hls",
            "Bitrate": 622014,
            "Height": 480,
            "Width": 640,
            "Duration": 48,
            "Rotate": 0,
            "VideoStreamSet": [
                {
                    "Bitrate": 592385,
                    "Height": 480,
                    "Width": 640,
                    "Codec": "h264",
                    "Fps": 25
                }
            ],
            "AudioStreamSet": [
                {
                    "Bitrate": 29629,
                    "SamplingRate": 44100,
                    "Codec": "aac"
                }
            ],
            "VideoDuration": 0,
            "AudioDuration": 0
        },
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

