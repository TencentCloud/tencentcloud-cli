**Example 1: 获取任务详情**

查询任务结果

Input: 

```
tccli mps DescribeTaskDetail --cli-unfold-argument  \
    --TaskId 235303****-WorkflowTask-80108cc3380155d98b2e3573a48a******
```

Output: 
```
{
    "Response": {
        "TaskType": "WorkflowTask",
        "Status": "FINISH",
        "CreateTime": "2019-07-16T06:21:27Z",
        "BeginProcessTime": "2019-07-16T06:21:28Z",
        "FinishTime": "2019-07-16T06:21:46Z",
        "WorkflowTask": {
            "TaskId": "235303****-WorkflowTask-80108cc3380155d98b2e3573a48a******",
            "Status": "FINISH",
            "ErrCode": 0,
            "Message": "",
            "InputInfo": {
                "Type": "COS",
                "CosInputInfo": {
                    "Bucket": "vodtestbj-235303****",
                    "Region": "ap-beijing",
                    "Object": "/input/videoplayback.mp4"
                },
                "S3InputInfo": null,
                "UrlInputInfo": null
            },
            "MetaData": {
                "AudioDuration": 380.9465637207031,
                "AudioStreamSet": [
                    {
                        "Channel": 0,
                        "Bitrate": 95999,
                        "Codec": "aac",
                        "Codecs": "mp4a.40.2",
                        "Loudness": 0,
                        "SamplingRate": 44100
                    }
                ],
                "Bitrate": 409657,
                "Container": "mov,mp4,m4a,3gp,3g2,mj2",
                "Duration": 380.9465637207031,
                "Height": 360,
                "Rotate": 0,
                "Size": 19626862,
                "VideoDuration": 380.8804931640625,
                "VideoStreamSet": [
                    {
                        "Bitrate": 313658,
                        "Codec": "h264",
                        "Codecs": "avc1.ffe100",
                        "Fps": 29,
                        "Height": 360,
                        "HdrType": "",
                        "ColorPrimaries": "",
                        "ColorSpace": "",
                        "ColorTransfer": "",
                        "Width": 480
                    }
                ],
                "Width": 480
            },
            "MediaProcessResultSet": [
                {
                    "Type": "Transcode",
                    "TranscodeTask": {
                        "Status": "SUCCESS",
                        "ErrCode": 0,
                        "Message": "SUCCESS",
                        "ErrCodeExt": "SUCCESS",
                        "Progress": 100,
                        "Input": {
                            "Definition": 210,
                            "WatermarkSet": [],
                            "MosaicSet": [],
                            "RawParameter": null,
                            "EndTimeOffset": 0,
                            "OverrideParameter": null,
                            "HeadTailParameter": null,
                            "StartTimeOffset": 0,
                            "OutputStorage": {
                                "Type": "COS",
                                "CosOutputStorage": {
                                    "Bucket": "vodtestgz-235303****",
                                    "Region": "ap-guangzhou"
                                },
                                "S3OutputStorage": null
                            },
                            "OutputObjectPath": "/hello/world/what/ever/videoplayback_transcode111_210",
                            "SegmentObjectName": "/hello/world/what/ever/no/problem/videoplayback_transcode11_210_{number}",
                            "ObjectNumberFormat": {
                                "InitialValue": 2,
                                "Increment": 3,
                                "MinLength": 1,
                                "PlaceHolder": "0"
                            }
                        },
                        "Output": {
                            "OutputStorage": {
                                "Type": "COS",
                                "CosOutputStorage": {
                                    "Bucket": "vodtestgz-235303****",
                                    "Region": "ap-guangzhou"
                                },
                                "S3OutputStorage": null
                            },
                            "Path": "/hello/world/what/ever/videoplayback_transcode111_210.m3u8",
                            "Definition": 210,
                            "Bitrate": 353297,
                            "Height": 240,
                            "Width": 320,
                            "Size": 5692,
                            "Duration": 380.9580078125,
                            "Container": "hls,applehttp",
                            "Md5": "ae0dfe7c7336291d6243463b7bb14fea",
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 302307,
                                    "Codec": "h264",
                                    "Codecs": "avc1.ffe100",
                                    "Fps": 24,
                                    "Height": 240,
                                    "HdrType": "",
                                    "ColorPrimaries": "",
                                    "ColorSpace": "",
                                    "ColorTransfer": "",
                                    "Width": 320
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Channel": 0,
                                    "Bitrate": 50990,
                                    "Codec": "aac",
                                    "Codecs": "mp4a.40.2",
                                    "Loudness": 0,
                                    "SamplingRate": 44100
                                }
                            ]
                        }
                    },
                    "AnimatedGraphicTask": null,
                    "SnapshotByTimeOffsetTask": null,
                    "SampleSnapshotTask": null,
                    "ImageSpriteTask": null,
                    "AdaptiveDynamicStreamingTask": null
                }
            ],
            "AiAnalysisResultSet": [],
            "AiRecognitionResultSet": [],
            "AiContentReviewResultSet": [],
            "AiQualityControlTaskResult": null
        },
        "TaskNotifyConfig": null,
        "EditMediaTask": null,
        "LiveStreamProcessTask": null,
        "ScheduleTask": null,
        "LiveScheduleTask": null,
        "TasksPriority": 0,
        "SessionId": "",
        "SessionContext": "",
        "ExtInfo": "",
        "RequestId": "04db7d25-f590-414a-a341-8f1584f15f84"
    }
}
```

