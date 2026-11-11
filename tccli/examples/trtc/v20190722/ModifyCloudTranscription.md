**Example 1: 更新转录任务**



Input: 

```
tccli trtc ModifyCloudTranscription --cli-unfold-argument  \
    --SdkAppId 1400704311 \
    --TaskId -nE****U7t3BGcLlSMQd6UAdKFhPRNXb****S4K-m928oZWQndibHjkrRJJAw****1SjcO6uCAE. \
    --SequenceNumber 3 \
    --SubscribeUserInfo.SubscribeList.0.UserId ****_test_0 \
    --TranslationParam.TargetLang en \
    --TranslationParam.Terminologies.0.TargetLang en \
    --TranslationParam.Terminologies.0.Terminology.0.Source 腾讯云音视频 \
    --TranslationParam.Terminologies.0.Terminology.0.Target TRTC \
    --TTSParam.0.Model flow_02_turbo \
    --TTSParam.0.Language en \
    --TTSParam.0.TargetUser.UserId ****_test_1 \
    --TTSParam.0.TTSRobotUser.UserId tts-robot1 \
    --TTSParam.0.Voice.VoiceId v-female-B7k5WxN4 \
    --TTSParam.0.Voice.Speed 1.99 \
    --TTSParam.0.Voice.Volume 9.99 \
    --TTSParam.0.Voice.Pitch -10
```

Output: 
```
{
    "Response": {
        "TaskId": "-nE5***U7t3BGcLlSMQd6UAdKFhPRNXb****S4K-m928oZWQndibHjkrRJJAw****1SjcO6uCAE.",
        "RequestId": "d6ddd3fa-108a-4dd5-b69b-43d93d6ab532"
    }
}
```

