**Example 1: 复制预监的布局配置到主监任务中**



Input: 

```
tccli live CreateCasterPgmFromPvw --cli-unfold-argument  \
    --CasterId 1234
```

Output: 
```
{
    "Response": {
        "PgmPlayUrl": "rtmp://www.example.com/live/example_stream_id",
        "PgmWebRTCPlayUrl": "webrtc://webrtc.example.com/live/example_stream_id",
        "CdnPlayUrl": "https://cdn.example.com/live/example_stream_id",
        "CdnStreamId": "example_stream_id",
        "RequestId": "84fea7c5-37e7-4d89-ba04-76338dc7b41d"
    }
}
```

