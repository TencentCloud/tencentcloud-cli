**Example 1: 说话人认证**



Input: 

```
tccli asr VoicePrintVerify --cli-unfold-argument  \
    --VoiceFormat 1 \
    --SampleRate 16000 \
    --VoicePrintId 0928d167-dcd0-xxxx-85d303273a72 \
    --AudioUrl https://xxxx-test-xxxx.cos.ap-nanjing.myqcloud.com/%E5%A3%BxxxxE6%95%B0%E6%8D%AE/test.wav
```

Output: 
```
{
    "Response": {
        "Data": {
            "Decision": 1,
            "Score": "100.0",
            "VoicePrintId": "0928d167-dcd0-xxxx-9465-85d303273a72"
        },
        "RequestId": "be2ce6ff-b1ab-xxxx-9c17-876a73d6f56f"
    }
}
```

