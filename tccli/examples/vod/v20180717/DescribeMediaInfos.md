**Example 1: 获取媒体详细信息**

获取媒体全部信息，不指定 Filters。

Input: 

```
tccli vod DescribeMediaInfos --cli-unfold-argument  \
    --FileIds 5285485487985271488 5285485487985271487
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "MediaInfoSet": [
            {
                "FileId": "5285485487985271487",
                "BasicInfo": {
                    "Name": "test file",
                    "Description": "",
                    "CreateTime": "2017-01-23T07:25:52Z",
                    "UpdateTime": "2017-01-23T07:25:52Z",
                    "ExpireTime": "2017-03-23T07:25:52Z",
                    "ClassId": 1,
                    "ClassName": "测试",
                    "ClassPath": "测试",
                    "CoverUrl": "http://xx.vod2.myqcloud.com/xxxxxxxx/shotup/f0.100_0.jpg",
                    "Type": "mp4",
                    "MediaUrl": "http://xx.vod2.myqcloud.com/xx/xx/f0.mp4",
                    "TagSet": [],
                    "SourceInfo": {
                        "SourceType": "Record",
                        "SourceContext": "",
                        "TrtcRecordInfo": null
                    },
                    "Category": "Video",
                    "Vid": "",
                    "StorageClass": "STANDARD",
                    "StorageRegion": "gzp",
                    "Status": "Normal"
                },
                "MetaData": {
                    "AudioDuration": 3601,
                    "VideoDuration": 3601,
                    "Md5": "",
                    "Size": 10556,
                    "Container": "m4a",
                    "Duration": 3601,
                    "Bitrate": 246035,
                    "Height": 480,
                    "Width": 640,
                    "Rotate": 0,
                    "VideoStreamSet": [
                        {
                            "Bitrate": 246000,
                            "Height": 480,
                            "Width": 640,
                            "Codec": "h264",
                            "Fps": 222,
                            "DynamicRangeInfo": {}
                        }
                    ],
                    "AudioStreamSet": [
                        {
                            "Codec": "aac",
                            "SamplingRate": 44100,
                            "Bitrate": 35
                        }
                    ]
                },
                "TranscodeInfo": {
                    "TranscodeSet": [
                        {
                            "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/f0.mp4",
                            "Definition": 0,
                            "Bitrate": 563477,
                            "Height": 378,
                            "Width": 672,
                            "Container": "m4a",
                            "Duration": 3601,
                            "Size": 10502,
                            "Md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                            "DigitalWatermarkType": "None",
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {}
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ]
                        },
                        {
                            "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/f0.f210.m3u8",
                            "Definition": 211,
                            "Bitrate": 563477,
                            "Height": 378,
                            "Width": 672,
                            "Container": "mov",
                            "Duration": 3601,
                            "Size": 10502,
                            "Md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                            "DigitalWatermarkType": "None",
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {}
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ]
                        },
                        {
                            "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/master_playlist.m3u8",
                            "Definition": 10000,
                            "Duration": 145,
                            "Size": 265,
                            "Bitrate": 2840055,
                            "Height": 1080,
                            "Width": 1920,
                            "Container": "hls,applehttp",
                            "Md5": "bfcf7c6f154b18890661f9e80b0731d0",
                            "DigitalWatermarkType": "None",
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 2794233,
                                    "Height": 1080,
                                    "Width": 1920,
                                    "Codec": "h264",
                                    "Fps": 24,
                                    "DynamicRangeInfo": {}
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "SamplingRate": 44100,
                                    "Bitrate": 45822,
                                    "Codec": "aac"
                                }
                            ]
                        }
                    ]
                },
                "AnimatedGraphicsInfo": {
                    "AnimatedGraphicsSet": [
                        {
                            "Url": "http://125xx.vod2.myqcloud.com/xx/xx/f20000.gif",
                            "Definition": 20000,
                            "Container": "gif",
                            "Height": 480,
                            "Width": 640,
                            "Bitrate": 1000000,
                            "Size": 600000,
                            "Md5": "bfcf7c6f154b1842a661f9e80b07a1d0",
                            "StartTimeOffset": 10,
                            "EndTimeOffset": 15
                        }
                    ]
                },
                "SampleSnapshotInfo": {
                    "SampleSnapshotSet": [
                        {
                            "Definition": 10,
                            "SampleType": "percent",
                            "Interval": 10,
                            "ImageUrlSet": [
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx1.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx2.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx3.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx4.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx5.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx6.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx7.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx8.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx9.png",
                                "http://125xx.vod2.myqcloud.com/xx/xx/shotup/xx10.png"
                            ]
                        }
                    ]
                },
                "ImageSpriteInfo": {
                    "ImageSpriteSet": [
                        {
                            "Definition": 10,
                            "Height": 576,
                            "Width": 1024,
                            "TotalCount": 100,
                            "ImageUrlSet": [
                                "http://xx.vod2.myqcloud.com/xx/xx/imageSprite/xx.100_0.jpg"
                            ],
                            "WebVttUrl": "http://xx.vod2.myqcloud.com/xxxx/xxxx/imageSprite/xx.vtt"
                        }
                    ]
                },
                "SnapshotByTimeOffsetInfo": {
                    "SnapshotByTimeOffsetSet": [
                        {
                            "Definition": 10,
                            "PicInfoSet": [
                                {
                                    "TimeOffset": 0,
                                    "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/snapshotByTime/xx1.jpg"
                                },
                                {
                                    "TimeOffset": 1000,
                                    "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/snapshotByTime/xx2.jpg"
                                }
                            ]
                        }
                    ]
                },
                "MiniProgramReviewInfo": {
                    "MiniProgramReviewList": [
                        {
                            "Url": "http://xx.vod2.myqcloud.com/xx/xx/f0.mp4",
                            "Definition": 0,
                            "ReviewResult": "pass",
                            "ReviewSummary": [
                                {
                                    "Confidence": 0,
                                    "Type": "Porn",
                                    "Suggestion": "pass"
                                }
                            ],
                            "MetaData": {
                                "Rotate": 0,
                                "Container": "m4a",
                                "AudioDuration": 0,
                                "VideoDuration": 3601,
                                "Md5": "",
                                "VideoStreamSet": [
                                    {
                                        "Bitrate": 246000,
                                        "Height": 480,
                                        "Width": 640,
                                        "Codec": "h264",
                                        "Fps": 222,
                                        "DynamicRangeInfo": {}
                                    }
                                ],
                                "Bitrate": 563477,
                                "Height": 378,
                                "Width": 672,
                                "Duration": 3601,
                                "Size": 10502,
                                "AudioStreamSet": [
                                    {
                                        "Codec": "aac",
                                        "SamplingRate": 44100,
                                        "Bitrate": 35
                                    }
                                ]
                            }
                        }
                    ]
                },
                "AdaptiveDynamicStreamingInfo": {
                    "AdaptiveDynamicStreamingSet": [
                        {
                            "Definition": 0,
                            "Package": "HLS",
                            "DrmType": "None",
                            "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/master_playlist.m3u8",
                            "Size": 0
                        }
                    ]
                },
                "KeyFrameDescInfo": {
                    "KeyFrameDescSet": [
                        {
                            "TimeOffset": 1,
                            "Content": "abc"
                        },
                        {
                            "TimeOffset": 100,
                            "Content": "def"
                        }
                    ]
                },
                "SubtitleInfo": {
                    "SubtitleSet": [
                        {
                            "Id": "subtitleId",
                            "Name": "English",
                            "Language": "en-US",
                            "Format": "vtt",
                            "Url": "http://123.vod2.myqcloud.com/vodgzp123/15517123183853310575/subtitles/subtitleId.vtt"
                        }
                    ]
                },
                "ReviewInfo": {
                    "MediaReviewInfo": {
                        "Definition": 10,
                        "Suggestion": "pass",
                        "TypeSet": [],
                        "ReviewTime": "2022-10-08T10:00:00Z"
                    },
                    "CoverReviewInfo": null
                }
            }
        ],
        "NotExistFileIdSet": [
            "5285485487985271488"
        ]
    }
}
```

**Example 2: 只获取媒体基础信息**

只获取媒体基础信息，Filters 指定 basicInfo。

Input: 

```
tccli vod DescribeMediaInfos --cli-unfold-argument  \
    --Filters basicInfo \
    --FileIds 5285485487985271488 5285485487985271487
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "MediaInfoSet": [
            {
                "FileId": "5285485487985271487",
                "BasicInfo": {
                    "Name": "test file",
                    "Description": "",
                    "CreateTime": "2017-01-23T07:25:52Z",
                    "UpdateTime": "2017-01-23T07:25:52Z",
                    "ExpireTime": "2017-03-23T07:25:52Z",
                    "ClassId": 1,
                    "ClassName": "测试",
                    "ClassPath": "测试",
                    "CoverUrl": "http://xx.vod2.myqcloud.com/xxxxxxxx/shotup/f0.100_0.jpg",
                    "Type": "mp4",
                    "MediaUrl": "http://xx.vod2.myqcloud.com/xx/xx/f0.mp4",
                    "TagSet": [],
                    "SourceInfo": {
                        "SourceType": "Record",
                        "SourceContext": "",
                        "TrtcRecordInfo": null
                    },
                    "Category": "Video",
                    "Vid": "",
                    "StorageClass": "STANDARD",
                    "StorageRegion": "gzp",
                    "Status": "Normal"
                },
                "MetaData": null,
                "TranscodeInfo": null,
                "AdaptiveDynamicStreamingInfo": null,
                "AnimatedGraphicsInfo": null,
                "SampleSnapshotInfo": null,
                "ImageSpriteInfo": null,
                "MiniProgramReviewInfo": null,
                "SubtitleInfo": null,
                "SnapshotByTimeOffsetInfo": null,
                "KeyFrameDescInfo": null,
                "ReviewInfo": null
            }
        ],
        "NotExistFileIdSet": [
            "5285485487985271488"
        ]
    }
}
```

