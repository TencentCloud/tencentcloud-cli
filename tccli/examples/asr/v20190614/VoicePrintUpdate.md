**Example 1: 说话人更新**

更新说话人的音频和昵称

Input: 

```
tccli asr VoicePrintUpdate --cli-unfold-argument  \
    --VoiceFormat 1 \
    --SampleRate 16000 \
    --VoicePrintId 0928d167-dcd0-44b6xxxx-85d303273a72 \
    --SpeakerNick 张三 \
    --AudioUrl https://adison-testxxxx.cos.ap-nanjing.myqcloud.com/%E5%xx%B0%E7xxx%BA%B9%E6%95%B0%E6%8D%AE/xxxx.wav
```

Output: 
```
{
    "Response": {
        "Data": {
            "SpeakerNick": "张三",
            "VoicePrintId": "0928d167-xxxx44b6-9465-85d303273a72"
        },
        "RequestId": "9ac61e25-3860-xxxxx-9b48-61a3c69ea408"
    }
}
```

