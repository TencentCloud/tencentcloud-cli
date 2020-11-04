**Example 1: 查询实时语音和离线语音2019-08-01至2019-08-03的用量统计**



Input: 

```
tccli gme DescribeAppStatistics --cli-unfold-argument  \
    --BizId 140000001\
    --StartDate 2019-08-01\
    --EndDate 2019-08-03\
    --Services RealTimeSpeech VoiceMessage
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppStatistics": [
                {
                    "Date": "2019-08-01",
                    "RealtimeSpeechStatisticsItem": {
                        "MainLandDau": 10000,
                        "MainLandPcu": 5000,
                        "MainLandDuration": 1000000,
                        "OverseaDau": 5000,
                        "OverseaPcu": 2000,
                        "OverseaDuration": 500000
                    },
                    "VoiceMessageStatisticsItem": {
                        "Dau": 68000
                    },
                    "VoiceFilterStatisticsItem": null
                },
                {
                    "Date": "2019-08-02",
                    "RealtimeSpeechStatisticsItem": {
                        "MainLandDau": 10000,
                        "MainLandPcu": 5000,
                        "MainLandDuration": 1000000,
                        "OverseaDau": 5000,
                        "OverseaPcu": 2000,
                        "OverseaDuration": 500000
                    },
                    "VoiceMessageStatisticsItem": {
                        "Dau": 68000
                    },
                    "VoiceFilterStatisticsItem": null
                },
                {
                    "Date": "2019-08-03",
                    "RealtimeSpeechStatisticsItem": {
                        "MainLandDau": 10000,
                        "MainLandPcu": 5000,
                        "MainLandDuration": 1000000,
                        "OverseaDau": 5000,
                        "OverseaPcu": 2000,
                        "OverseaDuration": 500000
                    },
                    "VoiceMessageStatisticsItem": {
                        "Dau": 68000
                    },
                    "VoiceFilterStatisticsItem": null
                }
            ]
        },
        "RequestId": "9b993045-9fa1-47f4-9d25-79160f305be8"
    }
}
```

