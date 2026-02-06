**Example 1: 开始一个语音合成**



Input: 

```
tccli trtc TextToSpeech --cli-unfold-argument  \
    --Text 你好呀 \
    --SdkAppId 1466000000 \
    --Voice.VoiceId 256
```

Output: 
```
{
    "Response": {
        "Audio": "inxxx",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

