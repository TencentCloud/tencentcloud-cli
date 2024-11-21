**Example 1: GeneralAccurateOCR调用**

图像整体文字的检测和识别，返回文字框位置与文字内容。 [ 前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Action=GeneralAccurateOCR)

Input: 

```
tccli ocr GeneralAccurateOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/GeneralAccurateOCR/GeneralAccurateOCR1.jpg
```

Output: 
```
{
    "Response": {
        "Angel": 359.989990234375,
        "Angle": 359.989990234375,
        "RequestId": "4021987a-5441-4160-981a-d084cd96b5ad",
        "TextDetections": [
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                "Confidence": 100,
                "DetectedText": "轻断食:正在横扫全球的瘦身革命",
                "ItemPolygon": {
                    "Height": 26,
                    "Width": 264,
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
                        "Y": 94
                    },
                    {
                        "X": 708,
                        "Y": 118
                    },
                    {
                        "X": 446,
                        "Y": 116
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}",
                "Confidence": 100,
                "DetectedText": "专题报道。",
                "ItemPolygon": {
                    "Height": 30,
                    "Width": 103,
                    "X": 47,
                    "Y": 198
                },
                "Polygon": [
                    {
                        "X": 47,
                        "Y": 201
                    },
                    {
                        "X": 148,
                        "Y": 198
                    },
                    {
                        "X": 149,
                        "Y": 225
                    },
                    {
                        "X": 48,
                        "Y": 227
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}",
                "Confidence": 100,
                "DetectedText": "2009年，我写了《减肥前要做的101件事》(101Things to Do",
                "ItemPolygon": {
                    "Height": 34,
                    "Width": 629,
                    "X": 88,
                    "Y": 243
                },
                "Polygon": [
                    {
                        "X": 88,
                        "Y": 243
                    },
                    {
                        "X": 716,
                        "Y": 246
                    },
                    {
                        "X": 716,
                        "Y": 276
                    },
                    {
                        "X": 88,
                        "Y": 273
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":3}}",
                "Confidence": 100,
                "DetectedText": "BeforeYou Diet)，归纳我尝试各种流行减肥法的气馁经验，每种方",
                "ItemPolygon": {
                    "Height": 31,
                    "Width": 675,
                    "X": 43,
                    "Y": 290
                },
                "Polygon": [
                    {
                        "X": 43,
                        "Y": 292
                    },
                    {
                        "X": 717,
                        "Y": 290
                    },
                    {
                        "X": 717,
                        "Y": 318
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
                "Confidence": 100,
                "DetectedText": "法似乎都注定失败。",
                "ItemPolygon": {
                    "Height": 30,
                    "Width": 194,
                    "X": 44,
                    "Y": 338
                },
                "Polygon": [
                    {
                        "X": 44,
                        "Y": 340
                    },
                    {
                        "X": 237,
                        "Y": 338
                    },
                    {
                        "X": 237,
                        "Y": 365
                    },
                    {
                        "X": 44,
                        "Y": 367
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 100,
                "DetectedText": "这二十年来我接触过的减肥方法中，只有轻断食让我在瘦下来之",
                "ItemPolygon": {
                    "Height": 30,
                    "Width": 635,
                    "X": 87,
                    "Y": 382
                },
                "Polygon": [
                    {
                        "X": 87,
                        "Y": 384
                    },
                    {
                        "X": 721,
                        "Y": 382
                    },
                    {
                        "X": 721,
                        "Y": 409
                    },
                    {
                        "X": 87,
                        "Y": 411
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":4}}",
                "Confidence": 100,
                "DetectedText": "后不反弹。至于抗衰老的健康益处，更是得来全不费工夫。",
                "ItemPolygon": {
                    "Height": 31,
                    "Width": 582,
                    "X": 41,
                    "Y": 430
                },
                "Polygon": [
                    {
                        "X": 41,
                        "Y": 432
                    },
                    {
                        "X": 622,
                        "Y": 430
                    },
                    {
                        "X": 622,
                        "Y": 457
                    },
                    {
                        "X": 41,
                        "Y": 460
                    }
                ],
                "WordCoordPoint": [],
                "Words": []
            }
        ]
    }
}
```

