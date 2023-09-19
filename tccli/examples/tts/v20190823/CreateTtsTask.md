**Example 1: API调用**

长文本语音合成请求

Input: 

```
tccli tts CreateTtsTask --cli-unfold-argument  \
    --Text 欢迎使用腾讯云长文本语音合成 \
    --Volume 0 \
    --Speed 0 \
    --ProjectId 0 \
    --ModelType 1 \
    --VoiceType 301001 \
    --PrimaryLanguage 1 \
    --SampleRate 16000 \
    --Codec mp3 \
    --CallbackUrl http://www.callback.com/tts_call \
    --EnableSubtitle True \
    --VoiceoverDialogueSplit False \
    --EmotionCategory neutral \
    --EmotionIntensity 100
```

Output: 
```
{
    "Response": {
        "RequestId": "fabc2d63-a1b7-40a0-b4c3-640f78974919",
        "Data": {
            "TaskId": "gz-5faa7bc8-6e78-46b9-90ea-5ebba32aa04c"
        }
    }
}
```

**Example 2: 成功示例**

长文本语音合成请求

Input: 

```
tccli tts CreateTtsTask --cli-unfold-argument  \
    --Text 字符串 \
    --ProjectId 1 \
    --ModelType 1 \
    --Volume 0 \
    --Codec mp3 \
    --VoiceType 101001 \
    --SampleRate 16000 \
    --PrimaryLanguage 1 \
    --Speed 0
```

Output: 
```
{
    "Response": {
        "RequestId": "41a54cd2-3941-4a85-8b9a-f1e8b0000be5",
        "Data": {
            "TaskId": "gz-53c9e73a-d8ec-4792-bc9e-e982115623a5"
        }
    }
}
```

