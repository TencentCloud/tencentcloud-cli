**Example 1: 发起字幕框检测**



Input: 

```
tccli mps DetectVideoSubtitleArea --cli-unfold-argument  \
    --InputInfo.Type URL \
    --InputInfo.UrlInputInfo.Url http://*********************************************************************************************************************************************.mp4 \
    --VideoLanguage zh_en \
    --UserExtPara 
```

Output: 
```
{
    "Response": {
        "Height": 1280,
        "Result": [
            {
                "Area": {
                    "LeftTopX": 64,
                    "LeftTopY": 748,
                    "RightBottomX": 576,
                    "RightBottomY": 791,
                    "Unit": 2
                },
                "Confidence": 70
            }
        ],
        "Width": 720,
        "RequestId": "4af4d815-d608-4aff-afb3-45f3b46563b0"
    }
}
```

