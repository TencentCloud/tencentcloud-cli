**Example 1: 获取实时音视频的时长统计数据 。走计费渠道第二版**



Input: 

```
tccli trtc DescribeExternalTrtcMeasure --cli-unfold-argument  \
    --EndTime 2022-01-01 00:00:00 \
    --StartTime 2022-01-03 00:00:00 \
    --SdkAppId 1
```

Output: 
```
{
    "Response": {
        "AnchorUsageMode": "xx",
        "AudienceUsageMode": "xx",
        "RequestId": "xx",
        "SdkAppIdTrtrTimeUsages": [
            {
                "TrtcTimeUsages": [
                    {
                        "AudioTime": 1,
                        "Video4KTime": 1,
                        "VideoTime": 1,
                        "Class1VideoTime": 1,
                        "TimeKey": "xx",
                        "Class3VideoTime": 1,
                        "Video2KTime": 1,
                        "Bandwidth": 0.0,
                        "VoiceUserNum": 1,
                        "Class2VideoTime": 1
                    },
                    {
                        "AudioTime": 1,
                        "Video4KTime": 1,
                        "TimeKey": "xx",
                        "Class1VideoTime": 1,
                        "VideoTime": 1,
                        "Class3VideoTime": 1,
                        "Video2KTime": 1,
                        "Bandwidth": 0.0,
                        "VoiceUserNum": 1,
                        "Class2VideoTime": 1
                    },
                    {
                        "AudioTime": 1,
                        "Video4KTime": 1,
                        "TimeKey": "xx",
                        "Class1VideoTime": 1,
                        "VideoTime": 1,
                        "Class3VideoTime": 1,
                        "Video2KTime": 1,
                        "Bandwidth": 0.0,
                        "VoiceUserNum": 1,
                        "Class2VideoTime": 1
                    }
                ],
                "AudienceTrtcTimeUsages": [
                    {
                        "AudioTime": 1,
                        "Video4KTime": 1,
                        "VideoTime": 1,
                        "Class1VideoTime": 1,
                        "TimeKey": "xx",
                        "Class3VideoTime": 1,
                        "Video2KTime": 1,
                        "Bandwidth": 0.0,
                        "VoiceUserNum": 1,
                        "Class2VideoTime": 1
                    }
                ],
                "SdkAppId": "xx"
            }
        ]
    }
}
```

