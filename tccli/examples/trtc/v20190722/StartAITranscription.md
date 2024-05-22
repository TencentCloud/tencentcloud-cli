**Example 1: 样例**



Input: 

```
tccli trtc StartAITranscription --cli-unfold-argument  \
    --SdkAppId 1234 \
    --RoomId 1234 \
    --RoomIdType 1 \
    --TranscriptionParams.UserId abc \
    --TranscriptionParams.UserSig abc \
    --TranscriptionParams.IMAdminUserId abc \
    --TranscriptionParams.IMAdminUserSig abc \
    --TranscriptionParams.MaxIdleTime 60 \
    --TranscriptionParams.TranscriptionMode 1 \
    --TranscriptionParams.TargetUserId abc
```

Output: 
```
{
    "Response": {
        "TaskId": "abc",
        "RequestId": "abc"
    }
}
```

