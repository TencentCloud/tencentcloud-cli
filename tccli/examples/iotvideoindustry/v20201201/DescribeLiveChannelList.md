**Example 1: 直播列表接口**



Input: 

```
tccli iotvideoindustry DescribeLiveChannelList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "LiveChannels": [
            {
                "LiveChannelId": "cea6f74f29164253b43411fd888f4dc3",
                "LiveChannelName": "001",
                "LiveChannelType": 1,
                "PushStreamAddress": "rtmp://127.0.0.1:19350/liveFixed/cea6f74f29164253b43411fd888f4dc3",
                "CreateTime": "2021-09-07 19:49:10",
                "UpdateTime": "2021-09-07 19:49:10",
                "LiveStatus": 0
            },
            {
                "LiveChannelId": "e4a6427192a34cca8ea1d74815b7f458",
                "LiveChannelName": "004",
                "LiveChannelType": 1,
                "PushStreamAddress": "rtmp://127.0.0.1:19350/liveFixed/e4a6427192a34cca8ea1d74815b7f458",
                "CreateTime": "2021-09-07 19:41:08",
                "UpdateTime": "2021-09-07 19:42:58",
                "LiveStatus": 0
            }
        ],
        "RequestId": "fd344df8-6121-4e75-b417-383a67268354111",
        "Total": 2
    }
}
```

