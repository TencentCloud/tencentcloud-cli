**Example 1: 文生音效**



Input: 

```
tccli vod CreateAigcAudioTask --cli-unfold-argument  \
    --ModelName Kling \
    --SceneType sfx \
    --Prompt 春节庆祝时的烟花声 \
    --OutputConfig.StorageMode Temporary \
    --OutputConfig.Duration 6
```

Output: 
```
{
    "Response": {
        "TaskId": "251441341-AigcAudioTask-f3259ddeb615203726d73c03da05d9fft",
        "RequestId": "4794b445-abc7-46c6-9e74-b30429f3a2c6"
    }
}
```

