**Example 1: 办公文档还原示例代码 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=RecognizeDocumentOCR))**

办公文档还原示例

Input: 

```
tccli ocr RecognizeDocumentOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "ImageContent": [],
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
                "DetectedText": "实验",
                "Words": [
                    {
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ],
                        "Color": "0A0A0A",
                        "WordPolygon": {
                            "Y": 0,
                            "X": 0,
                            "Height": 0,
                            "Width": 0
                        },
                        "Character": "实",
                        "FontAttribute": "__font__:报宋;__handwritting__:0;__midline__:0;__underline__:0",
                        "FontSize": 100
                    },
                    {
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ],
                        "Color": "0A0A0A",
                        "WordPolygon": {
                            "Y": 0,
                            "X": 0,
                            "Height": 0,
                            "Width": 0
                        },
                        "Character": "验",
                        "FontAttribute": "__font__:报宋;__handwritting__:0;__midline__:0;__underline__:0",
                        "FontSize": 100
                    }
                ],
                "GroupID": 0,
                "ItemType": "ti"
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
                "DetectedText": "章节",
                "Words": [
                    {
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ],
                        "Color": "0A0A0A",
                        "WordPolygon": {
                            "Y": 0,
                            "X": 0,
                            "Width": 0,
                            "Height": 0
                        },
                        "Character": "章",
                        "FontAttribute": "__font__:报宋;__handwritting__:0;__midline__:0;__underline__:0",
                        "FontSize": 100
                    },
                    {
                        "Confidence": 0,
                        "Polygon": [
                            {
                                "Y": 0,
                                "X": 0
                            }
                        ],
                        "Color": "0A0A0A",
                        "WordPolygon": {
                            "Y": 0,
                            "X": 0,
                            "Width": 0,
                            "Height": 0
                        },
                        "Character": "节",
                        "FontAttribute": "__font__:报宋;__handwritting__:0;__midline__:0;__underline__:0",
                        "FontSize": 100
                    }
                ],
                "GroupID": 0,
                "ItemType": "ti"
            }
        ],
        "RequestId": "8e6bfecf-ada0-425a-80f8-ff666dbae88f",
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
                "TableContent": [],
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
                "TableContent": [],
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
                "TableContent": [],
                "ElemType": 3,
                "GroupID": 2
            }
        ]
    }
}
```

