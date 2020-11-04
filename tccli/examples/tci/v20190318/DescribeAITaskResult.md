**Example 1: 获取 AI 助教结果**

获取 AI 助教分析后的结果

Input: 

```
tccli tci DescribeAITaskResult --cli-unfold-argument  \
    --TaskId 2516205217
```

Output: 
```
{
    "Response": {
        "TaskId": 2516205217,
        "RequestId": "885661be-0fc8-47c2-b1af-3ff1d6a54ecd",
        "ImageResult": {
            "Status": "",
            "Message": "",
            "TotalCount": 153,
            "ResultSet": [
                {
                    "FaceIdentify": null,
                    "FaceInfo": {
                        "Left": 0,
                        "Top": 0,
                        "Width": 0,
                        "Height": 0,
                        "FrameWidth": 0,
                        "FrameHeight": 0,
                        "FaceRatio": 0
                    },
                    "FacePose": {
                        "Direction": "frontal",
                        "Yaw": -0.29673076,
                        "Pitch": 9.21381,
                        "Roll": -0.82792795
                    },
                    "FaceAttr": {
                        "Sex": "female",
                        "Age": 23
                    },
                    "FaceExpression": {
                        "Expression": "neutral",
                        "Confidence": 0.6842983
                    },
                    "HandTracking": null,
                    "Gesture": null,
                    "TeacherBodyMovement": null,
                    "StudentBodyMovement": null,
                    "Light": null,
                    "TimeInfo": {
                        "StartTs": 200,
                        "EndTs": 200,
                        "Duration": 0
                    },
                    "ActionInfo": null
                }
            ],
            "Statistic": {
                "FaceIdentify": [
                    {
                        "PersonId": "tci_person_1561445819427009841231",
                        "Similarity": 0.9951723,
                        "StartTs": 200,
                        "EndTs": 4800,
                        "Duration": 5600
                    }
                ],
                "FaceExpression": [
                    {
                        "PersonId": "tci_person_1561445819427009841231",
                        "ExpressRatio": [
                            {
                                "Express": "neutral",
                                "Ratio": 0.80435,
                                "Count": 37
                            },
                            {
                                "Express": "surprise",
                                "Ratio": 0.19565,
                                "Count": 9
                            }
                        ]
                    }
                ],
                "Handtracking": null,
                "Gesture": null,
                "TeacherMovement": null,
                "StudentMovement": null,
                "Light": null
            }
        },
        "VideoResult": {
            "Status": "",
            "Message": "",
            "HighlightsInfo": [
                {
                    "HighlightsUrl": "http://videowonderful-1255701415.cos.ap-guangzhou.myqcloud.com/test/20190625_162809--ef_wonderful_20190625_162758_.mp4?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEOuBIhv4wHI2ChdxFbnngLxbrzpUGo8H%26q-sign-time%3D1561451290%3B1561451590%26q-key-time%3D1561451290%3B1561451590%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D154fba6daabaef5017849f6dd957cc8c67e3c8ed",
                    "Smile": [
                        {
                            "StartTime": 2000,
                            "EndTime": 17000
                        }
                    ],
                    "Concentration": null,
                    "PersonId": ""
                },
                {
                    "HighlightsUrl": "http://videowonderful-1255701415.cos.ap-guangzhou.myqcloud.com/test/20190625_162818--ef_wonderful_20190625_162758_tci_person_1561445819427009841231.mp4?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEOuBIhv4wHI2ChdxFbnngLxbrzpUGo8H%26q-sign-time%3D1561451299%3B1561451599%26q-key-time%3D1561451299%3B1561451599%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3Db2540e56515761565f11a9e608414a205d153c47",
                    "Smile": [
                        {
                            "StartTime": 6000,
                            "EndTime": 19000
                        }
                    ],
                    "Concentration": null,
                    "PersonId": "tci_person_1561445819427009841231"
                }
            ]
        },
        "AudioResult": {
            "Status": "",
            "Message": "",
            "TotalCount": 0,
            "Texts": [
                {
                    "TextItem": {
                        "Mbtm": 1790,
                        "Metm": 7120,
                        "Text": "He or she. ",
                        "TextSize": 11,
                        "Confidence": 0.030193144,
                        "Tag": 0,
                        "Words": [
                            {
                                "Mbtm": 2220,
                                "Metm": 2660,
                                "Text": "he",
                                "Wsize": 2,
                                "Confidence": 0
                            },
                            {
                                "Mbtm": 2940,
                                "Metm": 4180,
                                "Text": "or",
                                "Wsize": 2,
                                "Confidence": 0
                            },
                            {
                                "Mbtm": 4540,
                                "Metm": 5240,
                                "Text": "she",
                                "Wsize": 3,
                                "Confidence": 0
                            }
                        ]
                    },
                    "Speed": 0.750469,
                    "MaxVolume": 0,
                    "MinVolume": 0,
                    "AvgVolume": 0
                }
            ],
            "VocabAnalysisDetailInfo": null,
            "AsrStat": {
                "TotalDuration": 19820,
                "SoundDuration": 8250,
                "MuteDuration": 11570,
                "VadNum": 3,
                "WordNum": 5,
                "AvgSpeed": 0.6060606,
                "MaxVolume": 0,
                "MinVolume": 0,
                "AvgVolume": 0
            },
            "VocabAnalysisStatInfo": null
        }
    }
}
```

