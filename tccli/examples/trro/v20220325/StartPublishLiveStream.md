**Example 1: 启动腾讯云直播单流转推**



Input: 

```
tccli trro StartPublishLiveStream --cli-unfold-argument  \
    --PublishParams.0.PublishUrl rtmp://live-push-test.tencentcs.com/live/test1?txSecret=abcd1234567890&txTime=679C9784 \
    --PublishParams.0.IsTencentUrl 1 \
    --MaxIdleTime 20 \
    --VideoParams.Width 1920 \
    --VideoParams.Height 1080 \
    --VideoParams.Fps 30 \
    --VideoParams.BitRate 1500 \
    --VideoParams.Gop 2 \
    --VideoParams.VideoList.0.VideoStreamId 0 \
    --VideoParams.VideoList.0.Width 1920 \
    --VideoParams.VideoList.0.Height 1080 \
    --VideoParams.VideoList.0.DeviceId geek_gw_2 \
    --VideoParams.VideoList.0.ProjectId m82k5408n675phvb \
    --WithTranscoding 1
```

Output: 
```
{
    "Response": {
        "RequestId": "StartPublishCdnStream-1",
        "TaskId": "D0xOlGVRsurq9PRB-Iuak6f-J0ac-twfB4hQwbFucIB9muIw9pP0FOpOYkgdMNK52kIoPlhHe96RlTGxKzJwUgzjD-8pZgA."
    }
}
```

