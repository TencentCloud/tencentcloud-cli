**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveStreamPushInfoList --cli-unfold-argument  \
    --PushDomain 5000.pushdomain.com \
    --AppName live \
    --PageNum 1 \
    --PageSize 1000
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "StreamName": "test1",
                "AppName": "live",
                "ClientIp": "127.0.0.1",
                "ServerIp": "127.0.0.1",
                "VideoFps": 100,
                "VideoSpeed": 100,
                "AudioFps": 40,
                "AudioSpeed": 40,
                "AsampleRate": 48000,
                "PushDomain": "5000.pushdomain.com",
                "BeginPushTime": "2019-02-01 00:00:00",
                "Acodec": "AAC",
                "Vcodec": "H264",
                "Resolution": "350*350",
                "MetaAudioSpeed": 22,
                "MetaFps": 30,
                "MetaVideoSpeed": 4885
            }
        ],
        "PageNum": 1,
        "PageSize": 1000,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

