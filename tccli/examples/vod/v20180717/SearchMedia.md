**Example 1: 根据推流直播码搜索一定时间范围内的录制文件，并且按创建时间降序排序**

搜索直播码为 StreamId_test1 和 StreamId_test2 、创建时间在 2020-12-10T07:25:52Z 到 2020-12-13T07:25:52Z 之间的录制文件，按创建时间进行降序排序，只返回符合条件的第一个文件。

Input: 

```
tccli vod SearchMedia --cli-unfold-argument  \
    --Sort.Field CreateTime \
    --Sort.Order Desc \
    --StreamIds StreamId_test2 StreamId_test1 \
    --Limit 1 \
    --SourceTypes Record \
    --Offset 0 \
    --CreateTime.After 2020-12-10T07:25:52Z \
    --CreateTime.Before 2020-12-13T07:25:52Z
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TotalCount": 1,
        "MediaInfoSet": [
            {
                "FileId": "5285485487985271487",
                "BasicInfo": {
                    "Name": "Sport file",
                    "Description": "",
                    "CreateTime": "2020-12-11T07:25:52Z",
                    "UpdateTime": "2020-12-11T07:25:52Z",
                    "ExpireTime": "9999-12-31T23:59:59Z",
                    "ClassId": 123,
                    "ClassName": "测试",
                    "ClassPath": "测试",
                    "CoverUrl": "http://xx.vod2.myqcloud.com/xxxxxxxx/shotup/f0.100_0.jpg",
                    "Type": "mp4",
                    "MediaUrl": "http://xx.vod2.myqcloud.com/xxx/xx/f0.mp4",
                    "TagSet": [
                        "tag1",
                        "tag2"
                    ],
                    "SourceInfo": {
                        "SourceType": "Record",
                        "SourceContext": "",
                        "TrtcRecordInfo": {
                            "SdkAppId": 1,
                            "RoomId": "RoomId",
                            "TaskId": "TaskId",
                            "UserIds": [
                                "UserId"
                            ]
                        }
                    },
                    "StorageRegion": "ap-chongqing",
                    "Category": "Image",
                    "Vid": "5285485487985271487",
                    "Status": "Normal",
                    "StorageClass": "STANDARD"
                },
                "MetaData": {
                    "Size": 10556,
                    "Container": "m4a",
                    "Duration": 3601,
                    "Bitrate": 246035,
                    "Height": 480,
                    "Width": 640,
                    "Rotate": 0,
                    "VideoDuration": 3601,
                    "AudioDuration": 3601,
                    "Md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                    "VideoStreamSet": [
                        {
                            "Bitrate": 246000,
                            "Height": 480,
                            "Width": 640,
                            "Codec": "h264",
                            "Fps": 222,
                            "DynamicRangeInfo": {
                                "Type": "HDR",
                                "HDRType": "hdr10"
                            }
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 2794233,
                                    "Height": 1080,
                                    "Width": 1920,
                                    "Codec": "h264",
                                    "Fps": 24,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "SamplingRate": 44100,
                                    "Bitrate": 45822,
                                    "Codec": "aac"
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                "MiniProgramReviewInfo": {
                    "MiniProgramReviewList": [
                        {
                            "Url": "url",
                            "Definition": 0,
                            "ReviewResult": "Pass",
                            "ReviewSummary": [
                                {
                                    "Confidence": 0,
                                    "Type": "Porn",
                                    "Suggestion": "pass"
                                }
                            ],
                            "MetaData": {
                                "Rotate": 0,
                                "Container": "mp4",
                                "AudioDuration": 0,
                                "Md5": "md5",
                                "VideoStreamSet": [
                                    {
                                        "Width": 0,
                                        "Codec": "h264",
                                        "Bitrate": 0,
                                        "Fps": 0,
                                        "Height": 0,
                                        "DynamicRangeInfo": {
                                            "Type": "HDR",
                                            "HDRType": "hdr10"
                                        }
                                    }
                                ],
                                "Height": 0,
                                "VideoDuration": 0,
                                "Width": 0,
                                "Duration": 0,
                                "Size": 0,
                                "Bitrate": 0,
                                "AudioStreamSet": [
                                    {
                                        "SamplingRate": 0,
                                        "Codec": "h264",
                                        "Bitrate": 0
                                    }
                                ]
                            }
                        }
                    ]
                },
                "AdaptiveDynamicStreamingInfo": {
                    "AdaptiveDynamicStreamingSet": [
                        {
                            "DrmType": "drm",
                            "Definition": 0,
                            "Url": "url",
                            "Package": "HLS"
                        }
                    ]
                },
                "SubtitleInfo": {
                    "SubtitleSet": [
                        {
                            "Url": "url",
                            "Format": "vtt",
                            "Name": "name",
                            "Language": "cn",
                            "Id": "id"
                        }
                    ]
                }
            }
        ]
    }
}
```

**Example 2: 根据文件名字前缀搜索一定时间范围内的文件，并且按创建时间降序排序**

搜索文件名前缀为 Sport、创建时间在 2020-12-10T07:25:52Z 到 2020-12-13T07:25:52Z 之间的文件，并按创建时间进行降序排序。

Input: 

```
tccli vod SearchMedia --cli-unfold-argument  \
    --Sort.Field CreateTime \
    --Sort.Order Desc \
    --NamePrefixes Sport \
    --CreateTime.After 2020-12-10T07:25:52Z \
    --CreateTime.Before 2020-12-13T07:25:52Z
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TotalCount": 1,
        "MediaInfoSet": [
            {
                "FileId": "5285485487985271487",
                "BasicInfo": {
                    "Name": "Sport file",
                    "Description": "",
                    "CreateTime": "2020-12-11T07:25:52Z",
                    "UpdateTime": "2020-12-11T07:25:52Z",
                    "ExpireTime": "9999-12-31T23:59:59Z",
                    "ClassId": 123,
                    "ClassName": "测试",
                    "ClassPath": "测试",
                    "CoverUrl": "http://xx.vod2.myqcloud.com/xxxxxxxx/shotup/f0.100_0.jpg",
                    "Type": "mp4",
                    "MediaUrl": "http://xx.vod2.myqcloud.com/xxx/xx/f0.mp4",
                    "TagSet": [],
                    "SourceInfo": {
                        "SourceType": "Record",
                        "SourceContext": "",
                        "TrtcRecordInfo": {
                            "SdkAppId": 1,
                            "RoomId": "RoomId",
                            "TaskId": "TaskId",
                            "UserIds": [
                                "UserId"
                            ]
                        }
                    },
                    "StorageRegion": "ap-chongqing",
                    "Category": "Video",
                    "Vid": "5285485487985271487",
                    "Status": "Normal",
                    "StorageClass": "STANDARD"
                },
                "MetaData": {
                    "Size": 10556,
                    "Container": "m4a",
                    "Duration": 3601,
                    "Bitrate": 246035,
                    "Height": 480,
                    "Width": 640,
                    "Rotate": 0,
                    "VideoDuration": 3601,
                    "AudioDuration": 3601,
                    "Md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                    "VideoStreamSet": [
                        {
                            "Bitrate": 246000,
                            "Height": 480,
                            "Width": 640,
                            "Codec": "h264",
                            "Fps": 222,
                            "DynamicRangeInfo": {
                                "Type": "HDR",
                                "HDRType": "hdr10"
                            }
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 2794233,
                                    "Height": 1080,
                                    "Width": 1920,
                                    "Codec": "h264",
                                    "Fps": 24,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "SamplingRate": 44100,
                                    "Bitrate": 45822,
                                    "Codec": "aac"
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                "MiniProgramReviewInfo": {
                    "MiniProgramReviewList": [
                        {
                            "Url": "url",
                            "Definition": 0,
                            "ReviewResult": "Pass",
                            "ReviewSummary": [
                                {
                                    "Confidence": 0,
                                    "Type": "Porn",
                                    "Suggestion": "pass"
                                }
                            ],
                            "MetaData": {
                                "Rotate": 0,
                                "Container": "mp4",
                                "AudioDuration": 0,
                                "Md5": "md5",
                                "VideoStreamSet": [
                                    {
                                        "Width": 0,
                                        "Codec": "h264",
                                        "Bitrate": 0,
                                        "Fps": 0,
                                        "Height": 0,
                                        "DynamicRangeInfo": {
                                            "Type": "HDR",
                                            "HDRType": "hdr10"
                                        }
                                    }
                                ],
                                "Height": 0,
                                "VideoDuration": 0,
                                "Width": 0,
                                "Duration": 0,
                                "Size": 0,
                                "Bitrate": 0,
                                "AudioStreamSet": [
                                    {
                                        "SamplingRate": 0,
                                        "Codec": "h264",
                                        "Bitrate": 0
                                    }
                                ]
                            }
                        }
                    ]
                },
                "AdaptiveDynamicStreamingInfo": {
                    "AdaptiveDynamicStreamingSet": [
                        {
                            "DrmType": "drm",
                            "Definition": 0,
                            "Url": "url",
                            "Package": "HLS"
                        }
                    ]
                },
                "SubtitleInfo": {
                    "SubtitleSet": [
                        {
                            "Url": "url",
                            "Format": "vtt",
                            "Name": "name",
                            "Language": "cn",
                            "Id": "id"
                        }
                    ]
                }
            }
        ]
    }
}
```

**Example 3: 根据文件名字模糊搜索一定时间范围内的文件，并且按创建时间降序排序**

搜索文件名字与关键词 Sport 相匹配的、创建时间在 2020-12-10T07:25:52Z 到 2020-12-13T07:25:52Z 之间的文件，并按创建时间进行降序排序。

Input: 

```
tccli vod SearchMedia --cli-unfold-argument  \
    --Sort.Field CreateTime \
    --Sort.Order Desc \
    --Names Sport \
    --CreateTime.After 2020-12-10T07:25:52Z \
    --CreateTime.Before 2020-12-13T07:25:52Z
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TotalCount": 1,
        "MediaInfoSet": [
            {
                "FileId": "5285485487985271487",
                "BasicInfo": {
                    "Name": "Sport file",
                    "Description": "",
                    "CreateTime": "2020-12-11T07:25:52Z",
                    "UpdateTime": "2020-12-11T07:25:52Z",
                    "ExpireTime": "9999-12-31T23:59:59Z",
                    "ClassId": 123,
                    "ClassName": "测试",
                    "ClassPath": "测试",
                    "CoverUrl": "http://xx.vod2.myqcloud.com/xxxxxxxx/shotup/f0.100_0.jpg",
                    "Type": "mp4",
                    "MediaUrl": "http://xx.vod2.myqcloud.com/xxx/xx/f0.mp4",
                    "TagSet": [],
                    "SourceInfo": {
                        "SourceType": "Record",
                        "SourceContext": "",
                        "TrtcRecordInfo": {
                            "SdkAppId": 1,
                            "RoomId": "RoomId",
                            "TaskId": "TaskId",
                            "UserIds": [
                                "UserId"
                            ]
                        }
                    },
                    "StorageRegion": "ap-chongqing",
                    "Category": "Video",
                    "Vid": "5285485487985271487",
                    "Status": "Normal",
                    "StorageClass": "STANDARD"
                },
                "MetaData": {
                    "Size": 10556,
                    "Container": "m4a",
                    "Duration": 3601,
                    "Bitrate": 246035,
                    "Height": 480,
                    "Width": 640,
                    "Rotate": 0,
                    "VideoDuration": 3601,
                    "AudioDuration": 3601,
                    "Md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                    "VideoStreamSet": [
                        {
                            "Bitrate": 246000,
                            "Height": 480,
                            "Width": 640,
                            "Codec": "h264",
                            "Fps": 222,
                            "DynamicRangeInfo": {
                                "Type": "HDR",
                                "HDRType": "hdr10"
                            }
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 2794233,
                                    "Height": 1080,
                                    "Width": 1920,
                                    "Codec": "h264",
                                    "Fps": 24,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "SamplingRate": 44100,
                                    "Bitrate": 45822,
                                    "Codec": "aac"
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                "MiniProgramReviewInfo": {
                    "MiniProgramReviewList": [
                        {
                            "Url": "url",
                            "Definition": 0,
                            "ReviewResult": "Pass",
                            "ReviewSummary": [
                                {
                                    "Confidence": 0,
                                    "Type": "Porn",
                                    "Suggestion": "pass"
                                }
                            ],
                            "MetaData": {
                                "Rotate": 0,
                                "Container": "mp4",
                                "AudioDuration": 0,
                                "Md5": "md5",
                                "VideoStreamSet": [
                                    {
                                        "Width": 0,
                                        "Codec": "h264",
                                        "Bitrate": 0,
                                        "Fps": 0,
                                        "Height": 0,
                                        "DynamicRangeInfo": {
                                            "Type": "HDR",
                                            "HDRType": "hdr10"
                                        }
                                    }
                                ],
                                "Height": 0,
                                "VideoDuration": 0,
                                "Width": 0,
                                "Duration": 0,
                                "Size": 0,
                                "Bitrate": 0,
                                "AudioStreamSet": [
                                    {
                                        "SamplingRate": 0,
                                        "Codec": "h264",
                                        "Bitrate": 0
                                    }
                                ]
                            }
                        }
                    ]
                },
                "AdaptiveDynamicStreamingInfo": {
                    "AdaptiveDynamicStreamingSet": [
                        {
                            "DrmType": "drm",
                            "Definition": 0,
                            "Url": "url",
                            "Package": "HLS"
                        }
                    ]
                },
                "SubtitleInfo": {
                    "SubtitleSet": [
                        {
                            "Url": "url",
                            "Format": "vtt",
                            "Name": "name",
                            "Language": "cn",
                            "Id": "id"
                        }
                    ]
                }
            }
        ]
    }
}
```

**Example 4: 根据标签搜索一定时间范围内的上传文件，并且按创建时间降序排序**

搜索标签为 tag1 和 tag2 、创建时间在 2020-12-10T07:25:52Z 到 2020-12-13T07:25:52Z 之间的、文件来源为 Upload 的文件，并按创建时间进行降序排序。

Input: 

```
tccli vod SearchMedia --cli-unfold-argument  \
    --Sort.Field CreateTime \
    --Sort.Order Desc \
    --CreateTime.After 2020-12-10T07:25:52Z \
    --CreateTime.Before 2020-12-13T07:25:52Z \
    --SourceTypes Upload \
    --Tags tag2 tag1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TotalCount": 1,
        "MediaInfoSet": [
            {
                "FileId": "5285485487985271487",
                "BasicInfo": {
                    "Name": "Sport file",
                    "Description": "",
                    "CreateTime": "2020-12-11T07:25:52Z",
                    "UpdateTime": "2020-12-11T07:25:52Z",
                    "ExpireTime": "9999-12-31T23:59:59Z",
                    "ClassId": 123,
                    "ClassName": "测试",
                    "ClassPath": "测试",
                    "CoverUrl": "http://xx.vod2.myqcloud.com/xxxxxxxx/shotup/f0.100_0.jpg",
                    "Type": "mp4",
                    "MediaUrl": "http://xx.vod2.myqcloud.com/xxx/xx/f0.mp4",
                    "TagSet": [
                        "tag1",
                        "tag2"
                    ],
                    "SourceInfo": {
                        "SourceType": "Upload",
                        "SourceContext": "",
                        "TrtcRecordInfo": {
                            "SdkAppId": 1,
                            "RoomId": "RoomId",
                            "TaskId": "TaskId",
                            "UserIds": [
                                "UserId"
                            ]
                        }
                    },
                    "StorageRegion": "ap-chongqing",
                    "Category": "Video",
                    "Vid": "5285485487985271487",
                    "Status": "Normal",
                    "StorageClass": "STANDARD"
                },
                "MetaData": {
                    "Size": 10556,
                    "Container": "m4a",
                    "Duration": 3601.0,
                    "Bitrate": 246035,
                    "Height": 480,
                    "Width": 640,
                    "Rotate": 0,
                    "VideoDuration": 3601.0,
                    "AudioDuration": 3601.0,
                    "Md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                    "VideoStreamSet": [
                        {
                            "Bitrate": 246000,
                            "Height": 480,
                            "Width": 640,
                            "Codec": "h264",
                            "Fps": 222,
                            "DynamicRangeInfo": {
                                "Type": "HDR",
                                "HDRType": "hdr10"
                            }
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
                            "Duration": 3601.0,
                            "Size": 10502,
                            "Md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
                        },
                        {
                            "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/f0.f210.m3u8",
                            "Definition": 211,
                            "Bitrate": 563477,
                            "Height": 378,
                            "Width": 672,
                            "Container": "mov",
                            "Duration": 3601.0,
                            "Size": 10502,
                            "Md5": "b3ae6ed07d9bf4efeeb94ed2d37ff3e3",
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 246000,
                                    "Height": 480,
                                    "Width": 640,
                                    "Codec": "h264",
                                    "Fps": 222,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "Codec": "aac",
                                    "SamplingRate": 44100,
                                    "Bitrate": 35
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
                        },
                        {
                            "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/master_playlist.m3u8",
                            "Definition": 10000,
                            "Duration": 145.0,
                            "Size": 265,
                            "Bitrate": 2840055,
                            "Height": 1080,
                            "Width": 1920,
                            "Container": "hls,applehttp",
                            "Md5": "bfcf7c6f154b18890661f9e80b0731d0",
                            "VideoStreamSet": [
                                {
                                    "Bitrate": 2794233,
                                    "Height": 1080,
                                    "Width": 1920,
                                    "Codec": "h264",
                                    "Fps": 24,
                                    "DynamicRangeInfo": {
                                        "Type": "HDR",
                                        "HDRType": "hdr10"
                                    }
                                }
                            ],
                            "AudioStreamSet": [
                                {
                                    "SamplingRate": 44100,
                                    "Bitrate": 45822,
                                    "Codec": "aac"
                                }
                            ],
                            "DigitalWatermarkType": "None",
                            "CopyRightWatermarkText": "None"
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
                            "StartTimeOffset": 10.0,
                            "EndTimeOffset": 15.0
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
                                    "TimeOffset": 0.0,
                                    "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/snapshotByTime/xx1.jpg"
                                },
                                {
                                    "TimeOffset": 1000.0,
                                    "Url": "http://xxxx.vod2.myqcloud.com/xx/xx/snapshotByTime/xx2.jpg"
                                }
                            ]
                        }
                    ]
                },
                "KeyFrameDescInfo": {
                    "KeyFrameDescSet": [
                        {
                            "TimeOffset": 1.0,
                            "Content": "abc"
                        },
                        {
                            "TimeOffset": 100.0,
                            "Content": "def"
                        }
                    ]
                },
                "MiniProgramReviewInfo": {
                    "MiniProgramReviewList": [
                        {
                            "Url": "url",
                            "Definition": 0,
                            "ReviewResult": "Pass",
                            "ReviewSummary": [
                                {
                                    "Confidence": 0.0,
                                    "Type": "Porn",
                                    "Suggestion": "pass"
                                }
                            ],
                            "MetaData": {
                                "Rotate": 0,
                                "Container": "mp4",
                                "AudioDuration": 0.0,
                                "Md5": "md5",
                                "VideoStreamSet": [
                                    {
                                        "Width": 0,
                                        "Codec": "h264",
                                        "Bitrate": 0,
                                        "Fps": 0,
                                        "Height": 0,
                                        "DynamicRangeInfo": {
                                            "Type": "HDR",
                                            "HDRType": "hdr10"
                                        }
                                    }
                                ],
                                "Height": 0,
                                "VideoDuration": 0.0,
                                "Width": 0,
                                "Duration": 0.0,
                                "Size": 0,
                                "Bitrate": 0,
                                "AudioStreamSet": [
                                    {
                                        "SamplingRate": 0,
                                        "Codec": "h264",
                                        "Bitrate": 0
                                    }
                                ]
                            }
                        }
                    ]
                },
                "AdaptiveDynamicStreamingInfo": {
                    "AdaptiveDynamicStreamingSet": [
                        {
                            "DrmType": "drm",
                            "Definition": 0,
                            "Url": "url",
                            "Package": "HLS"
                        }
                    ]
                },
                "SubtitleInfo": {
                    "SubtitleSet": [
                        {
                            "Url": "url",
                            "Format": "vtt",
                            "Name": "name",
                            "Language": "cn",
                            "Id": "id"
                        }
                    ]
                }
            }
        ]
    }
}
```

**Example 5: 根据分类搜索一定时间范围内的图片文件，并只返回文件基础信息，并且按创建时间降序排序**

搜索 ClassId 为123、创建时间在 2020-12-10T07:25:52Z 到 2020-12-13T07:25:52Z 之间的图片文件，按创建时间进行降序排序，并且只返回文件的基础信息。

Input: 

```
tccli vod SearchMedia --cli-unfold-argument  \
    --Sort.Field CreateTime \
    --Sort.Order Desc \
    --Filters basicInfo \
    --Categories Image \
    --ClassIds 123 \
    --CreateTime.After 2020-12-10T07:25:52Z \
    --CreateTime.Before 2020-12-13T07:25:52Z
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TotalCount": 2,
        "MediaInfoSet": [
            {
                "FileId": "5285890811175706012",
                "BasicInfo": {
                    "Name": "雾",
                    "Description": "",
                    "CreateTime": "2020-12-11T07:02:36Z",
                    "UpdateTime": "2020-12-11T07:02:37Z",
                    "ExpireTime": "9999-12-31T23:59:59Z",
                    "ClassId": 123,
                    "ClassName": "图标",
                    "ClassPath": "图标",
                    "CoverUrl": "",
                    "Type": "png",
                    "MediaUrl": "http://xxx.com/Tmf3xphxGoUA.png",
                    "TagSet": [],
                    "StorageRegion": "ap-shanghai",
                    "SourceInfo": {
                        "SourceType": "Upload",
                        "SourceContext": "",
                        "TrtcRecordInfo": {
                            "SdkAppId": 1,
                            "RoomId": "RoomId",
                            "TaskId": "TaskId",
                            "UserIds": [
                                "UserId"
                            ]
                        }
                    },
                    "Vid": "5285890811175706012",
                    "Category": "Image",
                    "Status": "Normal",
                    "StorageClass": "STANDARD"
                },
                "SubtitleInfo": {
                    "SubtitleSet": [
                        {
                            "Url": "url",
                            "Format": "vtt",
                            "Name": "name",
                            "Language": "cn",
                            "Id": "id"
                        }
                    ]
                },
                "MetaData": null,
                "TranscodeInfo": null,
                "AnimatedGraphicsInfo": null,
                "SampleSnapshotInfo": null,
                "ImageSpriteInfo": null,
                "SnapshotByTimeOffsetInfo": null,
                "KeyFrameDescInfo": null,
                "AdaptiveDynamicStreamingInfo": null,
                "MiniProgramReviewInfo": null
            },
            {
                "FileId": "5285890811175698692",
                "BasicInfo": {
                    "Name": "多云",
                    "Description": "",
                    "CreateTime": "2020-12-11T07:02:35Z",
                    "UpdateTime": "2020-12-11T07:02:36Z",
                    "ExpireTime": "9999-12-31T23:59:59Z",
                    "ClassId": 737598,
                    "ClassName": "图标",
                    "ClassPath": "图标",
                    "CoverUrl": "",
                    "Type": "png",
                    "MediaUrl": "http://xxx/uAgVpElena0A.png",
                    "TagSet": [],
                    "StorageRegion": "ap-shanghai",
                    "SourceInfo": {
                        "SourceType": "Upload",
                        "SourceContext": "",
                        "TrtcRecordInfo": {
                            "SdkAppId": 1,
                            "RoomId": "RoomId",
                            "TaskId": "TaskId",
                            "UserIds": [
                                "UserId"
                            ]
                        }
                    },
                    "Vid": "5285890811175698692",
                    "Category": "Image",
                    "Status": "Normal",
                    "StorageClass": "STANDARD"
                },
                "SubtitleInfo": {
                    "SubtitleSet": [
                        {
                            "Url": "url",
                            "Format": "vtt",
                            "Name": "name",
                            "Language": "cn",
                            "Id": "id"
                        }
                    ]
                },
                "MetaData": null,
                "TranscodeInfo": null,
                "AnimatedGraphicsInfo": null,
                "SampleSnapshotInfo": null,
                "ImageSpriteInfo": null,
                "SnapshotByTimeOffsetInfo": null,
                "KeyFrameDescInfo": null,
                "AdaptiveDynamicStreamingInfo": null,
                "MiniProgramReviewInfo": null
            }
        ]
    }
}
```

