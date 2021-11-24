**Example 1: 通用印刷体识别（高速版）示例代码**



Input: 

```
tccli ocr GeneralFastOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Angel": 359.989990234375,
        "Language": "zh",
        "PdfPageSize": 0,
        "RequestId": "770d1ec1-9bbf-4ec3-876c-5b6b66fc5c8c",
        "TextDetections": [
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                "Confidence": 99,
                "DetectedText": "Sun",
                "ItemPolygon": {
                    "Height": 35,
                    "Width": 74,
                    "X": 464,
                    "Y": 100
                },
                "Polygon": [
                    {
                        "X": 464,
                        "Y": 100
                    },
                    {
                        "X": 538,
                        "Y": 100
                    },
                    {
                        "X": 538,
                        "Y": 135
                    },
                    {
                        "X": 464,
                        "Y": 135
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}",
                "Confidence": 99,
                "DetectedText": "1月8日",
                "ItemPolygon": {
                    "Height": 18,
                    "Width": 52,
                    "X": 476,
                    "Y": 141
                },
                "Polygon": [
                    {
                        "X": 476,
                        "Y": 141
                    },
                    {
                        "X": 528,
                        "Y": 141
                    },
                    {
                        "X": 528,
                        "Y": 159
                    },
                    {
                        "X": 476,
                        "Y": 159
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}",
                "Confidence": 99,
                "DetectedText": "八色鸫",
                "ItemPolygon": {
                    "Height": 28,
                    "Width": 85,
                    "X": 62,
                    "Y": 443
                },
                "Polygon": [
                    {
                        "X": 62,
                        "Y": 443
                    },
                    {
                        "X": 147,
                        "Y": 442
                    },
                    {
                        "X": 147,
                        "Y": 470
                    },
                    {
                        "X": 63,
                        "Y": 471
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 97,
                "DetectedText": "Pilta nympha",
                "ItemPolygon": {
                    "Height": 17,
                    "Width": 96,
                    "X": 61,
                    "Y": 482
                },
                "Polygon": [
                    {
                        "X": 61,
                        "Y": 482
                    },
                    {
                        "X": 157,
                        "Y": 483
                    },
                    {
                        "X": 157,
                        "Y": 500
                    },
                    {
                        "X": 61,
                        "Y": 499
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":5}}",
                "Confidence": 99,
                "DetectedText": "八色鸫雌鸟和雄鸟一样漂亮。它经常在亚热带的森林地面上走动,捕",
                "ItemPolygon": {
                    "Height": 18,
                    "Width": 426,
                    "X": 60,
                    "Y": 506
                },
                "Polygon": [
                    {
                        "X": 60,
                        "Y": 506
                    },
                    {
                        "X": 486,
                        "Y": 503
                    },
                    {
                        "X": 486,
                        "Y": 521
                    },
                    {
                        "X": 60,
                        "Y": 523
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":5}}",
                "Confidence": 99,
                "DetectedText": "食落叶下的昆虫和蜥蜴等小动物,唱歌时会飞到树上。因为森林砍伐",
                "ItemPolygon": {
                    "Height": 16,
                    "Width": 426,
                    "X": 60,
                    "Y": 530
                },
                "Polygon": [
                    {
                        "X": 60,
                        "Y": 530
                    },
                    {
                        "X": 486,
                        "Y": 530
                    },
                    {
                        "X": 486,
                        "Y": 546
                    },
                    {
                        "X": 60,
                        "Y": 546
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":5}}",
                "Confidence": 99,
                "DetectedText": "和非法的玩赏鸟贸易,现在它的数量已明显减少。",
                "ItemPolygon": {
                    "Height": 18,
                    "Width": 308,
                    "X": 59,
                    "Y": 554
                },
                "Polygon": [
                    {
                        "X": 59,
                        "Y": 554
                    },
                    {
                        "X": 367,
                        "Y": 552
                    },
                    {
                        "X": 368,
                        "Y": 570
                    },
                    {
                        "X": 59,
                        "Y": 572
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            }
        ]
    }
}
```

