**Example 1: 查询旁路转码计费时长 通过计费二期接口**



Input: 

```
tccli trtc MeasureTrtcMcuExternal --cli-unfold-argument  \
    --EndTime 2021-01-01 00:00:00 \
    --StartTime 2021-01-01 00:00:00 \
    --SdkAppId 1
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "SdkAppId": "xx",
                "TotalNum": 1,
                "SdkAppIdTranscodeTimeUsages": [
                    {
                        "AudioTime": 1,
                        "VideoTimeH2642K": 1,
                        "VideoTimeH265FHD": 1,
                        "TimeKey": "xx",
                        "VideoTimeH264HD": 1,
                        "VideoTimeH264SD": 1,
                        "VideoTimeH2652K": 1,
                        "VideoTimeH265HD": 1,
                        "Flux": 0.0,
                        "VideoTimeH264FHD": 1,
                        "VideoTimeH2644K": 1,
                        "VideoTimeH2654K": 1,
                        "VideoTimeH265SD": 1
                    }
                ]
            }
        ],
        "Type": "xx",
        "RequestId": "xx"
    }
}
```

