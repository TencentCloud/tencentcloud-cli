**Example 1: 注册说话人**

通过一段音频数据进行说话人注册

Input: 

```
tccli asr VoicePrintEnroll --cli-unfold-argument  \
    --VoiceFormat 0 \
    --SampleRate 16000 \
    --SpeakerNick ross \
    --Data UklGRka1CQBXQVZFZm10IBAAAAABAAEAgD4E
```

Output: 
```
{
    "Response": {
        "Data": {
            "VoicePrintId": "db24a3e3-7926-5xxxxxxf01",
            "SpeakerNick": "ross"
        },
        "RequestId": "dbxxxxxxe3-7926-5xxxxxxf01"
    }
}
```

