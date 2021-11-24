**Example 1: 通用印刷体识别（精简版）示例代码 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=GeneralEfficientOCR)**



Input: 

```
tccli ocr GeneralEfficientOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Angel": 0,
        "RequestId": "389c588f-ae23-42f9-a34c-c5dfafc8fdd1",
        "TextDetections": [
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                "Confidence": 99,
                "DetectedText": "Sun",
                "ItemPolygon": {
                    "Height": 35,
                    "Width": 71,
                    "X": 467,
                    "Y": 104
                },
                "Polygon": [
                    {
                        "X": 467,
                        "Y": 104
                    },
                    {
                        "X": 537,
                        "Y": 104
                    },
                    {
                        "X": 537,
                        "Y": 138
                    },
                    {
                        "X": 467,
                        "Y": 138
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                "Confidence": 99,
                "DetectedText": "1月8日",
                "ItemPolygon": {
                    "Height": 19,
                    "Width": 55,
                    "X": 474,
                    "Y": 142
                },
                "Polygon": [
                    {
                        "X": 474,
                        "Y": 142
                    },
                    {
                        "X": 528,
                        "Y": 142
                    },
                    {
                        "X": 528,
                        "Y": 160
                    },
                    {
                        "X": 474,
                        "Y": 160
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}",
                "Confidence": 99,
                "DetectedText": "八色鸫",
                "ItemPolygon": {
                    "Height": 29,
                    "Width": 81,
                    "X": 66,
                    "Y": 443
                },
                "Polygon": [
                    {
                        "X": 66,
                        "Y": 443
                    },
                    {
                        "X": 146,
                        "Y": 443
                    },
                    {
                        "X": 146,
                        "Y": 471
                    },
                    {
                        "X": 66,
                        "Y": 471
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}",
                "Confidence": 86,
                "DetectedText": "Pilta nympha",
                "ItemPolygon": {
                    "Height": 19,
                    "Width": 95,
                    "X": 63,
                    "Y": 482
                },
                "Polygon": [
                    {
                        "X": 63,
                        "Y": 482
                    },
                    {
                        "X": 157,
                        "Y": 482
                    },
                    {
                        "X": 157,
                        "Y": 500
                    },
                    {
                        "X": 63,
                        "Y": 500
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 93,
                "DetectedText": "八色鸫雌鸟和雄鸟样漂亮。它经常在亚热带的森林地面上走动,捕",
                "ItemPolygon": {
                    "Height": 20,
                    "Width": 424,
                    "X": 63,
                    "Y": 505
                },
                "Polygon": [
                    {
                        "X": 63,
                        "Y": 505
                    },
                    {
                        "X": 486,
                        "Y": 505
                    },
                    {
                        "X": 486,
                        "Y": 524
                    },
                    {
                        "X": 63,
                        "Y": 524
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 98,
                "DetectedText": "食落叶下的昆虫和蜥蜴等小动物，唱歌时会飞到树上。因为森林砍伐",
                "ItemPolygon": {
                    "Height": 20,
                    "Width": 426,
                    "X": 61,
                    "Y": 529
                },
                "Polygon": [
                    {
                        "X": 61,
                        "Y": 529
                    },
                    {
                        "X": 486,
                        "Y": 529
                    },
                    {
                        "X": 486,
                        "Y": 548
                    },
                    {
                        "X": 61,
                        "Y": 548
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 98,
                "DetectedText": "和非法的玩赏鸟贸易，现在它的数量已明显减少。",
                "ItemPolygon": {
                    "Height": 18,
                    "Width": 309,
                    "X": 59,
                    "Y": 555
                },
                "Polygon": [
                    {
                        "X": 59,
                        "Y": 555
                    },
                    {
                        "X": 367,
                        "Y": 555
                    },
                    {
                        "X": 367,
                        "Y": 572
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

