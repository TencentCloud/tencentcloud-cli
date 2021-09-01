**Example 1: 发起 AI 助教**

发起 AI 助教，选择基础班功能

Input: 

```
tccli tci AIAssistant --cli-unfold-argument  \
    --FileContent https%3A%2F%2Fedu-test-1253131631.cos.ap-guangzhou.myqcloud.com%2Faieduautotest%2Fautotest_vedio.mp4 \
    --FileType vod_url \
    --Lang 0 \
    --LibrarySet library_15603955264181591716 \
    --VocabLibNameList testlib2 \
    --VoiceEncodeType 1 \
    --VoiceFileType 10
```

Output: 
```
{
    "Response": {
        "TaskId": 2516205217,
        "ImageResults": null,
        "RequestId": "82d23aac-ff81-4821-bd58-99d2caf6136f"
    }
}
```

