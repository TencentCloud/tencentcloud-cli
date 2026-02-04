**Example 1: 注册说话人**

通过一段音频数据进行说话人注册

Input: 

```
tccli asr VoicePrintEnroll --cli-unfold-argument  \
    --VoiceFormat 1 \
    --SampleRate 16000 \
    --SpeakerNick 李九州 \
    --AudioUrl https://xxx-test-xxx.cos.ap-nanjing.myqcloud.com/%E5%A3%Bxxxxx%E6%8D%AE/xxxx.mp3
```

Output: 
```
{
    "Response": {
        "Data": {
            "SpeakerNick": "李九州",
            "VoicePrintId": "23eda848-9c0a-xxxx-8b00-39df9c9617e7"
        },
        "RequestId": "cb82a203-xxxxx-43ec-b12a-d9dba5efd577"
    }
}
```

