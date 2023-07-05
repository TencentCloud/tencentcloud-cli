**Example 1: 说话人验证**

验证音频和说话人id是否一致

Input: 

```
tccli asr VoicePrintVerify --cli-unfold-argument  \
    --VoiceFormat 0 \
    --SampleRate 0 \
    --VoicePrintId abc \
    --Data abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "VoicePrintId": "abc",
            "Score": "abc",
            "Decision": 0
        },
        "RequestId": "abc"
    }
}
```

