**Example 1: 通过语音Url来调用接口**

用户通过语音Url的方式（SourceType为0）请求一句话识别服务，请求模型为电话 8k中文 （EngSerViceType = 8k_zh），音频格式为wav

Input: 

```
tccli asr SentenceRecognition --cli-unfold-argument  \
    --UsrAudioKey test \
    --SubServiceType 2 \
    --Url http://tes.cos.ap-guangzhou.myqcloud.com/test.wav \
    --ProjectId 0 \
    --EngSerViceType 8k_zh \
    --VoiceFormat wav \
    --SourceType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "41ed9283-0c09-46fb-917b-0b83fa95f0be",
        "Result": "腾讯云语音识别欢迎您。",
        "AudioDuration": 2430,
        "WordSize": 4,
        "WordList": [
            {
                "Word": "腾讯云",
                "StartTime": 120,
                "EndTime": 810
            },
            {
                "Word": "语音识别",
                "StartTime": 810,
                "EndTime": 1530
            },
            {
                "Word": "欢迎",
                "StartTime": 1530,
                "EndTime": 1890
            },
            {
                "Word": "您",
                "StartTime": 1890,
                "EndTime": 2250
            }
        ]
    }
}
```

**Example 2: 通过语音数据来调用接口**

用户通过上传语音数据（Data）的方式（SourceType为1）请求一句话识别服务，请求模型为电话 8k中文 （EngSerViceType = 8k_zh），音频格式为wav

Input: 

```
tccli asr SentenceRecognition --cli-unfold-argument  \
    --UsrAudioKey test \
    --SubServiceType 2 \
    --ProjectId 0 \
    --EngSerViceType 8k_zh \
    --VoiceFormat wav \
    --Data eGNmYXNkZmFzZmFzZGZhc2RmCg== \
    --SourceType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "41ed9283-0c09-46fb-917b-0b83fa95f0be",
        "Result": "腾讯云语音识别欢迎您。",
        "AudioDuration": 2430,
        "WordSize": 4,
        "WordList": [
            {
                "Word": "腾讯云",
                "StartTime": 120,
                "EndTime": 810
            },
            {
                "Word": "语音识别",
                "StartTime": 810,
                "EndTime": 1530
            },
            {
                "Word": "欢迎",
                "StartTime": 1530,
                "EndTime": 1890
            },
            {
                "Word": "您",
                "StartTime": 1890,
                "EndTime": 2250
            }
        ]
    }
}
```

