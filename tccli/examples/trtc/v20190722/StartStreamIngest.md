**Example 1: 启动拉流转推**

启动一个拉流转推任务，任务内容为两个在线媒体流"https://a.b/test.mp4","https://b.c/test.mp4"，音视频编码采用默认编码值，设置回调地址为 "https://b.c/callback"，转推成功后返回TaskId

Input: 

```
tccli trtc StartStreamIngest --cli-unfold-argument  \
    --SdkAppId 1234567890 \
    --RoomId room123 \
    --UserId robot123 \
    --UserSig xxxxxxxxxxxxxxxxxxxxxxxxxxxx \
    --PrivateMapKey abcdefg \
    --RoomIdType 1 \
    --SourceUrl https://a.b/test.mp4 https://b.c/test.mp4
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

