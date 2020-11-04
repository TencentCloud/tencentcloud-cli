**Example 1: 算式识别示例代码**



Input: 

```
tccli ocr ArithmeticOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "TextDetections": [
            {
                "DetectedText": "40*40=1600",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 92,
                    "Y": 146,
                    "Width": 201,
                    "Height": 38
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "90-60+50=80",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 374,
                    "Y": 147,
                    "Width": 195,
                    "Height": 37
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "30+22=52",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 102,
                    "Y": 214,
                    "Width": 172,
                    "Height": 38
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "54-2+30=82",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 366,
                    "Y": 216,
                    "Width": 212,
                    "Height": 38
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "46-20+9=17",
                "Result": false,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 383,
                    "Y": 282,
                    "Width": 193,
                    "Height": 44
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "43+9=52",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 107,
                    "Y": 284,
                    "Width": 174,
                    "Height": 40
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "48-20=28",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 105,
                    "Y": 353,
                    "Width": 172,
                    "Height": 36
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "22+(37+3)=62",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 380,
                    "Y": 351,
                    "Width": 210,
                    "Height": 40
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "96+3=99",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 112,
                    "Y": 421,
                    "Width": 160,
                    "Height": 46
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "20-(13-6)=13",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 379,
                    "Y": 420,
                    "Width": 206,
                    "Height": 43
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "50+40=90",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 107,
                    "Y": 491,
                    "Width": 177,
                    "Height": 41
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "45-(17-10)=38",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 385,
                    "Y": 492,
                    "Width": 206,
                    "Height": 38
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "34-(16+4)=14",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 387,
                    "Y": 561,
                    "Width": 213,
                    "Height": 40
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "78-23=25",
                "Result": false,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 115,
                    "Y": 567,
                    "Width": 156,
                    "Height": 38
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "48-31=17",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 121,
                    "Y": 634,
                    "Width": 136,
                    "Height": 40
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "60-(2+18)=40",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 382,
                    "Y": 631,
                    "Width": 217,
                    "Height": 38
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "78+(32-18)=92",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 382,
                    "Y": 699,
                    "Width": 222,
                    "Height": 37
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "36+28=64",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 125,
                    "Y": 707,
                    "Width": 157,
                    "Height": 41
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "40-(28-30)=38",
                "Result": false,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 375,
                    "Y": 769,
                    "Width": 235,
                    "Height": 40
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            },
            {
                "DetectedText": "25-10=15",
                "Result": true,
                "Confidence": 0,
                "ItemCoord": {
                    "X": 124,
                    "Y": 779,
                    "Width": 158,
                    "Height": 41
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
                "ExpressionType": "1",
                "AdvancedInfo": ""
            }
        ],
        "RequestId": "f3c5fbb6-151d-4f93-98d8-4e3980212dd6"
    }
}
```

