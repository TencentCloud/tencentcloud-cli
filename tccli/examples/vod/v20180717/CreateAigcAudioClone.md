**Example 1: 创建 AIGC 音频复刻**



Input: 

```
tccli vod CreateAigcAudioClone --cli-unfold-argument  \
    --SubAppId 221073 \
    --AudioFileInfo.Type Url \
    --AudioFileInfo.Url https://cg-sdk-1258344699.cos.ap-nanjing.myqcloud.com/personal/jeffgaogao/aigc/output2z.mp3 \
    --VoiceId maigua111 \
    --Text 华强怎么还没来 \
    --PromptAudioFileInfo.Type Url \
    --PromptAudioFileInfo.Url https://cg-sdk-1258344699.cos.ap-nanjing.myqcloud.com/personal/jeffgaogao/aigc/output2z.mp3 \
    --PromptText 你瞧瞧现在哪有瓜呀，这都是大棚的瓜，你嫌贵我还嫌贵呢。 \
    --Payload mypayload \
    --SessionId mySessionid \
    --SessionContext mySessionContext \
    --TasksPriority 10 \
    --ExtInfo myExtInfo
```

Output: 
```
{
    "Response": {
        "TaskId": "221073-CreateAigcAudioClone-4f736149667baa953315afe87daacad6t",
        "RequestId": "dcde7626-cee7-4005-8974-3696244613bf"
    }
}
```

