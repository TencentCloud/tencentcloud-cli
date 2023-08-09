**Example 1: 请求示例**



Input: 

```
tccli live DescribeStreamPushInfoList --cli-unfold-argument  \
    --EndTime 2019-06-21T12:01:02+08:00 \
    --StartTime 2019-06-21T12:00:00+08:00 \
    --StreamName abcd
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "abc",
                "PushDomain": "abc",
                "AppName": "abc",
                "ClientIp": "abc",
                "BeginPushTime": "abc",
                "Resolution": "abc",
                "VCodec": "abc",
                "ACodec": "abc",
                "Sequence": "abc",
                "VideoFps": 1,
                "VideoRate": 1,
                "AudioFps": 1,
                "AudioRate": 1,
                "LocalTs": 1,
                "VideoTs": 1,
                "AudioTs": 1,
                "MetaVideoRate": 1,
                "MetaAudioRate": 1,
                "MateFps": 1,
                "StreamParam": "abc",
                "Bandwidth": 0,
                "Flux": 0,
                "ServerIp": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

