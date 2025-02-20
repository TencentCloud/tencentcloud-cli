**Example 1: 通用卡证ps检测告警**

身份证

Input: 

```
tccli ocr RecognizeGeneralCardWarn --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/IDCardOCR/IDCardOCR1.jpg
```

Output: 
```
{
    "Response": {
        "Blur": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "BorderIncomplete": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "CardType": "IDCard",
        "Copy": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Ps": {
            "IsWarn": true,
            "Polygon": [
                {
                    "LeftBottom": {
                        "X": 477,
                        "Y": 494
                    },
                    "LeftTop": {
                        "X": 477,
                        "Y": 257
                    },
                    "RightBottom": {
                        "X": 662,
                        "Y": 494
                    },
                    "RightTop": {
                        "X": 662,
                        "Y": 257
                    }
                },
                {
                    "LeftBottom": {
                        "X": 309,
                        "Y": 551
                    },
                    "LeftTop": {
                        "X": 309,
                        "Y": 527
                    },
                    "RightBottom": {
                        "X": 617,
                        "Y": 551
                    },
                    "RightTop": {
                        "X": 617,
                        "Y": 527
                    }
                },
                {
                    "LeftBottom": {
                        "X": 210,
                        "Y": 461
                    },
                    "LeftTop": {
                        "X": 210,
                        "Y": 403
                    },
                    "RightBottom": {
                        "X": 417,
                        "Y": 461
                    },
                    "RightTop": {
                        "X": 417,
                        "Y": 403
                    }
                },
                {
                    "LeftBottom": {
                        "X": 218,
                        "Y": 284
                    },
                    "LeftTop": {
                        "X": 218,
                        "Y": 256
                    },
                    "RightBottom": {
                        "X": 284,
                        "Y": 284
                    },
                    "RightTop": {
                        "X": 284,
                        "Y": 256
                    }
                },
                {
                    "LeftBottom": {
                        "X": 216,
                        "Y": 379
                    },
                    "LeftTop": {
                        "X": 216,
                        "Y": 358
                    },
                    "RightBottom": {
                        "X": 268,
                        "Y": 379
                    },
                    "RightTop": {
                        "X": 268,
                        "Y": 358
                    }
                },
                {
                    "LeftBottom": {
                        "X": 309,
                        "Y": 377
                    },
                    "LeftTop": {
                        "X": 309,
                        "Y": 356
                    },
                    "RightBottom": {
                        "X": 326,
                        "Y": 377
                    },
                    "RightTop": {
                        "X": 326,
                        "Y": 356
                    }
                },
                {
                    "LeftBottom": {
                        "X": 361,
                        "Y": 378
                    },
                    "LeftTop": {
                        "X": 361,
                        "Y": 356
                    },
                    "RightBottom": {
                        "X": 386,
                        "Y": 378
                    },
                    "RightTop": {
                        "X": 386,
                        "Y": 356
                    }
                }
            ],
            "RiskConfidence": 0.9318133
        },
        "Reflection": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "Reprint": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.01
        },
        "RequestId": "b8b73be7-2d64-49c6-8cbc-3b1d2b5f3651"
    }
}
```

