**Example 1: 启动输入在线媒体流**

启动一个输入在线媒体流任务，将在线媒体流"https://a.b/test.mp4"输入TRTC房间，音视频编码采用默认编码值，转推成功后返回TaskId

Input: 

```
tccli trtc StartStreamIngest --cli-unfold-argument  \
    --SdkAppId 1234567890 \
    --RoomId room123 \
    --UserId robot123 \
    --UserSig xxxxxxxxxxxxxxx \
    --PrivateMapKey xxxxxxxxxxxxxxx \
    --RoomIdType 1 \
    --StreamUrl https://a.b/test.mp4
```

Output: 
```
{
    "Response": {
        "TaskId": "-gCTFWtU7t7DUlo7A8IswFszO9z2O-rbERqJAoK-4pycoZXKjIAAnasdcasdOEycyX4CnzhIm4RAQ..",
        "RequestId": "71993312-6ab8-4768-9124-118e0a20c45f"
    }
}
```

