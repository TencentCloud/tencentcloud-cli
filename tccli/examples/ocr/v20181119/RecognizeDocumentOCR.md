**Example 1: 办公文档还原示例代码 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=RecognizeDocumentOCR))**



Input: 

```
tccli ocr RecognizeDocumentOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "ImageContent": [
            "xx"
        ],
        "ItemContent": [
            {
                "Confidence": 99,
                "Polygon": [
                    {
                        "Y": 518,
                        "X": 230
                    },
                    {
                        "Y": 518,
                        "X": 291
                    },
                    {
                        "Y": 536,
                        "X": 291
                    },
                    {
                        "Y": 536,
                        "X": 230
                    }
                ],
                "ItemPolygon": {
                    "Y": 0,
                    "X": 0,
                    "Height": 0,
                    "Width": 0
                },
                "DetectedText": "xx",
                "Words": [
                    {
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ],
                        "Color": "",
                        "WordPolygon": {
                            "Y": 0,
                            "X": 0,
                            "Height": 0,
                            "Width": 0
                        },
                        "Character": "xx",
                        "FontAttribute": "xx",
                        "FontSize": 0
                    }
                ],
                "GroupID": 0,
                "ItemType": "xx"
            },
            {
                "Confidence": 99,
                "Polygon": [
                    {
                        "Y": 1078,
                        "X": 1017
                    },
                    {
                        "Y": 1078,
                        "X": 1049
                    },
                    {
                        "Y": 1090,
                        "X": 1049
                    },
                    {
                        "Y": 1090,
                        "X": 1017
                    }
                ],
                "ItemPolygon": {
                    "Y": 0,
                    "X": 0,
                    "Width": 0,
                    "Height": 0
                },
                "DetectedText": "xx",
                "Words": [
                    {
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ],
                        "Color": "",
                        "WordPolygon": {
                            "Y": 0,
                            "X": 0,
                            "Width": 0,
                            "Height": 0
                        },
                        "Character": "xx",
                        "FontAttribute": "xx",
                        "FontSize": 0
                    }
                ],
                "GroupID": 0,
                "ItemType": "xx"
            }
        ],
        "RequestId": "xx",
        "ElemContent": [
            {
                "Confidence": 0,
                "Polygon": [
                    {
                        "Y": 194,
                        "X": 156
                    },
                    {
                        "Y": 194,
                        "X": 1038
                    },
                    {
                        "Y": 564,
                        "X": 1038
                    },
                    {
                        "Y": 564,
                        "X": 156
                    }
                ],
                "ItemIDLists": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "TableContent": [
                    {
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ],
                        "ItemIDLists": [
                            0
                        ],
                        "ElemType": 0,
                        "CellIndex": [
                            0
                        ],
                        "Description": "xx"
                    }
                ],
                "ElemType": 1,
                "GroupID": 0
            },
            {
                "Confidence": 0,
                "Polygon": [
                    {
                        "Y": 568,
                        "X": 426
                    },
                    {
                        "Y": 568,
                        "X": 766
                    },
                    {
                        "Y": 589,
                        "X": 766
                    },
                    {
                        "Y": 589,
                        "X": 426
                    }
                ],
                "ItemIDLists": [
                    6
                ],
                "TableContent": [
                    {
                        "Confidence": 0,
                        "Description": "xx",
                        "ItemIDLists": [
                            0
                        ],
                        "ElemType": 0,
                        "CellIndex": [
                            0
                        ],
                        "Polygon": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ]
                    }
                ],
                "ElemType": 2,
                "GroupID": 0
            },
            {
                "Confidence": 0,
                "Polygon": [
                    {
                        "Y": 1192,
                        "X": 114
                    },
                    {
                        "Y": 1192,
                        "X": 575
                    },
                    {
                        "Y": 1363,
                        "X": 575
                    },
                    {
                        "Y": 1363,
                        "X": 114
                    }
                ],
                "ItemIDLists": [
                    0
                ],
                "TableContent": [
                    {
                        "Confidence": 100,
                        "Description": "xx",
                        "ItemIDLists": [
                            0
                        ],
                        "ElemType": 101,
                        "CellIndex": [
                            0,
                            0,
                            0,
                            0
                        ],
                        "Polygon": [
                            {
                                "Y": 1193,
                                "X": 137
                            },
                            {
                                "Y": 1193,
                                "X": 559
                            },
                            {
                                "Y": 1344,
                                "X": 559
                            },
                            {
                                "Y": 1344,
                                "X": 137
                            }
                        ]
                    }
                ],
                "ElemType": 3,
                "GroupID": 2
            }
        ]
    }
}
```

