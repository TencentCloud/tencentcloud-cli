**Example 1: 基础语音合成调用示例**

API调用

Input: 

```
tccli tts TextToVoice --cli-unfold-argument  \
    --Text 你好 \
    --SessionId session-1234 \
    --Volume 1 \
    --Speed 1 \
    --ProjectId 0 \
    --ModelType 1 \
    --VoiceType 1001 \
    --PrimaryLanguage 1 \
    --SampleRate 16000 \
    --Codec wav \
    --EnableSubtitle True
```

Output: 
```
{
    "Response": {
        "Audio": "UklGRqRwAABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YYBwAAAA......AAAAA=",
        "RequestId": "d91f1496-0514-4281-932e-15a022b67d16",
        "SessionId": "session-1234",
        "Subtitles": [
            {
                "BeginIndex": 0,
                "BeginTime": 250,
                "EndIndex": 1,
                "EndTime": 430,
                "Phoneme": "ni2",
                "Text": "你"
            },
            {
                "BeginIndex": 1,
                "BeginTime": 430,
                "EndIndex": 2,
                "EndTime": 670,
                "Phoneme": "hao3",
                "Text": "好"
            }
        ]
    }
}
```

