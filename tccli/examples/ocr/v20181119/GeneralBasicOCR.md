**Example 1: 通用印刷体识别示例代码 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=GeneralBasicOCR)**



Input: 

```
tccli ocr GeneralBasicOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Angel": 6.5,
        "TextDetections": [
            {
                "AdvancedInfo": "xx",
                "Polygon": [
                    {
                        "Y": 211,
                        "X": 450
                    },
                    {
                        "Y": 223,
                        "X": 560
                    },
                    {
                        "Y": 244,
                        "X": 558
                    },
                    {
                        "Y": 232,
                        "X": 448
                    }
                ],
                "Confidence": 99,
                "ItemPolygon": {
                    "Y": 273,
                    "X": 473,
                    "Height": 22,
                    "Width": 112
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
                        "Y": 233,
                        "X": 370
                    },
                    {
                        "Y": 265,
                        "X": 649
                    },
                    {
                        "Y": 331,
                        "X": 642
                    },
                    {
                        "Y": 299,
                        "X": 362
                    }
                ],
                "Confidence": 99,
                "ItemPolygon": {
                    "Y": 304,
                    "X": 396,
                    "Width": 282,
                    "Height": 68
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
                        "Y": 318,
                        "X": 402
                    },
                    {
                        "Y": 339,
                        "X": 587
                    },
                    {
                        "Y": 370,
                        "X": 584
                    },
                    {
                        "Y": 349,
                        "X": 398
                    }
                ],
                "Confidence": 99,
                "ItemPolygon": {
                    "Y": 385,
                    "X": 437,
                    "Width": 188,
                    "Height": 32
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
                        "Y": 366,
                        "X": 386
                    },
                    {
                        "Y": 390,
                        "X": 591
                    },
                    {
                        "Y": 423,
                        "X": 587
                    },
                    {
                        "Y": 399,
                        "X": 382
                    }
                ],
                "Confidence": 99,
                "ItemPolygon": {
                    "Y": 435,
                    "X": 427,
                    "Width": 207,
                    "Height": 34
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
        "Language": "xx",
        "PdfPageSize": 0
    }
}
```

