**Example 1: 创建异常信息**



Input: 

```
tccli trtc CreateTroubleInfo --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RoomId 1587879309 \
    --TeacherUserId 1587882309 \
    --StudentUserId 123456 \
    --TroubleUserId 123456 \
    --TroubleType 1 \
    --TroubleTime 87654321 \
    --TroubleMsg VoiceException
```

Output: 
```
{
    "Response": {
        "RequestId": "56b89272-cdff-46a3-a399-87ec6f209b53"
    }
}
```

