**Example 1: 成功**

 

Input: 

```
tccli iss ControlDeviceStream --cli-unfold-argument  \
    --ChannelId df27ec26-812c-443c-b594-f95bf383ef70
```

Output: 
```
{
    "Response": {
        "Data": {
            "FMp4": "https://test-play-gz.***********/live/df27ec26-****-443c-b594-************.live.mp4?token=cms_700000*****9_1791947426_H9MbdKLQZiX7C-a******w",
            "Flv": "https://test-play-gz.***********/live/df27ec26-****-443c-b594-************.live.flv?token=cms_700000*****_1791947426_H9MbdKLQZiX7C-********",
            "Hls": "https://test-play-gz.***********/.cn/live/df27ec26-812c-******-b594-f95bf383ef70/hls.m3u8?token=cms_700000*****_1791947426_H9MbdKLQZiX7C-******",
            "Rtmp": "rtmp://test-play-gz.***********/.cn/live/df27ec26-812c-******-b594-f95bf383ef70?token=cms_700000*****_1791947426_H9MbdKLQZiX7C-******"
        },
        "RequestId": "b62b4c63-0913-4a2b-85c9-4fc61d821530"
    }
}
```

