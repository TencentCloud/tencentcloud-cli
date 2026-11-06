**Example 1: 注册声纹测试用例**



Input: 

```
tccli trtc RegisterTRTCVoicePrint --cli-unfold-argument  \
    --SpeakerId usera \
    --Data base64_encoded_audio_data \
    --SdkAppId 1400123456 \
    --AudioFormat pcm
```

Output: 
```
{
    "Response": {
        "EffectiveAudioDuration": 25.4,
        "Message": "voiceprint enrolled successfully",
        "RequestId": "2ba4e1f9-208c-4d37-9cdc-baa6d8f52a52",
        "SNR": 5.8,
        "SpeakerId": "usera",
        "VoicePrintId": "19dbe5b905b_1024998c2a534879a78c600f7850874a"
    }
}
```

