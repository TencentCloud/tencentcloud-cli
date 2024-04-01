**Example 1: 音质检测**

音质检测

Input: 

```
tccli vrs DetectEnvAndSoundQuality --cli-unfold-argument  \
    --TextId 00020 \
    --AudioData  \
    --Codec wav \
    --TypeId 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "AudioId": "abc",
            "DetectionCode": 0,
            "DetectionMsg": "abc",
            "DetectionTip": [
                {
                    "PronAccuracy": 0,
                    "PronFluency": 0,
                    "Tag": 0,
                    "Word": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

