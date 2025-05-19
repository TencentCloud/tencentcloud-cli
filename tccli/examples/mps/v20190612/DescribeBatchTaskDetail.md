**Example 1: 查询结果**



Input: 

```
tccli mps DescribeBatchTaskDetail --cli-unfold-argument  \
    --TaskId 24xxxx-BatchTask-6b24c23ee5xxxxxx
```

Output: 
```
{
    "Response": {
        "BatchTaskResult": {
            "InputInfos": [
                {
                    "CosInputInfo": {
                        "Bucket": "",
                        "Object": "",
                        "Region": ""
                    },
                    "S3InputInfo": null,
                    "Type": "URL",
                    "UrlInputInfo": {
                        "Url": "http://tetst-xxxx-12234xxx.cos.ap-xxxx.myqcloud.com/processmedia/52.mp4"
                    }
                }
            ],
            "Metadatas": [
                {
                    "AudioDuration": 55.454,
                    "AudioStreamSet": [
                        {
                            "Bitrate": 252293,
                            "Channel": 1,
                            "Codec": "aac",
                            "Codecs": "",
                            "Loudness": 0,
                            "SamplingRate": 44100
                        }
                    ],
                    "Bitrate": 1734778,
                    "Container": "mp4",
                    "Duration": 55.455,
                    "Height": 1080,
                    "Rotate": 0,
                    "Size": 12025270,
                    "VideoDuration": 54.955,
                    "VideoStreamSet": [
                        {
                            "Bitrate": 1487136,
                            "Codec": "h264",
                            "Codecs": "",
                            "ColorPrimaries": "",
                            "ColorSpace": "",
                            "ColorTransfer": "",
                            "Fps": 32,
                            "FpsDenominator": 0,
                            "FpsNumerator": 0,
                            "HdrType": "sdr",
                            "Height": 1080,
                            "Width": 1920
                        }
                    ],
                    "Width": 1920
                }
            ],
            "SmartSubtitlesTaskResult": {
                "Input": {
                    "Definition": 0,
                    "RawParameter": {
                        "AsrHotWordsConfigure": null,
                        "ExtInfo": "",
                        "SubtitleFormat": "vtt",
                        "SubtitleType": 2,
                        "TranslateDstLanguage": "en",
                        "TranslateSwitch": "ON",
                        "VideoSrcLanguage": "zh"
                    }
                },
                "Outputs": [
                    {
                        "ErrCodeExt": "",
                        "Message": "SUCCESS",
                        "Progress": 100,
                        "Status": "SUCCESS",
                        "TransTextTask": {
                            "SegmentSet": [
                                {
                                    "Confidence": 99,
                                    "EndTimeOffset": 2.424,
                                    "StartTimeOffset": 1.774,
                                    "Text": "走路。",
                                    "Trans": "Walking.",
                                    "Wordlist": []
                                },
                                {
                                    "Confidence": 99,
                                    "EndTimeOffset": 55.121,
                                    "StartTimeOffset": 53.721,
                                    "Text": "就在你跟再说。",
                                    "Trans": "Just before you tell me.",
                                    "Wordlist": []
                                }
                            ],
                            "SubtitlePath": "http://tetst-xxxx-12234xxx.cos.ap-xxxx.myqcloud.com/output/3529.vtt"
                        }
                    }
                ]
            }
        },
        "BeginProcessTime": "2025-05-17T07:15:11Z",
        "CreateTime": "2025-05-17T07:15:11Z",
        "ExtInfo": "",
        "FinishTime": "2025-05-17T07:15:36Z",
        "RequestId": "0af8e6df-622d-49b5-98e6-4d8e3f294e5f",
        "SessionContext": "asdzxcs",
        "SessionId": "qwer123",
        "Status": "FINISH",
        "TaskId": "24xxxxx-BatchTask-e6fefa34fc497xxxxxxx7det20",
        "TaskNotifyConfig": {
            "AwsSQS": null,
            "CmqModel": "",
            "CmqRegion": "",
            "NotifyKey": "",
            "NotifyMode": "Finish",
            "NotifyType": "URL",
            "NotifyUrl": "http://xxxx.com/v2/push/mps_test?token=73YcsZyP",
            "QueueName": "",
            "TopicName": ""
        },
        "TaskType": "BatchTask",
        "TasksPriority": 0
    }
}
```

