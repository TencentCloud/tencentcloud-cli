**Example 1: 发起转录任务**



Input: 

```
tccli trtc CreateCloudTranscription --cli-unfold-argument  \
    --SdkAppId 14000000 \
    --RoomId 295000 \
    --RoomIdType 0 \
    --TranscriptionParam.UserId trtc_test_1 \
    --TranscriptionParam.UserSig eJjdaVgrxCdYrzkx*************BLATRT \
    --TranscriptionParam.SubscribeList.0.UserId user_1 \
    --TranscriptionParam.MaxIdleTime 30 \
    --TranscriptionParam.SendCustomMode 2 \
    --AsrParam.Lang 16k_zh_en \
    --AsrParam.VadSilenceTime 2000 \
    --TranslationParam.TargetLang en
```

Output: 
```
{
    "Response": {
        "TaskId": "-nE5dafd3iq51******41fnF8bp2NI65pgE.",
        "RequestId": "f98cb56d-2c70******b0-213ee0ef73ac"
    }
}
```

