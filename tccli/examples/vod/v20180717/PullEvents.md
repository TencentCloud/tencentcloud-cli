**Example 1: 拉取事件**

拉取事件

Input: 

```
tccli vod PullEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "EventHandle": "EventHandle1",
                "EventType": "ProcedureStateChanged",
                "FileUploadEvent": null,
                "ExtractCopyRightWatermarkCompleteEvent": null,
                "QualityInspectCompleteEvent": null,
                "ProcedureStateChangeEvent": {
                    "TaskId": "1256712345-Procedure-475b7237438a39560b9879a4556cb177t2",
                    "Status": "FINISH",
                    "ErrCode": 0,
                    "Message": "",
                    "FileId": "5285890784246869930",
                    "FileName": "small",
                    "FileUrl": "https://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/c643347c5285890784246869930/1546950643_4191274987.100_0.jpg",
                    "SessionContext": "",
                    "SessionId": "",
                    "OperationType": "",
                    "TasksNotifyMode": "Finish",
                    "TasksPriority": 0,
                    "Operator": "",
                    "MetaData": {
                        "AudioDuration": 59.990001678467,
                        "AudioStreamSet": [
                            {
                                "Bitrate": 383854,
                                "Codec": "aac",
                                "SamplingRate": 48000
                            }
                        ],
                        "Md5": "07d635581e7f295b623f40bad0fbfd4c1",
                        "Bitrate": 1021028,
                        "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                        "Duration": 60,
                        "Height": 480,
                        "Rotate": 0,
                        "Size": 7700180,
                        "VideoDuration": 60,
                        "VideoStreamSet": [
                            {
                                "Bitrate": 637174,
                                "Codec": "h264",
                                "CodecTag": "",
                                "Fps": 23,
                                "Height": 480,
                                "Width": 640,
                                "DynamicRangeInfo": {
                                    "HDRType": "",
                                    "Type": "SDR"
                                }
                            }
                        ],
                        "Width": 640
                    },
                    "MediaProcessResultSet": [
                        {
                            "Type": "Transcode",
                            "TranscodeTask": {
                                "Status": "SUCCESS",
                                "ErrCode": 0,
                                "ErrCodeExt": "",
                                "Message": "SUCCESS",
                                "Progress": 100,
                                "BeginProcessTime": "2023-09-08T02:23:29Z",
                                "FinishTime": "2023-09-08T03:23:29Z",
                                "Input": {
                                    "Definition": 20,
                                    "WatermarkSet": [],
                                    "TraceWatermark": {
                                        "Switch": "ON",
                                        "Definition": 1
                                    },
                                    "CopyRightWatermark": {
                                        "Text": "copyRightxxx"
                                    },
                                    "MosaicSet": [],
                                    "HeadTailSet": [],
                                    "StartTimeOffset": 2,
                                    "EndTimeOffset": 3
                                },
                                "Output": {
                                    "Url": "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/c643347c5285890784246869930/v.f20.mp4",
                                    "Size": 4189073,
                                    "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                                    "Height": 480,
                                    "Width": 640,
                                    "Bitrate": 552218,
                                    "Md5": "eff7031ad7877865f9a3240e9ab165ad",
                                    "Duration": 60.04700088501,
                                    "VideoStreamSet": [
                                        {
                                            "Bitrate": 503727,
                                            "Codec": "h264",
                                            "CodecTag": "",
                                            "Fps": 24,
                                            "Height": 480,
                                            "Width": 640,
                                            "DynamicRangeInfo": {
                                                "HDRType": "",
                                                "Type": "SDR"
                                            }
                                        }
                                    ],
                                    "AudioStreamSet": [
                                        {
                                            "Bitrate": 48491,
                                            "Codec": "aac",
                                            "SamplingRate": 44100
                                        }
                                    ],
                                    "Definition": 0,
                                    "DigitalWatermarkType": "None",
                                    "CopyRightWatermarkText": ""
                                }
                            },
                            "AnimatedGraphicTask": null,
                            "SnapshotByTimeOffsetTask": null,
                            "SampleSnapshotTask": null,
                            "ImageSpriteTask": null,
                            "CoverBySnapshotTask": null
                        }
                    ],
                    "AiContentReviewResultSet": [],
                    "AiAnalysisResultSet": [],
                    "AiRecognitionResultSet": []
                },
                "FileDeleteEvent": null,
                "PullCompleteEvent": null,
                "EditMediaCompleteEvent": null,
                "SplitMediaCompleteEvent": null,
                "ComposeMediaCompleteEvent": null,
                "WechatPublishCompleteEvent": null,
                "TranscodeCompleteEvent": null,
                "ConcatCompleteEvent": null,
                "ClipCompleteEvent": null,
                "CreateImageSpriteCompleteEvent": null,
                "SnapshotByTimeOffsetCompleteEvent": null,
                "WechatMiniProgramPublishCompleteEvent": null,
                "RemoveWatermarkCompleteEvent": null,
                "RestoreMediaCompleteEvent": null,
                "RebuildMediaCompleteEvent": null,
                "ExtractTraceWatermarkCompleteEvent": null,
                "ReviewAudioVideoCompleteEvent": null,
                "DescribeFileAttributesCompleteEvent": null,
                "ReduceMediaBitrateCompleteEvent": null,
                "QualityEnhanceCompleteEvent": null
            }
        ],
        "RequestId": "5ca61a3a-6b8e-4b4e-9256-fdc001190064ef0"
    }
}
```

