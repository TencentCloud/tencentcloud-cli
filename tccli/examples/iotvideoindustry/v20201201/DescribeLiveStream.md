**Example 1: 直播拉流接口**



Input: 

```
tccli iotvideoindustry DescribeLiveStream --cli-unfold-argument  \
    --LiveChannelId e4a6427192a34cca8ea1d74815b7f458 \
    --ExpireTime 124177555
```

Output: 
```
{
    "Response": {
        "Data": {
            "StreamId": "",
            "RtspAddr": "rtsp://127.0.0.1/live/test",
            "RtmpAddr": "rtmp://127.0.0.1/live/test",
            "HlsAddr": "http://127.0.0.1/live/test.m3u8",
            "FlvAddr": "http://127.0.0.1/live/test.flv"
        },
        "RequestId": "fd344df8-6121-4e75-b417-383a67268354111"
    }
}
```

