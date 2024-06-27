**Example 1: 查询特定工作流**

查询 ID 为78459的工作流。

Input: 

```
tccli mps DescribeWorkflows --cli-unfold-argument  \
    --WorkflowIds 78459
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "WorkflowInfoSet": [
            {
                "WorkflowId": 0,
                "WorkflowName": "abc",
                "Status": "abc",
                "Trigger": {
                    "Type": "abc",
                    "CosFileUploadTrigger": {
                        "Bucket": "abc",
                        "Region": "abc",
                        "Dir": "abc",
                        "Formats": [
                            "abc"
                        ]
                    },
                    "AwsS3FileUploadTrigger": {
                        "S3Bucket": "abc",
                        "S3Region": "abc",
                        "Dir": "abc",
                        "Formats": [
                            "abc"
                        ],
                        "S3SecretId": "abc",
                        "S3SecretKey": "abc",
                        "AwsSQS": {
                            "SQSRegion": "abc",
                            "SQSQueueName": "abc",
                            "S3SecretId": "abc",
                            "S3SecretKey": "abc"
                        }
                    }
                },
                "OutputStorage": {
                    "Type": "abc",
                    "CosOutputStorage": {
                        "Bucket": "abc",
                        "Region": "abc"
                    },
                    "S3OutputStorage": {
                        "S3Bucket": "abc",
                        "S3Region": "abc",
                        "S3SecretId": "abc",
                        "S3SecretKey": "abc"
                    }
                },
                "MediaProcessTask": {
                    "TranscodeTaskSet": [
                        {
                            "Definition": 1,
                            "RawParameter": {
                                "Container": "abc",
                                "RemoveVideo": 0,
                                "RemoveAudio": 0,
                                "VideoTemplate": {
                                    "Codec": "abc",
                                    "Fps": 0,
                                    "Bitrate": 0,
                                    "ResolutionAdaptive": "abc",
                                    "Width": 1,
                                    "Height": 1,
                                    "Gop": 1,
                                    "FillType": "abc",
                                    "Vcrf": 1,
                                    "SegmentType": 0
                                },
                                "AudioTemplate": {
                                    "Codec": "abc",
                                    "Bitrate": 0,
                                    "SampleRate": 1,
                                    "AudioChannel": 0
                                },
                                "TEHDConfig": {
                                    "Type": "abc",
                                    "MaxVideoBitrate": 0
                                }
                            },
                            "OverrideParameter": {
                                "Container": "abc",
                                "RemoveVideo": 1,
                                "RemoveAudio": 1,
                                "VideoTemplate": {
                                    "Codec": "abc",
                                    "Fps": 0,
                                    "Bitrate": 0,
                                    "ResolutionAdaptive": "abc",
                                    "Width": 1,
                                    "Height": 1,
                                    "Gop": 1,
                                    "FillType": "abc",
                                    "Vcrf": 1,
                                    "ContentAdaptStream": 1,
                                    "SegmentType": 0
                                },
                                "AudioTemplate": {
                                    "Codec": "abc",
                                    "Bitrate": 0,
                                    "SampleRate": 1,
                                    "AudioChannel": 0,
                                    "StreamSelects": [
                                        0
                                    ]
                                },
                                "TEHDConfig": {
                                    "Type": "abc",
                                    "MaxVideoBitrate": 0
                                },
                                "SubtitleTemplate": {
                                    "Path": "abc",
                                    "StreamIndex": 0,
                                    "FontType": "abc",
                                    "FontSize": "abc",
                                    "FontColor": "abc",
                                    "FontAlpha": 0
                                },
                                "AddonAudioStream": [
                                    {
                                        "Type": "abc",
                                        "CosInputInfo": {
                                            "Bucket": "abc",
                                            "Region": "abc",
                                            "Object": "abc"
                                        },
                                        "UrlInputInfo": {
                                            "Url": "abc"
                                        },
                                        "S3InputInfo": {
                                            "S3Bucket": "abc",
                                            "S3Region": "abc",
                                            "S3Object": "abc",
                                            "S3SecretId": "abc",
                                            "S3SecretKey": "abc"
                                        }
                                    }
                                ],
                                "StdExtInfo": "abc",
                                "AddOnSubtitles": [
                                    {
                                        "Type": "abc",
                                        "Subtitle": {
                                            "Type": "abc",
                                            "CosInputInfo": {
                                                "Bucket": "abc",
                                                "Region": "abc",
                                                "Object": "abc"
                                            },
                                            "UrlInputInfo": {
                                                "Url": "abc"
                                            },
                                            "S3InputInfo": {
                                                "S3Bucket": "abc",
                                                "S3Region": "abc",
                                                "S3Object": "abc",
                                                "S3SecretId": "abc",
                                                "S3SecretKey": "abc"
                                            }
                                        }
                                    }
                                ]
                            },
                            "WatermarkSet": [
                                {
                                    "Definition": 1,
                                    "RawParameter": {
                                        "Type": "abc",
                                        "CoordinateOrigin": "abc",
                                        "XPos": "abc",
                                        "YPos": "abc",
                                        "ImageTemplate": {
                                            "ImageContent": {
                                                "Type": "abc",
                                                "CosInputInfo": {
                                                    "Bucket": "abc",
                                                    "Region": "abc",
                                                    "Object": "abc"
                                                },
                                                "UrlInputInfo": {
                                                    "Url": "abc"
                                                },
                                                "S3InputInfo": {
                                                    "S3Bucket": "abc",
                                                    "S3Region": "abc",
                                                    "S3Object": "abc",
                                                    "S3SecretId": "abc",
                                                    "S3SecretKey": "abc"
                                                }
                                            },
                                            "Width": "abc",
                                            "Height": "abc",
                                            "RepeatType": "abc"
                                        }
                                    },
                                    "TextContent": "abc",
                                    "SvgContent": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "MosaicSet": [
                                {
                                    "CoordinateOrigin": "abc",
                                    "XPos": "abc",
                                    "YPos": "abc",
                                    "Width": "abc",
                                    "Height": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "StartTimeOffset": 0,
                            "EndTimeOffset": 0,
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "OutputObjectPath": "abc",
                            "SegmentObjectName": "abc",
                            "ObjectNumberFormat": {
                                "InitialValue": 1,
                                "Increment": 1,
                                "MinLength": 1,
                                "PlaceHolder": "abc"
                            },
                            "HeadTailParameter": {}
                        }
                    ],
                    "AnimatedGraphicTaskSet": [
                        {
                            "Definition": 1,
                            "StartTimeOffset": 0,
                            "EndTimeOffset": 0,
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "OutputObjectPath": "abc"
                        }
                    ],
                    "SnapshotByTimeOffsetTaskSet": [
                        {
                            "Definition": 1,
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "ExtTimeOffsetSet": [
                                "abc"
                            ],
                            "TimeOffsetSet": [
                                0
                            ],
                            "WatermarkSet": [
                                {
                                    "Definition": 1,
                                    "RawParameter": {
                                        "Type": "abc",
                                        "CoordinateOrigin": "abc",
                                        "XPos": "abc",
                                        "YPos": "abc",
                                        "ImageTemplate": {
                                            "Width": "abc",
                                            "Height": "abc",
                                            "RepeatType": "abc"
                                        }
                                    },
                                    "TextContent": "abc",
                                    "SvgContent": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "OutputObjectPath": "abc",
                            "ObjectNumberFormat": {
                                "InitialValue": 1,
                                "Increment": 1,
                                "MinLength": 1,
                                "PlaceHolder": "abc"
                            }
                        }
                    ],
                    "SampleSnapshotTaskSet": [
                        {
                            "Definition": 1,
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "WatermarkSet": [
                                {
                                    "Definition": 1,
                                    "RawParameter": {
                                        "Type": "abc",
                                        "CoordinateOrigin": "abc",
                                        "XPos": "abc",
                                        "YPos": "abc",
                                        "ImageTemplate": {
                                            "Width": "abc",
                                            "Height": "abc",
                                            "RepeatType": "abc"
                                        }
                                    },
                                    "TextContent": "abc",
                                    "SvgContent": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "OutputObjectPath": "abc",
                            "ObjectNumberFormat": {
                                "InitialValue": 1,
                                "Increment": 1,
                                "MinLength": 1,
                                "PlaceHolder": "abc"
                            }
                        }
                    ],
                    "ImageSpriteTaskSet": [
                        {
                            "Definition": 1,
                            "OutputObjectPath": "abc",
                            "WebVttObjectName": "abc"
                        }
                    ],
                    "AdaptiveDynamicStreamingTaskSet": [
                        {
                            "Definition": 1,
                            "WatermarkSet": [
                                {
                                    "Definition": 1,
                                    "RawParameter": {
                                        "Type": "abc",
                                        "CoordinateOrigin": "abc",
                                        "XPos": "abc",
                                        "YPos": "abc",
                                        "ImageTemplate": {
                                            "ImageContent": {
                                                "Type": "abc",
                                                "CosInputInfo": {
                                                    "Bucket": "abc",
                                                    "Region": "abc",
                                                    "Object": "abc"
                                                },
                                                "UrlInputInfo": {
                                                    "Url": "abc"
                                                },
                                                "S3InputInfo": {
                                                    "S3Bucket": "abc",
                                                    "S3Region": "abc",
                                                    "S3Object": "abc",
                                                    "S3SecretId": "abc",
                                                    "S3SecretKey": "abc"
                                                }
                                            },
                                            "Width": "abc",
                                            "Height": "abc",
                                            "RepeatType": "abc"
                                        }
                                    },
                                    "TextContent": "abc",
                                    "SvgContent": "abc",
                                    "StartTimeOffset": 0,
                                    "EndTimeOffset": 0
                                }
                            ],
                            "OutputStorage": {
                                "Type": "abc",
                                "CosOutputStorage": {
                                    "Bucket": "abc",
                                    "Region": "abc"
                                },
                                "S3OutputStorage": {
                                    "S3Bucket": "abc",
                                    "S3Region": "abc",
                                    "S3SecretId": "abc",
                                    "S3SecretKey": "abc"
                                }
                            },
                            "OutputObjectPath": "abc",
                            "SubStreamObjectName": "abc",
                            "SegmentObjectName": "abc",
                            "AddOnSubtitles": [
                                {
                                    "Type": "abc"
                                }
                            ],
                            "DrmInfo": {
                                "Type": "abc",
                                "SimpleAesDrm": {
                                    "Uri": "abc",
                                    "Key": "abc",
                                    "Vector": "abc"
                                }
                            },
                            "DefinitionType": "abc"
                        }
                    ]
                },
                "AiContentReviewTask": {
                    "Definition": 1
                },
                "AiAnalysisTask": {
                    "Definition": 1,
                    "ExtendedParameter": "abc"
                },
                "AiRecognitionTask": {
                    "Definition": 1
                },
                "TaskNotifyConfig": {
                    "NotifyType": "abc",
                    "NotifyMode": "abc",
                    "NotifyUrl": "abc",
                    "CmqModel": "abc",
                    "CmqRegion": "abc",
                    "TopicName": "abc",
                    "QueueName": "abc",
                    "AwsSQS": {
                        "SQSRegion": "abc",
                        "SQSQueueName": "abc",
                        "S3SecretId": "abc",
                        "S3SecretKey": "abc"
                    },
                    "NotifyKey": "abc"
                },
                "TaskPriority": 0,
                "OutputDir": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

