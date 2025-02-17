**Example 1: 查询旁路转码计费时长**

多日查询

Input: 

```
tccli trtc DescribeTrtcMcuTranscodeTime --cli-unfold-argument  \
    --EndTime 2020-09-08 \
    --StartTime 2020-09-07 \
    --SdkAppId 1400123456
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "SdkAppId": "1400123456",
                "TotalNum": 1,
                "SdkAppIdTranscodeTimeUsages": [
                    {
                        "Flux": 10,
                        "AudioTime": 12,
                        "VideoTimeHd": 21,
                        "VideoTimeFhd": 234,
                        "VideoTimeSd": 198,
                        "TimeKey": "2020-09-07"
                    }
                ]
            }
        ],
        "RequestId": "644956b8-9f7c-44c5-b833-31d91dba1b23"
    }
}
```

