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
            "AudioId": "vrs8270f89c-51f8-41c9-8bee-19fb5b8b9708",
            "DetectionCode": 0,
            "DetectionMsg": "Success",
            "DetectionTip": [
                {
                    "PronAccuracy": 0,
                    "PronFluency": 0,
                    "Tag": 0,
                    "Word": "我"
                }
            ]
        },
        "RequestId": "63f43c3d6e30af6bd63735b0"
    }
}
```

