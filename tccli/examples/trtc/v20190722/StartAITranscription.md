**Example 1: 样例**



Input: 

```
tccli trtc StartAITranscription --cli-unfold-argument  \
    --SdkAppId 1234 \
    --RoomId 500123 \
    --RoomIdType 1 \
    --TranscriptionParams.UserId test_user \
    --TranscriptionParams.UserSig your-usersig \
    --TranscriptionParams.MaxIdleTime 60 \
    --TranscriptionParams.TranscriptionMode 1 \
    --TranscriptionParams.TargetUserId test_user
```

Output: 
```
{
    "Response": {
        "TaskId": "taskid",
        "RequestId": "requestid"
    }
}
```

