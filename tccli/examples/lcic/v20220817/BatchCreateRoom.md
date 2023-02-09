**Example 1: 批量创建课堂**

批量创建课堂

Input: 

```
tccli lcic BatchCreateRoom --cli-unfold-argument  \
    --SdkAppId 1 \
    --RoomInfos.0.AutoMic 1 \
    --RoomInfos.0.Name xx \
    --RoomInfos.0.AudioQuality 1 \
    --RoomInfos.0.TurnOffMic 1 \
    --RoomInfos.0.MaxMicNumber 1 \
    --RoomInfos.0.SubType xx \
    --RoomInfos.0.StartTime 1 \
    --RoomInfos.0.TeacherId xx \
    --RoomInfos.0.EndTime 1 \
    --RoomInfos.0.Resolution 1 \
    --RoomInfos.0.DisableRecord 1
```

Output: 
```
{
    "Response": {
        "RoomIds": [
            301234567
        ],
        "RequestId": "213das"
    }
}
```

