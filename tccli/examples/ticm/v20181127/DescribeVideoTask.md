**Example 1: 查询视频审核任务的审核结果**



Input: 

```
tccli ticm DescribeVideoTask --cli-unfold-argument  \
    --VodTaskId 1254418846-procedurev2-62ba01a42e723df00a8807c84f728b54t0
```

Output: 
```
{
    "Response": {
        "PornResult": {
            "Confidence": 0,
            "Suggestion": "pass",
            "Label": "",
            "SegmentSet": [],
            "Code": 0,
            "Msg": "",
            "Status": "SUCCESS"
        },
        "TerrorismResult": {
            "Confidence": 0,
            "Suggestion": "pass",
            "Label": "",
            "SegmentSet": [],
            "Code": 0,
            "Msg": "",
            "Status": "SUCCESS"
        },
        "PoliticalResult": {
            "Confidence": 99,
            "Suggestion": "block",
            "Label": "violation_photo",
            "SegmentSet": [
                {
                    "StartTimeOffset": 1,
                    "EndTimeOffset": 35,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_1000.jpg",
                    "AreaCoordSet": [
                        533,
                        15,
                        572,
                        54
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                },
                {
                    "StartTimeOffset": 37,
                    "EndTimeOffset": 37,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_37000.jpg",
                    "AreaCoordSet": [
                        536,
                        18,
                        572,
                        53
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                },
                {
                    "StartTimeOffset": 38,
                    "EndTimeOffset": 73,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_38000.jpg",
                    "AreaCoordSet": [
                        532,
                        15,
                        572,
                        53
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                },
                {
                    "StartTimeOffset": 74,
                    "EndTimeOffset": 74,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_74000.jpg",
                    "AreaCoordSet": [
                        536,
                        16,
                        572,
                        52
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                },
                {
                    "StartTimeOffset": 75,
                    "EndTimeOffset": 90,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_75000.jpg",
                    "AreaCoordSet": [
                        533,
                        15,
                        572,
                        54
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                },
                {
                    "StartTimeOffset": 93,
                    "EndTimeOffset": 94,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_93000.jpg",
                    "AreaCoordSet": [
                        535,
                        17,
                        572,
                        54
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                },
                {
                    "StartTimeOffset": 97,
                    "EndTimeOffset": 99,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_97000.jpg",
                    "AreaCoordSet": [
                        533,
                        15,
                        572,
                        54
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                },
                {
                    "StartTimeOffset": 100,
                    "EndTimeOffset": 106,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_100000.jpg",
                    "AreaCoordSet": [
                        535,
                        17,
                        572,
                        54
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                },
                {
                    "StartTimeOffset": 107,
                    "EndTimeOffset": 117,
                    "Confidence": 99,
                    "Suggestion": "block",
                    "Name": "新唐人",
                    "Label": "violation_photo",
                    "Url": "http://251000800.vod2.myqcloud.com/1a168d62vodcq251000800/3eb99a035285890789088951756/645416944_107000.jpg",
                    "AreaCoordSet": [
                        533,
                        15,
                        572,
                        54
                    ],
                    "PicUrlExpireTimeStamp": 1558425271
                }
            ],
            "Code": 0,
            "Msg": "",
            "Status": "SUCCESS"
        },
        "PoliticalOcrResult": {
            "Confidence": 100,
            "Suggestion": "block",
            "SegmentSet": [
                {
                    "StartTimeOffset": 1,
                    "EndTimeOffset": 1,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 3,
                    "EndTimeOffset": 3,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 9,
                    "EndTimeOffset": 9,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 10,
                    "EndTimeOffset": 10,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 41,
                    "EndTimeOffset": 41,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 42,
                    "EndTimeOffset": 42,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 43,
                    "EndTimeOffset": 43,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 44,
                    "EndTimeOffset": 44,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 45,
                    "EndTimeOffset": 45,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 46,
                    "EndTimeOffset": 46,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 47,
                    "EndTimeOffset": 47,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 48,
                    "EndTimeOffset": 48,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 75,
                    "EndTimeOffset": 75,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 76,
                    "EndTimeOffset": 76,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 77,
                    "EndTimeOffset": 77,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 78,
                    "EndTimeOffset": 78,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 79,
                    "EndTimeOffset": 79,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 86,
                    "EndTimeOffset": 86,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 87,
                    "EndTimeOffset": 87,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 97,
                    "EndTimeOffset": 97,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 98,
                    "EndTimeOffset": 98,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 99,
                    "EndTimeOffset": 99,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        254,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 114,
                    "EndTimeOffset": 114,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 115,
                    "EndTimeOffset": 115,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 116,
                    "EndTimeOffset": 116,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                },
                {
                    "StartTimeOffset": 117,
                    "EndTimeOffset": 117,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "中國禁聞"
                    ],
                    "AreaCoordSet": [
                        113,
                        258,
                        228,
                        290
                    ]
                }
            ],
            "Code": 0,
            "Msg": "",
            "Status": "SUCCESS"
        },
        "PornOcrResult": {
            "Confidence": 0,
            "Suggestion": "pass",
            "SegmentSet": [],
            "Code": 0,
            "Msg": "",
            "Status": "SUCCESS"
        },
        "PornAsrResult": {
            "Confidence": 0,
            "Suggestion": "pass",
            "SegmentSet": [],
            "Code": 0,
            "Msg": "",
            "Status": "SUCCESS"
        },
        "PoliticalAsrResult": {
            "Confidence": 100,
            "Suggestion": "block",
            "SegmentSet": [
                {
                    "StartTimeOffset": 3.53,
                    "EndTimeOffset": 8.28,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "法轮功"
                    ]
                },
                {
                    "StartTimeOffset": 25.85,
                    "EndTimeOffset": 32.3,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "法轮功"
                    ]
                },
                {
                    "StartTimeOffset": 35.6,
                    "EndTimeOffset": 40.73,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "法轮功"
                    ]
                },
                {
                    "StartTimeOffset": 51.72,
                    "EndTimeOffset": 55.75,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "法轮功"
                    ]
                },
                {
                    "StartTimeOffset": 59.28,
                    "EndTimeOffset": 65.17,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "法轮功"
                    ]
                },
                {
                    "StartTimeOffset": 69.36,
                    "EndTimeOffset": 70.79,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "法轮功"
                    ]
                },
                {
                    "StartTimeOffset": 73.96,
                    "EndTimeOffset": 77.67,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "法轮功"
                    ]
                },
                {
                    "StartTimeOffset": 91.09,
                    "EndTimeOffset": 96.61,
                    "Confidence": 100,
                    "Suggestion": "block",
                    "KeywordSet": [
                        "法轮功"
                    ]
                }
            ],
            "Code": 0,
            "Msg": "",
            "Status": "SUCCESS"
        },
        "Status": "FINISH",
        "BeginProcessTime": "2019-05-14T07:53:40Z",
        "FinishTime": "2019-05-14T07:54:32Z",
        "RequestId": "02f1733c-1bfe-49ed-9e72-8ecd6ba058dd"
    }
}
```

