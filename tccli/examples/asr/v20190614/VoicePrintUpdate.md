**Example 1: 说话人更新**

更新说话人的音频和昵称

Input: 

```
tccli asr VoicePrintUpdate --cli-unfold-argument  \
    --VoiceFormat 0 \
    --SampleRate 0 \
    --SpeakerNick abc \
    --VoicePrintId abc \
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

