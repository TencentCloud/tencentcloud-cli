**Example 1: 中英文手写**

中英文手写

Input: 

```
tccli ocr HandwritingEssayOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/SmartStructuralOCR/SmartStructuralPro1.png \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q== \
    --PdfPageNumber 1
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "RequestId": "40f4b618-406c-47ad-b83d-137b500d7c5d",
        "WordList": [
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1,\"ParagType\":0,\"DetectNo\":1}}",
                "Coord": {
                    "LeftBottom": {
                        "X": 282,
                        "Y": 122
                    },
                    "LeftTop": {
                        "X": 282,
                        "Y": 63
                    },
                    "RightBottom": {
                        "X": 860,
                        "Y": 122
                    },
                    "RightTop": {
                        "X": 860,
                        "Y": 63
                    }
                },
                "DetectedText": "自杨树，谢谢你教会了我",
                "WordCoord": [
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 282,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 282,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 334,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 334,
                                "Y": 63
                            }
                        },
                        "DetectedText": "自"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 334,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 334,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 387,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 387,
                                "Y": 63
                            }
                        },
                        "DetectedText": "杨"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 387,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 387,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 439,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 439,
                                "Y": 63
                            }
                        },
                        "DetectedText": "树"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 439,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 439,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 492,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 492,
                                "Y": 63
                            }
                        },
                        "DetectedText": "，"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 492,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 492,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 544,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 544,
                                "Y": 63
                            }
                        },
                        "DetectedText": "谢"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 544,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 544,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 597,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 597,
                                "Y": 63
                            }
                        },
                        "DetectedText": "谢"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 597,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 597,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 649,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 649,
                                "Y": 63
                            }
                        },
                        "DetectedText": "你"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 649,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 649,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 702,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 702,
                                "Y": 63
                            }
                        },
                        "DetectedText": "教"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 702,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 702,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 754,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 754,
                                "Y": 63
                            }
                        },
                        "DetectedText": "会"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 754,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 754,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 807,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 807,
                                "Y": 63
                            }
                        },
                        "DetectedText": "了"
                    },
                    {
                        "Coord": {
                            "LeftBottom": {
                                "X": 807,
                                "Y": 122
                            },
                            "LeftTop": {
                                "X": 807,
                                "Y": 63
                            },
                            "RightBottom": {
                                "X": 860,
                                "Y": 122
                            },
                            "RightTop": {
                                "X": 860,
                                "Y": 63
                            }
                        },
                        "DetectedText": "我"
                    }
                ]
            }
        ]
    }
}
```

