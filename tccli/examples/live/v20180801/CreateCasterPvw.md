**Example 1: 请求示例**

创建使用布局Index 1的预监任务。

Input: 

```
tccli live CreateCasterPvw --cli-unfold-argument  \
    --CasterId 63501 \
    --PvwDisplayInfo.LayoutIndex 1
```

Output: 
```
{
    "Response": {
        "PvwPlayUrl": "rtmp://www.example.com/live/pvw_example",
        "PvwWebRTCPlayUrl": "webrtc://webrtc.example.domain/live/pvw_example",
        "RequestId": "6a2b5970-ffbb-419e-9667-13595e755143"
    }
}
```

