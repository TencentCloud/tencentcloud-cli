**Example 1: 更新音色信息**

更新音色信息

Input: 

```
tccli vod UpdateVoice --cli-unfold-argument  \
    --SubAppId 260***028 \
    --VoiceId v1_aBbiY3aN7tm7ff3S1gBZa************************plXzQDwNTiJQp2aYilZGv0= \
    --VoiceFields.Name 音色 \
    --VoiceFields.Description 音色简介 \
    --VoiceFields.Gender male \
    --VoiceFields.Age middle_aged \
    --VoiceFields.Languages zh \
    --VoiceFields.Labels 知性 \
    --VoiceFields.Scenes 通用 \
    --VoiceFields.AudioUrl https://laurie-tmp-1300828900.cos.ap-nanjing.myqcloud.com/sync_dubbing/27111c32-93e3-476e-8ab5-e7fb5838f994.wav \
    --ExtParam {"engine": "auto"}
```

Output: 
```
{
    "Response": {
        "Voice": {
            "Age": "middle_aged",
            "AudioUrl": "",
            "Category": "clone",
            "Description": "音色简介",
            "Gender": "male",
            "Labels": [
                "知性"
            ],
            "Languages": [
                "zh"
            ],
            "Name": "音色",
            "Scenes": [
                "通用"
            ],
            "VoiceId": "v1_aBbiY3aN7tm7ff3S1gBZamsLQyEsQswXoEpreGEStjnx2plXzQDwNTiJQp2aYilZGv0="
        },
        "RequestId": "83593c53-3379-4359-a25b-815bb562bf37"
    }
}
```

