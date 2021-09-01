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
        "TextDetections": [
            {
                "DetectedText": "Confetteria ",
                "Confidence": 91,
                "ItemPolygon": {
                    "X": 472,
                    "Y": 275,
                    "Width": 118,
                    "Height": 21
                },
                "Polygon": [
                    {
                        "X": 449,
                        "Y": 214
                    },
                    {
                        "X": 566,
                        "Y": 227
                    },
                    {
                        "X": 563,
                        "Y": 247
                    },
                    {
                        "X": 447,
                        "Y": 234
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
            },
            {
                "DetectedText": "Raffaello",
                "Confidence": 98,
                "ItemPolygon": {
                    "X": 395,
                    "Y": 305,
                    "Width": 281,
                    "Height": 69
                },
                "Polygon": [
                    {
                        "X": 370,
                        "Y": 235
                    },
                    {
                        "X": 648,
                        "Y": 266
                    },
                    {
                        "X": 640,
                        "Y": 334
                    },
                    {
                        "X": 362,
                        "Y": 303
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
            },
            {
                "DetectedText": "费列罗臻点坊",
                "Confidence": 99,
                "ItemPolygon": {
                    "X": 434,
                    "Y": 382,
                    "Width": 191,
                    "Height": 35
                },
                "Polygon": [
                    {
                        "X": 400,
                        "Y": 316
                    },
                    {
                        "X": 589,
                        "Y": 337
                    },
                    {
                        "X": 585,
                        "Y": 371
                    },
                    {
                        "X": 396,
                        "Y": 350
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
            },
            {
                "DetectedText": "拉斐尔@脆雪柔",
                "Confidence": 90,
                "ItemPolygon": {
                    "X": 427,
                    "Y": 434,
                    "Width": 205,
                    "Height": 36
                },
                "Polygon": [
                    {
                        "X": 387,
                        "Y": 367
                    },
                    {
                        "X": 590,
                        "Y": 389
                    },
                    {
                        "X": 586,
                        "Y": 424
                    },
                    {
                        "X": 383,
                        "Y": 402
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
            }
        ],
        "Angel": 6.3359375,
        "RequestId": "f522dcec-f977-4497-a342-66680eb6aa6f"
    }
}
```

