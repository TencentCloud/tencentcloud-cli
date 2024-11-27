**Example 1: 请求示例**

创建主监任务

Input: 

```
tccli live CreateCasterPgm --cli-unfold-argument  \
    --CasterId 1234 \
    --PgmDisplayInfo.LayoutIndex 1
```

Output: 
```
{
    "Response": {
        "PgmPlayUrl": "rtmp://www.example.com/live/example_stream_id",
        "CdnPlayUrl": "https://cdn.example.com/live/example_stream_id",
        "CdnStreamId": "example_stream_id",
        "PgmWebRTCPlayUrl": "webrtc://webrtc.example.com/live/example_stream_id",
        "RequestId": "6a2b5970-ffbb-419e-9667-13595e755143"
    }
}
```

