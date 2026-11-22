**Example 1: 创建一个声音克隆,不带试听文本**



Input: 

```
tccli trtc VoiceClone --cli-unfold-argument  \
    --SdkAppId 1466000000 \
    --VoiceName xiaoming_02 \
    --PromptAudio ejxxxxxx
```

Output: 
```
{
    "Response": {
        "VoiceId": "xiaoming_02_aidniwqndq",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 创建一个声音克隆，带试听文本**



Input: 

```
tccli trtc VoiceClone --cli-unfold-argument  \
    --SdkAppId 1466000000 \
    --VoiceName xiaoming_02 \
    --PromptAudio ejxxxxxx \
    --PreviewText 你好，这里是试听文本。
```

Output: 
```
{
    "Response": {
        "VoiceId": "xiaoming_02_aidniwqndq",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "PreviewUrl": "https://xxx.mp3"
    }
}
```

