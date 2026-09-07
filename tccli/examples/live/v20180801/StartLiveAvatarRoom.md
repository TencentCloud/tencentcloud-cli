**Example 1: 请求示例**



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

**Example 2: 交互模式测试**



Input: 

```
tccli live StartLiveAvatarRoom --cli-unfold-argument  \
    --RoomId 2147485667 \
    --Comment 推往trtc \
    --ToUrl rtmp://5000.livepush.myqcloud.com/live/qloud_push_test_test_50?txSecret=40e467c0e787205b7086c7fa9db0e3fd&txTime=6ba1006a \
    --SessionProtocol trtc \
    --TrtcSdkAppId 1600098322 \
    --TrtcUserSig eJwtzE8LgjAcxvH3smth29pfoUNdKvEiBhV0KZz1o6y5qQXRe2*lx*fzheeNNmkedcahGNEIo-F-Q2HuDZTQM2GSKS6EHKovrkdroUAxERhjraaU9sW8LDgTnHNOQ*q1gepnUinJtJCDejiH86WdW*pPN02Sx6LdHiam9T7tSvcUNWV2dZFVnY*S3X6dZTP0*QKnjTIx \
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

