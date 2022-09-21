**Example 1: 描述任务与任务结果**



Input: 

```
tccli ivld DescribeTaskDetail --cli-unfold-argument  \
    --TaskId task-l0ae7t96
```

Output: 
```
{
    "Response": {
        "AudioTaskData": null,
        "ImageTaskData": null,
        "TextTaskData": null,
        "RequestId": "a18b2219-445f-43b9-b844-077d72ebcb85",
        "TaskData": {
            "ShowInfo": {
                "AudioInfoSet": [
                    {
                        "Content": "这是我一四年的一件作品，制作的运行是济南的一处职工宿舍楼，材料主要是泡沫板，木板完了指导制作，周期两个月时间。",
                        "EndTimeStamp": 51.882,
                        "StartTimeStamp": 0.36,
                        "Tag": ""
                    }
                ],
                "ClassifiedPersonInfoSet": [],
                "Column": "",
                "CoverImageURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4_2021-11-04T12:14:17/cover/show_g8rktHiE.jpg",
                "Date": "",
                "FrameTagSet": {
                    "AppearInfo": {
                        "AudioAppearSet": [],
                        "TextAppearSet": [],
                        "VideoAppearSet": [
                            {
                                "EndTimeStamp": 34.84,
                                "ImageURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4_2021-11-04T12:14:17/cover/lens_popjK1fY.jpg",
                                "StartTimeStamp": 32.56
                            },
                            {
                                "EndTimeStamp": 39.52,
                                "ImageURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4_2021-11-04T12:14:17/cover/lens_7Mu2jPLZ.jpg",
                                "StartTimeStamp": 34.88
                            },
                            {
                                "EndTimeStamp": 41.64,
                                "ImageURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4_2021-11-04T12:14:17/cover/lens_KHT2pnwl.jpg",
                                "StartTimeStamp": 39.56
                            },
                            {
                                "EndTimeStamp": 45.44,
                                "ImageURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4_2021-11-04T12:14:17/cover/lens_GGvu3x4d.jpg",
                                "StartTimeStamp": 41.68
                            },
                            {
                                "EndTimeStamp": 49.56,
                                "ImageURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4_2021-11-04T12:14:17/cover/lens_QAt3s6nW.jpg",
                                "StartTimeStamp": 45.48
                            },
                            {
                                "EndTimeStamp": 39.52,
                                "ImageURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4_2021-11-04T12:14:17/cover/lens_7Mu2jPLZ.jpg",
                                "StartTimeStamp": 34.88
                            },
                            {
                                "EndTimeStamp": 39.52,
                                "ImageURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4_2021-11-04T12:14:17/cover/lens_7Mu2jPLZ.jpg",
                                "StartTimeStamp": 34.88
                            }
                        ]
                    },
                    "TagSet": [
                        {
                            "AppearIndexPairSet": [],
                            "FirstAppear": 0,
                            "L2TagSet": [
                                {
                                    "AppearIndexPairSet": [],
                                    "FirstAppear": 0,
                                    "L3TagSet": [
                                        {
                                            "AppearIndexPairSet": [
                                                {
                                                    "AppearIndex": 3,
                                                    "Index": 0
                                                },
                                                {
                                                    "AppearIndex": 3,
                                                    "Index": 1
                                                },
                                                {
                                                    "AppearIndex": 3,
                                                    "Index": 2
                                                },
                                                {
                                                    "AppearIndex": 3,
                                                    "Index": 3
                                                },
                                                {
                                                    "AppearIndex": 3,
                                                    "Index": 4
                                                }
                                            ],
                                            "FirstAppear": 3,
                                            "Name": "建筑物"
                                        }
                                    ],
                                    "Name": "城市景观"
                                },
                                {
                                    "AppearIndexPairSet": [],
                                    "FirstAppear": 0,
                                    "L3TagSet": [
                                        {
                                            "AppearIndexPairSet": [
                                                {
                                                    "AppearIndex": 3,
                                                    "Index": 5
                                                }
                                            ],
                                            "FirstAppear": 3,
                                            "Name": "农村风貌"
                                        }
                                    ],
                                    "Name": "农业场景"
                                }
                            ],
                            "Name": "场景"
                        },
                        {
                            "AppearIndexPairSet": [],
                            "FirstAppear": 0,
                            "L2TagSet": [
                                {
                                    "AppearIndexPairSet": [],
                                    "FirstAppear": 0,
                                    "L3TagSet": [
                                        {
                                            "AppearIndexPairSet": [
                                                {
                                                    "AppearIndex": 3,
                                                    "Index": 6
                                                }
                                            ],
                                            "FirstAppear": 3,
                                            "Name": "自行车"
                                        }
                                    ],
                                    "Name": "陆地交通工具"
                                }
                            ],
                            "Name": "交通工具"
                        }
                    ]
                },
                "Logo": "",
                "MediaClassifierSet": [
                    "知识科普"
                ],
                "Source": "",
                "SummarySet": [],
                "SummaryTagSet": [],
                "TextInfoSet": [
                    {
                        "Content": "这是我2014年的一个作品",
                        "EndTimeStamp": 39.52,
                        "StartTimeStamp": 34.88,
                        "Tag": "字幕"
                    },
                    {
                        "Content": "制作的原型是济南的一处宿舍楼",
                        "EndTimeStamp": 39.52,
                        "StartTimeStamp": 34.88,
                        "Tag": "字幕"
                    },
                    {
                        "Content": "材料主要是泡沫板木板瓦楞制等",
                        "EndTimeStamp": 45.44,
                        "StartTimeStamp": 41.68,
                        "Tag": "字幕"
                    },
                    {
                        "Content": "制作周期2个月时间",
                        "EndTimeStamp": 49.56,
                        "StartTimeStamp": 45.48,
                        "Tag": "字幕"
                    }
                ],
                "TextTagSet": {
                    "AppearInfo": {
                        "AudioAppearSet": [
                            {
                                "EndPosition": 37,
                                "Index": 0,
                                "StartPosition": 34
                            },
                            {
                                "EndPosition": 28,
                                "Index": 0,
                                "StartPosition": 25
                            },
                            {
                                "EndPosition": 25,
                                "Index": 0,
                                "StartPosition": 23
                            },
                            {
                                "EndPosition": 20,
                                "Index": 0,
                                "StartPosition": 18
                            }
                        ],
                        "TextAppearSet": [],
                        "VideoAppearSet": []
                    },
                    "TagSet": [
                        {
                            "AppearIndexPairSet": [],
                            "FirstAppear": 0,
                            "L2TagSet": [
                                {
                                    "AppearIndexPairSet": [],
                                    "FirstAppear": 0,
                                    "L3TagSet": [
                                        {
                                            "AppearIndexPairSet": [
                                                {
                                                    "AppearIndex": 1,
                                                    "Index": 0
                                                }
                                            ],
                                            "FirstAppear": 1,
                                            "Name": "泡沫板"
                                        },
                                        {
                                            "AppearIndexPairSet": [
                                                {
                                                    "AppearIndex": 1,
                                                    "Index": 1
                                                }
                                            ],
                                            "FirstAppear": 1,
                                            "Name": "宿舍楼"
                                        }
                                    ],
                                    "Name": "关键词"
                                },
                                {
                                    "AppearIndexPairSet": [],
                                    "FirstAppear": 0,
                                    "L3TagSet": [
                                        {
                                            "AppearIndexPairSet": [
                                                {
                                                    "AppearIndex": 1,
                                                    "Index": 2
                                                }
                                            ],
                                            "FirstAppear": 1,
                                            "Name": "职工"
                                        }
                                    ],
                                    "Name": "身份职位"
                                },
                                {
                                    "AppearIndexPairSet": [],
                                    "FirstAppear": 0,
                                    "L3TagSet": [
                                        {
                                            "AppearIndexPairSet": [
                                                {
                                                    "AppearIndex": 1,
                                                    "Index": 3
                                                }
                                            ],
                                            "FirstAppear": 1,
                                            "Name": "济南"
                                        }
                                    ],
                                    "Name": "地点"
                                }
                            ],
                            "Name": ""
                        }
                    ]
                },
                "TitleSet": [],
                "WebMediaURL": "https://ai-media-251202827.cos.ap-guangzhou.myqcloud.com/%E6%98%9F%E8%A7%86%E9%A2%91.mp4"
            }
        },
        "TaskInfo": {
            "FailedReason": "",
            "MediaId": "media-tqakf1vs",
            "MediaName": "星视频",
            "MediaPreknownInfo": {
                "MediaLabel": 3,
                "MediaLang": 1,
                "MediaSecondLabel": 0,
                "MediaType": 2
            },
            "TaskCreateTime": "2021-11-04T12:14:17+08:00",
            "TaskId": "task-l0ae7t96",
            "TaskName": "",
            "TaskProgress": 0,
            "TaskStartTime": "2021-11-04T12:14:18+08:00",
            "TaskStatus": 8,
            "TaskTimeCost": 110,
            "CallbackURL": "xx",
            "Label": "xxx"
        }
    }
}
```

