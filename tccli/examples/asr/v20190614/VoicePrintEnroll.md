**Example 1: 注册说话人**

通过一段音频数据进行说话人注册

Input: 

```
tccli asr VoicePrintEnroll --cli-unfold-argument  \
    --VoiceFormat 0 \
    --SampleRate 16000 \
    --SpeakerNick abc \
    --Data abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "VoicePrintId": "abc",
            "SpeakerNick": "abc"
        },
        "RequestId": "abc"
    }
}
```

