**Example 1: 直播详情接口**



Input: 

```
tccli iotvideoindustry DescribeLiveChannel --cli-unfold-argument  \
    --LiveChannelId e4a6427192a34cca8ea1d74815b7f458
```

Output: 
```
{
    "Response": {
        "LiveChannelId": "e4a6427192a34cca8ea1d74815b7f458",
        "LiveChannelName": "004",
        "LiveChannelType": 1,
        "LiveStatus": 0,
        "PushStreamAddress": "rtmp://:0/liveFixed/e4a6427192a34cca8ea1d74815b7f458",
        "RequestId": "fd344df8-6121-4e75-b417-383a67268354111",
        "CreateTime": "2021-11-10 11:11:10",
        "UpdateTime": "2021-11-10 11:11:10"
    }
}
```

