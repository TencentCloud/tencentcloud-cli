**Example 1: 更新声纹测试用例**



Input: 

```
tccli trtc UpdateTRTCVoicePrint --cli-unfold-argument  \
    --VoicePrintId 19dbb72269b_1e7b262ef347400490f19956bc293016 \
    --Data base64_encoded_audio_data \
    --SdkAppId 1400123456 \
    --AudioFormat pcm
```

Output: 
```
{
    "Response": {
        "EffectiveAudioDuration": 25.4,
        "Message": "voiceprint updated successfully",
        "RequestId": "c3baedee-e412-4ab1-96cb-049626f79b63",
        "SNR": 5.8,
        "VoicePrintId": "19dbb72269b_1e7b262ef347400490f19956bc293016"
    }
}
```

