**Example 1: 声音复刻任务创建**

声音复刻任务创建

Input: 

```
tccli vrs CreateVRSTask --cli-unfold-argument  \
    --SessionId 63f8xxx1897281d556df60b0 \
    --VoiceName 小娥 \
    --SampleRate 16000 \
    --VoiceGender 1 \
    --VoiceLanguage 1 \
    --Codec wav \
    --CallbackUrl http://example.com/callback \
    --AudioIdList 63f89bb
```

Output: 
```
{
    "Response": {
        "RequestId": "63f89bb1897281d556df60b0",
        "Data": {
            "TaskId": "ce68122c-0ca8-4fa6-99b1-90a28670626b"
        }
    }
}
```

