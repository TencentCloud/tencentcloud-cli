**Example 1: 通用印刷体识别（高精度版）示例代码 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=GeneralAccurateOCR)**



Input: 

```
tccli ocr GeneralAccurateOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "AdvancedInfo": "xx",
                "Polygon": [
                    {
                        "Y": 231,
                        "X": 449
                    },
                    {
                        "Y": 211,
                        "X": 452
                    },
                    {
                        "Y": 227,
                        "X": 563
                    },
                    {
                        "Y": 247,
                        "X": 560
                    }
                ],
                "Confidence": 99,
                "ItemPolygon": {
                    "Y": 211,
                    "X": 449,
                    "Height": 37,
                    "Width": 115
                },
                "WordCoordPoint": [
                    {
                        "WordCoordinate": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ]
                    }
                ],
                "DetectedText": "xx",
                "Words": [
                    {
                        "Confidence": 0,
                        "Character": "xx"
                    }
                ]
            },
            {
                "AdvancedInfo": "xx",
                "Polygon": [
                    {
                        "Y": 308,
                        "X": 361
                    },
                    {
                        "Y": 242,
                        "X": 368
                    },
                    {
                        "Y": 271,
                        "X": 648
                    },
                    {
                        "Y": 338,
                        "X": 641
                    }
                ],
                "Confidence": 99,
                "ItemPolygon": {
                    "Y": 242,
                    "X": 361,
                    "Width": 288,
                    "Height": 97
                },
                "WordCoordPoint": [
                    {
                        "WordCoordinate": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ]
                    }
                ],
                "DetectedText": "xx",
                "Words": [
                    {
                        "Confidence": 0,
                        "Character": "xx"
                    }
                ]
            },
            {
                "AdvancedInfo": "xx",
                "Polygon": [
                    {
                        "Y": 349,
                        "X": 394
                    },
                    {
                        "Y": 316,
                        "X": 398
                    },
                    {
                        "Y": 337,
                        "X": 593
                    },
                    {
                        "Y": 371,
                        "X": 589
                    }
                ],
                "Confidence": 99,
                "ItemPolygon": {
                    "Y": 316,
                    "X": 394,
                    "Width": 200,
                    "Height": 56
                },
                "WordCoordPoint": [
                    {
                        "WordCoordinate": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ]
                    }
                ],
                "DetectedText": "xx",
                "Words": [
                    {
                        "Confidence": 0,
                        "Character": "xx"
                    }
                ]
            },
            {
                "AdvancedInfo": "xx",
                "Polygon": [
                    {
                        "Y": 401,
                        "X": 381
                    },
                    {
                        "Y": 368,
                        "X": 385
                    },
                    {
                        "Y": 389,
                        "X": 594
                    },
                    {
                        "Y": 422,
                        "X": 590
                    }
                ],
                "Confidence": 98,
                "ItemPolygon": {
                    "Y": 368,
                    "X": 381,
                    "Width": 214,
                    "Height": 55
                },
                "WordCoordPoint": [
                    {
                        "WordCoordinate": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ]
                    }
                ],
                "DetectedText": "xx",
                "Words": [
                    {
                        "Confidence": 0,
                        "Character": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx",
        "Angel": 0.0
    }
}
```

