**Example 1: 请求示例**



Input: 

```
tccli live DescribeStreamPushInfoList --cli-unfold-argument  \
    --EndTime 2019-06-21T12:01:02+08:00 \
    --StartTime 2019-06-21T12:00:00+08:00 \
    --StreamName stream1
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-06-21T12:01:02+08:00",
                "PushDomain": "5000.livepush.com",
                "AppName": "live",
                "ClientIp": "43.12.9.2",
                "BeginPushTime": "2019-06-21T12:00:00+08:00",
                "Resolution": "1920*1080",
                "VCodec": "h264",
                "ACodec": "aac",
                "Sequence": "4543453324532",
                "VideoFps": 20,
                "VideoRate": 1,
                "AudioFps": 15,
                "AudioRate": 1,
                "LocalTs": 1,
                "VideoTs": 1,
                "AudioTs": 1,
                "MetaVideoRate": 1,
                "MetaAudioRate": 1,
                "MateFps": 1,
                "StreamParam": "param1=my",
                "Bandwidth": 0,
                "Flux": 0,
                "ServerIp": "127.0.0.1"
            }
        ],
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

