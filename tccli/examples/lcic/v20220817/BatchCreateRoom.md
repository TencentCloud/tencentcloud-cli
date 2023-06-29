**Example 1: 批量创建课堂**

批量创建课堂

Input: 

```
tccli lcic BatchCreateRoom --cli-unfold-argument  \
    --SdkAppId 1 \
    --RoomInfos.0.Name abc \
    --RoomInfos.0.StartTime 1 \
    --RoomInfos.0.EndTime 1 \
    --RoomInfos.0.TeacherId abc \
    --RoomInfos.0.Resolution 1 \
    --RoomInfos.0.MaxMicNumber 1 \
    --RoomInfos.0.AutoMic 1 \
    --RoomInfos.0.TurnOffMic 1 \
    --RoomInfos.0.AudioQuality 1 \
    --RoomInfos.0.SubType abc \
    --RoomInfos.0.DisableRecord 1 \
    --RoomInfos.0.Assistants abc \
    --RoomInfos.0.RTCAudienceNumber 1 \
    --RoomInfos.0.AudienceType 1 \
    --RoomInfos.0.RecordLayout 1 \
    --RoomInfos.0.GroupId abc \
    --RoomInfos.0.EnableDirectControl 1
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

