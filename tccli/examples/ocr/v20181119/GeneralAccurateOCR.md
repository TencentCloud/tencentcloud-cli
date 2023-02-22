**Example 1: 通用印刷体识别（高精度版）示例代码 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=GeneralAccurateOCR)**

图像整体文字的检测和识别，返回文字框位置与文字内容

Input: 

```
tccli ocr GeneralAccurateOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Angel": 359.989990234375,
        "RequestId": "05441696-96fb-48a8-a445-49df03836fba",
        "TextDetections": [
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                "Confidence": 99,
                "DetectedText": "轻断食:正在横扫全球的瘦身革命",
                "ItemPolygon": {
                    "Height": 22,
                    "Width": 263,
                    "X": 446,
                    "Y": 93
                },
                "Polygon": [
                    {
                        "X": 446,
                        "Y": 93
                    },
                    {
                        "X": 709,
                        "Y": 96
                    },
                    {
                        "X": 708,
                        "Y": 118
                    },
                    {
                        "X": 446,
                        "Y": 114
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}",
                "Confidence": 99,
                "DetectedText": "专题报道。",
                "ItemPolygon": {
                    "Height": 25,
                    "Width": 100,
                    "X": 47,
                    "Y": 201
                },
                "Polygon": [
                    {
                        "X": 47,
                        "Y": 201
                    },
                    {
                        "X": 147,
                        "Y": 200
                    },
                    {
                        "X": 147,
                        "Y": 225
                    },
                    {
                        "X": 48,
                        "Y": 226
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}",
                "Confidence": 99,
                "DetectedText": "2009年，我写了 《减肥前要做的101件事》(101 Things to Do",
                "ItemPolygon": {
                    "Height": 27,
                    "Width": 628,
                    "X": 88,
                    "Y": 244
                },
                "Polygon": [
                    {
                        "X": 88,
                        "Y": 244
                    },
                    {
                        "X": 716,
                        "Y": 247
                    },
                    {
                        "X": 716,
                        "Y": 274
                    },
                    {
                        "X": 88,
                        "Y": 271
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}",
                "Confidence": 99,
                "DetectedText": "Before You Diet), 归纳我尝试各种流行减肥法的气馁经验， 每种方",
                "ItemPolygon": {
                    "Height": 27,
                    "Width": 675,
                    "X": 42,
                    "Y": 292
                },
                "Polygon": [
                    {
                        "X": 42,
                        "Y": 292
                    },
                    {
                        "X": 717,
                        "Y": 290
                    },
                    {
                        "X": 717,
                        "Y": 317
                    },
                    {
                        "X": 43,
                        "Y": 320
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}",
                "Confidence": 99,
                "DetectedText": "法似乎都注定失败。",
                "ItemPolygon": {
                    "Height": 25,
                    "Width": 192,
                    "X": 45,
                    "Y": 340
                },
                "Polygon": [
                    {
                        "X": 45,
                        "Y": 340
                    },
                    {
                        "X": 237,
                        "Y": 340
                    },
                    {
                        "X": 237,
                        "Y": 365
                    },
                    {
                        "X": 45,
                        "Y": 365
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 99,
                "DetectedText": "这二十年来我接触过的减肥方法中， 只有轻断食让我在瘦下来之 ",
                "ItemPolygon": {
                    "Height": 27,
                    "Width": 633,
                    "X": 88,
                    "Y": 384
                },
                "Polygon": [
                    {
                        "X": 88,
                        "Y": 384
                    },
                    {
                        "X": 721,
                        "Y": 384
                    },
                    {
                        "X": 721,
                        "Y": 411
                    },
                    {
                        "X": 88,
                        "Y": 411
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 99,
                "DetectedText": "后不反弹。",
                "ItemPolygon": {
                    "Height": 24,
                    "Width": 105,
                    "X": 42,
                    "Y": 435
                },
                "Polygon": [
                    {
                        "X": 42,
                        "Y": 435
                    },
                    {
                        "X": 147,
                        "Y": 433
                    },
                    {
                        "X": 148,
                        "Y": 457
                    },
                    {
                        "X": 43,
                        "Y": 460
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 96,
                "DetectedText": "至于抗衰老的健康益处，",
                "ItemPolygon": {
                    "Height": 24,
                    "Width": 250,
                    "X": 148,
                    "Y": 433
                },
                "Polygon": [
                    {
                        "X": 148,
                        "Y": 433
                    },
                    {
                        "X": 398,
                        "Y": 433
                    },
                    {
                        "X": 398,
                        "Y": 457
                    },
                    {
                        "X": 148,
                        "Y": 457
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 99,
                "DetectedText": "更是得来全不费工夫。",
                "ItemPolygon": {
                    "Height": 26,
                    "Width": 223,
                    "X": 398,
                    "Y": 431
                },
                "Polygon": [
                    {
                        "X": 398,
                        "Y": 431
                    },
                    {
                        "X": 621,
                        "Y": 431
                    },
                    {
                        "X": 621,
                        "Y": 457
                    },
                    {
                        "X": 398,
                        "Y": 457
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            }
        ]
    }
}
```

