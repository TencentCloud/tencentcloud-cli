**Example 1: 交互模式测试**



Input: 

```
tccli live StartLiveAvatarRoom --cli-unfold-argument  \
    --RoomId 2147485667 \
    --Comment 推往trtc \
    --ToUrl rtmp://5000.livepush.myqcloud.com/live/qloud_push_test_test_50?txSecret=********************************&txTime=******** \
    --SessionProtocol trtc \
    --TrtcSdkAppId 1600098322 \
    --TrtcUserSig ******************************************************************************************************************************************************************************************************** \
    --TrtcRoomId 79059
```

Output: 
```
{
    "Response": {
        "RequestId": "79da8b98-8e57-4343-aba0-bc8f614ba8ba"
    }
}
```

**Example 2: 请求示例**



Input: 

```
tccli live StartLiveAvatarRoom --cli-unfold-argument  \
    --RoomId 10001 \
    --Comment wx \
    --ToUrl rtmp://5000.livepush.com/live/stream
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

