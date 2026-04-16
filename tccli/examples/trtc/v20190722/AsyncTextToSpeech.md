**Example 1: 开启异步任务**



Input: 

```
tccli trtc AsyncTextToSpeech --cli-unfold-argument  \
    --Text 你好 \
    --Voice.VoiceId v-female-R2s4N9qJ \
    --SdkAppId 1600019222 \
    --AlignmentMode 1 \
    --LanguageCode zh
```

Output: 
```
{
    "Response": {
        "TaskId": "3d5f26c1-**9*-*f***883e-b543337b8eab",
        "RequestId": "dcbccd58-c660-4546-b4fa-522d9223556e"
    }
}
```

