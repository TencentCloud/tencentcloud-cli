**Example 1: 创建支持页面录制的1小时标清直播1V1小班课**



Input: 

```
tccli lcic CreateRoom --cli-unfold-argument  \
    --Name 测试课堂 \
    --StartTime 1798768800 \
    --EndTime 1798772400 \
    --SdkAppId 3322111 \
    --Resolution 1 \
    --MaxMicNumber 1 \
    --SubType videodoc \
    --TeacherId 2qkMhWixIzNQC7UizlM7NabCdef \
    --AutoMic 1 \
    --RecordLayout 9
```

Output: 
```
{
    "Response": {
        "RoomId": 345678011,
        "RequestId": "efee43a2-704f-4b45-b62d-abcdefg12345"
    }
}
```

