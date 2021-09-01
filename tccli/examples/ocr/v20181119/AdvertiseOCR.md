**Example 1: 通用印刷体识别示例代码 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=AdvertiseOCR)**



Input: 

```
tccli ocr AdvertiseOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "DetectedText": "Confetteria",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 450,
                        "Y": 211
                    },
                    {
                        "X": 560,
                        "Y": 223
                    },
                    {
                        "X": 558,
                        "Y": 244
                    },
                    {
                        "X": 448,
                        "Y": 232
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}"
            },
            {
                "DetectedText": "Raffaello",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 370,
                        "Y": 233
                    },
                    {
                        "X": 649,
                        "Y": 265
                    },
                    {
                        "X": 642,
                        "Y": 331
                    },
                    {
                        "X": 362,
                        "Y": 299
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}"
            },
            {
                "DetectedText": "费列罗臻点坊",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 402,
                        "Y": 318
                    },
                    {
                        "X": 587,
                        "Y": 339
                    },
                    {
                        "X": 584,
                        "Y": 370
                    },
                    {
                        "X": 398,
                        "Y": 349
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
            },
            {
                "DetectedText": "拉斐尔脆雪柔",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 386,
                        "Y": 366
                    },
                    {
                        "X": 591,
                        "Y": 390
                    },
                    {
                        "X": 587,
                        "Y": 423
                    },
                    {
                        "X": 382,
                        "Y": 399
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}"
            }
        ],
        "RequestId": "03e66873-5209-4d26-abee-c4acd66fab91"
    }
}
```

