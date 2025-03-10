**Example 1: 批量创建课堂**

批量创建课堂

Input: 

```
tccli lcic BatchCreateRoom --cli-unfold-argument  \
    --SdkAppId 1 \
    --RoomInfos.0.Name testRoom \
    --RoomInfos.0.StartTime 1704074400 \
    --RoomInfos.0.EndTime 1704076200 \
    --RoomInfos.0.TeacherId 2i5WfUzRRC2Eb2uNmLNv96gzxCv \
    --RoomInfos.0.Resolution 1 \
    --RoomInfos.0.MaxMicNumber 1 \
    --RoomInfos.0.AutoMic 1 \
    --RoomInfos.0.TurnOffMic 1 \
    --RoomInfos.0.AudioQuality 1 \
    --RoomInfos.0.SubType video \
    --RoomInfos.0.DisableRecord 1 \
    --RoomInfos.0.Assistants 2d3FgsZRRB2EbRu5Cwe8Rd7R6Bc \
    --RoomInfos.0.AudienceType 1 \
    --RoomInfos.0.RecordLayout 1 \
    --RoomInfos.0.GroupId 2CvDgjRNjylAs \
    --RoomInfos.0.EnableDirectControl 1
```

Output: 
```
{
    "Response": {
        "RoomIds": [
            301234567
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

