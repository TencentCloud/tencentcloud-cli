**Example 1: 请求示例**



Input: 

```
tccli live DescribeStreamPushInfoList --cli-unfold-argument  \
    --StartTime '2019-06-21 12:00:00' \
    --EndTime '2019-06-21 12:01:02' \
    --StreamName abcd
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "StreamParam": "xx",
                "ACodec": "AAC",
                "AppName": "live",
                "AudioFps": 43,
                "AudioRate": 131580,
                "AudioTs": 5004,
                "BeginPushTime": "2019-06-21 00:29:12.252",
                "ClientIp": "125.39.132.102",
                "LocalTs": 5000,
                "PushDomain": "123.livepush.myqcloud.com",
                "Resolution": "368*640",
                "Sequence": "10151483429474411508",
                "Time": "2019-06-21 01:10:39.87",
                "VCodec": "H264",
                "VideoFps": 24,
                "VideoRate": 701528,
                "VideoTs": 5032,
                "MateFps": 30,
                "MetaAudioRate": 22,
                "MetaVideoRate": 4885,
                "Bandwidth": 1.0,
                "Flux": 1.0
            }
        ],
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

