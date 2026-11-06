**Example 1: 声纹验证测试用例**



Input: 

```
tccli trtc VerifyTRTCVoicePrint --cli-unfold-argument  \
    --VoicePrintId 19dbb72269b_1e7b262ef347400490f19956bc293016 \
    --Data base64_encoded_audio_data \
    --SdkAppId 1400123456 \
    --AudioFormat pcm
```

Output: 
```
{
    "Response": {
        "Decision": 1,
        "Message": "voiceprint verify success",
        "RequestId": "6dd6414b-3695-4db7-af24-7f1a3ef41d0c",
        "Score": "100.00",
        "SpeakerId": "user1",
        "VoicePrintId": "19dbb72269b_1e7b262ef347400490f19956bc293016"
    }
}
```

