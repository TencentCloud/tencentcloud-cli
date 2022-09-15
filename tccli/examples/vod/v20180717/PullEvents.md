**Example 1: 拉取事件**



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
                "ProcedureStateChangeEvent": {
                    "TaskId": "1256768367-Procedure-475b7237438a39560b9879a4556cb177t2",
                    "Status": "FINISH",
                    "ErrCode": 0,
                    "Message": "",
                    "FileId": "5285890784246869930",
                    "FileName": "small",
                    "FileUrl": "https://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/c643347c5285890784246869930/1546950643_4191274987.100_0.jpg",
                    "MetaData": {
                        "AudioDuration": 59.990001678467,
                        "AudioStreamSet": [
                            {
                                "Bitrate": 383854,
                                "Codec": "aac",
                                "SamplingRate": 48000
                            }
                        ],
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
                                "Fps": 23,
                                "Height": 480,
                                "Width": 640
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
                                "Message": "SUCCESS",
                                "Input": {
                                    "Definition": 20,
                                    "WatermarkSet": null
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
                                            "Fps": 24,
                                            "Height": 480,
                                            "Width": 640
                                        }
                                    ],
                                    "AudioStreamSet": [
                                        {
                                            "Bitrate": 48491,
                                            "Codec": "aac",
                                            "SamplingRate": 44100
                                        }
                                    ],
                                    "Definition": 0
                                }
                            },
                            "AnimatedGraphicTask": null,
                            "SnapshotByTimeOffsetTask": null,
                            "SampleSnapshotTask": null,
                            "ImageSpriteTask": null,
                            "CoverBySnapshotTask": null
                        },
                        {
                            "Type": "CoverBySnapshot",
                            "TranscodeTask": null,
                            "AnimatedGraphicTask": null,
                            "SnapshotByTimeOffsetTask": null,
                            "SampleSnapshotTask": null,
                            "ImageSpriteTask": null,
                            "CoverBySnapshotTask": {
                                "Status": "SUCCESS",
                                "ErrCode": 0,
                                "Message": "SUCCESS",
                                "Input": {
                                    "Definition": 10,
                                    "PositionType": "Time",
                                    "PositionValue": 0,
                                    "WatermarkSet": null
                                },
                                "Output": {
                                    "CoverUrl": "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/c643347c5285890784246869930/1546950643_4191274987.100_0.jpg"
                                }
                            }
                        }
                    ],
                    "AiContentReviewResultSet": null,
                    "AiRecognitionResultSet": null
                },
                "FileDeleteEvent": null,
                "PullCompleteEvent": null,
                "TranscodeCompleteEvent": null,
                "ConcatCompleteEvent": null,
                "ClipCompleteEvent": null,
                "CreateImageSpriteCompleteEvent": null,
                "SnapshotByTimeOffsetCompleteEvent": null
            },
            {
                "EventHandle": "EventHandle2",
                "EventType": "NewFileUpload",
                "FileUploadEvent": {
                    "FileId": "5285890784273533167",
                    "MediaBasicInfo": {
                        "Name": "small2",
                        "Description": "",
                        "CreateTime": "2019-01-09T16:36:22Z",
                        "UpdateTime": "2019-01-09T16:36:24Z",
                        "ExpireTime": "9999-12-31T23:59:59Z",
                        "ClassId": 0,
                        "ClassName": "其他",
                        "ClassPath": "其他",
                        "CoverUrl": "",
                        "Type": "mp4",
                        "MediaUrl": "http://123.vod2.myqcloud.com/1c1ae5d2vodgzp1256768367/9ce0cd925285890784273533167/q1BORBPQH1IA.mp4",
                        "TagSet": [],
                        "StorageRegion": "ap-guangzhou-2",
                        "SourceInfo": {
                            "SourceType": "Upload",
                            "SourceContext": ""
                        },
                        "Vid": "5285890784273533167"
                    },
                    "ProcedureTaskId": ""
                },
                "ProcedureStateChangeEvent": null,
                "FileDeleteEvent": null,
                "PullCompleteEvent": null,
                "TranscodeCompleteEvent": null,
                "ConcatCompleteEvent": null,
                "ClipCompleteEvent": null,
                "CreateImageSpriteCompleteEvent": null,
                "SnapshotByTimeOffsetCompleteEvent": null
            },
            {
                "EventHandle": "EventHandle3",
                "EventType": "ProcedureStateChanged",
                "FileUploadEvent": null,
                "ProcedureStateChangeEvent": {
                    "TaskId": "1256768367-procedurev2-49dfbaea6786dd78ecf70d6256c7ec20t0",
                    "Status": "FINISH",
                    "ErrCode": 0,
                    "Message": "",
                    "FileId": "5285890784273533167",
                    "FileName": "small2",
                    "FileUrl": "http://123.vod2.myqcloud.com/1c1ae5d2vodgzp1256768367/9ce0cd925285890784273533167/q1BORBPQH1IA.mp4",
                    "MetaData": {
                        "AudioDuration": 59.990001678467,
                        "AudioStreamSet": [
                            {
                                "Bitrate": 383854,
                                "Codec": "aac",
                                "SamplingRate": 48000
                            }
                        ],
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
                                "Fps": 23,
                                "Height": 480,
                                "Width": 640
                            }
                        ],
                        "Width": 640
                    },
                    "MediaProcessResultSet": [
                        {
                            "Type": "SampleSnapshot",
                            "TranscodeTask": null,
                            "AnimatedGraphicTask": null,
                            "SnapshotByTimeOffsetTask": null,
                            "SampleSnapshotTask": {
                                "Status": "SUCCESS",
                                "ErrCode": 0,
                                "Message": "SUCCESS",
                                "Input": {
                                    "Definition": 10,
                                    "WatermarkSet": null
                                },
                                "Output": {
                                    "ImageUrlSet": [
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_0.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_6000.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_12000.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_18000.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_24000.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_30000.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_36000.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_42000.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_48000.jpg",
                                        "http://123.vod2.myqcloud.com/d042887avodtransgzp1256768367/9ce0cd925285890784273533167/1547051785_1651252995.100_54000.jpg"
                                    ],
                                    "Definition": 0,
                                    "SampleType": "",
                                    "Interval": 0,
                                    "WaterMarkDefinition": null
                                }
                            },
                            "ImageSpriteTask": null,
                            "CoverBySnapshotTask": null
                        }
                    ],
                    "AiContentReviewResultSet": null,
                    "AiRecognitionResultSet": null
                },
                "FileDeleteEvent": null,
                "PullCompleteEvent": null,
                "TranscodeCompleteEvent": null,
                "ConcatCompleteEvent": null,
                "ClipCompleteEvent": null,
                "CreateImageSpriteCompleteEvent": null,
                "SnapshotByTimeOffsetCompleteEvent": null
            },
            {
                "EventHandle": "EventHandle4",
                "EventType": "EditMediaComplete",
                "FileUploadEvent": null,
                "ProcedureStateChangeEvent": null,
                "FileDeleteEvent": null,
                "PullCompleteEvent": null,
                "EditMediaCompleteEvent": {
                    "TaskId": "1256768367-procedurev2-1b0c3f17fad2f81a5327b57f1005e115t0",
                    "Status": "FINISH",
                    "ErrCode": 0,
                    "Message": "",
                    "Input": {
                        "InputType": "ConcatFiles",
                        "FileInfoSet": [
                            {
                                "FileId": "",
                                "StartTimeOffset": 1,
                                "EndTimeOffset": 5
                            }
                        ],
                        "StreamInfoSet": null
                    },
                    "Output": {
                        "FileType": "",
                        "FileId": "15517827183909093239",
                        "FileUrl": "http://1256768367.vod2.myqcloud.com/1c1ae5d2vodgzp1256768367/e0a739c115517827183909093239/clip.mp4"
                    },
                    "ProcedureTaskId": ""
                },
                "TranscodeCompleteEvent": null,
                "ConcatCompleteEvent": null,
                "ClipCompleteEvent": null,
                "CreateImageSpriteCompleteEvent": null,
                "SnapshotByTimeOffsetCompleteEvent": null,
                "ReviewAudioVideoCompleteEvent": null
            }
        ],
        "RequestId": "335bdaa3-db0e-46ce-9946-51941d9cb0f5"
    }
}
```

