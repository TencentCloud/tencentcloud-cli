**Example 1: 传入场景only_hw**

只输出手写体识别结果，过滤印刷体

Input: 

```
tccli ocr GeneralHandwritingOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/***/fakeurl.jpg \
    --Scene only_hw
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "DetectedText": "六习作表达30分",
                "Confidence": 99,
                "Polygon": [
                    {
                        "X": 43,
                        "Y": 29
                    },
                    {
                        "X": 176,
                        "Y": 25
                    },
                    {
                        "X": 177,
                        "Y": 49
                    },
                    {
                        "X": 43,
                        "Y": 53
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                "WordPolygon": [
                    {
                        "LeftBottom": {
                            "X": 97,
                            "Y": 204
                        },
                        "LeftTop": {
                            "X": 97,
                            "Y": 156
                        },
                        "RightBottom": {
                            "X": 134,
                            "Y": 204
                        },
                        "RightTop": {
                            "X": 134,
                            "Y": 156
                        }
                    }
                ]
            }
        ],
        "Angle": 0,
        "RequestId": "b57e40af-a73c-4844-ae7e-344f06efb9e5"
    }
}
```

**Example 2: 通用手写体识别示例代码**

通用手写体识别示例

Input: 

```
tccli ocr GeneralHandwritingOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/GeneralHandwritingOCR/GeneralHandwritingOCR1.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                "Confidence": 99,
                "DetectedText": "飞机飞过天空天空之城",
                "Polygon": [
                    {
                        "X": 99,
                        "Y": 154
                    },
                    {
                        "X": 490,
                        "Y": 154
                    },
                    {
                        "X": 490,
                        "Y": 207
                    },
                    {
                        "X": 99,
                        "Y": 207
                    }
                ],
                "WordPolygon": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}",
                "Confidence": 97,
                "DetectedText": "落雨下的黄昏的我们",
                "Polygon": [
                    {
                        "X": 170,
                        "Y": 216
                    },
                    {
                        "X": 471,
                        "Y": 227
                    },
                    {
                        "X": 469,
                        "Y": 286
                    },
                    {
                        "X": 168,
                        "Y": 275
                    }
                ],
                "WordPolygon": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}",
                "Confidence": 99,
                "DetectedText": "此刻我在异乡的夜里",
                "Polygon": [
                    {
                        "X": 130,
                        "Y": 289
                    },
                    {
                        "X": 455,
                        "Y": 292
                    },
                    {
                        "X": 455,
                        "Y": 351
                    },
                    {
                        "X": 130,
                        "Y": 348
                    }
                ],
                "WordPolygon": []
            },
            {
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":2}}",
                "Confidence": 98,
                "DetectedText": "感觉着你忽明忽暗",
                "Polygon": [
                    {
                        "X": 143,
                        "Y": 357
                    },
                    {
                        "X": 454,
                        "Y": 349
                    },
                    {
                        "X": 456,
                        "Y": 418
                    },
                    {
                        "X": 145,
                        "Y": 425
                    }
                ],
                "WordPolygon": []
            }
        ],
        "Angle": 0,
        "RequestId": "361e2ac6-ee7e-40d0-9463-5f05ecd4828e"
    }
}
```

