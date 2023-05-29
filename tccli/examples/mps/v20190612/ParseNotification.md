**Example 1: 解析事件通知内容**

解析事件通知内容

Input: 

```
tccli mps ParseNotification --cli-unfold-argument  \
    --Content {"EventType":"ProcedureStateChanged",XXX
```

Output: 
```
{
    "Response": {
        "EventType": "WorkflowTask",
        "WorkflowTaskEvent": {
            "TaskId": "1256768367-Procedure-475b7237438a39560b9879a4556cb177t1",
            "Status": "FINISH",
            "ErrCode": 0,
            "Message": "",
            "InputInfo": {
                "Type": "COS",
                "CosInputInfo": {
                    "Bucket": "TopRankVideo-125xxx88",
                    "Region": "ap-chongqing",
                    "Object": "/movie/201907/WildAnimal.mov"
                }
            },
            "MetaData": {
                "AudioDuration": 59.990001678467,
                "AudioStreamSet": [
                    {
                        "Bitrate": 383854,
                        "SamplingRate": 48000,
                        "Codec": "aac",
                        "Channel": 0,
                        "Loudness": 0
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
                        "Width": 640,
                        "ColorPrimaries": "abc",
                        "ColorSpace": "abc",
                        "ColorTransfer": "abc",
                        "HdrType": "abc"
                    }
                ],
                "Width": 640
            },
            "MediaProcessResultSet": [
                {
                    "Type": "Transcode",
                    "TranscodeTask": {
                        "Status": "SUCCESS",
                        "ErrCodeExt": "SUCCESS",
                        "ErrCode": 0,
                        "Message": "SUCCESS",
                        "Progress": 0,
                        "Input": {
                            "Definition": 20,
                            "WatermarkSet": null
                        },
                        "Output": {
                            "Path": "/movie/201907/WildAnimal_transcode_20.mp4",
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
                                    "Width": 640,
                                    "ColorPrimaries": "abc",
                                    "ColorSpace": "abc",
                                    "ColorTransfer": "abc",
                                    "HdrType": "abc"
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Bitrate": 48491,
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Channel": 0,
                                    "Loudness": 0
                                }
                            ],
                            "Definition": 0
                        }
                    },
                    "AnimatedGraphicTask": null,
                    "SnapshotByTimeOffsetTask": null,
                    "SampleSnapshotTask": null,
                    "ImageSpriteTask": null
                }
            ],
            "AiQualityControlTaskResult": null,
            "AiAnalysisResultSet": [],
            "AiRecognitionResultSet": [],
            "AiContentReviewResultSet": []
        },
        "RequestId": "335bdaa3-db0e-46ce-9946-51941d9cb0f5",
        "ScheduleTaskEvent": null,
        "EditMediaTaskEvent": null,
        "SessionId": "",
        "SessionContext": ""
    }
}
```

