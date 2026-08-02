**Example 1: 音色克隆示例**



Input: 

```
tccli mps CloneVoice --cli-unfold-argument  \
    --AudioUrl https://*****************.cos-internal.ap-nanjing.tencentcos.cn/common/***********/reel/test/narration_voice_zh.wav \
    --AudioLang zh \
    --VoiceProfile.Name new-clone-test
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "VoiceId": "v1_******BMqyjoY5+h4uWEkXUsTXzvBqORfjv9WZbpLIxGPzq3dm6qXYaOtO9C/9p68Gk=",
        "RequestId": "caeaf2ae-22f9-4a8e-a570-0558aefd1c15",
        "AudioUrl": "https://*********************.cos.accelerate.myqcloud.com/speech/771bdded-b55b-4745-82ae-caafb1136d7f-preview.mp3"
    }
}
```

