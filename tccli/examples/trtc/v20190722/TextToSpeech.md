**Example 1: 语音合成**



Input: 

```
tccli trtc TextToSpeech --cli-unfold-argument  \
    --Text 你好 \
    --Voice.VoiceId v-female-R2s4N9qJ \
    --SdkAppId 160001234 \
    --AlignmentMode 1
```

Output: 
```
{
    "Response": {
        "Alignments": [
            {
                "TextBegin": 0,
                "TextEnd": 2,
                "TimeBeginMs": 0,
                "TimeEndMs": 760
            }
        ],
        "Audio": "base64audio",
        "RequestId": "9b9b5959-8d17-46f2-a216-8a0ce219f92f"
    }
}
```

