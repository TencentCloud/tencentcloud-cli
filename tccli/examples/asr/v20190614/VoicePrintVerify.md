**Example 1: 说话人验证**

验证音频和说话人id是否一致

Input: 

```
tccli asr VoicePrintVerify --cli-unfold-argument  \
    --VoiceFormat 0 \
    --SampleRate 16000 \
    --VoicePrintId KJHGUGKGGGFGYFVDA \
    --Data UklGRiRTBwBXQVZFZm10IBAA
```

Output: 
```
{
    "Response": {
        "Data": {
            "VoicePrintId": "KJHGUGKGGGFGYFVDA",
            "Score": "60.0",
            "Decision": 1
        },
        "RequestId": "abc"
    }
}
```

