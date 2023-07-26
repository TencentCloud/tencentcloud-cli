**Example 1: 创建房间**

示例

Input: 

```
tccli lcic CreateRoom --cli-unfold-argument  \
    --Name abc \
    --StartTime 1 \
    --EndTime 1 \
    --TeacherId abc \
    --SdkAppId 1 \
    --Resolution 1 \
    --MaxMicNumber 1 \
    --AutoMic 1 \
    --TurnOffMic 1 \
    --AudioQuality 1 \
    --SubType abc \
    --DisableRecord 1 \
    --Assistants abc \
    --RTCAudienceNumber 1 \
    --AudienceType 1 \
    --RecordLayout 1 \
    --GroupId abc \
    --InteractionMode 1 \
    --VideoOrientation 1 \
    --IsGradingRequiredPostClass 1 \
    --RoomType 1 \
    --EnableDirectControl 0
```

Output: 
```
{
    "Response": {
        "RoomId": 1,
        "RequestId": "abc"
    }
}
```

