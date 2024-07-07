**Example 1: 查询媒体质检模板列表**



Input: 

```
tccli mps DescribeQualityControlTemplates --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Definitions 200058
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "QualityControlTemplateSet": [
            {
                "Definition": 200058,
                "Name": "0529",
                "Comment": "",
                "Type": "Custom",
                "QualityControlItemSet": [
                    {
                        "Type": "LowEvaluation",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "Mosaic",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "CrashScreen",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "Blur",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "BlackWhiteEdge",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "LowLighting",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HighLighting",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "NoVoice",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "LowVoice",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HighVoice",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoResolutionChanged",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioSampleRateChanged",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioChannelsChanged",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "ParameterSetsChanged",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "DarOrSarInvalid",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "TimestampFallback",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "DtsJitter",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "PtsJitter",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AACDurationDeviation",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioDroppingFrames",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoDroppingFrames",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AVTimestampInterleave",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "PtsLessThanDts",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "ReceiveFpsJitter",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "ReceiveFpsTooSmall",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "FpsJitter",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "StreamOpenFailed",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "StreamEnd",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "StreamParseFailed",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoFirstFrameNotIdr",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "StreamNALUError",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "TsStreamNoAud",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioStreamLack",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoStreamLack",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "LackAudioRecover",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "LackVideoRecover",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoBitrateOutofRange",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioBitrateOutofRange",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoDecodeFailed",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioDecodeFailed",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioOutOfPhase",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoDuplicatedFrame",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "AudioDuplicatedFrame",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoRotation",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "TsMultiPrograms",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "Mp4InvalidCodecFourcc",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSBadM3u8Format",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSInvalidMasterM3u8",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSInvalidMediaM3u8",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMasterM3u8Recommended",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaM3u8Recommended",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaM3u8DiscontinuityExist",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaSegmentsStreamNumChange",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaSegmentsPTSJitterDeviation",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "HLSMediaSegmentsDTSJitterDeviation",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "TimecodeTrackExist",
                        "Switch": "OFF",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 0,
                        "Threshold": ""
                    },
                    {
                        "Type": "VideoFreezedFrame",
                        "Switch": "ON",
                        "Sampling": "",
                        "IntervalTime": 0,
                        "Duration": 1000,
                        "Threshold": "0.001"
                    }
                ],
                "CreateTime": "2024-05-29T03:01:54Z",
                "UpdateTime": "2024-05-29T03:01:54Z"
            }
        ],
        "RequestId": "76d831ad-105e-48eb-90dd-00deaa00b52a"
    }
}
```

