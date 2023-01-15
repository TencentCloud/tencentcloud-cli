**Example 1: 查询实时语音和离线语音2019-08-01至2019-08-03的用量统计**

查询实时语音和离线语音2019-08-01至2019-08-03的用量统计

Input: 

```
tccli gme DescribeAppStatistics --cli-unfold-argument  \
    --Services VoiceMessage RealTimeSpeech \
    --StartDate 2019-08-01 \
    --EndDate 2019-08-03 \
    --BizId 140000001
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppStatistics": [
                {
                    "VoiceFilterStatisticsItem": {
                        "Duration": 1
                    },
                    "RealtimeSpeechStatisticsItem": {
                        "MainLandPcu": 1,
                        "OverseaDuration": 1,
                        "OverseaPcu": 1,
                        "OverseaDau": 1,
                        "MainLandDuration": 1,
                        "MainLandDau": 1
                    },
                    "StreamTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "RealtimeTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "VoiceMessageStatisticsItem": {
                        "Dau": 1
                    },
                    "AudioTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "Date": "2020-09-22",
                    "OverseaTextStatisticsItem": {
                        "Data": 0.0
                    }
                },
                {
                    "VoiceFilterStatisticsItem": {
                        "Duration": 1
                    },
                    "RealtimeSpeechStatisticsItem": {
                        "MainLandPcu": 1,
                        "MainLandDuration": 1,
                        "OverseaPcu": 1,
                        "OverseaDau": 1,
                        "OverseaDuration": 1,
                        "MainLandDau": 1
                    },
                    "Date": "2020-09-22",
                    "StreamTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "RealtimeTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "VoiceMessageStatisticsItem": {
                        "Dau": 1
                    },
                    "AudioTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "OverseaTextStatisticsItem": {
                        "Data": 0.0
                    }
                },
                {
                    "VoiceFilterStatisticsItem": {
                        "Duration": 1
                    },
                    "RealtimeSpeechStatisticsItem": {
                        "MainLandPcu": 1,
                        "MainLandDuration": 1,
                        "OverseaPcu": 1,
                        "OverseaDau": 1,
                        "OverseaDuration": 1,
                        "MainLandDau": 1
                    },
                    "Date": "2020-09-22",
                    "StreamTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "RealtimeTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "VoiceMessageStatisticsItem": {
                        "Dau": 1
                    },
                    "AudioTextStatisticsItem": {
                        "Data": 0.0
                    },
                    "OverseaTextStatisticsItem": {
                        "Data": 0.0
                    }
                }
            ]
        },
        "RequestId": "099d942a-f5c5-40d2-b96b-5c26a35813e0"
    }
}
```

