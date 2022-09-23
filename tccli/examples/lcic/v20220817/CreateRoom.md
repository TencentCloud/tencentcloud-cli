**Example 1: 创建房间**



Input: 

```
tccli lcic CreateRoom --cli-unfold-argument  \
    --AutoMic 1 \
    --Name xx \
    --AudioQuality 1 \
    --MaxMicNumber 1 \
    --SubType xx \
    --SdkAppId 1 \
    --StartTime 1 \
    --TeacherId xx \
    --EndTime 1 \
    --Resolution 1 \
    --DisableRecord 1
```

Output: 
```
{
    "Response": {
        "RoomId": 301234567,
        "RequestId": "213das"
    }
}
```

