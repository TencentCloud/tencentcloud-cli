**Example 1: 说话人更新**

更新说话人的音频和昵称

Input: 

```
tccli asr VoicePrintUpdate --cli-unfold-argument  \
    --VoiceFormat 0 \
    --SampleRate 0 \
    --SpeakerNick 小明 \
    --VoicePrintId 34a0a2b-922f******90302f155a6d \
    --Data UklGRka1CQBXQVZFZm10IBAAAAABAAEAgD4E
```

Output: 
```
{
    "Response": {
        "Data": {
            "VoicePrintId": "34a0a2b-922f******90302f155a6d",
            "SpeakerNick": "小明"
        },
        "RequestId": "676a22c********3625b0"
    }
}
```

