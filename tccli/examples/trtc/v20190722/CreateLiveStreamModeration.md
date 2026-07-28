**Example 1: 创建直播流审核任务**



Input: 

```
tccli trtc CreateLiveStreamModeration --cli-unfold-argument  \
    --SdkAppId 1400704311 \
    --Input.Url rtmp://43.173.153.79/pull/9988123?sdkappid=1400704311&userid=inspect&usersig=eJwsjt8KgjAUh9-l3BZyphvaoBuDyvUX6gVMlxxqc*iQQfTukXr7ffD7fR*4H2*RDo46DZIJIWJEXI6Uam09PUl3IIFs73TlYVJ9-Sqdoxok44gp8oSx2VADEgRi65uNSk6rYA72XAxlfslVkVVbfX3vlX0oU7ZmEXbVep70ZP4FacaFiBnyiQ7jeRwhfH8BAAD--0M4MiU_&use_number_room_id=1&remoteuserid=inspect \
    --Input.Format rtmp \
    --LiveModerationParams.ModerationType 3 \
    --LiveModerationParams.MaxIdleTime 30 \
    --LiveModerationParams.SliceVideo 5 \
    --LiveModerationParams.SliceAudio 1 \
    --LiveModerationParams.SaveModerationFile 1 \
    --LiveModerationParams.CallbackAllResults 0 \
    --DataId *********rtmp-test \
    --SourceInfo.RoomId rtmp_test \
    --SourceInfo.RoomIdType 1 \
    --SourceInfo.UserId user0 \
    --LiveModerationStorageParams.CloudModerationStorage.Vendor 0 \
    --LiveModerationStorageParams.CloudModerationStorage.Region ap-nanjing \
    --LiveModerationStorageParams.CloudModerationStorage.Bucket ai-c*******tion-test-1254340397 \
    --LiveModerationStorageParams.CloudModerationStorage.AccessKey AKID*Q*******sHOEmtjIaaIjunSrypPijTw \
    --LiveModerationStorageParams.CloudModerationStorage.SecretKey FPIuIPEle*******OQGo4LK1TeZDbojO \
    --LiveModerationStorageParams.CloudModerationStorage.FileNamePrefix file_test \
    --ResourceExpiredHour 48
```

Output: 
```
{
    "Response": {
        "TaskId": "WPqDNeW3D3UHPMW2q7FSYYz8VgxsBwiKFVq19GtbdXSkY4FJwWJsxU0UhrRTBEBupwKMn17ze1hYawpYtz9ANUVB5tPW0AkgEQxddua01cZuwpYVCb4H",
        "RequestId": "df91a81a-aeb9-4687-91fb-b356d448d453"
    }
}
```

