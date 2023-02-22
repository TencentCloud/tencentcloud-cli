**Example 1: 算式识别示例代码**

算式识别示例代码

Input: 

```
tccli ocr ArithmeticOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/document/ArithmeticOCR/ArithmeticOCR1.jpg \
    --SupportHorizontalImage True
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "RequestId": "c69aa49a-b6e2-40f7-a37f-b1802188165f",
        "TextDetections": [
            {
                "AdvancedInfo": "",
                "Answer": "",
                "Confidence": 0,
                "DetectedText": "40*40=1600",
                "ExpressionType": "1",
                "ItemCoord": {
                    "Height": 23,
                    "Width": 117,
                    "X": 290,
                    "Y": 244
                },
                "Polygon": [
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    }
                ],
                "Result": true
            },
            {
                "AdvancedInfo": "",
                "Answer": "",
                "Confidence": 0,
                "DetectedText": "40*50=2000",
                "ExpressionType": "1",
                "ItemCoord": {
                    "Height": 22,
                    "Width": 116,
                    "X": 291,
                    "Y": 283
                },
                "Polygon": [
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    }
                ],
                "Result": true
            },
            {
                "AdvancedInfo": "",
                "Answer": "55*66=3630",
                "Confidence": 0,
                "DetectedText": "55*66=121",
                "ExpressionType": "1",
                "ItemCoord": {
                    "Height": 24,
                    "Width": 106,
                    "X": 291,
                    "Y": 322
                },
                "Polygon": [
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    }
                ],
                "Result": false
            },
            {
                "AdvancedInfo": "",
                "Answer": "",
                "Confidence": 0,
                "DetectedText": "128*5=640",
                "ExpressionType": "1",
                "ItemCoord": {
                    "Height": 24,
                    "Width": 106,
                    "X": 292,
                    "Y": 360
                },
                "Polygon": [
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    }
                ],
                "Result": true
            },
            {
                "AdvancedInfo": "",
                "Answer": "",
                "Confidence": 0,
                "DetectedText": "500-(100+20)=380",
                "ExpressionType": "1",
                "ItemCoord": {
                    "Height": 22,
                    "Width": 156,
                    "X": 291,
                    "Y": 403
                },
                "Polygon": [
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    }
                ],
                "Result": true
            },
            {
                "AdvancedInfo": "",
                "Answer": "",
                "Confidence": 0,
                "DetectedText": "48-(10+20)=18",
                "ExpressionType": "1",
                "ItemCoord": {
                    "Height": 23,
                    "Width": 123,
                    "X": 295,
                    "Y": 441
                },
                "Polygon": [
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    },
                    {
                        "X": -1,
                        "Y": -1
                    }
                ],
                "Result": true
            }
        ]
    }
}
```

