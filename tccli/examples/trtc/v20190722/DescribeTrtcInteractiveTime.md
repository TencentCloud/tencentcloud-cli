**Example 1: 查询音视频互动计费时长（查询区间超过1天）**

查询的时间区间为多日

Input: 

```
tccli trtc DescribeTrtcInteractiveTime --cli-unfold-argument  \
    --SdkAppId 1400243510 \
    --StartTime 2020-09-07 \
    --EndTime 2020-09-08
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "TotalNum": 2,
                "SdkAppId": "1400243510",
                "SdkAppIdTrtcTimeUsages": [
                    {
                        "AudioVideoTime": 0,
                        "VideoTimeSd": 3633229,
                        "VideoTimeHd": 7266458,
                        "VideoTimeHdp": 10899687,
                        "AudioTime": 8435963,
                        "TimeKey": "2020-09-07"
                    },
                    {
                        "AudioVideoTime": 0,
                        "VideoTimeSd": 8896,
                        "VideoTimeHd": 17792,
                        "VideoTimeHdp": 26688,
                        "AudioTime": 30690,
                        "TimeKey": "2020-09-08"
                    }
                ]
            }
        ],
        "RequestId": "644956b8-9f7c-44c5-b833-31d91dba1b24"
    }
}
```

**Example 2: 查询音视频互动计费时长（查询区间为同一天）**



Input: 

```
tccli trtc DescribeTrtcInteractiveTime --cli-unfold-argument  \
    --SdkAppId 1400243510 \
    --StartTime 2020-09-08 \
    --EndTime 2020-09-08
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "TotalNum": 2,
                "SdkAppId": "1400243510",
                "SdkAppIdTrtcTimeUsages": [
                    {
                        "AudioVideoTime": 14706996,
                        "VideoTimeSd": 0,
                        "VideoTimeHd": 0,
                        "VideoTimeHdp": 0,
                        "AudioTime": 0,
                        "TimeKey": "2020-09-07 09:50:00"
                    },
                    {
                        "AudioVideoTime": 56820,
                        "VideoTimeSd": 0,
                        "VideoTimeHd": 0,
                        "VideoTimeHdp": 0,
                        "AudioTime": 0,
                        "TimeKey": "2020-09-08 09:55:00"
                    }
                ]
            }
        ],
        "RequestId": "644956b8-9f7c-44c5-b833-31d91dba1b24"
    }
}
```

**Example 3: 查询音视频互动计费时长（不传SDKAppID时的情况）**



Input: 

```
tccli trtc DescribeTrtcInteractiveTime --cli-unfold-argument  \
    --StartTime 2020-09-08 \
    --EndTime 2020-09-08
```

Output: 
```
{
    "Response": {
        "Usages": [
            {
                "SdkAppId": "total",
                "SdkAppIdTrtcTimeUsages": [
                    {
                        "TimeKey": "2020-09-08 00:05:00",
                        "AudioVideoTime": 512916,
                        "VideoTimeSd": 0,
                        "VideoTimeHd": 0,
                        "VideoTimeHdp": 0,
                        "AudioTime": 0
                    },
                    {
                        "TimeKey": "2020-09-08 00:10:00",
                        "AudioVideoTime": 523098,
                        "VideoTimeSd": 0,
                        "VideoTimeHd": 0,
                        "VideoTimeHdp": 0,
                        "AudioTime": 0
                    },
                    {
                        "TimeKey": "2020-09-08 00:15:00",
                        "AudioVideoTime": 512861,
                        "VideoTimeSd": 0,
                        "VideoTimeHd": 0,
                        "VideoTimeHdp": 0,
                        "AudioTime": 0
                    }
                ],
                "TotalNum": 3
            }
        ],
        "RequestId": "644956b8-9f7c-44c5-b833-31d91dba1b24"
    }
}
```

