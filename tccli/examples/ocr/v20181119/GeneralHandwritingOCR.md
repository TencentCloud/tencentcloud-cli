**Example 1: 传入场景only_hw**

只输出手写体识别结果，过滤印刷体

Input: 

```
tccli ocr GeneralHandwritingOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
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
        "Angel": 0,
        "RequestId": "b57e40af-a73c-4844-ae7e-344f06efb9e5"
    }
}
```

**Example 2: 通用手写体识别示例代码**



Input: 

```
tccli ocr GeneralHandwritingOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "DetectedText": "通用手写体文字识别",
                "Confidence": 97,
                "Polygon": [
                    {
                        "X": 42,
                        "Y": 268
                    },
                    {
                        "X": 570,
                        "Y": 268
                    },
                    {
                        "X": 570,
                        "Y": 314
                    },
                    {
                        "X": 42,
                        "Y": 314
                    }
                ],
                "AdvancedInfo": "{\"Parag\":{\"ParagNo\":1}}",
                "WordPolygon": []
            }
        ],
        "Angel": 0,
        "RequestId": "a57e40af-a73c-4844-ae7e-344f06efb9e5"
    }
}
```

