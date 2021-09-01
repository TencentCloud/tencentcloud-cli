**Example 1: 查询旁路转码计费时长**

多日查询

Input: 

```
tccli trtc DescribeTrtcMcuTranscodeTime --cli-unfold-argument  \
    --SdkAppId 1400123456 \
    --StartTime 2020-09-07 \
    --EndTime 2020-09-08
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
                        "AudioTime": 1,
                        "VideoTimeHd": 1,
                        "VideoTimeFhd": 1,
                        "VideoTimeSd": 1,
                        "TimeKey": "xx"
                    }
                ]
            }
        ],
        "RequestId": "644956b8-9f7c-44c5-b833-31d91dba1b23"
    }
}
```

